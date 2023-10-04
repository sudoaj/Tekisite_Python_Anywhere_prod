# Generated by Django 4.1.7 on 2023-05-04 20:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Course",
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
                    "department",
                    models.CharField(
                        choices=[
                            ("FE", "Frontend Engineering"),
                            ("BE", "Backend Engineering"),
                            ("FS", "Fullstack Engineering"),
                            ("DS", "Data Science"),
                            ("GT", "General Technology"),
                        ],
                        max_length=2,
                    ),
                ),
                (
                    "course_choice",
                    models.CharField(
                        choices=[
                            ("HTML", "HTML"),
                            ("CSS", "CSS"),
                            ("JAVASCRIPT", "JAVASCRIPT"),
                            ("TYPESCRIPT", "TYPESCRIPT"),
                            ("FIGMA", "FIGMA"),
                            ("UI", "UI"),
                            ("UX", "UX"),
                            ("PYTHON", "PYTHON"),
                            ("DJANGO", "DJANGO"),
                            ("REACT", "REACT"),
                            ("NODE", "NODE"),
                            ("MONGODB", "MONGODB"),
                            ("MYSQL", "MYSQL"),
                            ("GIT", "GIT"),
                            ("GITHUB", "GITHUB"),
                            ("AWS", "AWS"),
                            ("DOCKER", "DOCKER"),
                            ("KUBERNETES", "KUBERNETES"),
                            ("LINUX", "LINUX"),
                            ("BASH", "BASH"),
                            ("SHELL", "SHELL"),
                            ("C", "C"),
                            ("OTHER", "OTHER"),
                        ],
                        max_length=20,
                    ),
                ),
                ("course_name", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("credit_hours", models.FloatField()),
                ("slug", models.SlugField(blank=True, null=True, unique=True)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("start_date", models.DateTimeField()),
                ("end_date", models.DateTimeField()),
                ("updated_on", models.DateTimeField(auto_now=True)),
                ("is_active", models.BooleanField(default=False)),
                (
                    "instructor",
                    models.ManyToManyField(
                        related_name="Course_instructor", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
    ]
