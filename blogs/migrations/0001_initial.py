# Generated by Django 3.0 on 2020-11-29 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('article_s_num', models.AutoField(primary_key=True, serialize=False)),
                ('article_title', models.CharField(max_length=200)),
                ('article_text', models.TextField()),
                ('article_record_created', models.DateTimeField(auto_now=True)),
                ('article_record_updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Blogs__article',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tag_s_num', models.AutoField(primary_key=True, serialize=False)),
                ('tag_title', models.CharField(max_length=30)),
                ('tag_record_created', models.DateTimeField(auto_now=True)),
                ('tag_record_updated', models.DateTimeField(auto_now_add=True)),
                ('article_s_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.Article')),
            ],
            options={
                'db_table': 'Blogs__tag',
            },
        ),
    ]
