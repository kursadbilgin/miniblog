from django.contrib.sitemaps import Sitemap

from blog.models import Blog

class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Blog.objects.all()

class FirstBlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Blog.objects.filter(id=1)
