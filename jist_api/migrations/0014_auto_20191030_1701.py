# Generated by Django 2.2.5 on 2019-10-30 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jist_api', '0013_auto_20191030_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='depertment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jist_api.department'),
        ),
    ]
