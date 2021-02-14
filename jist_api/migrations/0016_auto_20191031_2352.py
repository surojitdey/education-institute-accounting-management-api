# Generated by Django 2.2.5 on 2019-10-31 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jist_api', '0015_auto_20191031_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depertment',
            name='dept_name',
            field=models.CharField(default='NULL', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='depertment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jist_api.Depertment'),
        ),
    ]
