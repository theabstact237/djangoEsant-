from django.urls import path

from . import views
from .views import ProductDetailView, CategoryView

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path('boutique/', views.boutique, name="boutique"),
	path('propos/', views.propos, name="propos"),
	path('conditions-générales-de-ventes/', views.cgv, name="conditions-générales-de-ventes"),
	path('paiement-et-livraison/', views.paiement, name="paiement-et-livraison"),
	path('faq/', views.faq, name="faq"),
    path('politique-de-retour/', views.retour, name="politique-de-retour"),
	path('politique-de-confidentialité/', views.politique, name="politique-de-confidentialité"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    path('contact/', views.contact, name="contact"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
    path('store/<int:pk>/', views.ProductDetailView.as_view(), name="product_detail"),
    path('category/<str:cats>/', views.CategoryView, name="category"), 
]