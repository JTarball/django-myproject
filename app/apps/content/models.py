#!/usr/bin/env python
"""
    content.models
    ==============

    Models for drilldown info.

    Language - language
    Category - 


    We separate the hierachy like this:

    Language
    --------
       |
       |
       |
       V
    Category
    --------
       |
       |
       |
       V
    SubCategory
    -----------

    <language>/<category>/<subcategory>

"""
from django.db import models
from django.utils.translation import ugettext as _


class Language(models.Model):
    """ A category model for languages in the most general sense. """
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, help_text='Used for URL. ')
    description = models.CharField(
        verbose_name=_(u'description'),
        max_length=255,
        help_text='Description of the Language.',
        blank=True
    )

    # DB Stuff #
    class Meta:
        #db_table = 'content_category_languages'          # name in the database
        ordering = ['-slug']                              # ordering when retrieved more than one object from the database.
        verbose_name_plural = 'languages'

    def __unicode__(self):
        return self.name                                  # return a string representation of our model

    @models.permalink
    def get_absolute_url(self):  # for routing urls (uses slug as title)
        return ('content:language', (), {'language': self.slug})


# # ========================== #
# # Category                   #
# # ========================== #
# # Language/Language Constructs should be added to through the admin
class Category(models.Model):
    """ A category model for languages in the most general sense. """
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, help_text='Used for URL. ')
    language = models.ManyToManyField(Language, null = True, blank = True )
    


    # Database Stuff
    class Meta:
        #db_table = 'content_category_languages'          # name in the database
        ordering = ['-slug']                    # ordering when retrieved more than one object from the database.
        verbose_name_plural = 'categories' 

    def __unicode__(self):
        return self.name                        # return a string representation of our model

    @models.permalink
    def get_absolute_url(self): # for routing urls (uses slug as title)
        return ('content:category', (), { 'category': self.slug })


# ========================== #
# Sub-Category               #
# ========================== #
# Language/Language Constructs should be added to through the admin
# Note: Inheritance from Language

class SubCategory(models.Model):
    """ model class containing information about a category in the product catalog """
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, help_text='Used for URL. ')
    parent_category = models.ManyToManyField(Category, blank=True)

    def __unicode__(self):
        return self.name                        # return a string representation of our model

    # Database Stuff
    class Meta:
        #db_table = 'content_sub-category_language_constructs'   # name in the database
        ordering = ['-slug'] # ordering when retrieved more than one object from the database.
        verbose_name_plural = 'SubCategories' 

    @models.permalink
    def get_absolute_url(self): # for routing urls (uses slug as title)
        return ('content:subcategory', (), { 'subcategory': self.slug })

    def save(self, *args, **kwargs):
        print self.child.all()
        if self.child.all() is None: super(SubCategory, self).save(*args, **kwargs)
        children = [child.id for child in self.child.all()]
        print children
        if self.parent is not None:
            if self.parent.id in children:
                print "EROORRORO!"
                ValidationError('You have not met a constraint!')
            else:
                super(SubCategory, self).save(*args, **kwargs)
        else:
            super(SubCategory, self).save(*args, **kwargs)





