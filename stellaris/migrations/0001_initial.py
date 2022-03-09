# Generated by Django 3.2.9 on 2022-03-08 14:23

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
                ('slug', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='images/category')),
                ('description', models.TextField(max_length=500)),
                ('availability', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(upload_to='images/gallery')),
                ('date_taken', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Gallery',
                'get_latest_by': 'date_taken',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('product_image', models.ImageField(upload_to='images/foods')),
                ('description', models.CharField(max_length=250)),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('availability', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stellaris.category')),
            ],
        ),
    ]
