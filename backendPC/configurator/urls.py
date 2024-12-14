from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    CaseViewSet, PowerSupplyViewSet, MotherboardViewSet,
    RAMViewSet, GPUViewSet, CPUViewSet, HardDriveViewSet, RegisterUserView, ListUsersView
)

# Создаем маршрутизатор
router = DefaultRouter()

# Регистрируем ViewSet'ы
router.register(r'cases', CaseViewSet)
router.register(r'power-supplies', PowerSupplyViewSet)
router.register(r'motherboards', MotherboardViewSet)
router.register(r'ram', RAMViewSet)
router.register(r'gpus', GPUViewSet)
router.register(r'cpus', CPUViewSet)
router.register(r'hard-drives', HardDriveViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/register/', RegisterUserView.as_view(), name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/users/', ListUsersView.as_view(), name='list_users'),
]
