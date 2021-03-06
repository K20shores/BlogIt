# Generated by Django 2.0.3 on 2018-03-30 05:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_auto_20180323_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='blog_author_user',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='blog_author',
            field=models.CharField(max_length=128),
        ),
    ]
