# Generated by Django 3.1.2 on 2020-10-16 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prodNm', models.CharField(max_length=30)),
                ('stckQty', models.IntegerField()),
                ('brnd', models.CharField(max_length=6)),
                ('cate', models.CharField(max_length=3)),
            ],
        ),
    ]
