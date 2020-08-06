from rest_framework.routers import DefaultRouter

from .api import BookViewSet

app_name = "api-book"

router = DefaultRouter()

router.register(r'books', BookViewSet, basename='books')

urlpatterns = router.urls
