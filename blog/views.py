from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader

from blog.models import Post


def about(request):
    template = loader.get_template("blog/about.html")
    return HttpResponse(template.render({}, request))


def index(request):
    posts = Post.objects.all()
    context = {"post_list": posts}
    return render(request, "blog/post_list.html", context=context)


def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post_detail.html", {"post": post})
