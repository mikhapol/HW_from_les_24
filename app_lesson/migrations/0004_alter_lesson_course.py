# Generated by Django 4.2.4 on 2023-09-04 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_course', '0001_initial'),
        ('app_lesson', '0003_alter_lesson_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lesson', to='app_course.course', verbose_name='курс'),
        ),
    ]
