# Generated by Django 5.1.2 on 2024-11-08 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_test_weaviate_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='cluster',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
