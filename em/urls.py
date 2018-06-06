from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'em'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('rider_details/<int:pk>', views.RiderDetailsView.as_view(), name='rider_details'),
    path('results/', views.ResultsView.as_view(), name='results'),
    path('rider_add/', views.rider_add, name='rider_add'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
