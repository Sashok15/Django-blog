# Generated by Django 2.0.6 on 2018-07-06 08:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180703_1340'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'permissions': (('can_update_article', 'To provide update own article'),)},
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 6, 8, 33, 9, 546533, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 6, 8, 33, 9, 547884, tzinfo=utc), verbose_name='date published'),
        ),
    ]
