# Generated by Django 4.2.6 on 2023-11-15 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0007_costumer_user_alter_order_stauts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='stauts',
            field=models.CharField(choices=[('Delivred', 'Delivred'), ('out of order', 'out of order'), ('in progress', 'in progress'), ('Peding', 'Peding')], max_length=190, null=True),
        ),
    ]
