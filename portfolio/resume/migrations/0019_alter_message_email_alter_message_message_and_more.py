# Generated by Django 4.2.2 on 2023-08-06 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0018_merge_20230806_0546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='message',
            name='phone_number',
            field=models.IntegerField(),
        ),
    ]