# Generated by Django 3.0.6 on 2021-01-20 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('job_title', models.CharField(max_length=200)),
                ('purpose', models.TextField()),
                ('address', models.TextField()),
                ('phone', models.IntegerField()),
                ('email_id', models.EmailField(max_length=254)),
                ('linkedIn', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='builder.Info')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks_10th', models.FloatField()),
                ('graduation_year_10th', models.IntegerField()),
                ('marks_12th', models.FloatField()),
                ('graduation_year_12th', models.IntegerField()),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='builder.Info')),
            ],
        ),
        migrations.CreateModel(
            name='Achievements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('year', models.IntegerField()),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='builder.Info')),
            ],
        ),
    ]
