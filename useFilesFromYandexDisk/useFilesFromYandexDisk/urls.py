from django.contrib import admin
from django.urls import path, include
from apiYandexDisk.views import TakeListFilesYandexDiskView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TakeListFilesYandexDiskView.as_view(),
         name='list_open_files_yandex_disk'),
    # path('api_yandex_disk/', include('apiYandexDisk.urls')),
]
