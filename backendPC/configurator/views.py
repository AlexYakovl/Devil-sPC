from .models import Case, PowerSupply, Motherboard, RAM, GPU, CPU, HardDrive
from .serializers import (
    CaseSerializer, PowerSupplySerializer, MotherboardSerializer,
    RAMSerializer, GPUSerializer, CPUSerializer, HardDriveSerializer, UserSerializer
)
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth.models import User



class CaseViewSet(viewsets.ModelViewSet):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer

class PowerSupplyViewSet(viewsets.ModelViewSet):
    queryset = PowerSupply.objects.all()
    serializer_class = PowerSupplySerializer

class MotherboardViewSet(viewsets.ModelViewSet):
    queryset = Motherboard.objects.all()
    serializer_class = MotherboardSerializer

class RAMViewSet(viewsets.ModelViewSet):
    queryset = RAM.objects.all()
    serializer_class = RAMSerializer

class GPUViewSet(viewsets.ModelViewSet):
    queryset = GPU.objects.all()
    serializer_class = GPUSerializer

class CPUViewSet(viewsets.ModelViewSet):
    queryset = CPU.objects.all()
    serializer_class = CPUSerializer

class HardDriveViewSet(viewsets.ModelViewSet):
    queryset = HardDrive.objects.all()
    serializer_class = HardDriveSerializer

class RegisterUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListUsersView(APIView):
    permission_classes = [IsAdminUser]  # Только администраторы имеют доступ

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


