# Generated by Django 3.2.6 on 2021-11-03 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0008_remove_recipe_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='img',
            field=models.ImageField(default='default.jpg', upload_to='recipe_imgs'),
        ),
    ]
