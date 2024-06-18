from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import UserSerializer 
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.files.base import ContentFile
from django.contrib.auth.hashers import make_password

# Create your views here.

from django.contrib.auth import authenticate

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from .serializers import UserSerializer

@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    if email is None or password is None:
        return Response({'error': 'Please provide both email and password'},
                        status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(request, email=email, password=password)

    if not user:
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
    refresh = RefreshToken.for_user(user)
    serializer = UserSerializer(user)

    return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'user': serializer.data,
        'role': user.is_staff
    })  
    

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid():
        # Extract user data from request
        email = request.data['email']
        name = request.data['name']
        cin = request.data['cin']
        password = request.data['password']
        
        # Check if a user with the given email already exists
        if CustomUser.objects.filter(email=email).exists():
            return Response({"error": "Email already exists"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Create the user
        user = CustomUser.objects.create(email=email, name=name, cin=cin)
        
        # Set the password
        user.set_password(password)
        
        # Save the user
        user.save()
        
        # Create a token for the user
        refresh = RefreshToken.for_user(user)
        
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "user": serializer.data
        })
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getId(request):
    user_id = request.user.id
    return Response({'user_id': user_id})


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("Accepted {}".format(request.user.email))




@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    try:
        # Retrieve the refresh token from the request data
        refresh_token = request.data.get('refresh')
        
        if not refresh_token:
            return Response({"error": "Refresh token is required."}, status=status.HTTP_400_BAD_REQUEST)

        # Blacklist the refresh token to invalidate it
        RefreshToken(refresh_token).blacklist()
        
        return Response({"success": "Successfully logged out."}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_data_view(request):
    user = request.user

    # Create a default response
    response_data = {
        'name': user.name,
        'cin': user.cin,
        'email': user.email,
        
    }

    # Check if profile image exists
    

    return Response(response_data, status=status.HTTP_200_OK)










@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def edit_profile(request):
    user = request.user

    # Exclude profile_image field from the request data
    request_data = request.data.copy()
   

    # Hash the password if it's included in the request data
    if 'password' in request_data:
        request_data['password'] = make_password(request_data['password'])

    # Validate and update user data
    serializer = UserSerializer(user, data=request_data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

