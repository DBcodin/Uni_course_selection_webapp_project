# Generated by Django 4.1.7 on 2023-04-22 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_alter_usermoduleinfo_user_student_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='moduleinfo',
            name='Test',
            field=models.CharField(default='hello', max_length=100),
        ),
    ]
