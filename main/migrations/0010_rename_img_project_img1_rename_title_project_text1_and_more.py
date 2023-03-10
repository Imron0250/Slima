# Generated by Django 4.1.4 on 2022-12-13 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_remove_project_text_text2_project_text2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='img',
            new_name='img1',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='title',
            new_name='text1',
        ),
        migrations.RemoveField(
            model_name='project',
            name='text',
        ),
        migrations.AddField(
            model_name='project',
            name='img2',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='img3',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='text3',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='title1',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='title2',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='title3',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
