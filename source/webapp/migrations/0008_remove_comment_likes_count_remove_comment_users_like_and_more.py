# Generated by Django 5.0.1 on 2024-02-08 17:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_alter_comment_author_alter_comment_post'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='likes_count',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='users_like',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='users_like',
        ),
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(related_name='loved_comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='publication',
            name='users_likes',
            field=models.ManyToManyField(related_name='loved_articles', to=settings.AUTH_USER_MODEL),
        ),
    ]
