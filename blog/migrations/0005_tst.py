# Generated by Django 3.1 on 2020-10-25 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_comment_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tst',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=150)),
                ('text', models.TextField()),
            ],
        ),
    ]
