# Generated by Django 4.0.1 on 2022-03-12 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0003_rename_c_id_customerwiseproduct_c_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customerwiseproduct',
            old_name='p_id',
            new_name='pc_id',
        ),
        migrations.AlterField(
            model_name='customerwiseproduct',
            name='pname',
            field=models.ForeignKey(db_column='p_id', on_delete=django.db.models.deletion.CASCADE, to='Product.product'),
        ),
    ]
