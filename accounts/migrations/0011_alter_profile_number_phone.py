# Generated by Django 3.2.8 on 2021-11-15 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_profile_number_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='number_phone',
            field=models.CharField(max_length=13, verbose_name='رقم الهاتف '),
        ),
    ]
