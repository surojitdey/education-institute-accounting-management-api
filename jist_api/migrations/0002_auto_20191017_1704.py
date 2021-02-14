# Generated by Django 2.2.5 on 2019-10-17 11:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jist_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='branch',
            field=models.CharField(choices=[('Physics', 'PHY'), ('Chemistry', 'CHEM'), ('Mathematics', 'MATH'), ('B.Sc.(IT)', 'B.Sc.(IT)'), ('Power Electronics & Instrumentation Engineering', 'PEIE'), ('Electronics & Telecommunication Engineering', 'ETE'), ('Civil Engineering', 'CE'), ('Mechanical Engineering', 'ME')], default='NULL', max_length=30),
        ),
        migrations.AddField(
            model_name='students',
            name='caste',
            field=models.CharField(choices=[('General', 'GENERAL'), ('OBC', 'OBC'), ('SC', 'SC'), ('ST', 'ST'), ('ST(H)', 'ST(H)')], default='NULL', max_length=30),
        ),
        migrations.AddField(
            model_name='students',
            name='date_of_birth',
            field=models.DateField(default=datetime.date(2019, 10, 17)),
        ),
        migrations.AddField(
            model_name='students',
            name='semester',
            field=models.CharField(choices=[('First', 'I'), ('Second', 'II'), ('Third', 'III'), ('Fourth', 'IV'), ('Fifth', 'V'), ('Sixth', 'VI'), ('Seventh', 'VII'), ('Eighth', 'VIII')], default='NULL', max_length=30),
        ),
        migrations.AlterField(
            model_name='students',
            name='depertment',
            field=models.CharField(choices=[('Bachelor of Science', 'B.Sc.'), ('Bachelor of Science in Information Technology', 'B.Sc.(IT)'), ('Master of Science', 'M.Sc.'), ('Bachelor of Engineering', 'B.E.'), ('PhD', 'PhD')], default='NULL', max_length=30),
        ),
        migrations.AlterField(
            model_name='students',
            name='first_name',
            field=models.CharField(default='NULL', max_length=50),
        ),
        migrations.AlterField(
            model_name='students',
            name='last_name',
            field=models.CharField(default='NULL', max_length=50),
        ),
    ]
