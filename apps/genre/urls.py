from django.db import router
from .views import GenreViewSet
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('genre', GenreViewSet)


urlpatterns = []
urlpatterns += router.urls
