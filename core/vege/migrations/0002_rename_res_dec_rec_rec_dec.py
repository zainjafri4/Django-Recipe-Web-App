# Generated by Django 4.2.6 on 2023-10-14 00:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rec',
            old_name='res_dec',
            new_name='rec_dec',
        ),
    ]
