# Generated by Django 4.1.4 on 2022-12-13 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_logo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logo',
            old_name='logo',
            new_name='logo1',
        ),
        migrations.AddField(
            model_name='logo',
            name='logo10',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logo',
            name='logo2',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logo',
            name='logo3',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logo',
            name='logo4',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logo',
            name='logo5',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logo',
            name='logo6',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logo',
            name='logo7',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logo',
            name='logo8',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logo',
            name='logo9',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
