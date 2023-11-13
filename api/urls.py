from django.urls import path, include
from rest_framework import routers

from .views import PostViewSet, PositionViewSet, TechStackViewSet

router = routers.DefaultRouter()
router.register('post', PostViewSet)
router.register('position', PositionViewSet)
router.register('techstack', TechStackViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
