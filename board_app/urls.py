from django.urls import path
from .views import (
   AdvertisementsList, AdvertisementDetail, AdvertisementCreate, AdvertisementUpdate, AdvertisementDelete,
   AuthorAdvertisementsList, ResponseCreate, ResponseList, ResponseDetail, ResponseDelete, ResponseUpdate,
   CommentatorresponsesList, AdvertisementsResponsesList
)


urlpatterns = [
   path('', AdvertisementsList.as_view(), name='advertisement_list'),
   path('<int:pk>/', AdvertisementDetail.as_view(), name='advertisement_detail'),
   path('create/', AdvertisementCreate.as_view(), name='advertisement_create'),
   path('<int:pk>/update/', AdvertisementUpdate.as_view(), name='advertisement_update'),
   path('<int:pk>/delete/', AdvertisementDelete.as_view(), name='advertisement_delete'),
   path('authors/<int:pk>/', AuthorAdvertisementsList.as_view(), name='authors_list'),
   path('<int:pk>/response/create/', ResponseCreate.as_view(), name='response_create'),
   path('responses/', ResponseList.as_view(), name='response_list'),
   path('responses/<int:pk>/', ResponseDetail.as_view(), name='response_detail'),
   path('responses/<int:pk>/delete/', ResponseDelete.as_view(), name='response_delete'),
   path('responses/<int:pk>/confirm', ResponseUpdate.as_view(), name='response_update'),
   path('responses/commentators/<int:pk>/', CommentatorresponsesList.as_view(), name='commentators_list'),
   path('responses/advertisements/<int:pk>/', AdvertisementsResponsesList.as_view(), name='commentators_list'),
]