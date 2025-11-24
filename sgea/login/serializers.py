from rest_framework import serializers
from login.models import *
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from .models import Usuario
from rest_framework_simplejwt.tokens import RefreshToken

class CustomAuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(label=_("Email"), write_only=True)
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    access = serializers.CharField(label=_("Access Token"), read_only=True)
    refresh = serializers.CharField(label=_("Refresh Token"), read_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'), 
                                username=email, 
                                password=password)
            
            # 2. Verifica se a autenticação foi bem sucedida
            if user:
                if not user.is_active:
                    raise serializers.ValidationError(_("Conta desativada."), code='authorization')

            if user and user.senha == password:
                refresh = RefreshToken.for_user(user)
                
                return {
                    'email': user.email,
                    'access': str(refresh.access_token),
                    'refresh': str(refresh),
                }
            else:
                raise serializers.ValidationError(
                    _("Impossível fazer login com as credenciais fornecidas."),
                    code='authorization'
                )
        raise serializers.ValidationError(
            _("Deve incluir 'email' e 'password'."),
            code='authorization'
        )

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'