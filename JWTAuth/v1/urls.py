from django.urls import path
from .views import RegisterView, CustomTokenObtainPairView
from .views import PrivateView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('private/', PrivateView.as_view(), name='private'),
]