from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from goods.models import Goods
from django.http import HttpResponse
from django.shortcuts import render


class IndexView(TemplateView):
    template_name = 'goods/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['title'] = 'Home'
        return context


class GoodsListView(ListView):
    template_name = 'goods/catalog.html'
    model = Goods

    def get_context_data(self, **kwargs):
        context = super(GoodsListView, self).get_context_data()
        context['title'] = 'Goods'
        return context


class ProductDetailView(ListView):
    template_name = 'goods/product.html'
    model = Goods

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data()
        context['title'] = 'Product'
        return context
