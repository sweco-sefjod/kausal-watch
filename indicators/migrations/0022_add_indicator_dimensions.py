# Generated by Django 3.0.6 on 2020-05-18 11:30

import aplans.utils
from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models


class Migration(migrations.Migration):

    dependencies = [
        ('django_orghierarchy', '0009_add_organization_distinct_name'),
        ('indicators', '0021_add_dataset_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommonIndicator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', aplans.utils.IdentifierField(max_length=50, validators=[aplans.utils.IdentifierValidator()], verbose_name='identifier')),
                ('quantity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='common_indicators', to='indicators.Quantity', verbose_name='quantity')),
            ],
            options={
                'abstract': False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Dimension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'dimension',
                'verbose_name_plural': 'dimensions',
                'ordering': ('id',),
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='DimensionCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='order')),
                ('dimension', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indicators.Dimension')),
            ],
            options={
                'verbose_name': 'dimension category',
                'verbose_name_plural': 'dimension categories',
                'ordering': ['dimension', 'order'],
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.AlterModelOptions(
            name='dataset',
            options={'verbose_name': 'dataset', 'verbose_name_plural': 'datasets'},
        ),
        migrations.AlterModelOptions(
            name='datasetlicense',
            options={'verbose_name': 'dataset license', 'verbose_name_plural': 'dataset licenses'},
        ),
        migrations.AddField(
            model_name='indicator',
            name='org',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='indicators', to='django_orghierarchy.Organization', verbose_name='organization'),
        ),
        migrations.AlterField(
            model_name='indicator',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='indicator',
            name='common_indicator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='indicators', to='indicators.CommonIndicator'),
        ),
        migrations.AddField(
            model_name='quantity',
            name='units',
            field=models.ManyToManyField(blank=True, to='indicators.Unit', verbose_name='units'),
        ),
        migrations.CreateModel(
            name='IndicatorDimension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='order')),
                ('dimension', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='indicators', to='indicators.Dimension')),
                ('indicator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dimensions', to='indicators.Indicator')),
            ],
            options={
                'verbose_name': 'indicator dimensino',
                'verbose_name_plural': 'indicator dimensions',
                'ordering': ['indicator', 'order'],
                'unique_together': {('indicator', 'dimension')},
            },
        ),
        migrations.CreateModel(
            name='DimensionTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=100)),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='indicators.Dimension')),
            ],
            options={
                'verbose_name': 'dimension Translation',
                'db_table': 'indicators_dimension_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='DimensionCategoryTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=100)),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='indicators.DimensionCategory')),
            ],
            options={
                'verbose_name': 'dimension category Translation',
                'db_table': 'indicators_dimensioncategory_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CommonIndicatorTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='indicators.CommonIndicator')),
            ],
            options={
                'verbose_name': 'common indicator Translation',
                'db_table': 'indicators_commonindicator_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]
