from datetime import datetime

from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from base.models import Order, OrderItem, Product, ShippingAddress
from base.serializers import OrderSerializer


class AddOrderItemsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        data = request.data

        orderItems = data["orderItems"]

        if orderItems and len(orderItems) == 0:
            return Response(
                {"detail": "No Order Items"}, status=status.HTTP_400_BAD_REQUEST
            )
        else:
            # (1) Create order
            order = Order.objects.create(
                user=user,
                paymentMethod=data["paymentMethod"],
                taxPrice=data["taxPrice"],
                shippingPrice=data["shippingPrice"],
                totalPrice=data["totalPrice"],
            )

            # (2) Create shipping address
            shipping = ShippingAddress.objects.create(
                order=order,
                address=data["shippingAddress"]["address"],
                city=data["shippingAddress"]["city"],
                postalCode=data["shippingAddress"]["postalCode"],
                country=data["shippingAddress"]["country"],
            )

            # (3) Create order items and set order to orderItem relationship
            for i in orderItems:
                product = Product.objects.get(_id=i["product"])

                item = OrderItem.objects.create(
                    product=product,
                    order=order,
                    name=product.name,
                    qty=i["qty"],
                    price=i["price"],
                    image=product.image.url,
                )

                # (4) Update stock
                product.countInStock -= item.qty
                product.save()

            serializer = OrderSerializer(order, many=False)
            return Response(serializer.data)


class GetMyOrdersAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        orders = user.order_set.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)


class GetOrdersAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)


class GetOrderByIdAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        user = request.user

        try:
            order = Order.objects.get(_id=pk)
            if user.is_staff or order.user == user:
                serializer = OrderSerializer(order, many=False)
                return Response(serializer.data)
            else:
                Response(
                    {"detail": "Not authorized to view this order"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except:
            return Response(
                {"detail": "Order does not exist"}, status=status.HTTP_400_BAD_REQUEST
            )


class UpdateOrderToPaidAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        order = Order.objects.get(_id=pk)

        order.isPaid = True
        order.paidAt = datetime.now()
        order.save()

        return Response("Order was paid")


class UpdateOrderToDeliveredAPIView(APIView):
    permission_classes = [IsAdminUser]

    def put(self, request, pk):
        order = Order.objects.get(_id=pk)

        order.isDelivered = True
        order.deliveredAt = datetime.now()
        order.save()

        return Response("Order was delivered")


from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from sslcommerz_client.client import SSLCommerzClient
from django.shortcuts import redirect


class PaymentInitAPIView(APIView):
    def post(self, request):
        client = SSLCommerzClient(
            store_id=settings.SSL_STORE_ID,
            store_passwd=settings.SSL_STORE_PASS,
            sandbox=True,
        )
        # serializer = PaymentInitSerializer(data=request.data, many=False)
        # if serializer.is_valid():
        #     amount = serializer.validated_data["amount"]
        #     donation_steam = serializer.validated_data["donation_stream"]
        #     name = serializer.validated_data["name"]
        #     email = serializer.validated_data["email"]
        #     reminder = serializer.validated_data["reminder"]

        #     url = request.build_absolute_uri(reverse("payment-status"))

        #     steam = DonationStream.objects.get(id=int(donation_steam))

        #     tran_id = tran_id_generator()
        #     tran_obj = Transaction.objects.create(tran_id=tran_id, amount=amount)

        #     order_obj = Order.objects.create(
        #         transaction=tran_obj,
        #         amount=amount,
        #         donation_steam=steam,
        #         name=name,
        #         email=email,
        #         reminder=reminder,
        #     )

        #     post_data = {
        #         "total_amount": amount,
        #         "currency": "BDT",
        #         "tran_id": tran_id,
        #         "product_category": "donation",
        #         "success_url": url,
        #         "fail_url": url,
        #         "cancel_url": url,
        #         "cus_name": name,
        #         "cus_email": email,
        #         "shipping_method": "NO",
        #         "num_of_item": 1,
        #         "product_name": "donation",
        #         "product_category": "donation",
        #         "product_profile": "general",
        #         "cus_add1": "Some Address",
        #         "cus_city": "Dhaka",
        #         "cus_country": "Bangladesh",
        #         "cus_phone": "01XX-XXXXXXX",
        #     }

        #     res = client.initiateSession(post_data)
        #     return Response(data=res.response.dict())
