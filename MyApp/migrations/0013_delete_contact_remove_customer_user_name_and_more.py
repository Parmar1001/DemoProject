# Generated by Django 4.0.2 on 2022-03-07 07:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("MyApp", "0012_alter_contact_message"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Contact",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="user_name",
        ),
        migrations.AddField(
            model_name="customer",
            name="user",
            field=models.ForeignKey(
                default=12,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
