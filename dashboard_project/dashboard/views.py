from django.http import JsonResponse
from .models import DataPoint
from .models import DashboardData

def get_data(request):
    data = DashboardData.objects.all().values()
    return JsonResponse({'data':list(data)})

def get_filtered_data(request):
    selected_year = request.GET.get('year')
    selected_topic = request.GET.get('topic')
    selected_region = request.GET.get('region')
    
    filters = {}
    if selected_year:
        filters['year'] = selected_year
    if selected_topic:
        filters['topics'] = selected_topic
    if selected_region:
        filters['region'] = selected_region

    filtered_data = DataPoint.objects.filter(**filters)
    
   
    serialized_data = [{
        "intensity": data.intensity,
        "likelihood": data.likelihood,
        "relevance": data.relevance,
        "year": data.year,
        "country": data.country,
        "topics": data.topics,
        "region": data.region,
        "city": data.city
    } for data in filtered_data]

    return JsonResponse(serialized_data, safe=False)
