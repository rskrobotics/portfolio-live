import uuid
from ckeditor.fields import RichTextField
from django.db import models
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator


class Tag(models.Model):
    '''Tag model'''
    name = models.CharField(max_length=25)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        '''Return the name of the model'''
        return self.name


class ImageAlbum(models.Model):
    name = models.CharField(max_length=255, default='Album')

    def full(self):
        return self.images.all()

    def default(self):
        return self.images.filter(default=True).first()

    def thumbnails(self):
        return self.images.filter(width__lt=100, length_lt=100)

    def __str__(self):
        '''Return the name of the model'''
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    default = models.BooleanField(default=False)
    width = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    album = models.ForeignKey(ImageAlbum, null=True, blank=True,
                              related_name='images',
                              on_delete=models.CASCADE)

    def __str__(self):
        '''Return the name of the model'''
        return self.name


class Project(models.Model):
    '''Model representing a project'''

    importance = models.PositiveIntegerField(default=5, validators=[
        MaxValueValidator(10),
        MinValueValidator(1)
    ])
    title = models.CharField(max_length=255)
    body = RichTextField(null=True, blank=True)
    thumbnail = models.ImageField(upload_to='thumbnails', blank=True)
    album = models.OneToOneField(ImageAlbum, null=True, blank=True,
                                 related_name='album',
                                 on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True)
    githuburl = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    tag = models.ManyToManyField(Tag, blank=True)
    video = models.URLField(null=True, blank=True)
    gif = models.URLField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        '''Return the name of the model'''
        return self.title
