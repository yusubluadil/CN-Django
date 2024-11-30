from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    render,
    redirect
)

from blogs.models import Blog
from blogs.forms import BlogForm


def all_blogs(request):
    blogs = Blog.objects.all() # SELECT * FROM blogs_blog
    context = {
        'blogs': blogs
    }
    return render(request, 'blogs/all_blogs.html', context)


@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.author = request.user
            # categories = form.cleaned_data['categories']

            form.save()
            new_form.save()
            # new_form.categories.set(categories)
            return redirect('all_blogs')
        else:
            messages.error(request, "Yanlış əməliyyat.")
            messages.error(request, form.errors)
            messages.error(request, "MM/DD/YYYY HH:MM")
            return redirect('create_blog')
    else:
        form = {
            'blog_form': BlogForm()
        }
        return render(request, 'blogs/create_blog.html', form)


def detail_blog(request, pk):
    blog = get_object_or_404(Blog, id=pk)

    context = {
        'blog': blog
    }
    return render(request, 'blogs/detail_blog.html', context)


@login_required
def update_blog(request, pk):
    blogs = Blog.objects.filter(author=request.user)
    blog = get_object_or_404(blogs, id=pk)

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('detail_blog', blog.id) # 127.0.0.1:8000/blogs/detail/5/
    else:
        form = BlogForm(instance=blog)

        context = {
            'form': form
        }
        return render(request, 'blogs/update_blog.html', context)

@login_required
def delete_blog(request, pk):
    blogs = Blog.objects.filter(author=request.user) # orm-de etrafli danis
    blog = get_object_or_404(blogs, id=pk)
    blog.delete()
    messages.success(request, 'Silmə əməliyyatı uğurla icra edildi!')
    return redirect('all_blogs')
