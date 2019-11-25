from wiki.models import Page
from rest_framework import viewsets
from .serializers import PageSerializer
from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class PageList(generics.ListCreateAPIView):
    serializer_class = PageSerializer
    queryset = Page.objects.all()

    def get(self, request):
        pages = Page.objects.all()[:20]
        data = PageSerializer(pages, many=True).data
        return Response(data)


class PageDetail(generics.RetrieveDestroyAPIView):
    serializer_class = PageSerializer
    queryset = Page.objects.all()

    def get(self, request, pk):
        page = get_object_or_404(Page, pk=pk)
        data = PageSerializer(Page).data
        return Response(data)
