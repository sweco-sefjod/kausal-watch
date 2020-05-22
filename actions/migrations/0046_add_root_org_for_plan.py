# Generated by Django 3.0.6 on 2020-05-18 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_orghierarchy', '0009_add_organization_distinct_name'),
        ('actions', '0045_internal_priority_can_be_blank'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='root_org',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='django_orghierarchy.Organization', verbose_name='root organization'),
        ),
    ]
