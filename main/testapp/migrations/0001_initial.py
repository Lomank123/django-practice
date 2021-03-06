# Generated by Django 4.0.3 on 2022-06-05 06:43

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
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='Last update')),
                ('name', models.CharField(max_length=120, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='Last update')),
                ('name', models.CharField(max_length=120, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='Last update')),
                ('name', models.CharField(max_length=120, verbose_name='Name')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.category', verbose_name='Category')),
                ('tag', models.ManyToManyField(blank=True, to='testapp.tag', verbose_name='Tag')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Items',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='Last update')),
                ('text', models.CharField(max_length=360, verbose_name='Text')),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='testapp.item', verbose_name='Item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
                'ordering': ['-id'],
            },
        ),
    ]
