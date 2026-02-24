from typing import Any

from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import reverse, redirect # type: ignore
from django.views import View
from django.contrib import messages
from produto.models import Variacao
from utils import utils
from .models import Pedido, ItemPedido
from django.views.generic import DetailView


class DispatchLoginRequired(View):
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('perfil:criar')

        return super().dispatch(*args, **kwargs)

class SalvarPedido(View):
    template_name = 'pedido/pagar.html'

    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            messages.error(
                self.request,
                'Faça o login e retorne ao carrinho.'
            )
            return redirect('perfil:criar')

        carrinho = self.request.session.get('carrinho')

        if not carrinho:
            messages.info(
                self.request,
                'Seu carrinho ainda está vazio.'
            )
            return redirect('produto:lista')

        carrinho_variacao_id = [v for v in carrinho]
        bd_variacoes = list(
            Variacao.objects.select_related('produto').filter(id__in=carrinho_variacao_id)
        )

        for variacao in bd_variacoes:
            vid = str(variacao.pk)
            estoque = variacao.estoque
            qtd_carrinho = carrinho[vid]['quantidade']
            preco_unit = carrinho[vid]['preco_unitario']
            preco_unit_promo = carrinho[vid]['preco_unitario_promocional']
            error_message_estoque = ''

            if estoque < qtd_carrinho:
                carrinho[vid]['quantidade'] = estoque
                carrinho[vid]['preco_quantitativo'] = estoque * preco_unit
                carrinho[vid]['preco_quantitativo_promocional'] = estoque * preco_unit_promo
                error_message_estoque = 'Estoque insuficiente para alguns produtos do seu carrinho. Reduzimos a quantidade desses produtos. Por favor, verifique quais produtos foram afetados a seguir.'

        if error_message_estoque:
            messages.error(
                self.request,
                error_message_estoque
            )

            self.request.session.save()
            return redirect('produto:carrinho')

        qtd_total_carrinho = utils.cart_qtd_total(carrinho)
        valor_total_carrinho = utils.cart_totals(carrinho)

        pedido = Pedido(
            usuario=self.request.user,
            total=valor_total_carrinho,
            qtd_total=qtd_total_carrinho,
            status='C',
        )

        pedido.save()

        ItemPedido.objects.bulk_create(
            [
                ItemPedido(
                    pedido = pedido,
                    produto = v['produto_nome'],
                    produto_id =  v['produto_id'],
                    variacao =  v['variacao_nome'],
                    variacao_id =  v['variacao_id'],
                    preco =  v['preco_quantitativo'],
                    preco_promocional =  v['preco_quantitativo_promocional'],
                    quantidade =  v['quantidade'],
                    imagem =  v['imagem'],
                ) for v in carrinho.values()
            ]
        )

        contexto = {}

        del self.request.session['carrinho']
        return redirect(
            reverse(
                'pedido:pagar',
                kwargs={
                    'pk': pedido.pk
                }
            )
        )


class Pagar(DispatchLoginRequired, DetailView):
    template_name = 'pedido/pagar.html'
    model = Pedido
    pk_url_kwarg = 'pk'
    context_object_name = 'pedido'

    def get_queryset(self, *args, **kwargs) -> QuerySet[Any]:
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(usuario=self.request.user)

        return qs


class Detalhe(View):
    def get(self, *args, **kwargs):
        return HttpResponse('DETALHE')

class Status(View):
    def get(self, *args, **kwargs):
        return HttpResponse('STATUS')
