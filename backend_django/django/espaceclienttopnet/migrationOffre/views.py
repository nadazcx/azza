from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import MigrationOffre
from .serializers import MigrationOffreSerializer

class MigrationOffreViewSet(viewsets.ModelViewSet):
    queryset = MigrationOffre.objects.all()
    serializer_class = MigrationOffreSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return MigrationOffre.objects.all()
        else:
            return MigrationOffre.objects.filter(client=user)

    @action(detail=True, methods=['post'])
    def accepter_offre(self, request, pk=None):
        offre = self.get_object()
        if not request.user.is_staff:
            return Response({'error': 'Permission denied.'}, status=status.HTTP_403_FORBIDDEN)

        offre.accepter_offre(request.user)
        return Response({'message': 'Offer accepted successfully.'})

    @action(detail=True, methods=['post'])
    def refuser_offre(self, request, pk=None):
        offre = self.get_object()
        if not request.user.is_staff:
            return Response({'error': 'Permission denied.'}, status=status.HTTP_403_FORBIDDEN)

        offre.refuser_offre(request.user)
        return Response({'message': 'Offer rejected successfully.'})
