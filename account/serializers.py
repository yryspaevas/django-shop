from rest_framework import serializers

from .models import User


class RegisterUserSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(min_length=4, required=True)


    class Meta:
        model = User
        fields = ('email', 'password', 'password_confirm')

    def validate(self, attrs):
        # attrs = {'email': "some@gmail.com", 'password':'1234444', 'password':'1234444'}
        pass1 = attrs.get('password')
        pass2 = attrs.pop('password_confirm')
        if pass1 != pass2:
            raise serializers.ValidationError('Passwords do not match')
        return attrs
    
    def validate_email(self, email):
        # email = "some@gmail.com"
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('User with this email already exists')
        return email

    def create(self, validated_data):
        # alidated_data = {'email': "some@gmail.com", 'password':'1234444', 'password':'1234444'}
        # тот же словарь, но уже прошедший все проверки
        return User.objects.create_user(**validated_data)