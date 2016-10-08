from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth import views
from accounts.views import SendConfirmationEmailView
from allauth.account.views import ConfirmEmailView
admin.autodiscover()
###############################################################################################################
## APP Url Imports
##############################################################################################################
#from search import urls as urls_search
from blog import urls as urls_blog
#from blog.views import PostEditView
from accounts import urls as urls_accounts
from search import urls as urls_search
#from stats import urls as urls_stats
#from services import urls as urls_services
#from content import urls as urls_content
#from users import urls as urls_users
#from .views_proj import *
from content import views as views_content


from rest_framework import renderers, response, schemas
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer


@api_view()
@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer, renderers.CoreJSONRenderer])
def schema_view(request):
    generator = schemas.SchemaGenerator(title='Pastebin API')
    return response.Response(generator.get_schema(request=request))

router = DefaultRouter()
router.register(r'content/language', views_content.LanguageViewSet)
router.register(r'content/category', views_content.CategoryViewSet)
router.register(r'content/subcategory', views_content.SubCategoryViewSet)

urlpatterns = patterns('',
    url(r'^$', schema_view),
    url(r'^blog/', include(urls_blog, namespace="blog")),
    url(r'^api/', include(router.urls)),

    # url(r'^home/', include(urls_content, namespace="content")),
    #url(r'^$', TemplateView.as_view(template_name="coming_soon.html"), {'website_name_1': 'tetherbox', 'website_name_2': ''}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/', include(urls_search, namespace="search")),
    #url(r'^services/', include(urls_services, namespace="services")),
    # url(r'^stats/', include(urls_stats, namespace="stats")),

    #url(r'^docs/', include('rest_framework_swagger.urls'), namespace='swagger'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # ==================================== #
    # User Profile & Registration
    # ==================================== #
    # (r'^users/profile/', include(urls_users)),
    url(r'^accounts/', include(urls_accounts, namespace="accounts")),
    # need this !!! as is as allatth iwll call
    #url(r'^account-confirm-email/(?P<key>\w+)/$', ConfirmEmailView.as_view(), name='account_confirm_email'),
    #url(r'^account-email-verification-sent/$', TemplateView.as_view(template_name='coming_soon.html'), name='account_email_verification_sent'),









    url(r'^account/', include('allauth.urls')),

    # url(r'^regression/', include(urls_regression, namespace="regression"))
    # this url is used to generate email content
    # url(r'^password/reset/confirm/(?P<uid>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #    views.password_reset_confirm,
    #    name='password_reset_confirm'),
    url('^', include('django.contrib.auth.urls')),

    # This url is used by django-allauth and empty TemplateView is
    # defined just to allow reverse() call inside app, for example when email
    # with verification link is being sent, then it's required to render email
    # content.

    # account_confirm_email - You should override this view to handle it in
    # your API client somehow and then, send post to /verify-email/ endpoint
    # with proper key.
    # If you don't want to use API on that step, then just use ConfirmEmailView
    # view from:
    # djang-allauth https://github.com/pennersr/django-allauth/blob/master/allauth/account/views.py#L190
    #url(r'^account-confirm-email/(?P<key>\w+)/$', ConfirmEmailView.as_view(),
    #    name='account_confirm_email'),
)


# ==================================== #
# Static Pages for Dev Only
# ==================================== #
# if DEBUG (This is implicit)  i.e. DEBUG must be set to TRUE

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns += staticfiles_urlpatterns()

# ==================================== #
# Other Pages
# ==================================== #
# 404  - defaults to 404.html
# 500  - defaults to 500.html
# 403  - defaults to 403.html in the root of the template directory
#handler404 = 'project.views.home'
