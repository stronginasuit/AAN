# Generated by Django 3.2.8 on 2021-10-31 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='walletdb',
            name='nft_contract',
            field=models.CharField(max_length=20000),
        ),
        migrations.AlterField(
            model_name='walletdb',
            name='private_key',
            field=models.CharField(max_length=20000),
        ),
        migrations.AlterField(
            model_name='walletdb',
            name='wallet_address',
            field=models.CharField(max_length=20000),
        ),
    ]
