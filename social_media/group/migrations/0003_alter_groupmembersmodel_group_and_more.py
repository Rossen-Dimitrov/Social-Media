# Generated by Django 4.2.3 on 2023-08-01 08:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("group", "0002_alter_groupmembersmodel_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="groupmembersmodel",
            name="group",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="membership",
                to="group.groupmodel",
            ),
        ),
        migrations.AlterField(
            model_name="groupmembersmodel",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="group_member",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]