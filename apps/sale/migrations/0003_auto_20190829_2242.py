# Generated by Django 2.2.4 on 2019-08-30 02:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0072_auto_20190829_0138'),
        ('sale', '0002_auto_20190829_2240'),
    ]

    operations = [
        migrations.CreateModel(
            name='PySaleOrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(blank=True, default=True, null=True)),
                ('fc', models.DateTimeField(auto_now_add=True, null=True)),
                ('fm', models.DateTimeField(auto_now=True, null=True)),
                ('uc', models.IntegerField(blank=True, null=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('quantity', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('amount_untaxed', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('amount_taxt', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('amount_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.PyProduct')),
                ('sale_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sale.PySaleOrder')),
            ],
        ),
        migrations.AddConstraint(
            model_name='pysaleorderdetail',
            constraint=models.UniqueConstraint(fields=('sale_order', 'product'), name='product_order_unique'),
        ),
    ]