# Generated by Django 4.1.3 on 2022-11-30 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catatan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bab_name', models.TextField(default='')),
                ('forum_id', models.BigIntegerField()),
                ('list_catatan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catatan.catatan')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.BigIntegerField()),
                ('course_name', models.TextField(default='')),
                ('list_bab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.bab')),
            ],
        ),
        migrations.CreateModel(
            name='DaftarCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
            ],
        ),
    ]
