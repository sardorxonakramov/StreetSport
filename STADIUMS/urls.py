from django.urls import path
from . import views

urlpatterns = [
    # ADMIN stadionlarni boshqaradi
    path('admin/stadions/', views.AdminStadionListCreateView.as_view(), name='admin-stadion-list-create'), # xatolik bor
    path('admin/stadions/<int:pk>/', views.AdminStadionDetailView.as_view(), name='admin-stadion-detail'),

    # OWNER o‘z stadionlari bilan ishlaydi
    path('owner/stadions/', views.OwnerStadionListView.as_view(), name='owner-stadion-list'),#  xatolik bor
    path('owner/stadions/create/', views.OwnerStadionCreateView.as_view(), name='owner-stadion-create'),
    path('owner/stadions/<int:pk>/', views.OwnerStadionDetailView.as_view(), name='owner-stadion-detail'),

    # OWNER → manager biriktirish
    path('owner/assign-manager/', views.AssignManagerView.as_view(), name='assign-manager'),

    # OWNER dashboard statistika
    path('owner/dashboard/', views.OwnerDashboardView.as_view(), name='owner-dashboard'),

    # MANAGER biriktirilgan stadionlar ro‘yxati
    path('manager/stadions/', views.ManagerAssignedStadionListView.as_view(), name='manager-stadion-list'),
]
