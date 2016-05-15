from django.shortcuts import render
from django.views.generic import TemplateView

from blog.models import Blog


class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        context.update({
            'blogs': Blog.objects.all().order_by('-created_date')
        })

        return context
