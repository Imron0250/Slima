# Generated by Django 4.1.4 on 2022-12-13 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_remove_about_advantege_delete_advantege'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suppor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('impor_title', models.CharField(max_length=255)),
                ('impor_text', models.CharField(max_length=255)),
                ('img1', models.ImageField(upload_to='')),
                ('numers1', models.IntegerField()),
                ('title1', models.CharField(max_length=255)),
                ('img2', models.ImageField(upload_to='')),
                ('numers2', models.IntegerField()),
                ('title2', models.CharField(max_length=255)),
                ('img3', models.ImageField(upload_to='')),
                ('numers3', models.IntegerField()),
                ('title3', models.CharField(max_length=255)),
                ('img4', models.ImageField(upload_to='')),
                ('numers4', models.IntegerField()),
                ('title4', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='about',
            name='youtube',
            field=models.TextField(blank=True, null=True),
        ),
    ]