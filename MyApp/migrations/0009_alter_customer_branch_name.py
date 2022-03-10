# Generated by Django 4.0.2 on 2022-02-25 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("MyApp", "0008_alter_customer_city"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="branch_name",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="customers",
                to="MyApp.branch",
            ),
        ),
    ]