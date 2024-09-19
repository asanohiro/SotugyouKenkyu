# Generated by Django 5.0.6 on 2024-08-12 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lostitem',
            old_name='comment',
            new_name='description',
        ),
        migrations.AddField(
            model_name='lostitem',
            name='status',
            field=models.CharField(default='unclaimed', max_length=50),
        ),
    ]