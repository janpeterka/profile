from .blog import BlogView
from .article import ArticleView

__all__ = [
    "BlogView",
    "ArticleView"
]


def register_all_controllers(application):
    BlogView.register(application)
    ArticleView.register(application)