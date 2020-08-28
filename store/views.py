from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import json
import datetime
from .models import * 
from .utils import cookieCart, cartData, guestOrder
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
	
)
from django.core.mail import send_mail
from .models import Product

class ProductDetailView(DetailView):
    model = Product

def CategoryView(request, cats):
	category_products = Product.objects.filter(category=cats)

	cat_menu = Category.objects.all()
	return render(request, 'store/categories.html', {'cats':cats.title(), 'category_products':category_products, 'cat_menu':cat_menu })



def store(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	cat_menu = Category.objects.all()

	products = Product.objects.all()
	context = {'products':products, 'cartItems':cartItems,'cat_menu':cat_menu}
	return render(request, 'store/accueil.html', context)

def boutique(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	cat_menu = Category.objects.all()
	
	products = Product.objects.all()
	context = {'products':products, 'items':items, 'order':order, 'cartItems':cartItems,'cat_menu':cat_menu }
	return render(request, 'store/boutique.html', context)

def propos(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	cat_menu = Category.objects.all()
	
	products = Product.objects.all()
	context = {'products':products, 'items':items, 'order':order, 'cartItems':cartItems,'cat_menu':cat_menu }
	return render(request, 'store/propos.html', context)

def cgv(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	cat_menu = Category.objects.all()

	products = Product.objects.all()
	context = {'products':products, 'items':items, 'order':order, 'cartItems':cartItems,'cat_menu':cat_menu }
	return render(request, 'store/conditions-generales-de-vente.html', context)
    
def cart(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	cat_menu = Category.objects.all()
	
	context = {'items':items, 'order':order, 'cartItems':cartItems,'cat_menu':cat_menu }
	return render(request, 'store/cart.html', context)
def politique(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	cat_menu = Category.objects.all()
	
	products = Product.objects.all()
	context = {'products':products, 'items':items, 'order':order, 'cartItems':cartItems,'cat_menu':cat_menu }
	return render(request, 'store/politique-de-confidentialite.html', context)
def retour(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	cat_menu = Category.objects.all()
	
	products = Product.objects.all()
	context = {'products':products, 'items':items, 'order':order, 'cartItems':cartItems,'cat_menu':cat_menu }
	return render(request, 'store/politique-de-retour.html', context)
def paiement(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	cat_menu = Category.objects.all()
	
	products = Product.objects.all()
	context = {'products':products, 'items':items, 'order':order, 'cartItems':cartItems,'cat_menu':cat_menu }
	return render(request, 'store/paiement-et-livraison.html', context)

def faq(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	cat_menu = Category.objects.all()
	
	products = Product.objects.all()
	context = {'products':products, 'items':items, 'order':order, 'cartItems':cartItems,'cat_menu':cat_menu }
	return render(request, 'store/faq.html', context)


def contact(request):
	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	cat_menu = Category.objects.all()

	context = {'items':items, 'order':order, 'cartItems':cartItems,'cat_menu':cat_menu }
	if request.method =="POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message_name = request.POST['message']
		send_mail( 
					message_name,#name
					message,#message
					message_email,#FromEmail
					['siakatayoukarlwilliam@gmail.com','alkainfri@gmail.com']#ToEmail
					)

	   
		return render(request, 'store/contact.html',{'message_name'})
	else:
		return render(request, 'store/contact.html', context)

def checkout(request):
	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('article ajouté', safe=False)

def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		country=data['shipping']['country'],
		zipcode=data['shipping']['zipcode'],
		)

	return JsonResponse('Payement transmit..', safe=False)