# Generated by Django 3.1 on 2023-06-22 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0004_hallityomaa_lumiesteidenasennus_rengashalli_rivitaloremontti'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ravitalonsahko',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=100, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.RemoveField(
            model_name='referencemedia',
            name='date',
        ),
        migrations.AlterField(
            model_name='hallityomaa',
            name='text',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='lumiesteidenasennus',
            name='text',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='referencemedia',
            name='text',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='rengashalli',
            name='text',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='rivitaloremontti',
            name='text',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
