# Generated by Django 2.2.5 on 2019-10-23 06:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jist_api', '0010_auto_20191021_1650'),
    ]

    operations = [
        migrations.CreateModel(
            name='signinInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_ip', models.CharField(max_length=50, null=True)),
                ('old_timestamp', models.DateTimeField(null=True)),
                ('new_timestamp', models.DateTimeField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
