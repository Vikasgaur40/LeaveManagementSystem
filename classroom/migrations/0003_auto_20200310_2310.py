# Generated by Django 2.2.3 on 2020-03-10 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0002_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachleaveapp',
            name='status',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='teachleaveapp',
            name='to_admin',
            field=models.ForeignKey(default=0, on_delete='CASCADE', to='classroom.Admin'),
            preserve_default=False,
        ),
    ]
