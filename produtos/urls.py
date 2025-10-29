from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProdutoList.as_view(), name='produto-list'),
    path('<int:pk>/', views.ProdutoDetail.as_view(), name='produto-detail'),
]
