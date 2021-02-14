# Generated by Django 2.1 on 2021-01-11 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jist_api', '0060_auto_20210111_1704'),
    ]

    operations = [
        migrations.CreateModel(
            name='hostel_fee_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(choices=[('Even', 'EVEN'), ('Odd', 'ODD')], default='NULL', max_length=100)),
                ('security_money', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('electricity_fee', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('mess_security', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('seat_rent', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('misc', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('late_fee', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('last_admission_date', models.DateField(null=True)),
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
            model_name='hosteladmission',
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