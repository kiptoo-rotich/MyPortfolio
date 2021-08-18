from django.db import models
from cloudinary.models import CloudinaryField
from tinymce.models import HTMLField
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User


technologies =(
    ('Django','Django'),
    ('Flask','Flask'),
    ('Angular','Angular'),
    ('Bootstrap','Bootstrap'),
    ('Git','Git'),
    ('Javascript','Javascript'),
    ('Postgresql','Postgresql'),
    ('DjangoREST','DjangoREST'),

)


class Project(models.Model):
    title = models.CharField(max_length=100)
    topics=models.CharField(max_length=20,null=True)
    description = HTMLField()
    screenshot=CloudinaryField('image',default='Image')
    repo_link = models.CharField(max_length=50,null=True)
    live_links = models.CharField(max_length=50,null=True)
    technologies = MultiSelectField(max_length=200,null=True,choices=technologies)

      
    def __str__(self):
        return self.title
    
    def save_project(self):
        self.save()

class Details(models.Model):
    name = models.CharField(max_length=30)
    role = models.CharField(max_length=50)
    quote = HTMLField()
    phone_number=models.CharField(max_length=13)
    github_link = models.CharField(max_length=100)
    city= models.CharField(max_length=60)
    country= models.CharField(max_length=60,null=True)
    linkedin=models.CharField(max_length=100)
    email= models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
    def save_details(self):
        self.save()


class Education(models.Model):
    certificate_type = models.CharField(max_length=100)
    institution = models.CharField(max_length=50)
    period = models.CharField(max_length=30)
    certificate_name= models.CharField(max_length=100)
    school_location= models.CharField(max_length=30)

    def __str__(self):
        return self.institution

    def save_education(self):
        self.save()
        
        
class Experience(models.Model):
    position = models.CharField(max_length=20)
    company=models.CharField(max_length=20)
    date= models.CharField(max_length=20)
    tasks=HTMLField()
    contact_info=models.CharField(max_length=30)
    
    def __str__(self):
        return self.company
    
    def save_experience(self):
        self.save()