# blog/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Blog, Comment, Like
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from notification.utils import create_notification
from datetime import datetime, timedelta
from django.db.models import Q
from django.db.models import Count
from django.http import JsonResponse

def all_blogs(request):
    # Get today's and yesterday's dates
    today = datetime.now().date()
    yesterday = today - timedelta(days=1)

    # Get blogs for today and yesterday
    today_blogs = Blog.objects.filter(created_at__date=today)
    yesterday_blogs = Blog.objects.filter(created_at__date=yesterday)

    # Get other blogs
    other_blogs = Blog.objects.exclude(created_at__date__in=[today, yesterday])

    # Filtering based on category or tags
    category = request.GET.get('category')
    tags = request.GET.getlist('tags')

    if category:
        other_blogs = other_blogs.filter(category__title=category)

    if tags:
        other_blogs = other_blogs.filter(tags__title__in=tags)

    # Searching
    query = request.GET.get('q')
    if query:
        other_blogs = other_blogs.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )

    # Paginate the other blogs
    paginator = Paginator(other_blogs, 6)
    page = request.GET.get('page')
    try:
        other_blogs_paginated = paginator.page(page)
    except PageNotAnInteger:
        other_blogs_paginated = paginator.page(1)
    except EmptyPage:
        other_blogs_paginated = paginator.page(paginator.num_pages)

    context = {
        'today_blogs': today_blogs,
        'yesterday_blogs': yesterday_blogs,
        'other_blogs': other_blogs_paginated,
        'category': category,
        'tags': tags,
        'query': query,
    }
    return render(request, 'blog/all_blogs.html', context)

@login_required
def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    comments = Comment.objects.filter(blog=blog).order_by('-created_at')
    liked = False

    if request.user.is_authenticated:
        liked = Like.objects.filter(source=request.user, blog=blog).exists()

    like_count = Like.objects.filter(blog=blog, like=True).count()

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'like':
            if not liked:
                Like.objects.create(source=request.user, blog=blog, like=True)
                liked = True
                create_notification(
                    user=request.user,
                    action='liked_blog',
                    target=blog.author,
                    blog=blog,
                )
            else:
                Like.objects.filter(source=request.user, blog=blog).delete()
                liked = False
            # Update like count after like/unlike
            like_count = Like.objects.filter(blog=blog, like=True).count()

        elif action == 'comment':
            comment_text = request.POST.get('comment_text')
            parent_id = request.POST.get('parent_id')
            parent_comment = None
            if parent_id:
                parent_comment = Comment.objects.get(id=parent_id)
            Comment.objects.create(
                source=request.user,
                blog=blog,
                commentary=comment_text,
            )
            create_notification(
                user=request.user,
                action='commented_blog',
                target=blog.author,
                blog=blog,
            )
            messages.success(request, 'Comment added successfully.')
            return redirect('blog_detail', blog_id=blog_id)

    context = {
        'blog': blog,
        'comments': comments,
        'liked': liked,
        'like_count': like_count,
    }
    return render(request, 'blog/blog_detail.html', context)


@login_required
def like_blog(request):
    if request.method == 'POST' and request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        blog_id = request.POST.get('blog_id')
        blog = get_object_or_404(Blog, id=blog_id)
        liked = Like.objects.filter(source=request.user, blog=blog).exists()

        if not liked:
            Like.objects.create(source=request.user, blog=blog, like=True)
        else:
            Like.objects.filter(source=request.user, blog=blog).delete()

        # Get the updated like count
        like_count = Like.objects.filter(blog=blog, like=True).count()

        return JsonResponse({'like_count': like_count})
    else:
        return JsonResponse({'error': 'Invalid request'})
