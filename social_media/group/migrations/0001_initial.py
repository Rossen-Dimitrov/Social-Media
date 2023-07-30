# Generated by Django 4.2.3 on 2023-07-30 04:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="GroupMembersModel",
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
            ],
        ),
        migrations.CreateModel(
            name="GroupModel",
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
                ("name", models.CharField(max_length=255, unique=True)),
                (
                    "slug",
                    models.SlugField(allow_unicode=True, editable=False, unique=True),
                ),
                ("description", models.TextField(blank=True, default="")),
                (
                    "description_html",
                    models.TextField(blank=True, default="", editable=False),
                ),
                (
                    "members",
                    models.ManyToManyField(
                        through="group.GroupMembersModel", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
            },
        ),
        migrations.AddField(
            model_name="groupmembersmodel",
            name="group",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="membership",
                to="group.groupmodel",
            ),
        ),
        migrations.AddField(
            model_name="groupmembersmodel",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="user_group",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterUniqueTogether(
            name="groupmembersmodel",
            unique_together={("group", "user")},
        ),
    ]
