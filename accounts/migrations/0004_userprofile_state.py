# Generated by Django 4.2.2 on 2023-08-03 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_userprofile_address_line_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='state',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
