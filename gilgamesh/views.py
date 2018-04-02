from django.shortcuts import render

# Create your views here.
def index(request):
	"""pagina inicial"""
	return render(request, 'gilgamesh/index.html')

def about(request):
	"""Pagina sobre (about)"""
	return render(request, 'gilgamesh/about.html')

def download(request):
	"""Pagina de downloads"""
	return render(request, 'gilgamesh/download.html')



