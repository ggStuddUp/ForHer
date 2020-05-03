# Generated by Django 3.0.5 on 2020-05-03 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataCenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(blank=True, max_length=40)),
                ('stime', models.CharField(max_length=30)),
                ('product', models.CharField(blank=True, max_length=40)),
                ('iver', models.CharField(blank=True, max_length=20)),
                ('mid', models.CharField(blank=True, max_length=100)),
                ('uid', models.CharField(blank=True, max_length=500)),
                ('ip', models.CharField(blank=True, max_length=30)),
            ],
            options={
                'verbose_name': '数据',
                'verbose_name_plural': '数据',
            },
        ),
    ]
