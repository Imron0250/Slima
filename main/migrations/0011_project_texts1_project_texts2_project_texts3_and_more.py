# Generated by Django 4.1.4 on 2022-12-13 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_rename_img_project_img1_rename_title_project_text1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='texts1',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='texts2',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='texts3',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='text1',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='text2',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='text3',
            field=models.TextField(),
        ),
    ]
