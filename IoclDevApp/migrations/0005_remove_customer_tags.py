# Generated by Django 4.0.7 on 2022-09-22 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IoclDevApp', '0004_remove_tag_emergencycontectperson_ph_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='tags',
        ),
    ]
