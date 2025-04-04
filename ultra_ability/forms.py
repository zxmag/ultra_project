
from django import forms; from . import models

class NewsletterSubscriptionForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Your Name'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'input-field', 'placeholder': 'Your Email'}))
    confirm_email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'input-field', 'placeholder': 'Confirm Email'}))

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        confirm_email = cleaned_data.get('confirm_email')

        if email and confirm_email and email != confirm_email:
            raise forms.ValidationError("Subscription UNSUCCESSFUL: email addresses do not match, try again!")

        if models.NewsletterSubscriber.objects.filter(email=email).exists():
            raise forms.ValidationError("MESSAGE: " + email + " is already subscribed!")

        return cleaned_data






from django import forms
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

class ContactForm(forms.Form):
    # Fields
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Your Name'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'input-field', 'placeholder': 'Your Email Address'}))
    confirm_email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'input-field', 'placeholder': "Confirm Email Address"}))
    GENDER_CHOICES = [ ('male', 'Male'), ('female', 'Female'), ]
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True, label="Your Gender")
    BIBLE_VERSIONS = [
        ("", ""),
        ('kjv', 'King James Version (KJV)'),
        ('niv', 'New International Version (NIV)'),
        ('esv', 'English Standard Version (ESV)'),
        ('other', 'Other'),
        ("N/A", "I don't have a Bible"),
    ]
    bible_version = forms.ChoiceField(choices=BIBLE_VERSIONS, required=False, label="What version of the Bible do you have?")
    ENROLLMENT_CHOICES = [ ("", ""), ("Yes", "Yes"), ("No", "No") ]
    enrollment = forms.ChoiceField(choices=ENROLLMENT_CHOICES, required=True, label="Would you like to enroll in free Bible study class?")
    comments = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'input-field-big', 'placeholder': "Your Questions or Comments (Optional)"}))

    # Custom validation to ensure email and confirm_email match
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        confirm_email = cleaned_data.get("confirm_email")

        if email and confirm_email and email != confirm_email:
            raise ValidationError("Submission UNSUCCESSFUL: email addresses do not match, try again!")
        return cleaned_data





