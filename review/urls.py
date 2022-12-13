from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ComentViewSet, CreateRatingAPIView

router = DefaultRouter()
router.register('comments', ComentViewSet)
# router.register('ratings', )

urlpatterns =[
    path('', include(router.urls)),
    path('rating/', CreateRatingAPIView.as_view()),
    
]