# Generated by Django 3.1.7 on 2021-12-23 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20211223_1441'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterBlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=100)),
            ],
        ),
    ]