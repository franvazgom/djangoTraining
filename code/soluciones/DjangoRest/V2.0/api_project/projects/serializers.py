from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'created',)
        read_only_fields = ('created',)

class SumSerializer(serializers.Serializer):
    num1 = serializers.IntegerField()
    num2 = serializers.IntegerField()

class ProjectParameterSerializer(serializers.Serializer):
    parameters = serializers.JSONField()