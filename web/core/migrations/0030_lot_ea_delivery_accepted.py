# Generated by Django 3.0.3 on 2020-04-01 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_auto_20200330_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='lot',
            name='ea_delivery_accepted',
            field=models.BooleanField(default=False),
        ),
    ]
