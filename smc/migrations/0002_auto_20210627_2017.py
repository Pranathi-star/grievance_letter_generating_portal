# Generated by Django 3.1.1 on 2021-06-27 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='city_smc',
            field=models.CharField(default='Hyderabad', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='letter',
            name='email_smc',
            field=models.EmailField(default='abc@xyz.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='letter',
            name='name_smc',
            field=models.CharField(default='John', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='letter',
            name='school_smc',
            field=models.CharField(default='Vidya High School', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='letter',
            name='state_smc',
            field=models.CharField(default='Telangana', max_length=200, null=True),
        ),
    ]
