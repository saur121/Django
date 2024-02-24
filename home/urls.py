from django.urls import path, include
from home import views
from django.contrib import admin

admin.site.site_header = "Travel India"
admin.site.site_title = "वसुधैव कुटुम्बकम्"
admin.site.index_title = "Love India"
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('projects', views.projects, name='projects'),
    path('contact', views.contact, name='contact')
]
