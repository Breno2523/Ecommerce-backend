from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'preco', 'descricao')  # mostra essas colunas no painel
    search_fields = ('nome', 'descricao')  # permite buscar por nome ou descrição
