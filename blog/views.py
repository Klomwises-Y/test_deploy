from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import Author, Post
from .forms import ContactForm

# Create your views here.
def home(request):
    all_posts = Post.objects.all()

    return render(request, 'blog/home.html', {'all_posts': all_posts})

def blog_details(request, id):
     single_post = Post.objects.get(id = id)

     return render(request, 'blog/blog-details.html', {'single_post': single_post})

def contact(request):
    form = ContactForm(request.POST)

    #Check incoming request
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        # print("This is not POST")
        form = ContactForm()
    
    return render(request, 'blog/forms.html', 
    {'form':form})