from django.db import models
from PIL import Image
from django.contrib.auth.models import User


class Post(models.Model):
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    nuotrauka = models.ImageField(blank=False, upload_to="uploads")

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.nuotrauka.path)
        if img.height > 600 or img.width > 600:
            new_img = (600,600)
            img.thumbnail(new_img)
            img.save(self.nuotrauka.path)

    def __str__(self):
        return self.description


class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, blank=False, related_name='comments')
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    date_commented = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.content


class Profilis(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, blank=True, null=True)
    nuotrauka = models.ImageField(default="default.png", upload_to="profile_pics")

    class Meta:
        verbose_name = 'Profilis'
        verbose_name_plural = 'Profiliai'

    def __str__(self):
        return f"{self.user.username} profilis"

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.nuotrauka.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.nuotrauka.path)
            print(self.nuotrauka.path)


class Like(models.Model):
	user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
	post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)

    