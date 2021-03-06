# Generated by Django 2.1 on 2020-07-17 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jist_api', '0056_auto_20200319_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='spot_admission_fee',
            name='college_festival_fee',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='spot_admission_fee',
            name='development_fee',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='spot_admission_fee',
            name='electricity_fee',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='spot_admission_fee',
            name='enrolment_fee',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='spot_admission_fee',
            name='examination_fee',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='spot_admission_fee',
            name='game_sports_fee',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='spot_admission_fee',
            name='govt_dues',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='spot_admission_fee',
            name='group_insurance_fee',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='spot_admission_fee',
            name='identity_fee',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='spot_admission_fee',
            name='internet_fee',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='spot_admission_fee',
            name='iste_fee',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='spot_admission_fee',
            name='laboratory_fee',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='spot_admission_fee',
            name='late_fee',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='spot_admission_fee',
            name='library_caution_fee',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='spot_admission_fee',
            name='magazine_fee',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='spot_admission_fee',
            name='medical_fee',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='spot_admission_fee',
            name='scout_guide_fee',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='spot_admission_fee',
            name='student_union_fee',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='spot_admission_fee',
            name='training_placement_fee',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='spot_admission_fee',
            name='transport_fee',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='spot_admission_fee',
            name='university_registration_fee',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='spot_admission_fee',
            name='welfare_fee',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
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
        migrations.AlterField(
            model_name='transfer_students',
            name='depertment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jist_api.Depertment'),
        ),
    ]
