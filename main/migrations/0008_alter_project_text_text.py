# Generated by Django 4.1.4 on 2022-12-13 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_project_text_text2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_text',
            name='text',
            field=models.TextField(),
        ),
    ]
