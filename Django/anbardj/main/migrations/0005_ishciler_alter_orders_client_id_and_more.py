# Generated by Django 4.1.1 on 2022-10-31 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_orders_tesdiq'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ishciler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=35, verbose_name='ad')),
                ('soyad', models.CharField(max_length=35, verbose_name='soyad')),
                ('telefon', models.CharField(max_length=35, verbose_name='telefon')),
                ('ev_tel', models.CharField(max_length=35, verbose_name='ev_tel')),
                ('unvan', models.CharField(max_length=35, verbose_name='unvan')),
                ('email', models.CharField(max_length=35, verbose_name='email')),
                ('vezife', models.CharField(max_length=35, verbose_name='vezife')),
                ('data_ishciler', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='orders',
            name='client_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.clients'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.products'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='tesdiq',
            field=models.IntegerField(verbose_name='tesdiq'),
        ),
    ]
