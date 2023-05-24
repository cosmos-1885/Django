# Generated by Django 4.1.6 on 2023-02-04 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                ("bid", models.IntegerField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=50)),
                ("author", models.CharField(max_length=50)),
                ("category", models.CharField(max_length=50)),
                ("pages", models.IntegerField()),
                ("price", models.IntegerField()),
                ("published_date", models.DateField()),
                ("description", models.TextField()),
            ],
        ),
    ]