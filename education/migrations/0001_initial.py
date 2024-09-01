# Generated by Django 3.0 on 2020-11-29 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('edu_institute_s_num', models.AutoField(primary_key=True, serialize=False)),
                ('edu_institute_name', models.TextField()),
                ('edu_institute_address', models.CharField(max_length=500)),
                ('edu_institute_from', models.DateField()),
                ('edu_institute_to', models.DateField()),
                ('edu_institute_board', models.CharField(max_length=500)),
                ('edu_downloadable', models.BooleanField(default=False)),
                ('edu_institute_website', models.CharField(max_length=1000)),
                ('edu_institute_record_created', models.DateTimeField(auto_now=True)),
                ('edu_institute_record_updated', models.DateTimeField(auto_now_add=True)),
                ('college_pic', models.ImageField(upload_to='static/images/education/colleges')),
            ],
            options={
                'db_table': 'Education__college',
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('edu_institute_s_num', models.AutoField(primary_key=True, serialize=False)),
                ('edu_institute_name', models.TextField()),
                ('edu_institute_address', models.CharField(max_length=500)),
                ('edu_institute_from', models.DateField()),
                ('edu_institute_to', models.DateField()),
                ('edu_institute_board', models.CharField(max_length=500)),
                ('edu_downloadable', models.BooleanField(default=False)),
                ('edu_institute_website', models.CharField(max_length=1000)),
                ('edu_institute_record_created', models.DateTimeField(auto_now=True)),
                ('edu_institute_record_updated', models.DateTimeField(auto_now_add=True)),
                ('school_pic', models.ImageField(upload_to='static/images/education/schools')),
            ],
            options={
                'db_table': 'Education__school',
            },
        ),
    ]
