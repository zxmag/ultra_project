from django.contrib import admin; from . import models

# Register your models here.
@admin.register(models.FOTS)
class FOTSAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "author", "publishTime", "status"]
    list_filter = ["status", "createdTime", "publishTime", "author"]
    search_fields = ["title", "body"]
    prepopulated_fields = { "slug": ("title",)} #a tuple with only one element is the value in this key-value pair of the dictionary.
    raw_id_fields = ["author"]
    date_hierarchy = "publishTime"
    ordering = ["status", "publishTime"]



@admin.register(models.FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "slug", "author", "publishTime", "status"]
    list_filter = ["status", "createdTime", "publishTime", "author"]
    search_fields = ["title", "body"]
    prepopulated_fields = { "slug": ("title",)} #a tuple with only one element is the value in this key-value pair of the dictionary.
    raw_id_fields = ["author"]
    date_hierarchy = "publishTime"
    ordering = ["status", "publishTime"]


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "author", "publishTime", "status"]
    list_filter = ["status", "createdTime", "publishTime", "author"]
    search_fields = ["title", "body"]
    prepopulated_fields = { "slug": ("title",)} #a tuple with only one element is the value in this key-value pair of the dictionary.
    raw_id_fields = ["author"]
    date_hierarchy = "publishTime"
    ordering = ["status", "publishTime"]



@admin.register(models.Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "author", "publishTime", "status"]
    list_filter = ["status", "createdTime", "publishTime", "author"]
    search_fields = ["title", "body"]
    prepopulated_fields = { "slug": ("title",)} #a tuple with only one element is the value in this key-value pair of the dictionary.
    raw_id_fields = ["author"]
    date_hierarchy = "publishTime"
    ordering = ["status", "publishTime"]


admin.site.register(models.NewsletterSubscriber)
admin.site.register(models.Student)
'''
@admin.register(models.Subscriber)
class SubscriberAdmin:
    list_display = ["full_name", "email", "subscribed_at"]
    ordering = ["subscribed_at"]
'''


