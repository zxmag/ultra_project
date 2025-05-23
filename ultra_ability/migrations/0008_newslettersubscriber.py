# Generated by Django 4.0.6 on 2025-02-22 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ultra_ability', '0007_delete_newslettersubscriber'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsletterSubscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('subscribed_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
