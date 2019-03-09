from django.urls import path, include
from django.views.generic import ListView, DetailView
from doctor.models import doctor


	
urlpatterns = [
	path( '', ListView.as_view(queryset = doctor.objects.all()[:20], template_name="доктор.html")),
	]
	