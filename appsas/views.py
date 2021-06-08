from django.http import request
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Like, Post, Profilis, PostComment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import User
from .forms import  UserUpdateForm, ProfilisUpdateForm
from datetime import datetime, timezone
from io import BytesIO
from django.core.files import File
from PIL import Image
from django.db.models import Q
from django.views.generic import DetailView



@login_required
def index(request):
    posts = Post.objects.all()
    if request.method=='POST':
        comment=PostComment(content=request.POST.get("komentaras"),
        date_commented=request.POST.get("date"),
        commenter= request.user,
        post=Post.objects.get(pk=request.POST.get("posto_id"))
        )
        comment.save()
        print(comment.date_commented-datetime.now(timezone.utc)),
    context = {
        'posts': posts,
    }
    return render(request, 'index.html', context=context)

@login_required
def profilis(request, id):
    user = User.objects.get(pk=id)
    posts = Post.objects.filter(uploaded_by=user)
    
    context = {
        'user': user,  
        'posts': posts,
    }

    return render(request, 'profilis.html', context)


@login_required
def edit_profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfilisUpdateForm(request.POST, request.FILES, instance=request.user.profilis)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Profilis atnaujintas")
            return redirect('profilis', id=request.user.id)
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfilisUpdateForm(instance=request.user.profilis)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'profilis_edit.html', context)

@csrf_protect
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} užimtas!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                    return redirect('register')
                else:
                    User.objects.create_user(username=username, email=email, password=password)
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
    return render(request, 'register.html')



@login_required()
def new_post(request):
    if request.method == "POST":
        nuotrauka = request.FILES['file']
        description = request.POST['description']
        uploaded_by = request.user
        Post.objects.create(uploaded_by=uploaded_by, nuotrauka=nuotrauka, description=description)
        return redirect('index')
    return render(request, 'new_post.html')



@login_required()
def detailed_post(request, post_id):
    post=Post.objects.get(id=post_id)

    if request.method=='POST':
        comment=PostComment(content=request.POST.get("komentaras"),
        date_commented=request.POST.get("date"),
        commenter= request.user,
        post=Post.objects.get(pk=post_id)
        )
        comment.save()
        print(comment.date_commented-datetime.now(timezone.utc)),

    context = {
        'post': post,
    }

    return render(request, 'post_detail.html', context)



@login_required()
def post_remove(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        post.delete()
    return redirect('index')


@login_required()
def comment_remove(request, comment_id):
    comment = get_object_or_404(PostComment, id=comment_id)
    if request.method == "POST":
        comment.delete()
        messages.error(request, 'Komentaras sekmingai istrintas')
    return redirect('post_detail', post_id=comment.post.id)

def search(request):
    query = request.GET.get('query')
    search_results = User.objects.filter(Q(username__icontains=query))
    return render(request, 'search.html', {'search_results': search_results, 'query': query})

@login_required()
def like_post(request):
    post = Post.objects.get(pk=request.POST.get("posto_id"))
    print(request.POST.get("posto_id"))
    user = request.user
    liked = False
    like = Like.objects.filter(user=user, post=post)
    if like:
        like.delete()
    else:
        liked = True
        Like.objects.create(user=user, post=post)
        # messages.success('You Liked the post')
    return redirect('index')