# Generated by Django 2.1.4 on 2019-03-02 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0008_auto_20190302_2038'),
    ]

    operations = [
        migrations.CreateModel(
            name='docto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='doctor/static/css')),
                ('photoname', models.TextField()),
                ('name', models.TextField()),
                ('information', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='doctor',
        ),
    ]