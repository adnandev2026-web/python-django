from django.shortcuts import render, redirect
from . models import MovieInfo
from .forms import MovieForm

def create(request):
    if request.method == 'POST': # Using request.method == 'POST' is safer
        # ADD request.FILES here
        frm = MovieForm(request.POST, request.FILES)
        if frm.is_valid():
            frm.save()
            return redirect('list') # Redirect after saving to prevent duplicate submissions
    else:
        frm = MovieForm()

    return render(request, 'create.html', {'frm': frm})

def edit(request, pk):
    instance_to_be_edited = MovieInfo.objects.get(pk=pk)
    if request.method == 'POST':
        # ADD request.FILES here too
        frm = MovieForm(request.POST, request.FILES, instance=instance_to_be_edited)
        if frm.is_valid():
            frm.save() # Change this from instance_to_be_edited.save() to frm.save()
            return redirect('list')
    else:
        frm = MovieForm(instance=instance_to_be_edited)
    return render(request, 'create.html', {'frm': frm})

# Keep your list and delete functions as they are


def list(request):
    movie_set=MovieInfo.objects.all()
    print(movie_set)
    return render(request, 'list.html', {'movies':movie_set})


def delete(request,pk):
    instance=MovieInfo.objects.get(pk=pk)
    instance.delete()
    movie_set=MovieInfo.objects.all()
    return render(request, 'list.html', {'movies':movie_set})