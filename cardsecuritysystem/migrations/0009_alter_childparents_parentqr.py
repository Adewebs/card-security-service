# Generated by Django 4.2.4 on 2023-08-25 19:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cardsecuritysystem", "0008_rename_parent_qr_childparents_parentqr"),
    ]

    operations = [
        migrations.AlterField(
            model_name="childparents",
            name="parentqr",
            field=models.ImageField(null=True, upload_to="parentsQR/"),
        ),
    ]
