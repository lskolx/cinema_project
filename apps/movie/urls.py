# from django.db import router
# from django.urls import path
# from rest_framework.routers import DefaultRouter
# from .views import FilmViewSet, FilmDetailView

# router = DefaultRouter()

# router.register('', FilmViewSet)

# urlpatterns = [
#     path('<int:pk>/', FilmDetailView.as_view()),
    
# ]
# urlpatterns += router.urls

from django.urls import path
from .views import FilmListView, CreateFilmView, RetrieveEditDestroyFilmView

urlpatterns = [
    path('', FilmListView.as_view()),
    path('film/', CreateFilmView.as_view()),
    path('film/<int:pk>/', RetrieveEditDestroyFilmView.as_view()),

]
