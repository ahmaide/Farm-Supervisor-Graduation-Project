# Generated by Django 4.1.12 on 2023-12-19 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HybridRecommender', '0011_rename_situation_locationdisease_cases_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locationpest',
            name='location',
        ),
        migrations.RemoveField(
            model_name='locationpest',
            name='pest',
        ),
        migrations.RemoveField(
            model_name='userdisease',
            name='disease',
        ),
        migrations.RemoveField(
            model_name='userdisease',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userpest',
            name='pest',
        ),
        migrations.RemoveField(
            model_name='userpest',
            name='user',
        ),
        migrations.DeleteModel(
            name='LocationDisease',
        ),
        migrations.DeleteModel(
            name='LocationPest',
        ),
        migrations.DeleteModel(
            name='UserDisease',
        ),
        migrations.DeleteModel(
            name='UserPest',
        ),
    ]
