# Generated by Django 3.1.1 on 2020-09-09 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_entry'),
    ]

    operations = [
        migrations.CreateModel(
            name='IntroduceTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
