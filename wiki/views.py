from .forms import PageForm
from wiki.models import Page
from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView


class PageListView(ListView):
    """ Renders a list of all Pages. """
    model = Page

    def get(self, request):
        """ GET a list of Pages. """
        pages = self.get_queryset().all()
        return render(request, 'list.html', {
            'pages': pages
        })


class PageDetailView(DetailView):
    """ Renders a specific page based on it's slug."""
    model = Page

    def get(self, request, slug):
        """ Returns a specific wiki page by slug. """
        page = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'page.html', {
            'page': page
        })


class PageCreateView(CreateView):

    # def get(self, request, *args, **kwargs):
    model = Page
    fields = ['title', 'content']

    # def new_page(self, request, *args, **kwargs):
    #     form = PageForm(data=request.POST, instance=Page)
    #     form.instance.created_by = self.request.user
    #     if form.is_valid():
    #         page = form.save(commit=False)
    #         page.author = request.user
    #         page.published_date = timezone.now()
    #         page.save()
    #         return HttpResponseRedirect(reverse_lazy('wiki-details-page', args=[page.slug]))
    #     return render(request, 'create_page.html', {'form': form})


class PageEditView(UpdateView):
    model = Page
    fields = ['title', 'content']

    def edit_page(self, request):
        form = PageForm(data=request.POST, instance=Page)
        form.instance.created_by = self.request.user
        pass
