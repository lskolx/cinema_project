from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

from apps.movie.filters import FilmGenreCountryFilter
from .models import Film, Favorites
from .serializers import FilmSerializer, FavoritesSerializer
from rest_framework import filters, generics


class FilmViewSet(ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    filterset_class = FilmGenreCountryFilter
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        elif self.action == 'like':
            self.permission_classes = [IsAuthenticated, ]
        elif self.action in ['update', 'create', 'partial_update', 'destroy']:
            self.permission_classes = [IsAdminUser, ]
        # else:
        #     self.permission_classes = [IsAdminUser, ]
        return [permission() for permission in self.permission_classes]

    @action(detail=True, methods=["POST"])
    def like(self, request, *args, **kwargs):
        film = self.get_object()
        favorite, _ = Favorites.objects.get_or_create(film=film, user=request.user)
        favorite.is_favorite = not favorite.is_favorite
        favorite.save()
        status = 'is_favorite'
        if not favorite.is_favorite:
            status = 'not_favorite'
        return Response({'status': status})


class FavoriteView(generics.ListAPIView):
    queryset = Favorites.objects.all()
    serializer_class = FavoritesSerializer
    permission_classes = IsAuthenticated
    







