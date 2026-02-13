from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class Pagar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('PAGAR')


class SalvarPedido(View):
    def get(self, *args, **kwargs):
        return HttpResponse('PFECHAR PEDIDO')


class Detalhe(View):
    def get(self, *args, **kwargs):
        return HttpResponse('DETALHE')
