from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def print_hello(request):
    movie_data={'movies' : [{
        'title':'Godfather',
        'year':1990,
        
        'success':False,
    },
    {
        'title':'titanic',
        'year':2002,
        'summary':'story of an underworld kin',
        'success':False,
    },
    {
        'title':'In to the wild',
        'year':1990,
        
        'success':True,
    },
    {
        'title':'Goldfish',
        'year':1980,
        'summary':'story of an sadd kin',
        'success':True,
    },
    {
        'title':'Goldfish',
        'year':1980,
        'summary':'story of an underworld kin',
        'success':True,
    }]}
    return render(request,'hello.html',movie_data)

