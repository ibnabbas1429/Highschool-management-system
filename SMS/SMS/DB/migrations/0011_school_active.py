# Generated by Django 2.2.5 on 2020-04-02 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DB', '0010_auto_20200330_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]