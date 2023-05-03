from django.db import models
from django.core.validators import FileExtensionValidator
from django.conf import settings

def custom_upload_path(instance, filename):
    # Generate the file path dynamically
    return 'user_{0}/{1}'.format(instance.user.id, filename)
# Create your models here.

class Tapes(models.Model):
    title = models.CharField(max_length=50)
    music_by = models.CharField(max_length=25, default='artist')
    singer = models.CharField(max_length=20, default='artist')
    album = models.CharField(max_length=20,default='unknown')

    record_file = models.FileField(blank=True, null=True, upload_to=custom_upload_path,
                                   validators=[FileExtensionValidator(allowed_extensions=['mp3'])])
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.user.id


