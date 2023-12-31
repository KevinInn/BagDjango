# Generated by Django 4.1.7 on 2023-07-25 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_bag_category_bag_note_bag_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pId', models.IntegerField()),
                ('picture', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pId', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('brand', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('size', models.CharField(default=' ', max_length=100)),
                ('likes', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Bag',
        ),
    ]
