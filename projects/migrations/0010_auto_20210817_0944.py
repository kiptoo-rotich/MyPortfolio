# Generated by Django 3.2.5 on 2021-08-17 06:44

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('projects', '0009_rename_languages_project_technologies'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('is_verified', models.BooleanField(default=False)),
                ('type', models.CharField(choices=[('DRIVER', 'Driver'), ('USER', 'User'), ('ADMIN', 'Admin')], default=django.contrib.auth.models.User, max_length=50, verbose_name='Type')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='technologies',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Django', 'Django'), ('Flask', 'Flask'), ('Angular', 'Angular'), ('Bootstrap', 'Bootstrap'), ('Git', 'Git'), ('Javascript', 'Javascript')], max_length=200, null=True),
        ),
    ]
