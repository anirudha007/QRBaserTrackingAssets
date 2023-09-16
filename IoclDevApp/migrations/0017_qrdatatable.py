# Generated by Django 4.0.7 on 2023-09-13 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IoclDevApp', '0016_alter_transiction_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qrdatatable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CustomerName', models.CharField(max_length=50, null=True)),
                ('QR_Data', models.CharField(max_length=150, null=True)),
                ('Qr_no', models.CharField(max_length=50, null=True)),
                ('uid', models.CharField(max_length=50, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('Imgpath', models.CharField(max_length=200, null=True)),
            ],
            options={
                'db_table': 'Qrdatatable',
            },
        ),
    ]