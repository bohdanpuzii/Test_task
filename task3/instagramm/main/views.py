from django.shortcuts import render, redirect, reverse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from datetime import datetime
from .forms import RegistrationForm, SignInForm, PostForm, CommentForm
from .models import User, Post, Comment


def logout_user(request):
    logout(request)
    return redirect(reverse('signin'))


def take_data_from_form(form):
    data = dict()
    data['user_email'] = form.cleaned_data['email']
    data['user_password'] = form.cleaned_data['password']
    data['user_name'] = data['user_email'].split('@')[0]
    return data


class Registration(View):
    def get(self, request):
        context = {'form': RegistrationForm}
        return render(request, 'registration.html', context=context)

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user_data = take_data_from_form(form)
            if not User.objects.filter(email=user_data['user_email']):
                new_user = User.objects.create_user(username=user_data['user_name'], email=user_data['user_email'])
                new_user.set_password(user_data['user_password'])
                new_user.save()
                login(request, new_user)
                return redirect(reverse('feed'))
            else:
                messages.warning(request, 'Account already exists')
                return HttpResponseRedirect(self.request.path_info)


class SignIn(View):
    def get(self, request):
        context = {'form': SignInForm}
        return render(request, 'signin.html', context=context)

    def post(self, request):
        form = SignInForm(request.POST)
        if form.is_valid():
            user_data = take_data_from_form(form)
            user = authenticate(username=user_data['user_name'], password=user_data['user_password'])
            if user is not None:
                login(request, user)
                return redirect(reverse('feed'))
            else:
                messages.warning(request, 'Wrong email or password')
                return HttpResponseRedirect(self.request.path_info)


class PostsFeed(View):
    def get(self, request):
        posts = Post.objects.all().order_by('-date')
        comments = Comment.objects.all().order_by('post')
        context = {'form': CommentForm, 'posts': posts, 'comments': comments}
        return render(request, 'feed.html', context=context)

    def post(self, request):
        post_id = request.POST['post_id']
        if 'comment_form' in request.POST:
            form = CommentForm(request.POST)
            if form.is_valid():
                commented_post = Post.objects.get(id=post_id)
                comment_text = form.cleaned_data['comment']
                comment = Comment.objects.create(author=request.user, post=commented_post, text=comment_text)
                comment.save()
        elif 'delete_form' in request.POST:
            post_to_delete = Post.objects.get(id=post_id)
            post_to_delete.delete()
        return HttpResponseRedirect(self.request.path_info)


class CreatePost(View):
    def get(self, request):
        context = {'form': PostForm}
        return render(request, 'create_post.html', context=context)

    def post(self, request):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post_photo = form.cleaned_data['photo']
            post_title = form.cleaned_data['title']
            post_description = form.cleaned_data['description']
            new_post = Post.objects.create(author=request.user, title=post_title,
                                           description=post_description,
                                           date=datetime.now(), photo=post_photo)
            new_post.save()
            return redirect(reverse('feed'))


class EditPost(View):
    def get(self, request, post_id):
        post_to_edit = Post.objects.get(id=post_id)
        context = {'post': post_to_edit}
        return render(request, 'edit_post.html', context=context)

    def post(self, request, post_id):
        post_to_edit = Post.objects.get(id=post_id)
        description = request.POST['description']
        title = request.POST['title']
        if description is not post_to_edit.description:
            post_to_edit.description = description
        if title is not post_to_edit.title:
            post_to_edit.title = title
        post_to_edit.save()
        return redirect(reverse('feed'))
