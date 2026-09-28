import asyncio
from django.shortcuts import render
from .models import Product, Manufacturer


async def get_products():
    return [p async for p in Product.objects.all()]


async def get_manufacturers():
    return [m async for m in Manufacturer.objects.all()]


async def products_view(request):
    products, manufacturers = await asyncio.gather(
        get_products(),
        get_manufacturers()
    )
    from asgiref.sync import sync_to_async
    return await sync_to_async(render)(request, 'products.html', {
        'products': products,
        'manufacturers': manufacturers,
    })