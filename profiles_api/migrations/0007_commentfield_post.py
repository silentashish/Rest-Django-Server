# Generated by Django 2.1.3 on 2018-12-28 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0006_commentfield'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentfield',
            name='post',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='profiles_api.ProfilesFeedItem'),
        ),
    ]
