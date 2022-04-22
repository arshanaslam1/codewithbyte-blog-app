from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from accounts.models import User
from django.utils.text import slugify
from hitcount.models import HitCount
from django.urls import reverse_lazy


class TimeStampedModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PostTag(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    cover = models.ImageField(upload_to='PostTag/%Y/%m/%d/', default='default.png', blank=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value)
        super(PostTag, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Post Tag'
        verbose_name_plural = 'Post Tags'


class PostCategory(models.Model):
    title = models.CharField(max_length=200)
    cover = models.ImageField(upload_to='PostCategory/%Y/%m/%d/', default='default.png', blank=False)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value)
        super(PostCategory, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Post Category'
        verbose_name_plural = 'Post Categories'


class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(status=True)

    def approved(self):
        return self.filter(active=True)


class Post(TimeStampedModel):
    ACTIVE = (
        (0, "Pending"),
        (1, "Approve")
    )
    STATUS = (
        (0, "Draft"),
        (1, "Publish")
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    active = models.BooleanField(default=True)
    category = models.ForeignKey('PostCategory', on_delete=models.CASCADE)
    content = models.TextField(blank=False, null=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
                                        related_query_name='hit_count_generic_relation')
    cover = models.ImageField(upload_to='users/%Y/%m/%d/',  default='default.png', blank=False)
    meta_description = models.TextField(null=True, blank=False)
    objects = PostQuerySet.as_manager()
    slug = models.SlugField(max_length=200, unique=True, blank=False)
    status = models.IntegerField(choices=STATUS, default=0, blank=False)
    title = models.CharField(max_length=200, unique=True, blank=False)
    tags = models.ManyToManyField('PostTag')
    likes = models.ManyToManyField(User, related_name="article_likes")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value)
        super(Post, self).save(*args, **kwargs)

        # for site maps

    def get_absolute_url(self):
        return reverse_lazy("post_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created_on']


class Comment(TimeStampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    comment = models.TextField()
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['-created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.comment, self.name)


class Subscribe(TimeStampedModel):
    email = models.EmailField(null=True, blank=True, unique=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Subscribe'
        verbose_name_plural = 'Subscribes'
        ordering = ['-created_on']


