from rest_framework.mixins import (CreateModelMixin, ListModelMixin,
                                   DestroyModelMixin)
from rest_framework.viewsets import GenericViewSet


class CreateReadAndDeleteModelViewSet(CreateModelMixin,
                                      ListModelMixin,
                                      DestroyModelMixin,
                                      GenericViewSet):
    """
    A viewset that provides default `create()`, `list()` and
    'destroy()' actions.
    """

    pass
