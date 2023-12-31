# Generated by Django 4.2.3 on 2023-08-07 15:46

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
                ("joined_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "Group Member",
                "verbose_name_plural": "Group Members",
            },
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
                (
                    "name",
                    models.CharField(max_length=255, unique=True, verbose_name="Name"),
                ),
                (
                    "slug",
                    models.SlugField(allow_unicode=True, editable=False, unique=True),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, default="", verbose_name="Description"
                    ),
                ),
                (
                    "description_html",
                    models.TextField(blank=True, default="", editable=False),
                ),
                (
                    "members",
                    models.ManyToManyField(
                        through="group.GroupMembersModel",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Members",
                    ),
                ),
            ],
            options={
                "verbose_name": "Group",
                "verbose_name_plural": "Groups",
                "ordering": ["name"],
            },
        ),
        migrations.AddField(
            model_name="groupmembersmodel",
            name="group",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="membership",
                to="group.groupmodel",
            ),
        ),
        migrations.AddField(
            model_name="groupmembersmodel",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="group_member",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterUniqueTogether(
            name="groupmembersmodel",
            unique_together={("group", "user")},
        ),
    ]
