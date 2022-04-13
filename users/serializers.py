from .models import UserTable
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTable
        fields = '__all__'