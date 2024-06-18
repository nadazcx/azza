# reclamations/views.py

from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Reclamation
from .serializers import ReclamationSerializer

class ReclamationViewSet(viewsets.ModelViewSet):
    queryset = Reclamation.objects.all()
    serializer_class = ReclamationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Reclamation.objects.all()
        else:
            return Reclamation.objects.filter(user=user)

    @action(detail=True, methods=['post'])
    def accepter_reclamation(self, request, pk=None):
        reclamation = self.get_object()
        if not request.user.is_staff:
            return Response({'error': 'Permission denied.'}, status=status.HTTP_403_FORBIDDEN)

        reclamation.accepter_reclamation(request.user)
        return Response({'message': 'Reclamation acceptée avec succès.'})

    @action(detail=True, methods=['post'])
    def resoudre_reclamation(self, request, pk=None):
        reclamation = self.get_object()
        if not request.user.is_staff:
            return Response({'error': 'Permission denied.'}, status=status.HTTP_403_FORBIDDEN)

        reclamation.resoudre_reclamation(request.user)
        return Response({'message': 'Reclamation résolue avec succès.'})

    @action(detail=True, methods=['post'])
    def refuser_reclamation(self, request, pk=None):
        reclamation = self.get_object()
        if not request.user.is_staff:
            return Response({'error': 'Permission denied.'}, status=status.HTTP_403_FORBIDDEN)

        reclamation.refuser_reclamation(request.user)
        return Response({'message': 'Reclamation refusée avec succès.'})
