from django.urls import path
from flats.views import (flats_list, flat_detail, flat_create, flat_edit,
                         flat_delete, send_deal_request, owner_deal_requests_list)


app_name = 'flats'

urlpatterns = [
    # https://localhost:8000/
    path('', flats_list, name='flats_list'),

    # https://localgost:8000/1/
    path('<int:flat_id>/', flat_detail, name='flat_detail'),

    path('add/', flat_create, name='flat_create'),

    path('<int:flat_id>/>', flat_edit, name='flat_edit'),

    path('<int:flat_id>/', flat_delete, name='flat_delete'),

    path('<int:flat_id>/deal-request/>', send_deal_request, name='send_deal_request'),

    path('my-deal-requests/', owner_deal_requests_list, name='owner_deal_requests_list'),
]