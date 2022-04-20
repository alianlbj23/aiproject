# Generated by Django 4.0.1 on 2022-04-20 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aiproject', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Chi_title', models.CharField(max_length=500)),
                ('Eng_title', models.CharField(max_length=500)),
                ('Editor', models.CharField(max_length=500)),
                ('Content', models.CharField(max_length=2000)),
                ('Data_url', models.CharField(max_length=500)),
            ],
        ),
    ]