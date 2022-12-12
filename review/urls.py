from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ComentViewSet, RatingViewSet

router = DefaultRouter()
router.register('comments', ComentViewSet)
router.register('ratings', RatingViewSet)

urlpatterns =[
    path('', include(router.urls)),
]