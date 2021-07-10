# Generated by Django 3.2.3 on 2021-07-05 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_imagealbum_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='album',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='core.imagealbum'),
        ),
    ]
