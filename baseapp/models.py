from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class ContactForm(models.Model):
    fname = models.CharField(verbose_name="First Name",max_length=20)
    lname = models.CharField(verbose_name="Last Name",max_length=20)
    phone = models.CharField(verbose_name="Phone Number", max_length=10)
    email = models.EmailField(verbose_name="Email", max_length=254)
    services = models.CharField(verbose_name="Service", max_length=50)
    message = models.TextField(verbose_name="Message")
    date = models.DateTimeField(verbose_name="Date", auto_now_add=True)
    
    class Meta:
        verbose_name = "Contact Form"
        verbose_name_plural = 'Contact Form'
        db_table = "ContactForm"

    def __str__(self):
        return self.fname + " " + self.lname



class Experience(models.Model):
    EXPERIENCE_TYPE_CHOICES = [
        ('work', 'Work Experience'),
        ('education', 'Education Experience'),
    ]

    type = models.CharField(max_length=10, choices=EXPERIENCE_TYPE_CHOICES)
    joining_date = models.DateField(verbose_name="Joining Date")
    # start_year = models.PositiveIntegerField(verbose_name="Start Year",)
    end_year = models.DateField(verbose_name="End Year",blank=True, null=True, help_text="Keep It Blank if you are currently doing this... ")
    title = models.CharField(verbose_name="Tittle", max_length=255, help_text="it can be Job title or Class")  # Job title or class
    organization = models.CharField(verbose_name="Organization",max_length=255, help_text="it can be Comany or School Name")  # Company or school
    def __str__(self):
        return f"{self.title} ({self.joining_date}-{self.end_year})"
    

class Projects(models.Model):
    name = models.CharField(max_length=30, help_text="Enter Project Name.  max character Length is 30 ")
    link = models.URLField(verbose_name="Project Live Link", help_text="example - https://www.kuldeepsaini.in", blank=True, null=True)
    image = models.ImageField(upload_to='images/projects')
    upload_date = models.DateField(auto_now=True)
    
    class Meta:
        verbose_name = "Projects"
        verbose_name_plural = 'Projects'
        db_table = 'Projects'
    
    def __str__(self):
        return self.name
    
class Skills(models.Model):
    VISIBLE_CHOICES = (
        ('hide', 'Hide'),
        ('visible', 'Visible')
    )
    name = models.CharField(verbose_name="Skill Name", max_length=50)
    knowledge = models.IntegerField(verbose_name="Skilles Covered ", validators=[MinValueValidator(10), MaxValueValidator(100)], default=50)
    image = models.FileField(verbose_name="Icon File", upload_to='Images/icons/tech')
    visiblity = models.CharField(verbose_name="Visiblity",choices=VISIBLE_CHOICES, max_length=10)
    
    class Meta:
        verbose_name = "Skills"
        db_table = "Skills"
    
    def __str__(self):
        return self.name
