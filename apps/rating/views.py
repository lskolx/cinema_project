from rest_framework import viewsets
# from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.rating.models import Rating
from apps.rating.permissions import IsRatingAuthor
from apps.rating.serializers import RatingSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsRatingAuthor(), ]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permissions = []
        else:
            permissions = [IsRatingAuthor, ]
        return [permission() for permission in permissions]

