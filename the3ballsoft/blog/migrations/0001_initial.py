# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-04 18:12
from __future__ import unicode_literals

import autoslug.fields
import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import versatileimagefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
                ('subtitle', models.CharField(blank=True, max_length=500)),
                ('photo', versatileimagefield.fields.VersatileImageField(upload_to='img/articles')),
                ('content', ckeditor.fields.RichTextField()),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='fecha de modificacion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
