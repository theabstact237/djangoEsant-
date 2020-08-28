from django.contrib import admin

from .models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Category)
admin.site.index_title = ('Panneau de control')
admin.site.site_header = ('plateforme Administration du site web ')
admin.site.site_title = ('gestion du site')