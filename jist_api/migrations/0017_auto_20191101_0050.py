# Generated by Django 2.2.5 on 2019-10-31 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jist_api', '0016_auto_20191031_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='depertment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jist_api.Depertment'),
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(default='NULL', max_length=100, unique=True)),
                ('branch_accronym', models.CharField(default='NULL', max_length=20)),
                ('depertment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jist_api.Depertment')),
            ],
        ),
    ]
