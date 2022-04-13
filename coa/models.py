from email.policy import default
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Content(models.Model):
    title = models.CharField(max_length=100)
    body = RichTextField(blank = True, null = True)
    objects = models.Manager()



class ServiceTag(models.Model):
    title = models.CharField(max_length= 100)

    def __str__(self):
        return self.title

    objects = models.Manager()

class Test(models.Model):
    title = models.CharField(max_length=100)

class Service(models.Model):
    name = models.CharField(max_length = 100)
    body = RichTextField(blank = True, null = True)
    tags = models.ManyToManyField(ServiceTag)
    link = models.URLField(default = None)
    objects = models.Manager()

class OrganizationTag(models.Model):
    title = models.CharField(max_length = 100)

    def __str__(self):
        return self.title

    objects = models.Manager()

class Cluster(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=100)
    logo = models.FileField(default="null")
    description = models.TextField(max_length= 1000, default = None)
    officer_name = models.CharField(max_length = 100, default = None)
    officer_email = models.EmailField(max_length = 100, default= None)
    officer_photo = models.FileField(default="null")

    def __str__(self):
        return self.name

    objects = models.Manager()    

class Office(models.Model):
    name = models.CharField(max_length=100)
    officer_name = models.CharField(max_length = 100)
    officer_position = models.CharField(max_length = 100)
    officer_photo = models.FileField(default="null")
    officer_email = models.EmailField(max_length = 100, default= None)
    office_description = RichTextField(blank = True, null = True)

    def __str__(self):
        return self.name

    objects = models.Manager()

class Organization(models.Model):
    name = models.CharField(max_length= 100)
    abbreviation = models.CharField(max_length=100)
    logo = models.FileField(default="null")
    description =  models.TextField(max_length= 1000, default = None)
    tags = models.ManyToManyField(OrganizationTag)
    cluster = models.ForeignKey(Cluster, default = None, on_delete=models.CASCADE)
    email = models.EmailField(max_length = 100, default= None, blank = True, null = True)
    website_link = models.URLField(max_length = 200, default = None, blank = True, null = True)
    facebook_link = models.URLField(max_length = 200, default = None, blank = True, null = True)
    twitter_link = models.URLField(max_length = 200, default = None, blank = True, null = True)
    instagram_link = models.URLField(max_length = 200, default = None, blank = True, null = True)
    advocacy = models.TextField(max_length= 1000, default = None)
    core_competencies = models.TextField(max_length= 1000, default = None)
    project1_name = models.CharField(max_length = 100, default = None)
    project1_description = models.TextField(max_length= 1000, default = None)
    project1_photo = models.FileField(default="null")
    project2_name = models.CharField(max_length = 100, default = None)
    project2_description = models.TextField(max_length= 1000, default = None)
    project2_photo = models.FileField(default="null")
    project3_name = models.CharField(max_length = 100, default = None)
    project3_description = models.TextField(max_length= 1000, default = None)
    project3_photo = models.FileField(default="null")
    memberstory1_name = models.CharField(max_length = 100, default = None)
    memberstory1_content = models.TextField(max_length = 1000, default = None)
    memberstory1_photo = models.FileField(default="null")
    memberstory2_name = models.CharField(max_length = 100, default = None)
    memberstory2_content = models.TextField(max_length = 1000, default = None)
    memberstory2_photo = models.FileField(default="null")

    def __str__(self):
        return self.abbreviation

    objects = models.Manager()

class Counter:
    count = 0

    def increment(self):
        self.count += 1
        return ''
    
    
class Event(models.Model):
    name = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    event_link = models.URLField(max_length = 200, default = None)
    start_date = models.DateField(default= None)
    end_date = models.DateField(default= None, blank = True, null = True)
    start_time = models.TimeField(default= None, blank = True, null = True)
    end_time = models.TimeField(default = None, blank = True, null = True)
    all_day = models.BooleanField(default = False, blank = True)
    organization = models.ForeignKey(Organization, default = None, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    # def start_date_as_list(self):
    #     return self.start_date.split(",")
    
    objects = models.Manager()

class NewsletterCategory(models.Model):
    title = models.CharField(max_length = 100)

    def __str__(self):
        return self.title

    objects = models.Manager()

class Newsletter(models.Model):
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    date = models.DateField(default = None)
    photo = models.FileField(default="null")
    photoCaption = models.CharField(max_length = 100)
    content = RichTextField(blank = True, null = True)
    category = models.ForeignKey(NewsletterCategory, default = None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    objects = models.Manager()