# Generated by Django 2.2.5 on 2020-04-22 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DB', '0017_auto_20200422_0759'),
        ('schedule', '0026_auto_20200422_0813'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='period',
            options={'ordering': ('-sort_order',)},
        ),
        migrations.RemoveField(
            model_name='subjectperiod',
            name='course',
        ),
        migrations.AddField(
            model_name='subjectperiod',
            name='subject',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='DB.Subject'),
            preserve_default=False,
        ),
    ]