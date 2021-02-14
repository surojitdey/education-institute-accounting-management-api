# Generated by Django 2.1 on 2021-01-11 11:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jist_api', '0058_auto_20200717_2222'),
    ]

    operations = [
        migrations.CreateModel(
            name='HostelAdmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(choices=[('NULL', ''), ('First', 'I'), ('Second', 'II'), ('Third', 'III'), ('Fourth', 'IV'), ('Fifth', 'V'), ('Sixth', 'VI'), ('Seventh', 'VII'), ('Eighth', 'VIII')], default='NULL', max_length=100)),
                ('admission_date', models.DateField(default=django.utils.timezone.now)),
                ('security_money', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('electricity_fee', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('mess_security', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('seat_rent', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('misc', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
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
            name='admission_year',
            field=models.IntegerField(default=2021),
        ),
        migrations.AlterField(
            model_name='students',
            name='caste',
            field=models.CharField(choices=[('General', 'GENERAL'), ('OBC', 'OBC'), ('MOBC', 'MOBC'), ('SC', 'SC'), ('ST', 'ST'), ('ST(H)', 'ST(H)')], default='NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='students',
            name='depertment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jist_api.Depertment'),
        ),
        migrations.AlterField(
            model_name='transfer_students',
            name='admission_year',
            field=models.IntegerField(default=2021),
        ),
        migrations.AlterField(
            model_name='transfer_students',
            name='depertment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jist_api.Depertment'),
        ),
        migrations.AddField(
            model_name='hosteladmission',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jist_api.Students'),
        ),
    ]
