from django.shortcuts import render, HttpResponse, redirect
from .models import Wine



# Add the Cat class & list and view function below the imports
# class Wine:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, description, price, year):
#     self.name = name
#     self.description = description
#     self.price = price
#     self.year = year

# wines = [
#   Wine('Domaine Leroy Chambertin Grand Cru ', 'Exprensive', 5921, 1994),
#   Wine('Domaine Georges & Christophe Roumier Musigny Grand Cru 1990', 'Le Musigny cineyard only produces 380 bottles a years', 11720, 1990 ),
#   Wine('Domaine Leroy Musigny Grand Cru 2012', 'Described as magical ans sumptuous wine', 14450, 2012),
# ]

# Create your views here.

def home(request):
	return HttpResponse('<h1>Hello</h1>')


def about(request):
	return render(request, 'about.html')

def wines_index(request):
	wines = Wine.objects.all()
	context = {
	'wines': wines
	}
	return render(request, 'wines/index.html', context)


def wines_detail(request, wine_id):
	wine = Wine.objects.get(id=wine_id)
	context = {
	'wine': wine,
	}
	return render(request, 'wines/detail.html', )













