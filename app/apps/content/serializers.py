#!/usr/bin/env python
"""
    content.serializers
    ================

    Serializers file for content app

"""
from rest_framework import serializers

from .models import Language, Category, SubCategory


class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category


class SubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SubCategory