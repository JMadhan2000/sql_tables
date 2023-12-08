# Generated by Django 4.2.6 on 2023-12-08 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bonus',
            fields=[
                ('emp_no', models.IntegerField(primary_key=True, serialize=False)),
                ('job', models.CharField(max_length=100)),
                ('sal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='salgrade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(max_length=100)),
                ('place_of_work', models.CharField(max_length=100)),
                ('emp_no', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.bonus')),
            ],
        ),
    ]
