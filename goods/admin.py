from django.contrib import admin

from goods.models import Goods, GoodsCategory

admin.site.register(Goods)
admin.site.register(GoodsCategory)
