# Generated by Django 3.0.6 on 2020-05-15 19:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('choice', models.BooleanField(choices=[(True, 'boasts'), (False, 'roasts')], default=True)),
                ('user_input', models.TextField()),
                ('up_votes', models.IntegerField()),
                ('down_votes', models.IntegerField()),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
