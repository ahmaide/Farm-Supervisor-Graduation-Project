# Generated by Django 4.1.12 on 2023-11-25 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HybridRecommender', '0007_alter_locationpest_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='pest',
            name='pestType',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
