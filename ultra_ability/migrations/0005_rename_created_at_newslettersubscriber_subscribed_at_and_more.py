# Generated by Django 4.0.6 on 2025-02-18 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ultra_ability', '0004_newslettersubscriber_delete_subscriber'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newslettersubscriber',
            old_name='created_at',
            new_name='subscribed_at',
        ),
        migrations.RemoveField(
            model_name='newslettersubscriber',
            name='full_name',
        ),
        migrations.AddField(
            model_name='newslettersubscriber',
            name='name',
            field=models.CharField(default='subscriber', max_length=100),
            preserve_default=False,
        ),
    ]
