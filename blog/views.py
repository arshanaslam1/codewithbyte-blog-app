from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from hitcount.views import HitCountDetailView

from accounts.models import User
from blog.utils.paginator import GenericPaginator
from .forms import CommentForm, SubscribeForm, PostForm
from .models import Post, PostTag, PostCategory


# Create your views here.
class PostCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = PostForm
    template_name = 'blog/post_create.html'
    success_message = 'You have Create successfully. Post will be live after moderation'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AuthorPostDetail(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'object'


class AuthorPostUpdate(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_create.html'
    success_message = 'You have update successfully.'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class AuthorPostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('blog')

    def form_valid(self, form):
        form.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class AuthorAllPostList(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Post
    template_name = 'blog/author_post_list.html'
    paginate_by = 7
    page_title = 'My All Posts:'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user = None

    def get_queryset(self):
        return Post.objects.filter(author=self.user).order_by('-created_on')

    def test_func(self):
        user_id = self.kwargs['pk']
        self.user = get_object_or_404(User, id=user_id)
        if self.request.user == self.user:
            return True
        return False


class AuthorPostPublishedList(ListView):
    model = Post
    template_name = 'blog/author_published_post_list.html'
    paginate_by = 7

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user = None

    def get_queryset(self):
        user_id = self.kwargs['pk']
        self.user = get_object_or_404(User, id=user_id)
        return Post.objects.approved().published().filter(author=self.user).order_by('-created_on')

    def page_title(self):
        if self.request.user == self.user:
            page_title = 'Published articles:'
        else:
            page_title = self.user.first_name.title() + " " + self.user.last_name.title() + ' published articles:'
        return page_title


class AuthorPostPendingList(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Post
    template_name = 'blog/author_pending_post_list.html'
    paginate_by = 7
    page_title = 'Pending:'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user = None

    def get_queryset(self):
        return Post.objects.published().filter(author=self.user, active=False).order_by('-created_on')

    def test_func(self):
        user_id = self.kwargs['pk']
        self.user = get_object_or_404(User, id=user_id)
        if self.request.user == self.user:
            return True
        return False


class AuthorPostDraftList(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Post
    template_name = 'blog/author_draft_post_list.html'
    paginate_by = 7
    page_title = 'Draft:'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user = None

    def get_queryset(self):
        return Post.objects.filter(author=self.user, status=False, active=False).order_by('-created_on')

    def test_func(self):
        user_id = self.kwargs['pk']
        self.user = get_object_or_404(User, id=user_id)
        if self.request.user == self.user:
            return True
        return False


class PostList(ListView):
    model = Post
    # context_object_name = 'object_list'
    # ordering = ['-updated_on']
    queryset = Post.objects.published().approved().filter().order_by('-created_on')
    paginate_by = 7

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        return context


class PostDetail(HitCountDetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'object'
    # set to True to count the hit
    count_hit = True
    queryset = Post.objects.filter().order_by('-created_on')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.object = None

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        slug = self.kwargs["slug"]
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.filter(active=True)
        related_posts = Post.objects.published().approved().filter(
            tags__in=list(self.object.tags.all())[:2]
        ).exclude(id=self.object.id).distinct()

        if post.likes.filter(id=self.request.user.id).exists():
            is_liked = True
        else:
            is_liked = False
        context['is_liked'] = is_liked

        context['related_objects'] = related_posts
        comment_form = CommentForm()
        new_comment = None
        context['comments'] = comments
        context['comment_form'] = comment_form
        context['new_comment'] = new_comment
        return context

    def post(self, request, *args, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        slug = self.kwargs["slug"]
        self.object = self.get_object()
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.filter(active=True)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
            context['new_comment'] = new_comment
        else:
            context['comment_form'] = comment_form

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class TagPostView(ListView):
    template_name = 'blog/tag_post_list.html'
    paginate_by = 7

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tag = None

    def get_queryset(self):
        tag_slug = self.kwargs['slug']
        self.tag = get_object_or_404(PostTag, slug=tag_slug)
        results_filter = Post.objects.approved().published().filter(tags=self.tag).order_by('-created_on')
        return results_filter

    def get_context_data(self, **kwargs):
        context = super(TagPostView, self).get_context_data(**kwargs)
        context['query'] = self.tag
        return context


class AuthorListView(ListView):
    template_name = 'blog/author_list.html'
    model = User
    context_object_name = 'object'
    paginate_by = 8
    queryset = User.objects.filter(is_active=True).order_by('first_name')

    def get_context_data(self, **kwargs):
        context = super(AuthorListView, self).get_context_data(**kwargs)
        return context


class CategoryListView(ListView):
    template_name = 'blog/category_list.html'
    model = PostCategory
    context_object_name = 'object'
    # ordering = ['-updated_on']
    paginate_by = 7

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        return context


class TagListView(ListView):
    template_name = 'blog/tag_list.html'
    model = PostTag
    context_object_name = 'object'
    # ordering = ['-updated_on']
    paginate_by = 7

    def get_context_data(self, **kwargs):
        context = super(TagListView, self).get_context_data(**kwargs)
        return context


class CategoryPostListView(ListView):
    template_name = 'blog/category_post_list.html'
    paginate_by = 7

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.category = None

    def get_queryset(self):
        # category_slug = self.request.GET.get('slug')
        category_slug = self.kwargs['slug']
        self.category = get_object_or_404(PostCategory, slug=category_slug)
        results_filter = Post.objects.approved().published().filter(
            category=self.category
        ).order_by('-created_on')
        return results_filter

    def get_context_data(self, **kwargs):
        context = super(CategoryPostListView, self).get_context_data(**kwargs)
        context['query'] = self.category
        return context


class SearchPostsListView(ListView):
    template_name = 'blog/search_post_list.html'
    paginate_by = 7

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.query = None

    def get_queryset(self):
        self.query = self.request.GET.get('query')
        try:
            search_posts = Post.objects.approved().published().filter(
                Q(title__icontains=self.query)
                #                Q(description__icontains=self.query) |
                #               Q(keywords__icontains=self.query) |
                #                Q(meta_description__icontains=self.query)
            ).order_by('-created_on').order_by('-id')
            return search_posts
        except:
            return Post.objects.published()

    def get_context_data(self, **kwargs):
        context = super(SearchPostsListView, self).get_context_data(**kwargs)
        context['query'] = self.query
        context['page_range'] = GenericPaginator(
            self.get_queryset(),
            self.paginate_by,
            self.request.GET.get('page')
        ).get_page_range()
        return context


# Json response
class JsonableResponseMixin:
    """
    Mixin to add JSON support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """

    def form_invalid(self, form):
        super().form_invalid(form)
        data = {
            'status': "False",
            'error': form.errors
        }
        # return JsonResponse(form.errors, status=400)
        return JsonResponse(data)

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        super().form_valid(form)
        form.send_email()
        data = {
            'status': "True",
            'message': self.success_message,
            'response': "response"
        }
        return JsonResponse(data, status=200)


# Handle Post data from Subscribe Form
class LikeView(LoginRequiredMixin, View):
    def post(self, request, pk):
        print(self.request.POST.get('article_id'))
        article = get_object_or_404(Post, id=self.request.POST.get('article_id'))
        if article.likes.filter(id=self.request.user.id).exists():
            article.likes.remove(self.request.user)
        else:
            article.likes.add(self.request.user)
        return HttpResponseRedirect(reverse('post_detail', args=[article.slug]))


# Handle Post data from Subscribe Form
class Subscribe(JsonableResponseMixin, CreateView):
    form_class = SubscribeForm
    success_url = "blog"
    template_name = ""
    success_message = 'You have subscribe successfully!'
