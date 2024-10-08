from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, NewArrivalsList , RegisterView, ProfileView, UserListView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/new-arrivals/', NewArrivalsList.as_view(), name='new-arrivals'),
    path('api/users/', UserListView.as_view(), name='user-list'),
    path('api/profile/', ProfileView.as_view(), name='profile'),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
