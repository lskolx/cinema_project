from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FilmViewSet, FavoriteView

router = DefaultRouter()

router.register('film', FilmViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('saved/', FavoriteView.as_view())
    
]
# urlpatterns += router.urls



# from django.urls import path
# from .views import FilmListView, CreateFilmView, UpdateFilmView, DestroyFilmView, FilmDetailView

# urlpatterns = [
#     path('', FilmListView.as_view()),
#     path('film/', CreateFilmView.as_view()),
#     path('film/<int:pk>/', FilmDetailView.as_view()),
#     path('film/update/<int:pk>/', UpdateFilmView.as_view()),
#     path('film/delete/<int:pk>/', DestroyFilmView.as_view()),

# ]
