# Generated by Django 3.0 on 2020-11-29 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('contact_s_num', models.AutoField(primary_key=True, serialize=False)),
                ('contact_type', models.CharField(choices=[('Email', 'Email'), ('LinkedIn', 'LinkedIn'), ('Github', 'Github'), ('GitLab', 'GitLab'), ('Facebook', 'Facebook')], max_length=30)),
                ('contact_link', models.TextField()),
                ('contact_downloadable', models.BooleanField(default=False)),
                ('contact_record_created', models.DateTimeField(auto_now=True)),
                ('contact_record_updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Contacts__contact',
            },
        ),
    ]
