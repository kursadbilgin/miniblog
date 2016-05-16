from django.db import models


class Blog(models.Model):
    title = models.CharField(verbose_name="Title", max_length=250)
    content = models.TextField(verbose_name="Content", max_length=10000)
    is_important = models.BooleanField(verbose_name="Important", default=False)
    created_date = models.DateTimeField(verbose_name="Created Date", auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name="Updated Date", auto_now=True)

    class Meta:
        verbose_name="Blog"
        verbose_name_plural="Blogs"

    def get_absolute_url(self):
        pass

    def __str__(self):
        return self.title
