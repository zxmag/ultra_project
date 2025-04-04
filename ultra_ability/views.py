from django.shortcuts import render, redirect, get_object_or_404; from . import models, forms
from django.http import Http404, HttpResponse; from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView; from django.views.decorators.http import require_POST
from django.contrib import messages; from django.conf import settings



def index(request):
    form = forms.NewsletterSubscriptionForm()
    last2Newsletters = models.Newsletter.objects.all().order_by("-publishTime")[:3]
    return render(request, "ultra_ability/index.html", {"form":form, "last2Newsletters":last2Newsletters})


def books(request):
    return redirect("http://www.shirleycheng.com/" + "?target=_blank")

'''
def contact(request):
    last2Newsletters = models.Newsletter.objects.all().order_by("-publishTime")[:3]
    form = forms.NewsletterSubscriptionForm()
    return render(request, "ultra_ability/contact.html", {"form":form, "last2Newsletters":last2Newsletters})

def FAQList(request):
    FAQList = models.FAQ.published.all()
    category1 = models.FAQ.objects.filter(category="About the Bible and Christianity.")

    last2Newsletters = models.Newsletter.objects.all().order_by("-publishTime")[:3]
    return render(request, "ultra_ability/FAQList.html", {"FAQList":FAQList, "last2Newsletters":last2Newsletters, "category1":category1})
'''

def FAQList(request):
    '''Retrieve all FAQ objects into 5 categories(python lists), according to their "category" django fields(class attributes)'''
    category1 = models.FAQ.objects.filter(category="About the Bible and Christianity.")
    category2 = models.FAQ.objects.filter(category="About Yahweh God, Jesus Christ & the Holy Spirit.")
    category3 = models.FAQ.objects.filter(category="About Eternal Life.")
    category4 = models.FAQ.objects.filter(category="About Living a Purposeful Life.")
    category5 = models.FAQ.objects.filter(category="About Humankind and the World.")

    '''Latest 3 Newsletters, to be displayed in the footer of the template'''
    last2Newsletters = models.Newsletter.objects.all().order_by("-publishTime")[:3]
    form = forms.NewsletterSubscriptionForm()
    return render(request, "ultra_ability/FAQList.html", {"form":form, "last2Newsletters":last2Newsletters, "category1":category1, "category2":category2, "category3":category3, "category4":category4, "category5":category5})


def FAQ(request, year, faq_slug):
    FAQ = get_object_or_404(models.FAQ, status=models.FAQ.Status.PUBLISHED, publishTime__year=year, slug=faq_slug)
    last2Newsletters = models.Newsletter.objects.all().order_by("-publishTime")[:3]
    form = forms.NewsletterSubscriptionForm()
    return render(request, "ultra_ability/FAQ.html", {"FAQ":FAQ, "last2Newsletters":last2Newsletters, "form":form})


def FOTSList(request):
    allFOTS = models.FOTS.published.all()
    paginator = Paginator(allFOTS, 10)
    pageNumber = request.GET.get("page", 1)
    try:
        FOTSList = paginator.page(pageNumber)
    except PageNotAnInteger:
        '''if the requested page number is not an interger, deliver the first page'''
        FOTSList = paginator.page(1)
    except EmptyPage:
        '''if the requested page number is out of range, deliver the last page of results'''
        FOTSList = paginator.page(paginator.num_pages)

    form = forms.NewsletterSubscriptionForm()
    last2Newsletters = models.Newsletter.objects.all().order_by("-publishTime")[:3]
    return render(request, "ultra_ability/FOTSList.html", {"FOTSList": FOTSList, "form":form, "last2Newsletters":last2Newsletters})


def FOTS(request, year, month, day, fots_slug):
    FOTS = get_object_or_404(models.FOTS, status=models.FOTS.Status.PUBLISHED, slug=fots_slug, publishTime__year=year, publishTime__month=month, publishTime__day=day)
    last2Newsletters = models.Newsletter.objects.all().order_by("-publishTime")[:3]
    form = forms.NewsletterSubscriptionForm()
    return render(request, "ultra_ability/FOTS.html", {"FOTS":FOTS, "last2Newsletters":last2Newsletters, "form":form})


def fundraiser(request):
    return redirect("https://gofundme.com/f/uniteinlove37" + "?target=_blank")

def image_credit(request):
    return redirect("https://pngtree.com" + "?target=_blank")


def mission(request):
    last2Newsletters = models.Newsletter.objects.all().order_by("-publishTime")[:3]
    form = forms.NewsletterSubscriptionForm()
    return render(request, "ultra_ability/mission.html", {"form":form, "last2Newsletters":last2Newsletters})

# Meet The Founder (MTF)
def MTF(request):
    last2Newsletters = models.Newsletter.objects.all().order_by("-publishTime")[:3]
    form = forms.NewsletterSubscriptionForm()
    return render(request, "ultra_ability/MTF.html", {"form":form, "last2Newsletters":last2Newsletters})


def newsletterList(request):
    allNewsletter = models.Newsletter.published.all().order_by("-publishTime")
    paginator = Paginator(allNewsletter, 10)
    pageNumber = request.GET.get("page", 1)
    try:
        newsletterList = paginator.page(pageNumber)
    except PageNotAnInteger:
        '''if the requested page number is not an interger, deliver the first page'''
        newsletterList = paginator.page(1)
    except EmptyPage:
        '''if the requested page number is out of range, deliver the last page of results'''
        newsletterList = paginator.page(paginator.num_pages)

    last2Newsletters = models.Newsletter.objects.all().order_by("-publishTime")[:3]
    form = forms.NewsletterSubscriptionForm()
    return render(request, "ultra_ability/newsletterList.html", {"newsletterList": newsletterList, "last2Newsletters":last2Newsletters, "form":form})


def newsletter(request, year, month, newsletter_slug):
    newsletter = get_object_or_404(models.Newsletter, status=models.Newsletter.Status.PUBLISHED, slug=newsletter_slug, publishTime__year=year, publishTime__month=month)
    last2Newsletters = models.Newsletter.objects.all().order_by("-publishTime")[:3]
    form = forms.NewsletterSubscriptionForm()
    return render(request, "ultra_ability/newsletter.html", {"form":form, "newsletter":newsletter, "last2Newsletters":last2Newsletters})

# Statement of Faith (SOF)
def SOF(request):
    last2Newsletters = models.Newsletter.objects.all().order_by("-publishTime")[:3]
    form = forms.NewsletterSubscriptionForm()
    return render(request, "ultra_ability/SOF.html", {"form":form, "last2Newsletters":last2Newsletters})


def support(request):
    last2Newsletters = models.Newsletter.objects.all().order_by("-publishTime")[:3]
    form = forms.NewsletterSubscriptionForm()
    return render(request, "ultra_ability/support.html", {"form":form, "last2Newsletters":last2Newsletters})

def testimonials(request):
    last2Newsletters = models.Newsletter.objects.all().order_by("-publishTime")[:3]
    form = forms.NewsletterSubscriptionForm()
    return render(request, "ultra_ability/testimonials.html", {"form":form, "last2Newsletters":last2Newsletters})

def uil_testimonials(request):
    last2Newsletters = models.Newsletter.objects.all().order_by("-publishTime")[:3]
    form = forms.NewsletterSubscriptionForm()
    return render(request, "ultra_ability/uil-testimonials.html", {"form":form, "last2Newsletters":last2Newsletters})


def subscribe_newsletter(request):
    if request.method == 'POST':
        form = forms.NewsletterSubscriptionForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            # Save the subscriber to the database
            models.NewsletterSubscriber.objects.create(name=name, email=email)

            subscriber = get_object_or_404(models.NewsletterSubscriber, email=email)
            # Send notification email to admin
            send_mail(
                subject="New Newsletter Subscription",
                message=f"New subscription from:\n\nName: {subscriber.name}\nEmail: {subscriber.email}",
                from_email="dancingtoilet@gmail.com",
                recipient_list=["dancingtoilet@gmail.com"],
                fail_silently=False,
            )

            '''
            # Send confirmation email to the user
            send_mail(
                subject="Thank you for subscribing!",
                message=f"Hi {subscriber.name},\n\nThank you for subscribing to Ultra-Ability monthly newsletter!",
                from_email="dancingtoilet@gmail.com",
                recipient_list=[subscriber.email],
                fail_silently=False,
            )
            '''
            messages.success(request, 'Newsletter subscription successful!')
            return redirect(request.META.get('HTTP_REFERER', 'index'))  # Redirect back to the previous page, defaults to the index page.
        else:
            # If the form is invalid, display the error messages, then return the user to the previous page, defaults to the index page.
            for error in form.errors.values():
                messages.error(request, error)
            return redirect(request.META.get('HTTP_REFERER', 'index'))  # Redirect back to the previous page, defaults to the index page.


    else:
        form = forms.NewsletterSubscriptionForm() #This is used to display the form( an empty NewsletterSubscriptionForm object) to the user when they first load/request (HTTP GET request) the page.

    last2Newsletters = models.Newsletter.objects.all().order_by("-publishTime")[:3]
    return render(request, 'ultra_ability/index.html', {'form': form, "last2Newsletters":last2Newsletters}) #This return statement will be executed only if both of the above, nested return statements are NOT executed.



def contact_me(request):
    if request.method == 'POST':
        form1 = forms.ContactForm(request.POST)
        if form1.is_valid():
            # Extract form data
            name = form1.cleaned_data['name']
            email = form1.cleaned_data['email']
            gender = form1.cleaned_data['gender']
            bible_version = form1.cleaned_data['bible_version']
            comments = form1.cleaned_data['comments']


            if models.Student.objects.filter(email=email).exists():
                pass
            else:
                # Save the new Student object to the database
                models.Student.objects.create(name=name, email=email)

            # Prepare email message
            subject = f"New Contact Form Submission from {name}"
            message = (
                f"Name: {name}\n"
                f"Email: {email}\n"
                f"Gender: {gender}\n"
                f"Bible Version: {bible_version}\n"
                f"Comments: {comments}\n"
            )
            send_mail(
                subject,
                message,
                "dancingtoilet@gmail.com",  # From email (set in settings.py)
                ["dancingtoilet@gmail.com"],    # To email (set in settings.py)
                fail_silently=False,
            )

            messages.success(request, "Thank you for contacting Dr. Shirley! She'll reply via email as soon as possible.")
            return redirect(request.META.get('HTTP_REFERER', 'index'))  # Redirect back to the previous page, defaults to the index page.
        else:
            # If the form is invalid, display the error messages, then return the user to the previous page, defaults to the index page.
            for error in form1.errors.values():
                messages.error(request, error)
            return redirect(request.META.get('HTTP_REFERER', 'index'))  # Redirect back to the previous page, defaults to the index page.

    else:
        form1 = forms.ContactForm()

    last2Newsletters = models.Newsletter.objects.all().order_by("-publishTime")[:3]
    form = forms.NewsletterSubscriptionForm()
    return render(request, "ultra_ability/contact.html", {'form1': form1, "form":form, "last2Newsletters":last2Newsletters})





