from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'em'
urlpatterns = [
    path('', views.RidersView.as_view(), name='riders'),
    path('rider_details/<int:pk>', views.RiderDetailsView.as_view(), name='rider_details'),
    path('rider_add/', views.rider_add, name='rider_add'),

    path('stages/', views.StagesView.as_view(), name='stages'),
    path('stage_details/<int:pk>', views.StageDetailsView.as_view(), name='stage_details'),
    path('stage_add/', views.stage_add, name='stage_add'),

    path('liderboard/', views.LiderboardView.as_view(), name='liderboard'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
