from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE,verbose_name=('user'))
	name = models.CharField(max_length=200, null=True,verbose_name=('name'))
	email = models.CharField(max_length=200,verbose_name=('email'))
 
	class Meta:
		verbose_name = _('client')
		verbose_name_plural = _('clients')

	def __str__(self):
		return self.name


class Product(models.Model):
	name = models.CharField(max_length=200, verbose_name=('name'))
	price = models.FloatField()
	category = models.CharField(max_length=200, null=True, verbose_name=('category') )
	available = models.BooleanField(default=False,null=True, blank=True, verbose_name=('available'))
	image = models.ImageField(null=True, blank=True)
	class Meta:
		verbose_name = _('produit')
		verbose_name_plural = _('produits')

	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url

class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=('customer'))
	date_ordered = models.DateTimeField(auto_now_add=True, verbose_name=('date_ordered'))
	complete = models.BooleanField(default=False, verbose_name=('complete'))
	transaction_id = models.CharField(max_length=100, null=True, verbose_name=('transaction_id'),)

		
	class Meta:
		verbose_name = _('commande')
		verbose_name_plural = _('commandes')


	def __str__(self):
		return str(self.id)
		
	@property
	def shipping(self):
		shipping = False
		orderitems = self.orderitem_set.all()
		for i in orderitems:
			if i.product.digital == False:
				shipping = True
		return shipping

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total 

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total 

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, verbose_name=('product'))
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, verbose_name=('order'))
	quantity = models.IntegerField(default=0, null=True, blank=True, verbose_name=('quantity') )

	date_added = models.DateTimeField(auto_now_add=True)
	class Meta:
		verbose_name = _('article commandé')
		verbose_name_plural = _('articles commandés')

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, verbose_name=('customer'))
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, verbose_name=('order'))
	address = models.CharField(max_length=200, null=False, verbose_name=('address') )
	city = models.CharField(max_length=200, null=False, verbose_name=('city'))
	state = models.CharField(max_length=200, null=False, verbose_name=('state'))
	zipcode = models.CharField(max_length=200, null=False, verbose_name=('zipcode'))
	date_added = models.DateTimeField(auto_now_add=True, verbose_name=('date_added'))
    
	class Meta:
		verbose_name = _('Adresse de livraison')
		verbose_name_plural = _('Addresses de livraison')


	def __str__(self):
		return self.address