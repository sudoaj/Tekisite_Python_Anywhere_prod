# Generated by Django 4.1.7 on 2023-05-04 20:13

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Assignment",
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
                (
                    "assignment_type",
                    models.CharField(
                        choices=[
                            ("homework", "Homework"),
                            ("quiz", "Quiz"),
                            ("project", "Project"),
                            ("challenge", "Challenge"),
                            ("exam", "Exam"),
                            ("misc", "Miscellaneous"),
                        ],
                        default="misc",
                        max_length=999,
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField()),
                (
                    "attachment",
                    models.FileField(blank=True, null=True, upload_to="assignments/"),
                ),
                ("due_date", models.DateField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("slug", models.SlugField(unique=True)),
                ("meta_tags", models.JSONField(blank=True, null=True)),
                ("is_published", models.BooleanField(default=False)),
                (
                    "creator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="created_assignments",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Submission",
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
                (
                    "attachment_one",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="submissions/",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=["pdf", "doc", "docx", "zip"]
                            )
                        ],
                    ),
                ),
                (
                    "attachment_two",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="submissions/",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=["pdf", "doc", "docx", "zip"]
                            )
                        ],
                    ),
                ),
                (
                    "attachment_three",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="submissions/",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=["pdf", "doc", "docx", "zip"]
                            )
                        ],
                    ),
                ),
                ("submitted_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_late", models.BooleanField(default=False, editable=False)),
                (
                    "assignment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="submissions",
                        to="homework.assignment",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="submissions",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Grade",
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
                ("score", models.DecimalField(decimal_places=2, max_digits=5)),
                ("grade", models.CharField(blank=True, max_length=2, null=True)),
                (
                    "assignment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="homework.assignment",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="assignment",
            name="students",
            field=models.ManyToManyField(
                related_name="assignments",
                through="homework.Grade",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
