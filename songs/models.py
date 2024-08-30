from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=75)
    audio_url = models.URLField()
    artist = models.CharField(max_length=40)
    release_year = models.PositiveIntegerField()
    genres = ArrayField(
        models.CharField(max_length=35),
        null=True,
        blank=True
    )
    cover_image = models.CharField(
        default='https://res.cloudinary.com/dcfi0p4p4/image/upload/v1724513202/song_placeholder_tnjmaf.png',
        blank=True,
    ) 
    owner = models.ForeignKey(
        'jwt_auth.User',
        on_delete=models.CASCADE,
        related_name='song_created'
    )
    

    def __str__(self):
        return f'{self.title} by {self.artist}, released {self.release_year}'

