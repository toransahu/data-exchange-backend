# Generated by Django 2.0.7 on 2018-07-23 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scheme',
            fields=[
                ('aadhar_number', models.CharField(max_length=15, primary_key=True, serialize=False, unique=True)),
                ('beneficiary_name', models.CharField(blank=True, max_length=50, null=True)),
                ('gender', models.CharField(blank=True, choices=[('F', 'Female'), ('M', 'Male'), ('T', 'Transgender')], max_length=1, null=True)),
                ('member_age', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('dist_name', models.CharField(blank=True, max_length=50, null=True)),
                ('scheme_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('ticket_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
