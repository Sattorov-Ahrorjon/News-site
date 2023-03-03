from django.shortcuts import render, redirect
from .models import NewImagePost, Category, Status
from django.db.models import Q
from .forms import CommentForm
from django.contrib import messages
from django.views.generic import ListView
from hitcount.views import HitCountMixin
from hitcount.utils import get_hitcount_model


def get_index(request):
    try:
        image_list = NewImagePost.objects.filter(status=Status.Published)[:6]
        category_list = Category.objects.all()
    except:
        image_list = ['']
        category_list = ['']
    context = {
        'object_list': image_list,
        'category_list': category_list,
    }
    return render(request, 'index.html', context=context)


def get_blog(request):
    try:
        image_list = NewImagePost.objects.filter(status=Status.Published)[:5]
        category_list = Category.objects.all()
    except:
        image_list = ['']
        category_list = ['']
    context = {
        'object_list': image_list,
        'category_list': category_list,
    }
    return render(request, 'blog.html', context=context)


def get_single(request, slug):
    try:
        first = NewImagePost.objects.filter(status=Status.Published).get(slug=slug)
        image_list = NewImagePost.objects.filter(status=Status.Published)[:6]
        category_list = Category.objects.all()
        # hitcount_logic
        context = {}
        hit_count = get_hitcount_model().objects.get_for_object(first)
        hits = hit_count.hits
        hitcontext = context['hitcount'] = {'pk': hit_count.pk}
        hit_count_response = HitCountMixin.hit_count(request, hit_count)
        if hit_count_response.hit_counted:
            hits = hits + 1
            hitcontext['hit_counted'] = hit_count_response.hit_counted
            hitcontext['hit_message'] = hit_count_response.hit_message
            hitcontext['total_hits'] = hits
        # comments_logic
        comments = first.comments.filter(active=True)
        comments_count = comments.count()
        if request.method == 'POST':
            if request.user.is_authenticated:
                messages.success(request, "The review has been saved !!!")
                comment_form = CommentForm(data=request.POST)
                if comment_form.is_valid():
                    new_comment = comment_form.save(commit=False)
                    new_comment.news = first
                    new_comment.user = request.user
                    new_comment.save()
                return redirect(f'/single/{first.slug}')
            else:
                return redirect('login')
        else:
            comment_form = CommentForm()
    except:
        first = ['']
        image_list = ['']
        category_list = ['']
    context = {
        'object_list': image_list,
        'category_list': category_list,
        'first': first,
        'comments_count': comments_count,
        'comments': comments,
        'comment_form': comment_form
    }
    return render(request, 'single.html', context=context)


def get_category(request, slug):
    try:
        image_list = NewImagePost.objects.filter(Q(status=Status.Published) & Q(category__slug=slug))[:6]
        category_list = Category.objects.all()
    except:
        image_list = ['']
        category_list = ['']
    context = {
        'object_list': image_list,
        'category_list': category_list
    }
    return render(request, 'blog.html', context=context)


class SearchResultsListView(ListView):
    model = NewImagePost
    template_name = 'search_result.html'
    context_object_name = 'objects'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return NewImagePost.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
        )
