# Generated by Django 4.1.4 on 2023-05-25 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=250, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_name', models.CharField(max_length=250, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=250, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_year', models.CharField(max_length=250, unique=True)),
                ('department', models.ManyToManyField(to='main.department')),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester_name', models.CharField(max_length=250, unique=True)),
                ('levels', models.ManyToManyField(to='main.level')),
            ],
        ),
        migrations.AddField(
            model_name='level',
            name='sessions',
            field=models.ManyToManyField(to='main.session'),
        ),
        migrations.AddField(
            model_name='department',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departments', to='main.faculty'),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('file', models.FileField(unique=True, upload_to='uploads/')),
                ('department', models.ManyToManyField(to='main.department')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.level')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='main.semester')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.session')),
            ],
        ),
    ]
