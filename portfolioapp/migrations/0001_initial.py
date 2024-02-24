# Generated by Django 4.2 on 2024-02-21 00:15

from django.db import migrations, models
import portfolioapp.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectDetails',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('descripition', models.TextField()),
                ('link', models.CharField(max_length=1000000)),
                ('img', models.ImageField(upload_to=portfolioapp.models.get_profile_image_filepath)),
                ('jobtype', models.CharField(choices=[('web', 'Web Project'), ('ui', 'UI Project')], max_length=50)),
            ],
        ),
    ]
