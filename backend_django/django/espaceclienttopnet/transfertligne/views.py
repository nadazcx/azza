# transferligne/views.py

from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import TransferLignes
from .serializers import TransferLignesSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class TransferLignesViewSet(viewsets.ModelViewSet):
    queryset = TransferLignes.objects.all()
    serializer_class = TransferLignesSerializer
    permission_classes = [permissions.IsAuthenticated]  # Adjust permissions as needed

    def list(self, request):
        queryset = self.get_queryset()
        serializer = TransferLignesSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def perform_create(self, serializer):
            serializer.save(user=self.request.user)


    @action(detail=True, methods=['post'])
    def accepter_demande(self, request, pk=None):
        transfer_ligne = self.get_object()
        if not request.user.is_staff:
            return Response({'error': 'Permission denied.'}, status=status.HTTP_403_FORBIDDEN)

        transfer_ligne.accepter_demande(request.user)
        return Response({'message': 'Demande acceptée avec succès.'})

    @action(detail=True, methods=['post'])
    def refuser_demande(self, request, pk=None):
        transfer_ligne = self.get_object()
        if not request.user.is_staff:
            return Response({'error': 'Permission denied.'}, status=status.HTTP_403_FORBIDDEN)

        transfer_ligne.refuser_demande(request.user)
        return Response({'message': 'Demande refusée avec succès.'})
