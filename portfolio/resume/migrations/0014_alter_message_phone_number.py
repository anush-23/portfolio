# Generated by Django 4.2.2 on 2023-08-04 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0013_message_alter_projects_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='phone_number',
            field=models.IntegerField(),
        ),
    ]