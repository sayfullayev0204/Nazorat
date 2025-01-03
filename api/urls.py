from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
    TokenObtainPairView,
)
from django.urls import path
from .views import (
    ProfileAPIView,HomeAPIView, GroupDetailAPIView, StudentsInGroupAPIView,
    ApartmentDetailAPIView, ApartmentStudentsAPIView, ApartmentSituationAPIView
)


urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("profile/", ProfileAPIView.as_view(), name="profile"),
]

urlpatterns += [
    path('home/', HomeAPIView.as_view(), name='home-api'),
    path('group/<int:pk>/', GroupDetailAPIView.as_view(), name='group-detail'),
    path('group/<int:group_id>/students/', StudentsInGroupAPIView.as_view(), name='group-students'),
    path('apartment/<int:pk>/', ApartmentDetailAPIView.as_view(), name='apartment-detail'),
    path('apartment/<int:appartment_id>/students/', ApartmentStudentsAPIView.as_view(), name='apartment-students'),
    path('apartment/<int:pk>/situation/', ApartmentSituationAPIView.as_view(), name='apartment-situation')
]
