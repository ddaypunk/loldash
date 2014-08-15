from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin


base_urlpatterns = [
    url(r'^', include('summoners.urls')),

    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns = [
    url(r'^api/', include(base_urlpatterns)),
]
