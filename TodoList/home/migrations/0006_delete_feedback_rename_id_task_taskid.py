# Generated by Django 4.1.3 on 2023-01-11 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_rename_feedback_feedback_feed_back'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Feedback',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='id',
            new_name='taskID',
        ),
    ]