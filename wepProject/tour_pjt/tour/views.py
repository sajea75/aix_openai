from django.shortcuts import render

def tour(request):
    return render(request,'tour.html')