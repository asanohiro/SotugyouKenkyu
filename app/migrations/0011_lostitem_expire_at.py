# Generated by Django 4.2.16 on 2024-12-04 04:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_chatroom_user_remove_lostitem_expire_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lostitem',
            name='expire_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 3, 4, 49, 5, 408150, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
