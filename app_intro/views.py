from django.shortcuts import render
import random
from faker import Faker
# Create your views here.

def index(request):
    return render(request, 'index.html')

def hello(request):
    username = '알리샤'
    
    result = {
        'username': username,
    }
    
    return render(request, 'hello.html', result)

def dinner(request):
    menus = ['라면', '김밥', '떡볶이']
    pick = random.choice(menus)

    result = {
        'pick': pick,
    }
    return render(request, 'dinner.html', result)

def lotto(request):
    numbers = range(1,46)
    lot_nums = random.sample(numbers, 6)
    result = {
        'lot_nums': lot_nums
    }
    return render(request,'lotto.html', result)

def greeting(request, name):

    result = {
        'name': name,
    }
    return render(request, 'greeting.html', result)


def cube(request, num):
    result = {
        'num': num,
        'cube': num ** 3,
    }
    return render(request, 'cube.html', result)


def posts(request):
    posts = []

    fake = Faker()

    for i in range(100):
        posts.append(fake.text())

    result = {
        'posts': posts,
    }
    return render(request, 'posts.html', result)