# Generated by Django 2.1 on 2020-01-28 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jist_api', '0045_auto_20200128_1213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spot_admission_fee',
            name='medical_fee',
        ),
        migrations.AlterField(
            model_name='admission',
            name='depertment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jist_api.Depertment'),
        ),
        migrations.AlterField(
            model_name='admission',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jist_api.Students'),
        ),
        migrations.AlterField(
            model_name='be_fee_table',
            name='depertment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jist_api.Depertment'),
        ),
        migrations.AlterField(
            model_name='betterment_fee_table',
            name='depertment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jist_api.Depertment'),
        ),
        migrations.AlterField(
            model_name='betterment_fee_table',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jist_api.Students'),
        ),
        migrations.AlterField(
            model_name='branch',
            name='depertment',
            field=models.ManyToManyField(to='jist_api.Depertment'),
        ),
        migrations.AlterField(
            model_name='compartmental_fee_table',
            name='depertment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jist_api.Depertment'),
        ),
        migrations.AlterField(
            model_name='compartmental_fee_table',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jist_api.Students'),
        ),
        migrations.AlterField(
            model_name='exam_fee_table',
            name='depertment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jist_api.Depertment'),
        ),
        migrations.AlterField(
            model_name='examination_fee_table',
            name='depertment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jist_api.Depertment'),
        ),
        migrations.AlterField(
            model_name='examination_fee_table',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jist_api.Students'),
        ),
        migrations.AlterField(
            model_name='semester_fees',
            name='depertment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jist_api.Depertment'),
        ),
        migrations.AlterField(
            model_name='students',
            name='depertment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jist_api.Depertment'),
        ),
    ]
