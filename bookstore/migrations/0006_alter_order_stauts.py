# Generated by Django 4.2.6 on 2023-11-04 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0005_alter_order_stauts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='stauts',
            field=models.CharField(choices=[('in progress', 'in progress'), ('Peding', 'Peding'), ('out of order', 'out of order'), ('Delivred', 'Delivred')], max_length=190, null=True),
        ),
    ]
