# Generated by Django 3.0.7 on 2020-07-11 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
