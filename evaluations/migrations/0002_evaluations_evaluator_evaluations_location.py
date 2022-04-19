# Generated by Django 4.0.4 on 2022-04-19 19:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('evaluations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluations',
            name='Evaluator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='evaluations',
            name='Location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.site'),
        ),
    ]