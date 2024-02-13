# Generated by Django 4.2.6 on 2023-10-23 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=190, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bookstore.book'),
        ),
        migrations.AddField(
            model_name='order',
            name='costumer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bookstore.costumer'),
        ),
        migrations.AlterField(
            model_name='order',
            name='stauts',
            field=models.CharField(choices=[('Delivred', 'Delivred'), ('Peding', 'Peding'), ('Sool', 'Sool')], max_length=190, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='tages',
            field=models.ManyToManyField(to='bookstore.tag'),
        ),
    ]
