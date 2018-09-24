# Generated by Django 2.1.1 on 2018-09-23 16:40

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('date', models.DateTimeField(default=datetime.datetime(2018, 9, 23, 22, 25, 19, 165653))),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Book')),
                ('writtenBy', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]