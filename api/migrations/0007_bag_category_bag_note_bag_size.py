# Generated by Django 4.1.7 on 2023-07-22 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_bag_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='bag',
            name='category',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AddField(
            model_name='bag',
            name='note',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AddField(
            model_name='bag',
            name='size',
            field=models.CharField(default=' ', max_length=100),
        ),
    ]
