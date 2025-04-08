# Generated by Django 5.1.7 on 2025-04-08 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_delete_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.CharField(choices=[('web', 'Web Development'), ('data', 'Data Analytics'), ('cloud', 'Clouds')], default='web', max_length=50),
        ),
    ]
