# Generated by Django 4.1.7 on 2023-07-25 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_picture_product_delete_bag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='pId',
        ),
        migrations.RemoveField(
            model_name='picture',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='product',
            name='age',
        ),
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='product',
            name='name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='pId',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
    ]
