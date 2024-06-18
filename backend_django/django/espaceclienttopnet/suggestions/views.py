from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Suggestion
from .serializers import SuggestionSerializer

class SuggestionViewSet(viewsets.ModelViewSet):
    queryset = Suggestion.objects.all()
    serializer_class = SuggestionSerializer
    permission_classes = [permissions.IsAuthenticated]  # Adjust permissions as needed

    def list(self, request):
        queryset = self.get_queryset()
        serializer = SuggestionSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def accepter_suggestion(self, request, pk=None):
        suggestion = self.get_object()
        if not request.user.is_staff:
            return Response({'error': 'Permission denied.'}, status=status.HTTP_403_FORBIDDEN)

        # Logic to accept suggestion, update status, etc.
        suggestion.accepter_suggestion(request.user)
        return Response({'message': 'Suggestion accepted successfully.'})

    @action(detail=True, methods=['post'])
    def refuser_suggestion(self, request, pk=None):
        suggestion = self.get_object()
        if not request.user.is_staff:
            return Response({'error': 'Permission denied.'}, status=status.HTTP_403_FORBIDDEN)

        # Logic to reject suggestion, update status, etc.
        suggestion.refuser_suggestion(request.user)
        return Response({'message': 'Suggestion rejected successfully.'})
