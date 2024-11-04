'''
# Create your models here.
from django.db import models
from django.utils.text import slugify
from django.utils import timezone

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    class Meta:
        ordering = ['-pub_date']  # Ensures posts are ordered by publication date in descending order

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
from django.contrib import admin
from .models import BlogPost
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')  # Display the title and publication date in the admin
    prepopulated_fields = {"slug": ("title",)}  # Automatically populate the slug field based on the title

admin.site.register(BlogPost, BlogPostAdmin)
'''
from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=200, unique=True, blank=True)  # Slug for friendly URLs

    class Meta:
        ordering = ['-pub_date']  # Order by publication date (newest first)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # Automatically generate slug from the title
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

from adminapp.models import StudentList

class AddCourse(models.Model):
    COURSE_CHOICES =[
        ('AOOP' , 'ADVANCED OBJECT ORIENTED PROGRAMMING'),
        ('PFSD', 'PYTHON FULL STACK DEVELOPMENT'),
    ]
    SECTION_CHOICES=[
        ('S11','SECTION S11'),
        ('S12', 'SECTION S12'),
        ('S13', 'SECTION S13'),
        ('S14', 'SECTION S14'),
        ('S15', 'SECTION S15'),
        ('S16', 'SECTION S16'),
        ('S17', 'SECTION S17'),
    ]
    student = models.ForeignKey(StudentList, on_delete= models.CASCADE)
    course=models.CharField(max_length=50, choices = COURSE_CHOICES)
    section = models.CharField(max_length=50, choices=SECTION_CHOICES)
    def __str__(self):
        return f'{self.student.Register_Number} - {self.course} ({self.section})'

class Marks(models.Model):
    COURSE_CHOICES = [
        ('AOOP', 'ADVANCED OBJECT ORIENTED PROGRAMMING'),
        ('PFSD', 'PYTHON FULL STACK DEVELOPMENT'),
    ]
    student=models.ForeignKey(StudentList,on_delete=models.CASCADE)
    course=models.CharField(max_length=50,choices=COURSE_CHOICES)
    marks=models.IntegerField()
    def __str__(self):
        return f"{self.student.name}-{self.course}"


