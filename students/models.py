from django.db import models


# Where we define our database models which django automatically translate into database tables here.
# Migrations folder keep track of any changes to our models.py files so it stays in sync with our database

class Student(models.Model):
    student_number = models.PositiveIntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    field_of_study = models.CharField(max_length=50)
    gpa = models.FloatField()

    def __str__(self):
        return f'Students: {self.first_name} {self.last_name}'
