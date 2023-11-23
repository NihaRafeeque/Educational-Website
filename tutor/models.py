from django.db import models


# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length=200)
    password = models.IntegerField()
    utype = models.CharField(max_length=200)


class Tutor(models.Model):
    name = models.CharField(max_length=200)
    housename = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    post = models.CharField(max_length=200)
    pin = models.IntegerField()
    district = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    qualification = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    cv = models.CharField(max_length=200)
    login = models.ForeignKey(Login, default=1, on_delete=models.CASCADE)


class Student(models.Model):
    name = models.CharField(max_length=200)
    housename = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    post = models.CharField(max_length=200)
    pin = models.IntegerField()
    district = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    login = models.ForeignKey(Login, default=1, on_delete=models.CASCADE)


class Complaint(models.Model):
    student = models.ForeignKey(Student, default=1, on_delete=models.CASCADE)
    complaint = models.CharField(max_length=800)
    complaint_date = models.CharField(max_length=200)
    reply = models.CharField(max_length=800)
    reply_date = models.CharField(max_length=200)


class Course(models.Model):
    coursename = models.CharField(max_length=200)


class Subject(models.Model):
    subjectname = models.CharField(max_length=200)


class Feedback(models.Model):
    student = models.ForeignKey(Student, default=1, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=800)
    date = models.CharField(max_length=200)


class Chat(models.Model):
    student = models.ForeignKey(Student, default=1, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Tutor, default=1, on_delete=models.CASCADE)
    chat = models.CharField(max_length=800)
    date = models.CharField(max_length=200)
    type = models.CharField(max_length=200)


class AllocateSubject(models.Model):
    course = models.ForeignKey(Course, default=1, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, default=1, on_delete=models.CASCADE)


class SelectSubject(models.Model):
    allocatesubject = models.ForeignKey(AllocateSubject, default=1, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Tutor, default=1, on_delete=models.CASCADE)


class Materials(models.Model):
    selectsubject = models.ForeignKey(SelectSubject, on_delete=models.CASCADE)
    material = models.CharField(max_length=800)
    date = models.CharField(max_length=200)
    time = models.CharField(max_length=200)


class Class(models.Model):
    selectsubject = models.ForeignKey(SelectSubject, default=1, on_delete=models.CASCADE)
    classes = models.CharField(max_length=800)
    date = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    thumbnail = models.ImageField()
