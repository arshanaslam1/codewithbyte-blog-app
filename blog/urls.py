from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap


sitemaps = {
    "posts": PostSitemap,
}

urlpatterns = [

    path('blog/categories/', views.CategoryListView.as_view(), name='category_list'),
    path('blog/tags/', views.TagListView.as_view(), name='tags_list'),
    path('blog/authors/', views.AuthorListView.as_view(), name='author_list'),
    path('blog/subscribe/', views.Subscribe.as_view(), name='subscribe'),
    path('blog/search/', views.SearchPostsListView.as_view(), name='search_post_list'),
    path('blog/like/<int:pk>/', views.LikeView.as_view(), name="like_article"),


    path('', views.PostList.as_view(), name='blog'),

    path('blog/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('blog/create', views.PostCreate.as_view(), name='post-create'),

    path('blog/<int:pk>/all/posts', views.AuthorAllPostList.as_view(), name='author-all-post-list'),
    path('blog/<int:pk>/published/posts', views.AuthorPostPublishedList.as_view(), name='author-published-post-list'),
    path('blog/<int:pk>/pending/posts', views.AuthorPostPendingList.as_view(), name='author-pending-post-list'),
    path('blog/<int:pk>/draft/posts', views.AuthorPostDraftList.as_view(), name='author-draft-post-list'),
    path('blog/tag/<slug:slug>/', views.TagPostView.as_view(), name='tag_post_list'),
    path('blog/category/<slug:slug>/', views.CategoryPostListView.as_view(), name='category_post_list'),
    path('blog/<slug:slug>/detail/', views.AuthorPostDetail.as_view(), name='author-post-detail'),
    path('blog/<slug:slug>/update/', views.AuthorPostUpdate.as_view(), name='author-post-update'),
    path('blog/<slug:slug>/delete/', views.AuthorPostDelete.as_view(), name='author-post-delete'),
    path("sitemap.xml/", sitemap, {"sitemaps": sitemaps}, name="sitemap"),

]
