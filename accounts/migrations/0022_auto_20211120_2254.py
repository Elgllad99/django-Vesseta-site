# Generated by Django 3.2.8 on 2021-11-20 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_alter_profile_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='doctor',
            field=models.CharField(choices=[('تخسيس', 'تخسيس وتغذية'), ('مخ', 'مخ واعصاب'), ('اطفال', 'اطفال حديثي الولادة'), ('نفسي', 'نفسي'), ('تجميل', 'جراحة تجميل'), ('اورام', 'جراحة اورام'), ('باطنه', 'باطنه'), ('اوعيه', 'جراحة اوعية دموية'), ('اورام', 'اورام'), ('سمنه', 'جراحه سمنة ومناظير'), ('امراض', 'امراض دم'), ('اسنان', 'اسنان'), ('قلب', 'قلب واوعية دموية'), ('اطفال', 'جراحة اطفال'), ('عظام', 'عظام'), ('انف', 'انف واذن وحنجرة'), ('نساء', 'نساء وتوليد'), ('جلدية', 'جلدية')], max_length=60, verbose_name='دكتور :'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='specialist',
            field=models.CharField(choices=[('تخسيس', 'تخسيس وتغذية'), ('مخ', 'مخ واعصاب'), ('اطفال', 'اطفال حديثي الولادة'), ('نفسي', 'نفسي'), ('تجميل', 'جراحة تجميل'), ('اورام', 'جراحة اورام'), ('باطنه', 'باطنه'), ('اوعيه', 'جراحة اوعية دموية'), ('اورام', 'اورام'), ('سمنه', 'جراحه سمنة ومناظير'), ('امراض', 'امراض دم'), ('اسنان', 'اسنان'), ('قلب', 'قلب واوعية دموية'), ('اطفال', 'جراحة اطفال'), ('عظام', 'عظام'), ('انف', 'انف واذن وحنجرة'), ('نساء', 'نساء وتوليد'), ('جلدية', 'جلدية')], max_length=80, verbose_name='التخصص : '),
        ),
    ]
