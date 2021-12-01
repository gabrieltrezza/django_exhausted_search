# Generated by Django 3.2.9 on 2021-11-29 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_delete_dealerships'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dealership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dealerName', models.CharField(max_length=255, verbose_name='dealerName')),
                ('zipCode', models.CharField(max_length=255, verbose_name='zipCode')),
                ('state', models.CharField(max_length=5, verbose_name='state')),
                ('address', models.CharField(max_length=350, verbose_name='address')),
                ('ids', models.IntegerField(verbose_name='ids')),
            ],
        ),
    ]
