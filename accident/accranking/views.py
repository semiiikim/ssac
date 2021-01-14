from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse 

# Create your views here.

class HomeView(TemplateView):
    template_name = 'accranking/home-accident.html'

class AccRankingCountView(View):
    def get(self, request, key1, key2):
        from .accrankig_repository import AccrankingRepository
        import json
        
        repository = AccrankingRepository()
        select_count = repository.select_accrankig_count(key1, key2)
        json_select_count = json.dumps(select_count, ensure_ascii=False)
        return HttpResponse(json_select_count, content_type="application/json")

class AccRankingDeathView(View):
    def get(self, request, key1, key2):
        from .accrankig_repository import AccrankingRepository
        import json
        
        repository = AccrankingRepository()
        select_death = repository.select_accrankig_death(key1, key2)
        json_select_death = json.dumps(select_death, ensure_ascii=False)
        return HttpResponse(json_select_death, content_type="application/json")

class AccRankingInjuryView(View):
    def get(self, request, key1, key2):
        from .accrankig_repository import AccrankingRepository
        import json
        
        repository = AccrankingRepository()
        select_injury = repository.select_accrankig_injury(key1, key2)
        json_select_injury = json.dumps(select_injury, ensure_ascii=False)
        return HttpResponse(json_select_injury, content_type="application/json")
