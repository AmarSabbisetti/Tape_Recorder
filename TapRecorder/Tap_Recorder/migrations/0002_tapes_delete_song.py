# Generated by Django 4.2 on 2023-05-02 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Tap_Recorder", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tapes",
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
                ("title", models.TextField()),
                ("artist", models.TextField()),
                ("record_file", models.FileField(blank=True, null=True, upload_to="")),
            ],
        ),
        migrations.DeleteModel(
            name="Song",
        ),
    ]
