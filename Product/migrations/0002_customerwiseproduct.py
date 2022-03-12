# Generated by Django 4.0.1 on 2022-03-12 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerWiseProduct',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('c_id', models.CharField(max_length=255)),
                ('pprice', models.CharField(max_length=255)),
                ('pname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.product')),
            ],
        ),
    ]