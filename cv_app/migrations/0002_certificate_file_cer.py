# Generated by Django 3.2.8 on 2023-12-05 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='file_cer',
            field=models.FileField(default='default_certificate.pdf', upload_to='certificates/'),
        ),
    ]
