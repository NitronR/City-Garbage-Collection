# Generated by Django 2.0.4 on 2018-04-15 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientapp', '0006_auto_20180413_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gcrequest',
            name='status',
            field=models.CharField(choices=[('Not responded yet', 'Not responded yet'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Not responded yet', max_length=20),
        ),
    ]
