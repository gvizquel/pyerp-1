# Generated by Django 2.2.4 on 2019-09-15 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_auto_20190914_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='pycompany',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]