from django.contrib import admin
from django.urls import path,include
from login import views
from login.views import VerEventos 
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView    

 
router = routers.DefaultRouter()
router.register('ver_eventos', views.VerEventos, basename = 'Eventos')


urlpatterns = [
    path('admin/', admin.site.urls),
    
    #Página incial
    path('', views.cadastro_usuarios, name = "cadastro"),
    path("sobre/", views.sobre, name = "sobre"),
    
    #Verificar usuários cadastrados
    path("usuarios/", views.ver_usuarios, name = "listagem_usuarios"),
    
    #Operações com os usuários
    path("inscrever/<int:usuario_id>/<int:evento_id>/", views.inscricao_evento, name = "inscricao_evento"),
    path("deletar_usuario/", views.deletar_usuario, name = "deletar_usuario"),
    path("meus_eventos/", views.usuario_eventos, name = "meus_eventos"),
    path("meus_certificados/", views.meus_certificados, name = "meus_certificados"),
    path("editar_usuario/", views.editar_usuario, name="editar_usuario"),
    
    #Operações com os eventos
    path("cadastro_eventos/", views.ev, name = 'ev'),
    path("eventos/", views.eventos, name = 'visu_eventos'),
    path("todos_eventos/", views.todos_eventos, name = "even"),
    path("deletar_evento/<int:pk>/", views.deletar_evento, name = "deletar_evento"),
    path("editar_evento/<int:pk>", views.editar_evento, name = "editar_evento"),
    
    #Login do usuário
    path("login/", views.loginU, name = "login"),
    path("home_inscricao/", views.home_inscricao, name = "inscricao"),

    #Operações com certificados
    path("emitir_certificados/", views.emitir_certificados, name = "emitir_certificados"),
    path("certificados/", views.ver_certificados, name = "ver_certs"),
    
    #Finalizar sessão (logout)
    path("logout/", views.logout, name = "logout"),
    
    #Operaçõs com registros
    path("registros/", views.registros, name = "registro"),
    
    # API------------------------------------------------------------------------------------------------------------
    path('eventoss/', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='api_token_auth'),
    path('token_refresh/', TokenRefreshView.as_view(), name='api_token_refresh'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)