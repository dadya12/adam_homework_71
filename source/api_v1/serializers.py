from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from webapp.models import Publication

class PublicationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ['id', 'picture', 'description', 'author']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['author'] = AuthorModelSerializer(instance.author).data
        return data

    def validate_title(self, title):
        if len(title) < 8:
            raise ValidationError("Title must be at least 8 characters")
        return title

class AuthorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'first_name', 'last_name')