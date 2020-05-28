# Generated by Django 2.2.12 on 2020-05-28 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_table', '0005_auto_20200528_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='tablemodel',
            name='body_row_classes',
            field=models.TextField(blank=True, verbose_name='Body Row Classes'),
        ),
        migrations.AddField(
            model_name='tablemodel',
            name='cell_classes',
            field=models.TextField(blank=True, verbose_name='Cell Classes'),
        ),
        migrations.AddField(
            model_name='tablemodel',
            name='footer_row_classes',
            field=models.TextField(blank=True, verbose_name='Footer Row Classes'),
        ),
        migrations.AddField(
            model_name='tablemodel',
            name='header_cell_classes',
            field=models.TextField(blank=True, verbose_name='Header Cell Classes'),
        ),
        migrations.AddField(
            model_name='tablemodel',
            name='header_row_classes',
            field=models.TextField(blank=True, verbose_name='Header Row Classes'),
        ),
        migrations.AddField(
            model_name='tablemodel',
            name='table_classes',
            field=models.TextField(blank=True, default='table table-hover', verbose_name='Table Classes'),
        ),
        migrations.AddField(
            model_name='tablemodel',
            name='table_settings',
            field=models.TextField(blank=True, verbose_name='Table Settings'),
        ),
    ]
