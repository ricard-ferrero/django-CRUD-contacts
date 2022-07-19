from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import Contact

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# READ
class Index(generic.ListView):
	template_name = 'CRUD/index.html'

	def get_queryset(self):
		return Contact.objects.order_by('name')

# CREATE
def new(request):
	return render(request, 'CRUD/new.html')

def create(request):
	name = request.POST['name']
	phone = request.POST['phone']
	Contact(name=name, phone=phone).save()
	return HttpResponseRedirect(reverse('crud:read'))

# UPDATE
class Edit(generic.DetailView):
	template_name = 'CRUD/edit.html'
	model = Contact

def update(request, contact_id):
	contact = get_object_or_404(Contact, pk=contact_id)
	contact.name = request.POST['name']
	contact.phone = request.POST['phone']
	contact.save()
	return HttpResponseRedirect(reverse('crud:read'))

# DELETE
class Remove(generic.DetailView):
	template_name = 'CRUD/remove.html'
	model = Contact

def delete(request, contact_id):
	contact = get_object_or_404(Contact, pk=contact_id)
	contact.delete()
	return HttpResponseRedirect(reverse('crud:read'))