from django.urls import path, include
from django.views.generic import ListView, DetailView
from Contacts.models import komc


	
urlpatterns = [
	path( '', ListView.as_view(queryset = komc.objects.all()[:20], template_name="контакты1.html")),

	]