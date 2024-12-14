from rest_framework import serializers
from .models import Case, PowerSupply, Motherboard, RAM, GPU, CPU, HardDrive
from django.contrib.auth.models import User




class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = ['id', 'name', 'specifications']

class PowerSupplySerializer(serializers.ModelSerializer):
    class Meta:
        model = PowerSupply
        fields = ['id', 'name', 'specifications']

class MotherboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motherboard
        fields = ['id', 'name', 'specifications']

class RAMSerializer(serializers.ModelSerializer):
    class Meta:
        model = RAM
        fields = ['id', 'name', 'specifications']

class GPUSerializer(serializers.ModelSerializer):
    class Meta:
        model = GPU
        fields = ['id', 'name', 'specifications']

class CPUSerializer(serializers.ModelSerializer):
    class Meta:
        model = CPU
        fields = ['id', 'name', 'specifications']

class HardDriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = HardDrive
        fields = ['id', 'name', 'specifications']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user