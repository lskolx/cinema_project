# from rest_framework.viewsets import ModelViewSet
# from rest_framework import permissions

# from apps.movie.filters import FilmGenreCountryFilter
# from .models import Film
# from .serializers import FilmSerializer
# from rest_framework import filters, generics


# class FilmViewSet(ModelViewSet):
#     queryset = Film.objects.all()
#     serializer_class = FilmSerializer
#     filterset_class = FilmGenreCountryFilter
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['title']

#     def retrieve(self, request, *args, **kwargs):
#         film = self.get_object()
#         film.views_count += 1
#         film.save()
#         return super(FilmViewSet, self).retrieve(request, *args, **kwargs)

#     def get_permissions(self):
#         if self.action in ['list', 'retrieve']:
#             self.permission_classes = [permissions.AllowAny]
#         elif self.action in ['update', 'create', 'partial_update', 'destroy']:
#             self.permission_classes = [permissions.IsAdminUser]
#         return [permission() for permission in self.permission_classes]

# class FilmDetailView(generics.RetrieveAPIView):
#     queryset = Film.objects.all()
#     serializer_class = FilmSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework import permissions
from rest_framework import generics, filters
from .serializers import FilmSerializer
from .models import Film
from rest_framework.pagination import PageNumberPagination


class CreateFilmView(generics.CreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UpdateFilmView(generics.UpdateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



class DestroyFilmView(generics.DestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FilmListView(generics.ListAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    permission_classes = [permissions.AllowAny]
    pagination_class = PageNumberPagination
    search_fields = ['title']

    def get_serializer_context(self):
        return {'request': self.request}


class FilmDetailView(generics.RetrieveAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer





