# Generated by Django 4.1.3 on 2022-11-23 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_alter_useranime_watchlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useranime',
            name='watchlist',
            field=models.BooleanField(null=True),
        ),
    ]
