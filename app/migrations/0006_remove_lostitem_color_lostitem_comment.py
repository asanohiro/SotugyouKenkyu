# Generated by Django 4.2.16 on 2024-11-20 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_lostitem_location_remove_lostitem_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lostitem',
            name='color',
        ),
        migrations.AddField(
            model_name='lostitem',
            name='comment',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
