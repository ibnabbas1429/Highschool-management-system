# Generated by Django 2.2.5 on 2020-01-11 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DB', '0016_auto_20200111_0534'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='address',
            field=models.ForeignKey(blank=True, default='1', on_delete=django.db.models.deletion.CASCADE, to='DB.Address'),
            preserve_default=False,
        ),
    ]