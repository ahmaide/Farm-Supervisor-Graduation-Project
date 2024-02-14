# Generated by Django 4.1.12 on 2023-12-19 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HybridRecommender', '0008_pest_pesttype'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationdisease',
            name='situation',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='locationpest',
            name='situation',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userdisease',
            name='situation',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userpest',
            name='situation',
            field=models.IntegerField(default=0),
        ),
    ]
