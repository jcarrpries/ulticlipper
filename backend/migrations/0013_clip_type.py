# Generated by Django 4.1.1 on 2023-03-28 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0012_tag_type_tag_value_taggroup_type_alter_tag_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='clip',
            name='type',
            field=models.CharField(choices=[('generated', 'Generated'), ('custom', 'Custom')], default='generated', max_length=20),
        ),
    ]
