# Generated by Django 2.1.4 on 2019-03-02 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0007_auto_20190302_2037'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='docto',
            new_name='doctor',
        ),
    ]