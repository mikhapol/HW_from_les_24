# Generated by Django 4.2.4 on 2023-09-15 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_course', '0003_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='amount',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='цена курса'),
        ),
    ]