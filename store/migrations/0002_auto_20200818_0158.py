# Generated by Django 3.0.8 on 2020-08-17 23:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'customer', 'verbose_name_plural': 'customers'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'order', 'verbose_name_plural': 'orders'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
        migrations.AlterModelOptions(
            name='shippingaddress',
            options={'verbose_name': 'shippin Address', 'verbose_name_plural': 'shipping Addresses'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='digital',
        ),
        migrations.AddField(
            model_name='product',
            name='available',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='available'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=200, null=True, verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(max_length=200, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=200, null=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='order',
            name='complete',
            field=models.BooleanField(default=False, verbose_name='complete'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.Customer', verbose_name='customer'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_ordered',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date_ordered'),
        ),
        migrations.AlterField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(max_length=100, null=True, verbose_name='transaction_id'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.Order', verbose_name='order'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.Product', verbose_name='product'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='quantity'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='address',
            field=models.CharField(max_length=200, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='city',
            field=models.CharField(max_length=200, verbose_name='city'),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.Customer', verbose_name='customer'),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date_added'),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.Order', verbose_name='order'),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='state',
            field=models.CharField(max_length=200, verbose_name='state'),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='zipcode',
            field=models.CharField(max_length=200, verbose_name='zipcode'),
        ),
    ]
