# Generated by Django 2.0.3 on 2019-09-19 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20190918_0041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='id',
        ),
        migrations.AlterField(
            model_name='client',
            name='username',
            field=models.CharField(max_length=64, primary_key=True, serialize=False, unique=True),
        ),
    ]
