"""
    content.views
    =============

"""
import logging

from rest_framework import viewsets

from project.permissions import IsAdminOrReadOnly

from .models import Language, Category, SubCategory
from .serializers import LanguageSerializer, CategorySerializer, SubCategorySerializer


logger = logging.getLogger('project_logger')


class LanguageViewSet(viewsets.ModelViewSet):
    """
        Gets/Updates/Deletes a single or list of languages.
        This viewset automatically provides `list`, `create`, `retrieve`,`update` and `destroy` actions.
    """
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = (IsAdminOrReadOnly, )


class CategoryViewSet(viewsets.ModelViewSet):
    """
        Gets/Updates/Deletes a single or list of languages.
        This viewset automatically provides `list`, `create`, `retrieve`,`update` and `destroy` actions.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly, )


class SubCategoryViewSet(viewsets.ModelViewSet):
    """
        Gets/Updates/Deletes a single or list of languages.
        This viewset automatically provides `list`, `create`, `retrieve`,`update` and `destroy` actions.
    """
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = (IsAdminOrReadOnly, )
