# Generated by Django 4.1.1 on 2023-02-27 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_userdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='clip',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clips', to='backend.team'),
        ),
        migrations.AddField(
            model_name='comment',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='backend.team'),
        ),
        migrations.AddField(
            model_name='tag',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='backend.team'),
        ),
        migrations.AddField(
            model_name='taggroup',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tag_groups', to='backend.team'),
        ),
        migrations.AddField(
            model_name='video',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='backend.team'),
        ),
        migrations.AlterField(
            model_name='invitecode',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='active_codes', to='backend.team'),
        ),
    ]