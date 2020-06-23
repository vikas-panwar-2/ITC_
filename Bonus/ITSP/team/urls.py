from django.urls import path
from . import views 

from rest_framework.urlpatterns import format_suffix_patterns
app_name='team'

urlpatterns = format_suffix_patterns([
    path('<team_id>/detail/', views.team_detail, name='team'),
    path('<team_id>/', views.api_detail_view, name='team-detail'),
    path('', views.api_list_view, name='team-list')
])
