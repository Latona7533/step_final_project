# Generated by Django 4.0.4 on 2022-04-23 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='project',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.portfolio'),
        ),
    ]