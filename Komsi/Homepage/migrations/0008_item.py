# Generated by Django 4.2.7 on 2023-11-25 13:09

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0007_hietaniemenkadulta_alter_hallityomaa_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', embed_video.fields.EmbedVideoField()),
            ],
        ),
    ]
