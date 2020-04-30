# Generated by Django 2.2.5 on 2020-02-23 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_argent', models.CharField(help_text='User agent. We can use this to determine operating system and browser in use.', max_length=2000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('ip', models.GenericIPAddressField()),
                ('usage', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('value', models.TextField(blank=True)),
                ('file', models.FileField(blank=True, help_text='Some configuration options are file uploads', null=True, upload_to='configuration_files')),
                ('help_text', models.TextField(blank=True)),
            ],
        ),
    ]