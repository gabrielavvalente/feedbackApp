from django.urls import path
from main import views
from main import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.home, name="home"),
    #path("/admin", admin.site.urls),
    path("main/<name>", views.hello_there, name="hello_there"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact")
]

urlpatterns += staticfiles_urlpatterns()
