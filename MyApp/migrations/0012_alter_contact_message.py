# Generated by Django 4.0.2 on 2022-03-02 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("MyApp", "0011_alter_customer_profile_pic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="message",
            field=models.TextField(max_length=1000),
        ),
    ]