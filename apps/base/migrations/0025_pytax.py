# Generated by Django 2.2.4 on 2019-09-15 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0024_pyproduct_uom_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='PyTax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(blank=True, default=True, null=True)),
                ('fc', models.DateTimeField(auto_now_add=True, null=True)),
                ('fm', models.DateTimeField(auto_now=True, null=True)),
                ('uc', models.IntegerField(blank=True, null=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('company_id', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Amount')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
