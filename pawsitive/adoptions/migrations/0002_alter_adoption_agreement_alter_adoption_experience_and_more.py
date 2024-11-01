# Generated by Django 5.1.2 on 2024-10-28 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoptions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adoption',
            name='agreement',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10),
        ),
        migrations.AlterField(
            model_name='adoption',
            name='experience',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10),
        ),
        migrations.AlterField(
            model_name='adoption',
            name='time_for_pet',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Maybe', 'Maybe')], max_length=10),
        ),
        migrations.AlterField(
            model_name='donation',
            name='payment_screenshot',
            field=models.ImageField(upload_to='payment/'),
        ),
    ]
