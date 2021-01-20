from django.db import models


class Info(models.Model):
    full_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=200)
    purpose = models.TextField()
    address = models.TextField()
    phone = models.IntegerField()
    email_id = models.EmailField()
    linkedIn = models.URLField()


class Education(models.Model):
    info = models.ForeignKey('Info', on_delete=models.CASCADE)
    marks_10th = models.FloatField()
    graduation_year_10th = models.IntegerField()
    marks_12th = models.FloatField()
    graduation_year_12th = models.IntegerField()


class Achievements(models.Model):
    info = models.ForeignKey('Info', on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()
    year = models.IntegerField()


class Experience(models.Model):
    info = models.ForeignKey('Info', on_delete=models.CASCADE)
    year = models.IntegerField()
    title = models.TextField()
    description = models.TextField()

