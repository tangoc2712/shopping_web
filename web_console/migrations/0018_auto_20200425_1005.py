# Generated by Django 3.1.dev20200307214613 on 2020-04-25 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_console', '0017_auto_20200424_0320'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='order',
            name='country',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='order',
            name='orderNote',
            field=models.CharField(default='No note', max_length=200),
        ),
    ]
