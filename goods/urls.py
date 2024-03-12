from django.urls import path
from goods.views import GoodsListView, ProductDetailView

app_name = 'goods'

urlpatterns = [
    path('', GoodsListView.as_view(), name='index'),
    path('product/', ProductDetailView.as_view(), name='product')
]