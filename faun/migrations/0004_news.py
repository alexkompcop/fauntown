# Generated by Django 2.1.4 on 2019-03-04 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faun', '0003_auto_20190303_2304'),
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True)),
                ('article', models.TextField(blank=True)),
            ],
        ),
    ]