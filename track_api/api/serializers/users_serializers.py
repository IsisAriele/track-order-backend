# serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name", "password"]

    def create(self, validated_data):
        # Remove o campo 'password' dos dados validados
        password = validated_data.pop("password")
        # Cria uma nova instância de User sem a senha
        user = User(**validated_data)
        # Define a senha de forma segura usando set_password
        user.set_password(password)
        # Salva o usuário no banco de dados
        user.save()
        return user

    def update(self, instance, validated_data):
        # Remove o campo 'password' dos dados validados, se presente
        password = validated_data.pop("password", None)
        # Atualiza os outros campos
        instance = super().update(instance, validated_data)
        # Se a senha foi fornecida, atualiza-a corretamente
        if password:
            instance.set_password(password)
            instance.save()
        return instance


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
