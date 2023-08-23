from django.db import models

# Create your models here.

class user_info(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    status = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title
    
class document_save(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, null=True)
    document = models.FileField(upload_to='document/', null=True)
    video_file = models.FileField(upload_to='video/', null=True, blank=True)
    # video_file = models.ArrayField(upload_to='video/', null=True)

class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='songs/')
    # Add more fields as needed (e.g., album, genre, etc.)

    def __str__(self):
        return self.title
