# Generated by Django 3.0.8 on 2020-07-26 17:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GhostPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_boast', models.BooleanField(blank=True, default=True)),
                ('post', models.CharField(max_length=280)),
                ('up_votes', models.IntegerField(default=0)),
                ('down_votes', models.IntegerField(default=0)),
                ('submission', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]