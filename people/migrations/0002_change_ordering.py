# Generated by Django 2.2.4 on 2019-09-12 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ('last_name', 'first_name'), 'verbose_name': 'person', 'verbose_name_plural': 'people'},
        ),
    ]
