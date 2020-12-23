from django.urls import path
from .views import (
    index,
    file_upload_view,
    view_image
)

urlpatterns = [
    path('',index.as_view(),name='index'),
    path('upload/',file_upload_view),
    path('img/<int:image_id>',view_image,name='disp'),

]
