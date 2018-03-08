# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-08 08:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.URLField(blank=True)),
                ('picture', models.ImageField(blank=True, upload_to='profile_images')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CoffeeBean',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('location', models.CharField(max_length=128)),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('price', models.FloatField(blank=True, default=None, null=True)),
                ('average_rating', models.FloatField(default=0)),
                ('t_type', models.CharField(blank=True, max_length=128)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'ordering': ('average_rating',),
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('favourite_coffee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bean_app.CoffeeBean')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('comment', models.TextField(blank=True, max_length=240)),
                ('coffee_bean', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bean_app.CoffeeBean')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bean_app.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='SignupForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(default=0)),
                ('coffee_bean', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='bean_app.CoffeeBean')),
            ],
        ),
        migrations.CreateModel(
            name='TagType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saved_coffees', models.ManyToManyField(to='bean_app.CoffeeBean')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('business_name', models.CharField(max_length=128, unique=True)),
                ('url_online_shop', models.URLField(blank=True)),
                ('address', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('lat', models.FloatField(blank=True, default=None)),
                ('long', models.FloatField(blank=True, default=None)),
                ('products_in_stock', models.ManyToManyField(to='bean_app.CoffeeBean')),
            ],
        ),
        migrations.CreateModel(
            name='VendorAccountForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.URLField(blank=True)),
                ('picture', models.ImageField(blank=True, upload_to='profile_images')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VendorSignupForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='tag',
            name='tag_type',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='bean_app.TagType'),
        ),
    ]