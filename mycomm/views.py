from django.shortcuts import render
from rest_framework.views import APIView
from .models import usersInfo,product,orders
from .serializers import RegisterSerializer,LoginSerializer,ProductSerializer,OrderSerializer,UserBasedOrderSerializers
from rest_framework.response import Response

class register(APIView):
    def post(self,request):
        RegisterSer=RegisterSerializer(data=request.data)
        if RegisterSer.is_valid():
            RegisterSer.save()
            return Response({"msg":"Register sucessfully"},status=200)
        else:
             return Response({"msg":"Register issues"},status=404)

class login(APIView):
    def post(self,request):
        Loginser=LoginSerializer(data=request.data)
        if Loginser.is_valid():
            username=Loginser.validated_data["username"]
            password=Loginser.validated_data["password"]
            usercheck=usersInfo.objects.get(username=username)
            if usercheck.password==password:
                request.session['UserId']=usercheck.id
                return Response({"msg":f"{usercheck.username} login sucessfully"}, status=200)
                
            else:
                return Response({"msg":"Invalid id or password"}, status=404)
            
        return Response({"msg":"Login Issues"}, status=404)
            

       
class productview(APIView):
    def get(self,request):
        product_details=product.objects.all()
        Product_get_ser=ProductSerializer(product_details,many=True).data
        return Response(Product_get_ser,status=200)
    def post(self,request):
        Productser=ProductSerializer(data=request.data)
        if Productser.is_valid():
            Productser.save()
            return Response({"msg":"Product Added Sucessfully"})
        return Response({"msg":"Product Added"})
    

class ordersview(APIView):
    def post(self, request):
        Orderser = OrderSerializer(data=request.data)
        if Orderser.is_valid():
            userid = Orderser.validated_data['userid'].id
            productid = Orderser.validated_data['productid'].id
            quantity = Orderser.validated_data['quantity']

            try:
                user = usersInfo.objects.get(id=userid)
            except usersInfo.DoesNotExist:
                return Response({"error": "User not exists"}, status=404)

            try:
                pro = product.objects.get(id=productid)
            except product.DoesNotExist:
                return Response({"error": "Product not exists"}, status=404)

            total_price = quantity * pro.Price

            order = orders.objects.create(
                userid=user,
                productid=pro,
                quantity=quantity,
                totalamount=total_price
            )

            return Response({
                "message": "Order created successfully",
                "order_id": order.id,
                "user": user.username,
                "product": pro.ProductName,
                "quantity": quantity,
                "price_per_item": pro.Price,
                "total_price": total_price,
                "created_at": order.created_at
            }, status=201)

        return Response(Orderser.errors, status=400)
    
class UserBasedOrderview(APIView):
    def post(self, request,Uid):
        Orderser = OrderSerializer(data=request.data)
        if Orderser.is_valid():
            productid = Orderser.validated_data['productid'].id
            quantity = Orderser.validated_data['quantity']

            try:
                user = usersInfo.objects.get(id=Uid)
            except usersInfo.DoesNotExist:
                return Response({"error": "User not exists"}, status=404)

            try:
                pro = product.objects.get(id=productid)
            except product.DoesNotExist:
                return Response({"error": "Product not exists"}, status=404)

            total_price = quantity * pro.Price

            order = orders.objects.create(
                userid=user,
                productid=pro,
                quantity=quantity,
                totalamount=total_price
            )

            return Response({
                "message": "Order created successfully",
                "order_id": order.id,
                "user": user.username,
                "product": pro.ProductName,
                "quantity": quantity,
                "price_per_item": pro.Price,
                "total_price": total_price,
                "created_at": order.created_at
            }, status=201)

        return Response(Orderser.errors, status=400)
    def get(self,request,Uid):
        
        UserOrder=orders.objects.filter(userid=Uid)
        if not UserOrder.exists():
            return Response("userid not exists",status=404)

        
        productlist=[]
        for usersInfo in UserOrder:
            productlist.append(
                
                {   "username":usersInfo.userid.username,
                    "ProductName":usersInfo.productid.ProductName,
                    "ProductCatgies":usersInfo.productid.ProductCatageries,
                    "Price":usersInfo.totalamount
                }
            )

        return Response({"productdetails":productlist},status=200)
           
