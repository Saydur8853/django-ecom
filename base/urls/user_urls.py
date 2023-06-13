from django.urls import path

from base.views.user_views import (
    DeleteUserAPIView,
    GetUserByIdAPIView,
    GetUserProfileAPIView,
    GetUsersAPIView,
    MyTokenObtainPairView,
    RegisterUserAPIView,
    UpdateUserAPIView,
    UpdateUserProfileAPIView,
)

urlpatterns = [
    path("login/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("register/", RegisterUserAPIView.as_view(), name="register"),
    path("profile/", GetUserProfileAPIView.as_view(), name="users-profile"),
    path(
        "profile/update/",
        UpdateUserProfileAPIView.as_view(),
        name="user-profile-update",
    ),
    path("", GetUsersAPIView.as_view(), name="users"),
    path("<str:pk>/", GetUserByIdAPIView.as_view(), name="user"),
    path("update/<str:pk>/", UpdateUserAPIView.as_view(), name="user-update"),
    path("delete/<str:pk>/", DeleteUserAPIView.as_view(), name="user-delete"),
]
