from celery import shared_task
import time
from .models import Product
@shared_task
def print_message():
        print("Hello, this is a message every 1 seconds!")
        time.sleep(1)

@shared_task
def new_task():
    print("Hello, this is a message every 3 seconds!")
    time.sleep(3)

@shared_task
def add_items_to_database(obj):
    Product.objects.create(name = obj["name"])
