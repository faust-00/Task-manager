from pickle import FALSE

from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'user', 'title', 'description', 'deadline', 'is_done', 'created_at', 'updated_at')
        model = Task


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline']

    def create(self, validated_data):
        """Yangi Task yaratishda 'author'ni avtomatik ravishda foydalanuvchi bilan to'ldiramiz."""
        user = self.context['request'].user
        task = Task.objects.create(user=user, **validated_data)
        return task




