from django.db import models

# Create your models here.

# A model is a Python class that has fields for each piece of information that
# we want to track.

# Model representing a course:
class Course(models.Model):
    # Fields for the information about a course that we're interested in
    # (Django always generates an ID field automatically)
    
    # Department (text)
    dept = models.CharField(max_length=4)
    
    # Course number (integer)
    number = models.IntegerField()
    
    # Title (text)
    title = models.CharField(max_length=50)
    
    # Instructor: an instance of the Professor model
    # In the database, every course is going to also store the
    # ID number of a Professor
    # "null=True": the field is nullable (it can be NULL)
    instructor = models.ForeignKey('Professor', blank=True, null=True)
    
    # Function that converts a Course into a string (for use in the
    # admin site etc.)
    def __str__(self):
        return '%s %d: %s' % (self.dept, self.number, self.title)
        
# Model representing a student
class Student(models.Model):
    # First and last names (text)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=40)
    
    # Birthdate (date)
    birthdate = models.DateField()
    
    # E-mail address
    email = models.EmailField()
    
    def __str__(self):
        return '%09d: %s, %s' % (self.id, self.lname, self.fname)
        
class Professor(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=40)
    
    email = models.EmailField()
    # "blank=True": this field can be empty
    extension = models.IntegerField(blank=True)
    
    office = models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        return '%s %s' % (self.fname, self.lname)
        
    
    
    
    
    
    
    
    
    
    