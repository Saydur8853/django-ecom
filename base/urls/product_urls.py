from django.urls import path

from base.views.product_views import (
    ProductDetailAPIView,
    ProductListAPIView,
    TopProductsAPIView,
    createProductReview,
    uploadImage,
)

urlpatterns = [
    path("", ProductListAPIView.as_view(), name="products"),
    path("create/", ProductListAPIView.as_view(), name="product-create"),
    path("upload/", uploadImage, name="image-upload"),
    path("<str:pk>/reviews/", createProductReview, name="create-review"),
    path("top/", TopProductsAPIView.as_view(), name="top-products"),
    path("<str:pk>/", ProductDetailAPIView.as_view(), name="product"),
    path("update/<str:pk>/", ProductDetailAPIView.as_view(), name="product-update"),
    path("delete/<str:pk>/", ProductDetailAPIView.as_view(), name="product-delete"),
]
