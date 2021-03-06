# Generated by Django 3.2.13 on 2022-07-15 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Standing',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rank', models.IntegerField()),
                ('based', models.TextField()),
                ('team', models.TextField()),
                ('match', models.IntegerField()),
                ('wpoint', models.IntegerField()),
                ('win', models.IntegerField()),
                ('draw', models.IntegerField()),
                ('defeat', models.IntegerField()),
                ('goal', models.IntegerField()),
                ('loss', models.IntegerField()),
                ('gol', models.IntegerField()),
            ],
            options={
                'db_table': 'standing',
            },
        ),
    ]
