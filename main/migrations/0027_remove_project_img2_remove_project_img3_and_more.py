# Generated by Django 4.1.4 on 2022-12-14 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_remove_communyte_imgs2_remove_communyte_imgs3_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='img2',
        ),
        migrations.RemoveField(
            model_name='project',
            name='img3',
        ),
        migrations.RemoveField(
            model_name='project',
            name='text2',
        ),
        migrations.RemoveField(
            model_name='project',
            name='text3',
        ),
        migrations.RemoveField(
            model_name='project',
            name='texts2',
        ),
        migrations.RemoveField(
            model_name='project',
            name='texts3',
        ),
        migrations.RemoveField(
            model_name='project',
            name='title2',
        ),
        migrations.RemoveField(
            model_name='project',
            name='title3',
        ),
    ]
