# Generated by Django 2.2.1 on 2022-04-10 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_products'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cartlist')),
                ('prodt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.products')),
            ],
        ),
    ]
