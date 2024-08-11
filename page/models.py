from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.TextField(max_length=30, null=True)
    category = models.TextField(max_length=30, null=True)
    location = models.TextField(max_length=30, null=True)
    year = models.IntegerField(null=True)
    branding = models.TextField(max_length=30, null=True)
    url_project = models.URLField(null=True)

    image = models.FileField(upload_to="project/", null=True)
    image_2 = models.FileField(upload_to="project/", null=True)
    image_3 = models.FileField(upload_to="project/", null=True)

    visible_home = models.BooleanField(null=True)
    visible_work = models.BooleanField(null=True)
    design = models.BooleanField(null=True)
    development = models.BooleanField(null=True)


    def __str__(self):
        return self.name


class Mockup(models.Model):
    MOCKUP_TYPE_CHOICES = (
        ('phone', 'phone'),
        ('iphone 15', 'iphone 15'),
        ('phone prototype', 'phone Prototype'),
        ('ipad', 'ipad'),
        ('mac pro', 'mac pro'),
        ('mac pro studio', 'mac pro studio'),
        ('prototype', 'prototype'),
        ('big video', 'big video'),
        ('big image', 'big image'),
    )

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    mockup_type = models.TextField(max_length=30, null=True, choices=MOCKUP_TYPE_CHOICES)
    background_color = models.TextField(max_length=10, null=True)
    order = models.IntegerField(null=True)

    main_file = models.FileField(upload_to="project/", null=True)
    file_1 = models.FileField(upload_to="project/", null=True)
    file_2 = models.FileField(upload_to="project/", null=True)
    file_3 = models.FileField(upload_to="project/", null=True)

    def __str__(self):
        return f"{self.project.name}_{self.mockup_type}_{self.order}"
    
class Contact(models.Model):
    name = models.CharField(max_length=30, null=True)
    email = models.CharField(max_length=30, null=True)
    company = models.CharField(max_length=30, null=True)
    service = models.CharField(max_length=100, null=True)
    message = models.CharField(max_length=1000, null=True)

class Site_data(models.Model):
    first_name = models.CharField(max_length=30, null=True)
    middle_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    work_1 = models.CharField(max_length=30, null=True)
    work_2 = models.CharField(max_length=30, null=True)
    location = models.CharField(max_length=30, null=True)
    desc_1 = models.CharField(max_length=1000, null=True)
    desc_2 = models.CharField(max_length=1000, null=True)
    horizontal_items_1 = models.FileField(upload_to="project/", null=True)
    horizontal_items_2 = models.FileField(upload_to="project/", null=True)
    horizontal_items_3 = models.FileField(upload_to="project/", null=True)
    horizontal_items_4 = models.FileField(upload_to="project/", null=True)
    horizontal_items_5 = models.FileField(upload_to="project/", null=True)
    horizontal_items_6 = models.FileField(upload_to="project/", null=True)
    horizontal_items_7 = models.FileField(upload_to="project/", null=True)
    horizontal_items_8 = models.FileField(upload_to="project/", null=True)

    about_title = models.CharField(max_length=30, null=True)
    about_title_2 = models.CharField(max_length=30, null=True)    
    about_1 = models.CharField(max_length=1000, null=True)
    about_2_title = models.CharField(max_length=30, null=True)
    about_2 = models.CharField(max_length=1000, null=True)
    service_1_title = models.CharField(max_length=30, null=True)
    service_1 = models.CharField(max_length=300, null=True)
    service_2_title = models.CharField(max_length=30, null=True)
    service_2 = models.CharField(max_length=300, null=True)
    service_3_title = models.CharField(max_length=30, null=True)
    service_3 = models.CharField(max_length=300, null=True)

    work_title_1 = models.CharField(max_length=30, null=True)
    work_title_2 = models.CharField(max_length=30, null=True)

    contact_title_1 = models.CharField(max_length=30, null=True)
    contact_title_2 = models.CharField(max_length=30, null=True)
    contact_title_3 = models.CharField(max_length=30, null=True)
    contact_title_4 = models.CharField(max_length=30, null=True)
    business_data_1 = models.CharField(max_length=30, null=True)
    business_data_2 = models.CharField(max_length=30, null=True)
    business_data_3 = models.CharField(max_length=30, null=True)
    
    email = models.CharField(max_length=30, null=True)
    phone_number = models.CharField(max_length=30, null=True)
    edition = models.CharField(max_length=30, null=True)
    social_1 = models.URLField(null=True)
    social_2 = models.URLField(null=True)
    social_3 = models.URLField(null=True)
    social_4 = models.URLField(null=True)
    social_1_name = models.CharField(max_length=30, null=True)
    social_2_name = models.CharField(max_length=30, null=True)
    social_3_name = models.CharField(max_length=30, null=True)
    social_4_name = models.CharField(max_length=30, null=True)
    edition = models.CharField(max_length=4, null=True)
    
     
    
