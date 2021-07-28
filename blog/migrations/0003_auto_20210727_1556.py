# Generated by Django 3.2.5 on 2021-07-27 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(default='comment'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='content',
            field=models.TextField(default='comment'),
            preserve_default=False,
        ),
    ]
