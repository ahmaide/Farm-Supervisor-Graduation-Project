# Generated by Django 4.1.12 on 2023-12-29 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HybridRecommender', '0015_rename_last_date_locationdisease_last_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disease',
            name='causes',
            field=models.CharField(max_length=200),
        ),
    ]
