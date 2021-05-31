from django.shortcuts import render, redirect
from .models import Post, Profilis, PostComment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import User
from .forms import  UserUpdateForm, ProfilisUpdateForm, AddPostForm
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
    # view_user = User.objects.get(id=profilis.user.id)
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
            return redirect('profilis')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfilisUpdateForm(instance=request.user.profilis)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'profilis_edit.html', context)

# class PostLibrary(LoginRequiredMixin, ListView):
#     model = Post
#     contex_object_name = 'post'
#     template_name = 'profilis.html'

#     def get_queryset(self):
#         return Post.objects.filter(User=Post.request.nuotrauka.all())

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
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.uploaded_by = request.user
            form.save()
            messages.success(request, f'Nuotrauka sėkmingai įkelta')
        return redirect('index')
    else:
        form = AddPostForm(request.POST, request.FILES)
    context = {
        'form': form,
    }
    return render(request, 'new_post.html', context)



# @login_required()
# def other_profile(request,id):
#     profile_user=User.objects.filter(id=id).first()
#     posts=Post.objects.all()
#     # username = User.objects.filter(username=request.username).first()

#     return render(request, 'profilis.html',{"profile_user": profile_user,"posts":posts})


# @login_required()
# def detailed_post(request):
#     posts=Post.objects.filter(id=Post.id)
#     uploaded_by=posts.uploaded_by
#     comments=PostComment.objects.all()


#     def delete(request):
#         if request:

#     context = {
#         'posts': posts,
#         'uploaded_by': uploaded_by,
#         'comments': comments,
#     }
# 
    # return render(request, 'post_detail.html', context)
@login_required()
class DetailedPostView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post_detail.html'

