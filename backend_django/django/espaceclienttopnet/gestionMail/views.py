# gestionMail/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Email
from .serializers import EmailSerializer
from rest_framework.decorators import api_view
class EmailViewSet(viewsets.ModelViewSet):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer

    def accept_email(self, request, pk=None):
        email = self.get_object()
        email.adminResulat = 'Accepted'
        email.save()
        serializer = self.get_serializer(email)
        return Response(serializer.data)

    def refuse_email(self, request, pk=None):
        email = self.get_object()
        email.adminResulat = 'Refused'
        email.save()
        serializer = self.get_serializer(email)
        return Response(serializer.data)
@api_view(['GET'])
def getId(request):
    email_id = request.email.id
    return Response({'email_id': email_id})