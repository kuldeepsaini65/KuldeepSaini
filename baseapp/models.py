from django.db import models



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