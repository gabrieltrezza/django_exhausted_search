# Generated by Django 3.2.9 on 2021-11-30 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0024_dealer'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpost',
            name='zipCode',
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
    ]
