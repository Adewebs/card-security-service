# Generated by Django 4.2.4 on 2023-08-25 19:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cardsecuritysystem", "0006_childparents_parent_qr"),
    ]

    operations = [
        migrations.AlterField(
            model_name="childparents",
            name="parent_qr",
            field=models.ImageField(
                default="avatar.svg", null=True, upload_to="parentsQR/"
            ),
        ),
    ]
