# Generated by Django 4.2.4 on 2023-08-26 17:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cardsecuritysystem", "0016_pupil_part_payment_alter_pupil_email_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="pupil",
            name="teachers_comment",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
