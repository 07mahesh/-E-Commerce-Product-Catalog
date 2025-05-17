
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer
from rest_framework import status

@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def product_detail(request, product_id):
    try:
        product=Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        if request.method == 'GET':
            serilizer=ProductSerializer(product)
            return Response(serilizer.data,status=status.HTTP_200_OK)
        

       
@api_view(['POST'])
def add_product(request):
    if request.user.is_staff:
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response({"error": "Unauthorized"}, status=403)




@api_view(['DELETE'])
def delete_product(request, product_id):
    if request.user.is_staff:
        product =Product.objects.get(Product, id=product_id)
        product.delete()
        return Response({"message": "Product deleted"}) 
    return Response({"error": "Unauthorized"}, status=403)



# @api_view(['GET',"POST"])
# def  product_list(request):
#     if request.method == 'GET':
#         products = Product.objects.all()  
#         serializer = ProductSerializer(products , many=True)  
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     else:
#         if request.method == 'POST':
#             serializer=products(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(status=status.HTTP_400_BAD_REQUEST)



# @api_view(['GET','PUT','DELETE'])    
# def onestudent(request, pk):
#     one=student.objects.get(pk=pk)
#     if request.method=='GET':
#         serializer=studentdata(one)
#         return Response(serializer.data,status=status.HTTP_200_OK)
#     elif request.method=='PUT':
#         serializer=studentdata(one,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data,status=status.HTTP_200_OK)
#     else:
#         if request.method=='DELETE':
#             one.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)





def product_list(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})




def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, "product_detail.html", {"product": product})



