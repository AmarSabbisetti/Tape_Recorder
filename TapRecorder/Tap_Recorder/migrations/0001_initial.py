# Generated by Django 4.2 on 2023-05-02 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Song",
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
                ("image", models.ImageField(upload_to="")),
                ("audio_file", models.FileField(blank=True, null=True, upload_to="")),
                ("audio_link", models.CharField(blank=True, max_length=200, null=True)),
                ("duration", models.CharField(max_length=20)),
            ],
        ),
    ]
