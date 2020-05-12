from django.shortcuts import render, redirect
from .models import Computer
#from django.views.generic import View

def all_computers(request):
	comps_list = Computer.objects.all()
	return render(request, 'computers/main-page.html', {'comps_list': comps_list})

def desktop(request):
	comps_list = Computer.objects.all()
	return render(request, 'computers/desktop_category.html', {'comps_list': comps_list})

def monoblock(request):
	comps_list = Computer.objects.all()
	return render(request, 'computers/monoblock_category.html', {'comps_list': comps_list})

def delivery(request):
	comps_list = Computer.objects.all()
	return render(request, 'computers/delivery.html', {'comps_list': comps_list})

def busket(request):
	comps_list = Computer.objects.all()
	return render(request, 'computers/busket.html', {'comps_list': comps_list})

def show_computer(request):
	pass

# class delivery(View):
#     def post(self, *args, **kwargs):
#         return redirect('delivery')