# Generated by Django 4.1.3 on 2022-11-22 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_remove_useranime_notes_useranime_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='grade',
            field=models.CharField(max_length=100),
        ),
    ]
