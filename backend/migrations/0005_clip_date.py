# Generated by Django 4.1.1 on 2022-10-25 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_remove_tag_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='clip',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]