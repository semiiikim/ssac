from django.shortcuts import render
from django.views.generic.base import View, TemplateView
from django.http import HttpResponse

# Create your views here.
 
class HomeView(TemplateView):
    template_name='accyear/home-accident.html'

class TotalView(View):
    def get(self, request):
        from .accyear_repository import AccyearRepository
        import json

        repository = AccyearRepository()
        total_accyear = repository.select_car_accident_by_name()
        json_accyear = json.dumps(total_accyear, ensure_ascii=False)
        return HttpResponse(json_accyear, content_type="application/json")

class SearchView(View):
    def get(self,request, key):
        from .accyear_repository import AccyearRepository
        import json
 
        repository2 = AccyearRepository()
        searched_year = repository2.select_car_accident_by_year(key)
        json_searchyear = json.dumps(searched_year, ensure_ascii=False)
        return HttpResponse(json_searchyear, content_type="application/json")

class YearDetailView(View):
    def get(self, request, key):
        from .accyear_repository import AccyearRepository
        import json

        repository3 = AccyearRepository()
        detail_year = repository3.select_car_accident_by_local(key)
        json_detailyear = json.dumps([detail_year], ensure_ascii=False) # 여기서 목록으로 반환하도록 [] 표시를 추가했어요
        return HttpResponse(json_detailyear, content_type="application/json")
        
