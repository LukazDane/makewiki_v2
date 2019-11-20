from django.urls import path
from wiki.views import PageListView, PageDetailView, PageCreateView
from . import views


urlpatterns = [

    path('', PageListView.as_view(), name='wiki-list-page'),
    path('<str:slug>/', PageDetailView.as_view(), name='wiki-details-page'),
    path('page/new/', PageCreateView.as_view(), name='new_page'),

]
