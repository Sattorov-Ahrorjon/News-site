# Generated by Django 4.1.7 on 2023-03-03 12:59

import ckeditor.fields
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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65)),
                ('slug', models.SlugField(default='', editable=False, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='NewImagePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(default='', editable=False, max_length=250)),
                ('body', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('published_time', models.DateTimeField(auto_now=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('DFDraft', 'Draft'), ('PBPublished', 'Published')], default='DFDraft', max_length=20)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='new.category')),
            ],
            options={
                'ordering': ['-published_time'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='Leave a comment')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comments', to='new.newimagepost')),
            ],
            options={
                'ordering': ['created_time'],
            },
        ),
    ]
