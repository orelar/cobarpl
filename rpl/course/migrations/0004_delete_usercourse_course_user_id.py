# Generated by Django 4.1.3 on 2022-12-02 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_usercourse_remove_bab_forum_id_remove_bab_id_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserCourse',
        ),
        migrations.AddField(
            model_name='course',
            name='user_id',
            field=models.TextField(default=''),
        ),
    ]
