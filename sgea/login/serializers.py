from rest_framework import serializers
from login.models import *
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from .models import Usuario

class CustomAuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(label=_("Email"), write_only=True) 
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(label=_("Token"), read_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password') 

        if email and password:
            try:
                user = Usuario.objects.get(email=email)
            except Usuario.DoesNotExist:
                user = None
                
            if user and user.senha == password:
                attrs['user'] = user
                return attrs
            else:
                raise serializers.ValidationError(
                    _("Impossível fazer login com as credenciais fornecidas."),
                    code='authorization'
                )
        
        raise serializers.ValidationError(
            _("Deve incluir 'email' e 'password'."), 
            code='authorization'
        )
        
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        
class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'