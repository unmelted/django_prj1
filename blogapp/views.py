from django.shortcuts import render
from .models import Post, Category, Tag
from django.views.generic import ListView, DetailView

# Create your views here.

class PostList(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.order_by('-created')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['posts_without_category'] = Post.objects.filter(category=None).count()

        return context


class PostDetail(DetailView):
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['posts_without_category'] = Post.objects.filter(category=None).count()

        return context


class PostListByCategory(ListView):

    def get_queryset(self):
        slug = self.kwargs['slug']

        if slug =='_none':
            category = None
        else:
            category = Category.objects.get(slug=slug)

        return Post.objects.filter(category=category).order_by('-created')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(type(self), self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['posts_without_category'] = Post.objects.filter(category=None).count()

        slug = self.kwargs['slug']

        if slug =='_none':
            context['category'] = 'uncategorized'
        else:
            category = Category.objects.get(slug=slug)
            context['category'] = category

        #context['title'] = 'Blog - {}'.format(category.name)
        return context

class PostListByTag(ListView):
    def get_queryset(self):
        slug = self.kwargs['slug']
        tag = Tag.objects.get(slug=slug)

        return tag.post_set.order_by('-created')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(type(self), self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['posts_without_category'] = Post.objects.filter(category=None).count()

        slug = self.kwargs['slug']
        context['tag'] = Tag.objects.get(slug=slug)

        return context

'''
def post_detail(request, pk):
    blog_post = Post.objects.get(pk=pk)

    return render(
        request,
        'blogapp/post_detail.html',
        {
            'blog_post': blog_post,
        }
    )
'''