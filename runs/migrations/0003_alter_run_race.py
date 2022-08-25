# Generated by Django 3.2.14 on 2022-08-09 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('races', '0003_alter_race_owner'),
        ('runs', '0002_auto_20220809_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='run',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='runs', to='races.race'),
        ),
    ]