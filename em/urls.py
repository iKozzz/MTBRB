from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'em'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('riders/', views.RidersView.as_view(), name='riders'),
    path('rider_details/<int:pk>', views.RiderDetailsView.as_view(), name='rider_details'),
    path('rider_add/', views.rider_add, name='rider_add'),
    path('rider_delete/<int:rider_id>', views.rider_delete, name='rider_delete'),
    path('rider_prepare_to_race/<int:rider_id>', views.rider_prepare_to_race, name='rider_prepare_to_race'),
    path('rider_stage_assign/<int:rider_id>/<int:stage_id>', views.rider_stage_assign, name='rider_stage_assign'),
    path('rider_stage_unassign/<int:rider_id>/<int:stage_id>', views.rider_stage_unassign, name='rider_stage_unassign'),
    # path('rider_race_assign/<int:race_id>/<int:race_id>', views.rider_race_assign, name='rider_race_assign'),
    # path('rider_race_unassign/<int:race_id>/<int:race_id>', views.rider_race_unassign, name='rider_race_unassign'),

    path('stages/', views.StagesView.as_view(), name='stages'),
    path('stage_details/<int:pk>', views.stage_details, name='stage_details'),
    path('stage_add/', views.stage_add, name='stage_add'),
    path('stage_delete/<int:stage_id>', views.stage_delete, name='stage_delete'),
    path('rider_delete/<int:rider_id>', views.rider_delete, name='rider_delete'),

    path('races/', views.RacesView.as_view(), name='races'),
    path('race_details/<int:pk>', views.race_details, name='race_details'),
    path('race_add/', views.race_add, name='race_add'),
    path('race_delete/<int:race_id>', views.race_delete, name='race_delete'),

    path('liderboard/', views.LiderboardView.as_view(), name='liderboard'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
