from django.core.management.base import BaseCommand
from blog.models import Post, User
import json




class Command(BaseCommand):
    help = "create default products"

    def handle(self, *args, **kwargs):
        json_data = open('C:\\Users\\efert\\Project\\Python\\myblog1\\blogdjango\\blog\\management\\commands\\product.json')
        data1 = json.load(json_data)
        data2 = json.dumps(data1)
        output = json.loads(data2)
        products = Post.objects.all()
        for product in output:
            if product['id'] not in [i.id for i in products]:
                Post.objects.create(
                    id = product['id'],
                    title= product['title'],
                    text = product['text'],
                    image = product['image'],
                    author= User.objects.get(id=product['author']),            
                )
        if products.count == 5:
            print("add products success")
