from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include

urlpatterns = i18n_patterns(
    url(r'^admin/', admin.site.urls),
)

api_urlpatterns = [
    url(r"^v1/book/", include("apps.book.routes", namespace='api-book')),
]

urlpatterns.extend(api_urlpatterns)
