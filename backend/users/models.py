from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class Profile(models.Model):

    """ Profile Model """

    GENDERS = (
        ('M', 'Masculine'),
        ('F', 'Feminine')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default='', blank=True)
    website = models.URLField(blank=True)
    gender = models.CharField(max_length=1, choices=GENDERS)
    avatar = ProcessedImageField(upload_to='avatars',
                                 processors=[ResizeToFill(100, 50)],
                                 format='JPEG',
                                 options={'quality': 60}, blank=True)
    following = models.ManyToManyField(
        'self', blank=True, symmetrical=False, related_name='following_users')
    followers = models.ManyToManyField(
        'self', blank=True, symmetrical=False, related_name='followed_by')

    def __str__(self):
        return self.user.username

    @property
    def post_count(self):
        return self.user.images.all().count()

    @property
    def followers_count(self):
        return self.followers.all().count()

    @property
    def following_count(self):
        return self.following.all().count()