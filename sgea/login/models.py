from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UsuarioManager 

class Usuario(AbstractBaseUser, PermissionsMixin):
    # Campos obrigatórios pelo AbstractBaseUser
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    id_usuario = models.AutoField(primary_key=True, unique=True)
    
    # ID e senha são gerenciados pelo login do Django
    email = models.EmailField(max_length=255, unique=True) 
    nome = models.CharField(max_length=255, null=False) 
    sobrenome = models.CharField(max_length=255, null=False) 
    telefone = models.CharField(max_length=13, unique=True, null=False)
    instituicao = models.CharField(max_length=50, null=False)
    tipo = models.CharField(max_length=50, choices=[("estudante", "Estudante"), ("professor", "Professor"), ("organizador", "Organizador")], default="estudante")
    codigo = models.CharField(max_length=6, null=True, blank=True)
    
    # Definições de autenticação
    objects = UsuarioManager() 
    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = ['nome', 'sobrenome', 'telefone', 'instituicao', 'tipo'] 

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        
class Evento(models.Model):
    id_evento = models.AutoField(primary_key = True)
    nome = models.TextField(max_length = 255, null = True)
    tipoevento = models.TextField(max_length = 255)
    dataI = models.DateField()
    dataF = models.DateField()
    horarioI = models.TimeField()
    horarioF = models.TimeField()    
    local = models.TextField(max_length = 255)
    quantPart = models.IntegerField()
    organResp = models.TextField(max_length = 255)
    vagas = models.IntegerField()
    emitido = models.BooleanField(default = False)
    assinatura = models.TextField(max_length = 255, null = False)
    horas = models.DecimalField(decimal_places = 2, max_digits = 5, null = True, blank = True)
    descricao = models.TextField(max_length = 999, null = False)
    imagem = models.ImageField(upload_to = 'eventos/imagens/', blank = True, null = True)

    @property
    def horas_e_minutos(self):

        horas_str = str(self.horas)
        
        # Separa os números a partir do '.' em uma lista. ex: ['12', '45']
        horas_min = horas_str.split(".")
        
        # Primeiro valor da lista
        horasInteiras = horas_min[0]
        minutos = horas_min[1]
        total = ""
        
        if len(horas_min) > 1:
            minutos = int(horas_min[1][:2])
    
        if horasInteiras == 1:
            total = f"{horasInteiras} Hora e "
        else:
            total = f"{horasInteiras} Horas e "
        
        if minutos > 0:
            if minutos == 1:
                total += f"{minutos} Minuto"
            else:    
                total += f"{minutos} Minutos"
        else:
            return "0 minutos"

        return total
    
class Inscrito(models.Model):
    id_inscricao = models.AutoField(primary_key = True)
    usuario_id = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    evento_id = models.ForeignKey(Evento, on_delete = models.CASCADE)
    data_inscricao = models.DateTimeField(auto_now_add = True)
    
class Certificado(models.Model):
    id_cert = models.AutoField(primary_key = True)
    usuario_id = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    evento_id = models.ForeignKey(Evento, on_delete = models.CASCADE)
    assinatura = models.TextField(max_length = 255, null = True, blank = True)
    data_emissao = models.DateTimeField(default = timezone.now)
    horas = models.TextField(max_length = 255, null = True, blank = True)
    
class Registro(models.Model):
    id_registro = models.AutoField(primary_key = True, unique = True)
    hora = models.DateTimeField(default = timezone.now)
    usuario_id = models.TextField(max_length = 50, null = True)
    evento_id = models.TextField(max_length = 50, null = True)
    acao = models.TextField(max_length = 50, null = False)