# Generated by Django 2.1 on 2020-03-19 08:20

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jist_api', '0055_auto_20200319_1339'),
    ]

    operations = [
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
            model_name='form_and_prospectus_table',
            name='purchase_date',
            field=models.DateField(default=django.utils.timezone.now, null=True),
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
        migrations.AlterField(
            model_name='transfer_students',
            name='depertment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jist_api.Depertment'),
        ),
    ]