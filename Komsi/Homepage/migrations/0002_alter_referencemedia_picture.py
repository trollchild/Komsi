# Generated by Django 4.1.3 on 2022-11-26 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referencemedia',
            name='picture',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
