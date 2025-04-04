'''copied from blogApp - Django4ByExample, 4th Edition.'''
from django.db import models; from django.db.models.query import QuerySet
from django.utils import timezone; from django.contrib.auth.models import User
from django.urls  import reverse

'''Our custom django model [python class] manager, PublishedManager'''
class PublishedManager(models.Manager):
    def get_queryset(self) -> QuerySet:   # the -> notation simply indicates the return type of the function/method, a QuerySet in this case.
        return super().get_queryset().filter(status=FOTS.Status.PUBLISHED)


'''Fruit Of The Spirit(FOTS) django-model/python-class/database-table'''
class FOTS(models.Model):

    class Status(models.TextChoices):
        DRAFT = "DF", "Draft"   #tuple assignment, choice1
        PUBLISHED = "PB", "Published"   #tuple assignment, choice2

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date="publishTime")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ultra_ability_FOTS")
    body = models.TextField()
    publishTime = models.DateTimeField(default=timezone.now)
    createdTime = models.DateTimeField(auto_now_add=True)
    updatedTime = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    objects = models.Manager() # the default, built-in model manager
    published = PublishedManager() # our custom model manager.

    class Meta:
        '''this class defines the metadata for this model(FOTS)'''
        ordering = ["publishTime"]
        indexes = [
            models.Index(fields=["-publishTime"]),
        ]

    def __str__(self):
        #this method stringify's the title field
        return self.title

    '''generate/retrieve the canonical, python object-specific URL'''
    def getAbsoluteUrl(self):
        return reverse("ultra_ability:FOTSURL", args=[self.publishTime.year, self.publishTime.month, self.publishTime.day, self.slug])





'''Frequently Asked Question(FAQ) django-model/python-class/database-table'''
class FAQ(models.Model):

    class Status(models.TextChoices):
        DRAFT = "DF", "Draft"   #tuple assignment, choice1
        PUBLISHED = "PB", "Published"   #tuple assignment, choice2

    title = models.CharField(max_length=250)
    category = models.CharField(max_length=100, default="About Humankind and the World.")
    slug = models.SlugField(max_length=250, unique_for_date="publishTime")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ultra_ability_FAQ")
    body = models.TextField()
    publishTime = models.DateTimeField(default=timezone.now)
    createdTime = models.DateTimeField(auto_now_add=True)
    updatedTime = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    objects = models.Manager() # the default, built-in model manager
    published = PublishedManager() # our custom model manager.

    class Meta:
        '''this class defines the metadata for this model(FAQ)'''
        ordering = ["publishTime"]
        indexes = [
            models.Index(fields=["-publishTime"]),
        ]

    def __str__(self):
        #this method stringify's the title field
        return self.title

    '''generate/retrieve the canonical, python object-specific URL'''
    def getAbsoluteUrl(self):
        return reverse("ultra_ability:FAQsURL", args=[self.publishTime.year, self.slug])


'''Book django-model/python-class/database-table'''
class Book(models.Model):

    class Status(models.TextChoices):
        DRAFT = "DF", "Draft"   #tuple assignment, choice1
        PUBLISHED = "PB", "Published"   #tuple assignment, choice2

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date="publishTime")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ultra_ability_book")
    body = models.TextField()
    publishTime = models.DateTimeField(default=timezone.now)
    createdTime = models.DateTimeField(auto_now_add=True)
    updatedTime = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    objects = models.Manager() # the default, built-in model manager
    published = PublishedManager() # our custom model manager.

    class Meta:
        '''this class defines the metadata for this model(Book)'''
        ordering = ["publishTime"]
        indexes = [
            models.Index(fields=["-publishTime"]),
        ]

    def __str__(self):
        #this method stringify's the title field
        return self.title

    '''generate/retrieve the canonical, python object-specific URL'''
    def getAbsoluteUrl(self):
        return reverse("ultra_ability:books", args=[self.publishTime.year, self.publishTime.month, self.publishTime.day, self.slug])




'''Newsletter django-model/python-class/database-table'''
class Newsletter(models.Model):

    class Status(models.TextChoices):
        DRAFT = "DF", "Draft"   #tuple assignment, choice1
        PUBLISHED = "PB", "Published"   #tuple assignment, choice2

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date="publishTime")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="shirleyApp_newsletter")
    body = models.TextField()
    publishTime = models.DateTimeField(default=timezone.now)
    createdTime = models.DateTimeField(auto_now_add=True)
    updatedTime = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    objects = models.Manager() # the default, built-in model manager
    published = PublishedManager() # our custom model manager.

    class Meta:
        '''this class defines the metadata for this model(Newsletter)'''
        ordering = ["publishTime"]
        indexes = [
            models.Index(fields=["-publishTime"]),
        ]

    def __str__(self):
        #this method stringify's the title field
        return self.title

    '''generate/retrieve the canonical, python object-specific URL'''
    def getAbsoluteUrl(self):
        return reverse("ultra_ability:newsletterURL", args=[self.publishTime.year, self.publishTime.month, self.slug])


class NewsletterSubscriber(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # Ensure emails are unique
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return f"{self.name} - {self.email}"



class Student(models.Model):
    '''Python class representing a student enrolled to Dr. Shirley Cheng's Bible Study class'''
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # Ensure emails are unique
    enrolled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return f"{self.name} - {self.email}"














