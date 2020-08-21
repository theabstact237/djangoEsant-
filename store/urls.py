from django.urls import path

from . import views
from .views import ProductDetailView

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	 path('boutique/', views.contact, name="boutique"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    path('contact/', views.contact, name="contact"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
    path('product_detail/', views.ProductDetailView.as_view(), name="detail"),

]