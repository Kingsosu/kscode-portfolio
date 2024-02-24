from django.db import models
import uuid

# Create your models here.

def get_profile_image_filepath(self, filename):
    return 'profile_images/' + str(self.pk) + '/profile_image.png'

class ProjectDetails(models.Model):
    
    JOB_CHOICES = [
        ('web', 'Web Project'),
        ('ui', 'UI Project'),
    ]
        
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length=200)
    description = models.TextField()  # Corrected the field name to 'description'
    link = models.CharField(max_length=1000000)
    img = models.ImageField(upload_to=get_profile_image_filepath)
    jobtype = models.CharField(max_length=50, choices=JOB_CHOICES)

    def get_profile_image_filepath(self):
        return str(self.profile_image)[str(self.profile_image).index('profile_images/' + str(self.pk) + "/"):]

    def __str__(self):
        return self.name
