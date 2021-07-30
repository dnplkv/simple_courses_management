# Generated by Django 3.2.5 on 2021-07-30 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudentName', models.CharField(max_length=200, null=True)),
                ('StudentId', models.CharField(max_length=50, null=True)),
                ('LecturesAttended', models.IntegerField(null=True)),
                ('TotalLectures', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudentName', models.CharField(max_length=200, null=True)),
                ('StudentId', models.CharField(max_length=50, null=True)),
                ('PhysicsMarks', models.IntegerField(null=True)),
                ('ChemistryMarks', models.IntegerField(null=True)),
                ('MathsMarks', models.IntegerField(null=True)),
                ('EnglishMarks', models.IntegerField(null=True)),
                ('ComputerMarks', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Message', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
