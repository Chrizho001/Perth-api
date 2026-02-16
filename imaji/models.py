from django.db import models
from django.contrib.auth.models import AbstractUser
import cloudinary
import cloudinary.models
from django_prose_editor.fields import ProseEditorField
from taggit.managers import TaggableManager


class User(AbstractUser):

    def __str__(self):
        return self.username


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = ProseEditorField(
        extensions={
            "Bold": True,
            "Italic": True,
            "BulletList": True,
            "ListItem": True,
            "Link": True,
        },
        sanitize=True,  # sanitize HTML before saving
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    image = cloudinary.models.CloudinaryField("image", blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=[("draft", "Draft"), ("published", "Published")],
        default="draft",
    )

    # add tags here
    tags = TaggableManager()

   

    def __str__(self):
        return self.title
