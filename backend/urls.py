from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers, permissions
from produtos.views import ProdutoViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configuração do router
router = routers.DefaultRouter()
router.register(r'produtos', ProdutoViewSet)

# Configuração da documentação (Swagger)
schema_view = get_schema_view(
    openapi.Info(
        title="API da Loja",
        default_version='v1',
        description="Documentação da API com autenticação JWT",
        contact=openapi.Contact(email="contato@loja.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Adiciona o esquema de autenticação Bearer ao Swagger
schema_view.security_definitions = {
    'Bearer': {
        'type': 'apiKey',
        'name': 'Authorization',
        'in': 'header',
        'description': 'Digite: **Bearer <seu_token_jwt>**',
    }
}

# Rotas do projeto
urlpatterns = [
    path('admin/', admin.site.urls),

    # Rotas principais
    path('api/', include(router.urls)),
    path('api/produtos/', include('produtos.urls')),
    path('api/usuarios/', include('usuarios.urls')),

    # JWT Auth
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Documentação Swagger e Redoc
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
