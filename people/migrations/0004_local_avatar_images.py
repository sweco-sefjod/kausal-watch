# Generated by Django 2.2.4 on 2019-09-17 15:57

import aplans.model_images
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_make_person_email_non_nullable'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='avatar_updated_at',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='image',
            field=models.ImageField(blank=True, height_field='image_height', upload_to=aplans.model_images.image_upload_path, verbose_name='image', width_field='image_width'),
        ),
        migrations.AddField(
            model_name='person',
            name='image_cropping',
            field=image_cropping.fields.ImageRatioField('image', '1280x720', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='image cropping'),
        ),
        migrations.AddField(
            model_name='person',
            name='image_height',
            field=models.PositiveIntegerField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='image_width',
            field=models.PositiveIntegerField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='user',
            field=models.OneToOneField(blank=True, editable=False, help_text='Set if the person has an user account', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='person', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]
