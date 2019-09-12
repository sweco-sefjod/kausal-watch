# Generated by Django 2.2.4 on 2019-09-12 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_change_ordering'),
        ('actions', '0021_change_ordering'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='contact_persons',
            field=models.ManyToManyField(blank=True, related_name='contact_for_actions_old', to='people.Person', verbose_name='contact persons'),
        ),
        migrations.CreateModel(
            name='ActionContactPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='order')),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actions.Action', verbose_name='action')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.Person', verbose_name='person')),
            ],
            options={
                'verbose_name': 'action contact person',
                'verbose_name_plural': 'action contact persons',
                'ordering': ['action', 'order'],
                'unique_together': {('action', 'person')},
                'index_together': {('action', 'order')},
            },
        ),
        migrations.AddField(
            model_name='action',
            name='contact_persons_ordered',
            field=models.ManyToManyField(blank=True, related_name='contact_for_actions', through='actions.ActionContactPerson', to='people.Person', verbose_name='contact persons'),
        ),
    ]
