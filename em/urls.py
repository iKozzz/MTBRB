from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from em.controllers.buzzer_controller import server_startup_alert
from . import views

app_name = 'em'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('riders/', views.RidersView.as_view(), name='riders'),
    path('rider_details/<int:pk>', views.RiderDetailsView.as_view(), name='rider_details'),
    path('rider_add/', views.rider_add, name='rider_add'),
    path('rider_delete/<int:rider_id>', views.rider_delete, name='rider_delete'),
    path('rider_prepare_to_ride_with_time/<int:rider_id>/<int:track_id>/<int:stage_id>', views.rider_prepare_to_ride_with_time, name='rider_prepare_to_ride_with_time'),
    path('rider_prepare_to_ride_with_points/<int:rider_id>/<int:track_id>/<int:stage_id>', views.rider_prepare_to_ride_with_points, name='rider_prepare_to_ride_with_points'),
    path('rider_cancel_ride/<int:track_id>/<int:stage_id>', views.rider_cancel_ride, name='rider_cancel_ride'),
    path('rider_set_status/<int:rider_id>/<int:track_id>/<int:stage_id>', views.rider_set_status, name='rider_set_status'),
    path('rider_stage_assign/<int:rider_id>/<int:stage_id>', views.rider_stage_assign, name='rider_stage_assign'),
    path('rider_stage_unassign/<int:rider_id>/<int:stage_id>', views.rider_stage_unassign, name='rider_stage_unassign'),

    path('stages/', views.StagesView.as_view(), name='stages'),
    path('stage_details/<int:pk>', views.stage_details, name='stage_details'),
    path('stage_add/', views.stage_add, name='stage_add'),
    path('stage_delete/<int:stage_id>', views.stage_delete, name='stage_delete'),

    path('track_details/<int:pk>/<int:stage_id>', views.track_details, name='track_details'),
    path('track_add/<int:stage_id>', views.track_add, name='track_add'),
    path('track_delete/<int:track_id>/<int:stage_id>', views.track_delete, name='track_delete'),
    path('track_finalize/<int:track_id>/<int:stage_id>', views.track_finalize, name='track_finalize'),

    path('result_delete/<int:result_id>/<int:track_id>/<int:stage_id>', views.result_delete, name='result_delete'),

    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('leaderboard/export/', views.export_leaders_xls, name='export_leaders_xls'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

server_startup_alert()
