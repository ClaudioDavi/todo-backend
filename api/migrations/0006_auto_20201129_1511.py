# Generated by Django 3.1.3 on 2020-11-29 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0005_auto_20201128_2003"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task",
            old_name="status",
            new_name="completed",
        ),
    ]
