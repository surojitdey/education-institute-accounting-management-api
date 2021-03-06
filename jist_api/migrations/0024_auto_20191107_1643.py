# Generated by Django 2.2.5 on 2019-11-07 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jist_api', '0023_auto_20191107_1539'),
    ]

    operations = [
        migrations.CreateModel(
            name='odd_semester_fees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admission_fee', models.IntegerField(default=0)),
                ('tuition_fee', models.IntegerField(default=0)),
                ('identity_fee', models.IntegerField(default=0)),
                ('examination_fee', models.IntegerField(default=0)),
                ('student_union_fee', models.IntegerField(default=0)),
                ('game_sports_fee', models.IntegerField(default=0)),
                ('magazine_fee', models.IntegerField(default=0)),
                ('laboratory_fee', models.IntegerField(default=0)),
                ('university_registration_fee', models.IntegerField(default=0)),
                ('enrolment_fee', models.IntegerField(default=0)),
                ('electricity_fee', models.IntegerField(default=0)),
                ('group_insurance_fee', models.IntegerField(default=0)),
                ('scout_guide_fee', models.IntegerField(default=0)),
                ('internet_fee', models.IntegerField(default=0)),
                ('welfare_fee', models.IntegerField(default=0)),
                ('development_fee', models.IntegerField(default=0)),
                ('library_caution_fee', models.IntegerField(default=0)),
                ('transport_fee', models.IntegerField(default=0)),
                ('training_placement_fee', models.IntegerField(default=0)),
                ('college_festival_fee', models.IntegerField(default=0)),
                ('late_fee', models.IntegerField(default=0)),
                ('last_admission_date', models.DateField(null=True)),
                ('depertment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jist_api.Depertment')),
            ],
        ),
        migrations.DeleteModel(
            name='bsc_odd_semester_fees',
        ),
        migrations.AlterField(
            model_name='branch',
            name='depertment',
            field=models.ManyToManyField(to='jist_api.Depertment'),
        ),
        migrations.AlterField(
            model_name='students',
            name='depertment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jist_api.Depertment'),
        ),
    ]
