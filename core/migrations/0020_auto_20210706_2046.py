# Generated by Django 3.2.3 on 2021-07-06 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_rename_length_image_height'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='height',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='width',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
