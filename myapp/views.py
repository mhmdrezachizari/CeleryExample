from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from .tasks import print_message ,new_task ,add_items_to_database

def start_task(request):
    print_message.apply_async(priority=13)
    new_task.apply_async(priority=10)
    return JsonResponse({"status": "Task started"})

class productViews(APIView):
    def post(self, request, *args, **kwargs):
        ser_data = ProductSerializer(data=request.data)
        if ser_data.is_valid():
            add_items_to_database.delay(ser_data.validated_data)
            return Response("add succses", status=status.HTTP_200_OK)
        return JsonResponse(ser_data.errors, status=400)

    def get(self,request):
        dd = Product.objects.all()
        ser_data = ProductSerializer(dd , many=True)
        return JsonResponse(ser_data.data, safe=False)