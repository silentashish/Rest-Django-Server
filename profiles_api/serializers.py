from rest_framework import serializers

from . import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView."""

    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects."""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Create and return a new user."""

        user = models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class ProfilesFeedItemSerializer(serializers.ModelSerializer):
    """A serializer for profile feed item."""
    file_name = serializers.ReadOnlyField(source='user_profile.name')
    file_email = serializers.ReadOnlyField(source='user_profile.email')

    class Meta:
        model = models.ProfilesFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on','file_name','file_email')
        extra_kwargs = {'user_profile': {'read_only': True}}

class ImageFieldSerializer(serializers.ModelSerializer):
    """A serializser for uploading image and saving it"""

    class Meta:
        model = models.ImageUploadField
        fields=('id','user_profile','image','created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}

class ImageSerializer(serializers.ModelSerializer):
    """A serializser for uploading image and saving it"""

    class Meta:
        model = models.ImageField
        fields=('image',)

class CommentFieldSerializer(serializers.ModelSerializer):
    """A serializser for uploading image and saving it"""
    # comment = serializers.SlugRelatedField(read_only=True, slug_field='comment')
    file_name = serializers.ReadOnlyField(source='user_profile.name')
    file_email = serializers.ReadOnlyField(source='user_profile.email')

    class Meta:
        model = models.CommentField
        fields=('id','user_profile','comment','created_on','post','file_name','file_email')
        extra_kwargs = {'user_profile': {'read_only': True}}

class TokenSerializer(serializers.ModelSerializer):
    """A serializser for uploading image and saving it"""

    class Meta:
        model = models.TokenFiled
        fields=('token',)
