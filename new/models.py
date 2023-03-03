from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify


class Status(models.TextChoices):
    Draft = "DF" "Draft"
    Published = "PB" "Published"


class Category(models.Model):
    name = models.CharField(max_length=65)
    slug = models.SlugField(
        default='',
        editable=False,
        max_length=150,
    )

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class NewImagePost(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(
        default='',
        editable=False,
        max_length=250,
    )
    body = RichTextField()
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    published_time = models.DateTimeField(auto_now=True)
    created_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20,
                              choices=Status.choices,
                              default=Status.Draft
                              )

    class Meta:
        ordering = ['-published_time']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


class Comment(models.Model):
    news = models.ForeignKey(
        NewImagePost,
        on_delete=models.PROTECT,
        related_name='comments'
    )
    body = models.TextField(verbose_name="Leave a comment")
    created_time = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_time']

    def __str__(self):
        return self.body