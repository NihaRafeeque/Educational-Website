# Generated by Django 3.2.16 on 2023-05-16 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllocateSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coursename', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.IntegerField()),
                ('utype', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjectname', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('housename', models.CharField(max_length=200)),
                ('place', models.CharField(max_length=200)),
                ('post', models.CharField(max_length=200)),
                ('pin', models.IntegerField()),
                ('district', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('qualification', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('cv', models.CharField(max_length=200)),
                ('login', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tutor.login')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('housename', models.CharField(max_length=200)),
                ('place', models.CharField(max_length=200)),
                ('post', models.CharField(max_length=200)),
                ('pin', models.IntegerField()),
                ('district', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('login', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tutor.login')),
            ],
        ),
        migrations.CreateModel(
            name='SelectSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allocatesubject', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tutor.allocatesubject')),
                ('tutor', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tutor.tutor')),
            ],
        ),
        migrations.CreateModel(
            name='Materials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(max_length=800)),
                ('date', models.CharField(max_length=200)),
                ('time', models.CharField(max_length=200)),
                ('selectsubject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutor.selectsubject')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(max_length=800)),
                ('date', models.CharField(max_length=200)),
                ('student', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tutor.student')),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint', models.CharField(max_length=800)),
                ('complaint_date', models.CharField(max_length=200)),
                ('reply', models.CharField(max_length=800)),
                ('reply_date', models.CharField(max_length=200)),
                ('student', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tutor.student')),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classes', models.CharField(max_length=800)),
                ('date', models.CharField(max_length=200)),
                ('time', models.CharField(max_length=200)),
                ('thumbnail', models.ImageField(upload_to='')),
                ('selectsubject', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tutor.selectsubject')),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat', models.CharField(max_length=800)),
                ('date', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('student', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tutor.student')),
                ('tutor', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tutor.tutor')),
            ],
        ),
        migrations.AddField(
            model_name='allocatesubject',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tutor.course'),
        ),
        migrations.AddField(
            model_name='allocatesubject',
            name='subject',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tutor.subject'),
        ),
    ]
