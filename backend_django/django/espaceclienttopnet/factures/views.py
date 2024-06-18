# factures/views.py
from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Facture
from .serializers import FactureSerializer
from .permissions import IsOwnerOrAdmin
from rest_framework.permissions import IsAuthenticated
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getId(request):
    user_id = request.user.id
    return Response({'user_id': user_id})

class FactureList(generics.ListCreateAPIView):
    serializer_class = FactureSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Get the authenticated user's ID
        user_id = self.request.user.id
        
        # Filter factures by client_id (user's ID)
        return Facture.objects.filter(client_id=user_id)

    

class FactureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Facture.objects.all()
    serializer_class = FactureSerializer
    permission_classes = [IsOwnerOrAdmin]

    def get_queryset(self):
        # Admin can see all factures, clients can only see their own factures
        if self.request.user.is_staff:
            return Facture.objects.all()
        return Facture.objects.filter(client_id=self.request.user.id)
