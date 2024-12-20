# Generated by Django 5.1.1 on 2024-10-20 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freshness_detector', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freshnessprediction',
            name='confidence_score',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='freshnessprediction',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='freshnessprediction',
            name='predicted_class',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='freshnessprediction',
            name='time_taken',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
