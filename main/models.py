from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    likes = models.IntegerField(default=0, blank=True, null=True)
    repost = models.IntegerField(default=0, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="images/")

    def get_absolute_url(self):
        return f"/blog/{self.pk}"

    def __str__(self):
        return self.title[:15]





