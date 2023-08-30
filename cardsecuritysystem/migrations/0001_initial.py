# Generated by Django 4.2.4 on 2023-08-24 17:34

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="ChildParents",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=10, null=True)),
                ("first_name", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "middle_name",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("last_name", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "phone_number",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, null=True, unique=True
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True, default="default_image.jpg", null=True, upload_to=""
                    ),
                ),
                ("places_of_work", models.TextField(blank=True, null=True)),
                ("address", models.TextField(blank=True, null=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True, related_name="parents", to="auth.group"
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True, related_name="parents", to="auth.permission"
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Pupil",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=200)),
                ("middle_name", models.CharField(max_length=200)),
                ("last_name", models.CharField(max_length=200)),
                ("registration_number", models.CharField(max_length=200)),
                ("age", models.CharField(max_length=200)),
                ("skin_color", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=254, null=True, unique=True)),
                ("school_fee", models.CharField(max_length=200, null=True)),
                (
                    "avatar",
                    models.ImageField(default="avatar.svg", null=True, upload_to=""),
                ),
                (
                    "QR_Code",
                    models.ImageField(default="avatar.svg", null=True, upload_to=""),
                ),
                (
                    "Bar_Code",
                    models.ImageField(default="avatar.svg", null=True, upload_to=""),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="pupils",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]