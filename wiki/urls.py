from django.urls import path
from wiki.views import PageListView, PageDetailView, PageCreateView, PageEditView
from . import views


urlpatterns = [

    path('', PageListView.as_view(), name='wiki-list-page'),
    path('create/', PageCreateView.as_view(), name='new_page'),
    path('<str:slug>/', PageDetailView.as_view(), name='wiki-details-page'),
    path('<str:slug>/edit', PageEditView.as_view(), name='edit_page'),

]
