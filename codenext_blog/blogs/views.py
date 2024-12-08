from django.views import View
from django.views import generic
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    render,
    redirect
)

from blogs.models import Blog
from blogs.forms import BlogForm

# select_related -> OneToOneField and ForeignKey
# prefetch_related -> ManyToManyField and Reverse relation


# def all_blogs(request):
#     blogs = Blog.objects.select_related('author').prefetch_related('categories')

#     context = {
#         'blogs': blogs,
#     }
#     return render(request, 'blogs/all_blogs.html', context)


# @login_required
# def create_blog(request):
#     if request.method == 'POST':
#         form = BlogForm(request.POST, request.FILES)
#         if form.is_valid():
#             new_form = form.save(commit=False)
#             new_form.author = request.user
#             # categories = form.cleaned_data['categories']

#             form.save()
#             new_form.save()
#             # new_form.categories.set(categories)
#             return redirect('all_blogs')
#         else:
#             messages.error(request, "Yanlış əməliyyat.")
#             messages.error(request, form.errors)
#             messages.error(request, "MM/DD/YYYY HH:MM")
#             return redirect('create_blog')
#     else:
#         form = {
#             'blog_form': BlogForm()
#         }
#         return render(request, 'blogs/create_blog.html', form)


# def detail_blog(request, pk):
#     blog = get_object_or_404(Blog, id=pk)

#     context = {
#         'blog': blog
#     }
#     return render(request, 'blogs/detail_blog.html', context)


# @login_required
# def update_blog(request, pk):
#     blogs = Blog.objects.filter(author=request.user)
#     blog = get_object_or_404(blogs, id=pk)

#     if request.method == 'POST':
#         form = BlogForm(request.POST, request.FILES, instance=blog)
#         if form.is_valid():
#             form.save()
#             return redirect('detail_blog', blog.id) # 127.0.0.1:8000/blogs/detail/5/
#     else:
#         form = BlogForm(instance=blog)

#         context = {
#             'form': form
#         }
#         return render(request, 'blogs/update_blog.html', context)

# @login_required
# def delete_blog(request, pk):
#     blogs = Blog.objects.filter(author=request.user) # orm-de etrafli danis
#     blog = get_object_or_404(blogs, id=pk)
#     blog.delete()
#     messages.success(request, 'Silmə əməliyyatı uğurla icra edildi!')
#     return redirect('all_blogs')



# class ListBlogView(View):
#     def get(self, request):
#         blogs = Blog.objects.select_related('author').prefetch_related('categories')

#         context = {
#             'blogs': blogs,
#         }
#         return render(request, 'blogs/all_blogs.html', context)


class ListBlogView(generic.ListView):
    model = Blog
    template_name = 'blogs/all_blogs.html'
    context_object_name = 'blogs'


class CreateBlogView(LoginRequiredMixin, View):
    def get(self, request):
        form = {
            'blog_form': BlogForm()
        }
        return render(request, 'blogs/create_blog.html', form)

    def post(self, request):
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


class DetailBlogView(View):
    def get_object(self, pk):
        return get_object_or_404(Blog, id=pk)

    def get(self, request, pk):
        blog = self.get_object(pk=pk)

        context = {
            'blog': blog
        }
        return render(request, 'blogs/detail_blog.html', context)


class UpdateBlogView(LoginRequiredMixin, View):
    def get_object(self, request_user, pk):
        blogs = Blog.objects.filter(author=request_user)
        blog = get_object_or_404(blogs, id=pk)
        return blog

    def get(self, request, pk):
        blog = self.get_object(request.user, pk)
        form = BlogForm(instance=blog)

        context = {
            'form': form
        }
        return render(request, 'blogs/update_blog.html', context)

    def post(self, request, pk):
        blog = self.get_object(request.user, pk)
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('detail_blog', blog.id) # 127.0.0.1:8000/blogs/detail/5/


class DeleteBlogView(LoginRequiredMixin, View):
    def get_object(self, request_user, pk):
        blogs = Blog.objects.filter(author=request_user)
        blog = get_object_or_404(blogs, id=pk)
        return blog

    def post(self, request, pk):
        blog = self.get_object(request.user, pk)
        self.perform_delete(blog)
        messages.success(request, 'Silmə əməliyyatı uğurla icra edildi!')
        return redirect('all_blogs')

    def perform_delete(self, obj):
        obj.delete()
