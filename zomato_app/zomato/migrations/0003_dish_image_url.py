# Generated by Django 4.2.4 on 2023-08-13 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zomato', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='image_url',
            field=models.CharField(default='https://placehold.co/400', max_length=255),
        ),
    ]
