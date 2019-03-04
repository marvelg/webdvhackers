# Generated by Django 2.0.2 on 2019-03-04 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_footer'),
    ]

    operations = [
        migrations.CreateModel(
            name='portfolioCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectImage', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('projectName', models.CharField(blank=True, max_length=150, null=True)),
                ('projectCategory', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]