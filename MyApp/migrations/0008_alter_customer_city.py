# Generated by Django 4.0.2 on 2022-02-25 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0007_alter_customer_branch_name_alter_customer_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.CharField(choices=[('Indore', 'Indore'), ('Dewas', 'Dewas'), ('Mhow', 'Mhow'), ('Bhopal', 'Bhopal')], default='Indore', max_length=30),
        ),
    ]
