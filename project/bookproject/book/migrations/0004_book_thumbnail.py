# Generated by Django 4.2.11 on 2024-05-02 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
