# Generated by Django 5.0.2 on 2024-02-15 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_alter_albummodel_id_alter_categorymodel_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albummodel',
            name='id',
            field=models.BigAutoField(auto_created=True, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='categorymodel',
            name='id',
            field=models.BigAutoField(auto_created=True, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='musicmodel',
            name='id',
            field=models.BigAutoField(auto_created=True, editable=False, primary_key=True, serialize=False),
        ),
    ]
