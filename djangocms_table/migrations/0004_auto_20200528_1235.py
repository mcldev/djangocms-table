# Generated by Django 2.2.12 on 2020-05-28 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_table', '0003_auto_20200528_1229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tablemodel',
            old_name='headers_bottom',
            new_name='footer_rows',
        ),
        migrations.RenameField(
            model_name='tablemodel',
            old_name='headers_left',
            new_name='header_rows_left',
        ),
        migrations.RenameField(
            model_name='tablemodel',
            old_name='headers_top',
            new_name='header_rows_top',
        ),
    ]