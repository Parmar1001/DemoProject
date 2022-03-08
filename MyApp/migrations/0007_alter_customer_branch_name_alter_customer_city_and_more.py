# Generated by Django 4.0.2 on 2022-02-25 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("MyApp", "0006_alter_customer_account_type_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="branch_name",
            field=models.ForeignKey(
                choices=[
                    ("State Bank of India", "State Bank of India"),
                    ("Axis Bank", "Axis Bank"),
                    ("HDFC Bank", "HDFC Bank"),
                    ("ICICI Bank", "ICICI Bank"),
                    ("Kotak Mahindra Bank", "Kotak Mahindra Bank"),
                    ("RBL Bank", "RBL Bank"),
                    ("Union Bank of India", "Union Bank of India"),
                    ("Central Bank of India", "Central Bank of India"),
                ],
                default="State Bank of India",
                on_delete=django.db.models.deletion.CASCADE,
                to="MyApp.branch",
            ),
        ),
        migrations.AlterField(
            model_name="customer",
            name="city",
            field=models.CharField(default="Indore", max_length=30),
        ),
        migrations.AlterField(
            model_name="customer",
            name="state",
            field=models.CharField(
                choices=[
                    ("Madhya Pradesh", "Madhya Pradesh"),
                    ("Maharashtra", "Maharashtra"),
                    ("Manipur", "Manipur"),
                    ("Meghalaya", "Meghalaya"),
                    ("Mizoram", "Mizoram"),
                ],
                default="Madhya Pradesh",
                max_length=255,
            ),
        ),
    ]
