# Generated by Django 3.2.8 on 2023-12-05 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv_app', '0002_certificate_file_cer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='thumbnail',
            field=models.FileField(blank=True, null=True, upload_to='testimonials'),
        ),
    ]
