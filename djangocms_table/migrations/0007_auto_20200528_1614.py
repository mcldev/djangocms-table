# Generated by Django 2.2.12 on 2020-05-28 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_table', '0006_auto_20200528_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablemodel',
            name='name',
            field=models.TextField(blank=True, null=True, verbose_name='name'),
        ),
    ]