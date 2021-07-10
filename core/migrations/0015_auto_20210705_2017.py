# Generated by Django 3.2.3 on 2021-07-05 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_alter_image_album'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='core.imagealbum'),
        ),
        migrations.AlterField(
            model_name='project',
            name='album',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='album', to='core.imagealbum'),
        ),
    ]