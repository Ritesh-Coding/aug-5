from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChatMessageViewSet

router = DefaultRouter()
router.register(r'chat', ChatMessageViewSet,basename='chat-app')

urlpatterns = [
    path('', include(router.urls)),
]
