# Generated by Django 4.2.7 on 2023-11-25 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0012_alter_order_stauts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='stauts',
            field=models.CharField(choices=[('out of order', 'out of order'), ('Delivred', 'Delivred'), ('in progress', 'in progress'), ('Peding', 'Peding')], max_length=190, null=True),
        ),
    ]