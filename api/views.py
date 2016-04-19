from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from django.db.models import Count
from models import Message
# Create your views here.


@cache_page(60)
def get(request):
    data = Message.objects.values('city', 'username').aggregate(
                                    Count('city', distinct=True),
                                    Count('username', distinct=True))
    response = JsonResponse(data, safe=False)
    return(response)
