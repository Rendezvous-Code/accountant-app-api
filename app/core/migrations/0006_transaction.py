# Generated by Django 3.1.2 on 2020-11-01 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_bankaaccount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_code', models.CharField(max_length=3)),
                ('purpose', models.CharField(max_length=255)),
                ('debt', models.CharField(blank=True, max_length=255)),
                ('credit', models.CharField(blank=True, max_length=255)),
                ('beneficiary', models.CharField(max_length=255)),
                ('beneficiary_acc_no', models.CharField(blank=True, max_length=255)),
                ('receipt_date', models.CharField(max_length=30)),
                ('account_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.bankaaccount')),
            ],
        ),
    ]