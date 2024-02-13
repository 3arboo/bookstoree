# Generated by Django 4.2.6 on 2023-11-15 21:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookstore', '0006_alter_order_stauts'),
    ]

    operations = [
        migrations.AddField(
            model_name='costumer',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='stauts',
            field=models.CharField(choices=[('in progress', 'in progress'), ('Delivred', 'Delivred'), ('out of order', 'out of order'), ('Peding', 'Peding')], max_length=190, null=True),
        ),
    ]