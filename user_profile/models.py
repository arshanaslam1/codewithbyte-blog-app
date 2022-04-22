from django.db import models
from django.template.context_processors import static
from django.urls import reverse_lazy
from accounts.models import User


class TimeStampedModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('Male', "Male"),
        ('Female', "Female"),
        ('Others', "Others")
    )
    # Managed fields
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE, primary_key=True)
    avatar = models.ImageField(upload_to="profiles/avatars/", default='default.png', null=True, blank=True)

    # about
    thumbnail = models.ImageField(upload_to="profiles/thumbnail/", default='default.png', null=True, blank=True)
    introvideo = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=7, choices=GENDER_CHOICES, null=True, blank=True)
    phone = models.CharField(max_length=32, null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    cv = models.CharField(max_length=255, null=True, blank=True)

    # Socials
    facebook = models.CharField(max_length=255, null=True, blank=True)
    instagram = models.CharField(max_length=255, null=True, blank=True)
    twitter = models.CharField(max_length=255, null=True, blank=True)
    linkedin = models.CharField(max_length=255, null=True, blank=True)
    github = models.CharField(max_length=255, null=True, blank=True)
    youtube = models.CharField(max_length=255, null=True, blank=True)
    whatsapp = models.CharField(max_length=255, null=True, blank=True)

    # addresses
    address = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=32, null=True, blank=True)
    country = models.CharField(max_length=32, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    zip = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return self.user.username

    @property
    def get_avatar(self):
        return self.avatar.url if self.avatar else static('assets/default.png')

    def get_absolute_url(self):
        return reverse_lazy("profile", kwargs={"pk": self.user.id})


class Resume(models.Model):
    CATEGORY = (
        ('Education', "Education"),
        ('Experience', "Experience"),
        ('Certification', "Certification"),
        ('Awards', "Awards")
    )

    # Managed fields
    user = models.ForeignKey(User, related_name="resume", on_delete=models.CASCADE)
    category = models.CharField(max_length=13, choices=CATEGORY, null=True, blank=False)
    issueDate = models.DateField(max_length=150, blank=False, null=True)
    expirationDate = models.DateField(max_length=150, blank=True, null=True)
    name = models.CharField(max_length=150, null=True, blank=False)
    organization = models.CharField(max_length=255, null=True, blank=False)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Resume'
        verbose_name_plural = 'Resumes'

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse_lazy("profile", kwargs={"pk": self.user.id})


class Skills(models.Model):
    CATEGORY = (
        ('Skills', "Skills"),
        ('Knowledge', "Knowledge"),
        ('Language', "Language"),
    )

    # Managed fields
    user = models.ForeignKey(User, related_name="skills", on_delete=models.CASCADE)
    category = models.CharField(max_length=10, choices=CATEGORY, null=True, blank=False)
    percentage = models.IntegerField(null=True, blank=False)
    title = models.CharField(max_length=32, null=True, blank=False)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse_lazy("profile", kwargs={"pk": self.user.id})


class Project(models.Model):

    # Managed fields
    user = models.ForeignKey(User, related_name="project", on_delete=models.CASCADE)
    category = models.CharField(max_length=32, null=True, blank=False)
    title = models.CharField(max_length=32, null=True, blank=False)
    web = models.ImageField(upload_to="portfolio/web/avatars/", default='default.png', null=True, blank=True)
    mob = models.ImageField(upload_to="portfolio/mob/avatars/", default='default.png', null=True, blank=True)
    link = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolio'

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse_lazy("profile", kwargs={"pk": self.user.id})


class Contact(TimeStampedModel):
    General = 'General'
    ProjectReview = 'Project Review'
    HireMe = 'Hire Me'
    SUBJECT = (
        (General, "General"),
        (ProjectReview, "ProjectReview"),
        (HireMe, "HireMe")
    )
    user = models.ForeignKey(User, related_name="contact", on_delete=models.CASCADE)
    email = models.EmailField(unique=False)
    phone = models.PositiveBigIntegerField(unique=False)
    subject = models.CharField(
        max_length=14,
        choices=SUBJECT,
        default=General
    )
    message = models.CharField(max_length=1000, unique=False)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        ordering = ['-created_on']
