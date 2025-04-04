from django.urls import path, re_path; from . import views


app_name = "ultra_ability"

urlpatterns = [
    path("", views.index, name="indexURL"),
    path("dr shirley christian books/", views.books, name="booksURL"),
    path("frequently asked questions/", views.FAQList, name="FAQListURL"),
    path("<int:year>/<slug:faq_slug>", views.FAQ, name="FAQsURL"),
    path("<int:year>/<int:month>/<int:day>/<slug:post>/", views.FOTS, name="FOTSURL"),
    path("fruits of the spirit/", views.FOTSList , name="FOTSListURL"),
    path("<int:year>/<int:month>/<int:day>/<slug:fots_slug>", views.FOTS, name="FOTSURL"),
    path("fundraiser", views.fundraiser, name="fundraiserURL"),
    path("image_credit", views.image_credit, name="image_creditURL"),
    path("mission", views.mission, name="missionURL"),
    path("meet the founder", views.MTF, name="MTFURL"),
    path("ultra-ability monthly newsletter/", views.newsletterList, name="newsletterListURL"),
    path("<int:year>/<int:month>/<slug:newsletter_slug>", views.newsletter, name="newsletterURL"),
    path("stament of faith/", views.SOF, name="SOFURL"),
    path("support the ministry/", views.support, name="supportURL"),
    path("bible study testimonials/", views.testimonials, name="testimonialsURL"),
    path("uil testimonials/", views.uil_testimonials, name="uil-testimonialsURL"),
    path('subscribe/', views.subscribe_newsletter, name='subscribe_newsletter'),
    path('contact chaplain shirley/', views.contact_me, name='contactURL'),

]



