# Generated by Django 3.1.5 on 2021-04-09 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transiction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_user', models.CharField(default=0, max_length=50)),
                ('to_user', models.CharField(default=0, max_length=50)),
                ('ammount', models.IntegerField(default=0)),
                ('date', models.DateField(default=2019)),
            ],
        ),
    ]
