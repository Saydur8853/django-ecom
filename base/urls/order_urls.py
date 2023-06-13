from django.urls import path

from base.views.order_views import (
    AddOrderItemsAPIView,
    GetMyOrdersAPIView,
    GetOrderByIdAPIView,
    GetOrdersAPIView,
    UpdateOrderToDeliveredAPIView,
    UpdateOrderToPaidAPIView,
)

urlpatterns = [
    path("", GetOrdersAPIView.as_view(), name="orders"),
    path("add/", AddOrderItemsAPIView.as_view(), name="orders-add"),
    path("myorders/", GetMyOrdersAPIView.as_view(), name="myorders"),
    path(
        "<str:pk>/deliver/",
        UpdateOrderToDeliveredAPIView.as_view(),
        name="order-delivered",
    ),
    path("<str:pk>/", GetOrderByIdAPIView.as_view(), name="user-order"),
    path("<str:pk>/pay/", UpdateOrderToPaidAPIView.as_view(), name="pay"),
]
