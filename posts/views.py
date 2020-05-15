from django.shortcuts import render, reverse, HttpResponseRedirect
from posts.models import Post
from posts.forms import AddPostForm

# Create your views here.


def Index(request):
    data = Post.objects.all()
    return render(request, 'index.html', {'data': data})


def AddPost(request):
    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Post.objects.create(
                name=data['name'],
                choice=data['choice'],
                user_input=data['user_input'],
                up_votes=0,
                down_votes=0
            )
            return HttpResponseRedirect(reverse('home'))

    form = AddPostForm()

    return render(request, 'post.html', {"form": form})


def LikeView(request, id):
    post = Post.objects.get(id=id)
    post.up_votes += 1
    post.save()
    return HttpResponseRedirect(reverse('home'))


def DislikeView(request, id):
    post = Post.objects.get(id=id)
    post.down_votes += 1
    post.save()
    return HttpResponseRedirect(reverse('home'))
