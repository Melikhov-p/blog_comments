# Generated by Django 3.2.5 on 2021-07-27 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210727_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='blog.article'),
            preserve_default=False,
        ),
    ]
