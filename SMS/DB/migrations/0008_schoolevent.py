# Generated by Django 2.2.5 on 2020-01-09 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DB', '0007_term_term_ends_on'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('term', models.CharField(blank=True, choices=[('ONE', 'One'), ('TWO', 'Two'), ('THREE', 'Three')], max_length=10, null=True)),
                ('starts_on', models.DateField()),
                ('ends_on', models.DateField(blank=True, null=True)),
                ('academic_year', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='DB.AcademicYear')),
            ],
        ),
    ]