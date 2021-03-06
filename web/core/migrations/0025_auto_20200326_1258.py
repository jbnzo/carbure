# Generated by Django 3.0.3 on 2020-03-26 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_lot_ghg_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='lot',
            name='ea_override',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='lot',
            name='ea_overriden',
            field=models.BooleanField(default=False),
        ),
    ]
