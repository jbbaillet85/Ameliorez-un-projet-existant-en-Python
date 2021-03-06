# Generated by Django 3.2.7 on 2021-11-30 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('pnns_groups_1', models.CharField(
                    max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(
                    default='pas de nom de produit', max_length=150)),
                ('nutriscore_grade', models.CharField(
                    default='0', max_length=1)),
                ('image_url', models.ImageField(default='', upload_to='')),
                ('ingredients_text', models.TextField(
                    default="pas d'ingrédients renseignés")),
                ('url', models.URLField(unique=True)),
                ('pnns_groups_1', models.ForeignKey(
                    default='', on_delete=django.db.models.deletion.CASCADE,
                    to='products.category')),
            ],
        ),
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='products.product')),
            ],
        ),
    ]
