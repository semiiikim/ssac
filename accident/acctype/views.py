from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse

# Create your views here.
 
class HomeView(TemplateView):
    template_name = 'acctype/home-accident.html'

class AccCountView(View):
    def get(self, request, key, key2):
        from .acctype_repository import AcctypeRepository
        import json

        repository = AcctypeRepository()
        select_acccount = repository.select_acctype_acccount(key, key2)
        json_select_acccount = json.dumps(select_acccount, ensure_ascii=False)
        return HttpResponse(json_select_acccount, content_type="application/json")

class DeathCountView(View):
    def get(self, request, key, key2):
        from .acctype_repository import AcctypeRepository
        import json

        repository = AcctypeRepository()
        select_deathcount = repository.select_acctype_deathcount(key, key2)
        json_select_deathcount = json.dumps(select_deathcount, ensure_ascii=False)
        return HttpResponse(json_select_deathcount, content_type="application/json")

class InjuryCountView(View):
    def get(self, request, key, key2):
        from .acctype_repository import AcctypeRepository
        import json

        repository = AcctypeRepository()
        select_injurycount = repository.select_acctype_injurycount(key, key2)
        json_select_injurycount = json.dumps(select_injurycount, ensure_ascii=False)
        return HttpResponse(json_select_injurycount, content_type="application/json")
