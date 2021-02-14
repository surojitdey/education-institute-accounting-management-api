from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date


class signinInfo(models.Model):
    #id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    client_ip = models.CharField(max_length=50,null=True)
    old_timestamp = models.DateTimeField(null=True)
    new_timestamp = models.DateTimeField(null=True)

    def __str__(self):
        return '%s' %(self.user.username)
    def save(self, *args, **kwargs):
        self.user = User.objects.get(id = 1)
        super().save(*args, **kwargs)




class students(models.Model):
    DEPT_CHOICES = (
        ('Bachelor of Science','B.Sc.'),
        ('Bachelor of Science in Information Technology','B.Sc.(IT)'),
        ('Master of Science','M.Sc.'),
        ('Bachelor of Engineering','B.E.'),
        ('PhD','PhD'),
    )
    BRANCH_CHOICES = (
        ('Physics','PHY'),
        ('Chemistry','CHEM'),
        ('Mathematics','MATH'),
        ('B.Sc.(IT)','B.Sc.(IT)'),
        ('Power Electronics & Instrumentation Engineering','PEIE'),
        ('Electronics & Telecommunication Engineering','ETE'),
        ('Civil Engineering','CE'),
        ('Mechanical Engineering','ME'),
    )
    CASTE_CHOICES = (
        ('General','GENERAL'),
        ('OBC','OBC'),
        ('SC','SC'),
        ('ST','ST'),
        ('ST(H)','ST(H)'),
    )
    SEMESTER_CHOICES = (
        ('First','I'),
        ('Second','II'),
        ('Third','III'),
        ('Fourth','IV'),
        ('Fifth','V'),
        ('Sixth','VI'),
        ('Seventh','VII'),
        ('Eighth','VIII'),
    )

    first_name = models.CharField(max_length=100,null=False,default="NULL")
    last_name = models.CharField(max_length=100,null=False,default="NULL")
    date_of_birth = models.DateField(null=False,default=timezone.now)
    depertment = models.CharField(max_length=100,null=False, choices=DEPT_CHOICES, default="NULL")
    branch = models.CharField(max_length=100,null=False, choices=BRANCH_CHOICES, default="NULL")
    caste = models.CharField(max_length=100,null=False, choices=CASTE_CHOICES, default="NULL")
    semester = models.CharField(max_length=100,null=False, choices=SEMESTER_CHOICES, default="NULL")

    def __str__(self):
        return self.first_name


class department(models.Model):
    DEPT_CHOICES = (
        ('Bachelor of Science','B.Sc.'),
        ('Bachelor of Science in Information Technology','B.Sc.(IT)'),
        ('Master of Science','M.Sc.'),
        ('Bachelor of Engineering','B.E.'),
        ('PhD','PhD'),
    )
    dept_name = models.CharField(max_length=100,null=False, choices=DEPT_CHOICES, default="NULL")
    dept_short = models.CharField(max_length=100,null=False, default="NULL")

    def dept_acronym(self):
        for dept in self.DEPT_CHOICES:
            if dept[1] == self.dept_name:
                return dept[1]
            else:
                return "NULL"
    def save(self, *args, **kwargs):
        if self.dept_short=="NULL":
            self.dept_short = self.dept_acronym()
        super().save(*args, **kwargs)
