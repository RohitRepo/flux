from django.shortcuts import render, redirect

from .models import Contact


def home(request):
	if request.method == "POST":
		mobile = request.POST.get('Mobile')
		name = request.POST.get('Name')
		if name and mobile and len(mobile) < 15 and len(name) < 50:
			Contact.objects.create(mobile=mobile, name=name)
			return redirect("/congratulations")
	
	return render(request, "index.html")