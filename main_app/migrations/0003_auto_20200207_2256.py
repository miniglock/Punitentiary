# Generated by Django 3.0.2 on 2020-02-07 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20200207_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joke',
            name='punchline',
            field=models.CharField(max_length=300, null=True),
        ),
    ]