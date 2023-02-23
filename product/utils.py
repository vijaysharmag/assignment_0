
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.pagination import PageNumberPagination



class ReadNestedViewMixin(GenericViewSet):
    read_serializer_class = None

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        serializer = self.read_serializer_class(serializer.instance, context={"request": request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.read_serializer_class(instance, context={"request": request})
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.read_serializer_class(page, many=True, context={"request": request})
            return self.get_paginated_response(serializer.data)
        serializer = self.read_serializer_class(queryset, many=True, context={"request": request})
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        instance = self.get_object()
        serializer = self.serializer_class(instance, context={"request": request})
        return Response(serializer.data)




class CustomPagination(PageNumberPagination):
    """
    ?page=all
    For retrieve all list without pagination
    """
    all = 'all'
    page_size_query_param = 'page_size'

    def get_page_size(self, request):
        if request.query_params.get(self.page_query_param) == self.all:
            return None
        return super().get_page_size(request)
