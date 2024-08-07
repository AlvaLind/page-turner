from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from .views import handler404, handler500


urlpatterns = [
    path("about_us/", include("about_us.urls"), name="about_us-urls"),
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('book_request/', include("book_request.urls"),
        name="book_request-urls"),
    path('summernote/', include('django_summernote.urls')),
    path("", include("books.urls"), name="books-urls"),
    path('profile/', include("user_profile.urls"), name="user_profile-urls"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'page_turner.views.handler404'
handler500 = 'page_turner.views.handler500'
