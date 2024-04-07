# Generated by Django 4.2.7 on 2024-04-05 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netlab', '0002_candidate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='name',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='modified_by',
        ),
        migrations.AddField(
            model_name='candidate',
            name='decision',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='des', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='value',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='status',
            field=models.CharField(default='awaiting permission', max_length=50),
        ),
    ]