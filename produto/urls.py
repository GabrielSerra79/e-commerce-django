from django.urls import path
from . import views

app_name = 'produto'

urlpatterns = [
    path('', views.ListaProdutos.as_view(), name='lista'),
    path('<slug>/', views.DetalheProdutos.as_view(), name='detalhe'),
    path('addaocarrinho/', views.AdicionarAoCarrinho.as_view(), name='addaocarrinho'),
    path('removedocarrinho/', views.RemoverDoCarrinho.as_view(), name='removedocarrinho'),
    path('carrinho/', views.Carrinho.as_view(), name='carrinho'),
    path('finalizar/', views.Finalizar.as_view(), name='finalizar'),
]
