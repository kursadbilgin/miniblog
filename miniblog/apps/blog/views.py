from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import TemplateView

from blog.models import Blog


class HomeView(TemplateView):
    #template_name = "index.html"

    def get_section(self):
        return self.kwargs.get('section') or 'home'

    def get_template_names(self):
        section = self.get_section()

        if section in ['about', 'blogs']:
            template_name = '{template_name}.html'.format(template_name=section)
        else:
            template_name = 'index.html'

        return template_name

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        important_blogs = Blog.objects.filter(is_important=True)
        if not important_blogs:
            important_blogs = Blog.objects.order_by('?').first()

        print(important_blogs)


        context.update({
            'all_blogs': Blog.objects.all().order_by('-created_date'),
            'important_blogs': important_blogs
        })

        return context


class BlogView(TemplateView):
    template_name = "single.html"
    blog = None

    def get_id(self):
        return int(self.kwargs.get('id')) or None

    def get_blog(self):
        try:
            blog = Blog.objects.get(pk=self.get_id())
        except Blog.DoesNotExist:
            blog = None

        return blog

    def dispatch(self, request, *args, **kwargs):
        self.blog = self.get_blog()

        if self.blog == None:
            return redirect('index', section="blogs")

        return super(BlogView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)

        context.update({
            'blog': self.blog
        })

        return context
