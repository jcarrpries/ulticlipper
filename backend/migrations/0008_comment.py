# Generated by Django 4.1.1 on 2023-02-05 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_alter_tag_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=280)),
                ('timestamp', models.IntegerField()),
                ('annotation', models.CharField(max_length=65000)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.video')),
            ],
            options={
                'ordering': ['timestamp'],
            },
        ),
    ]
