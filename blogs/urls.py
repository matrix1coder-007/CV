from django.urls import path

# Create your urls here
from .views import ArticleGetView, ArticlePostView, TagGetView, TagPostView, TaggedArticleGetView

appname = "blogs"

urlpatterns = [
    path("article/", ArticleGetView.as_view(), name="article_get"),
    path("article/post/", ArticlePostView.as_view(), name="article_post"),
    path("tag/", TagGetView.as_view(), name="tags_get"),
    path("tag/post/", TagPostView.as_view(), name="tags_post"),
    path("tagged_articles/", TaggedArticleGetView.as_view(), name="tagged_articles")
]