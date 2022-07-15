
import json
from django.db.models import Count
from django.shortcuts import render
from django.views import View
from schedule.models import Schedule

# K리그 일정 -> K리그 1 뷰


class KL1View(View):
    def get(self, request):
        form = request.GET.dict()
        mbs = Schedule.objects.all()

        if (form != {}):
            match = Schedule.objects.get(id=form['id'])
        else:
            match = Schedule.objects.get(id='1')

        context = {'mbs': mbs,
                   'date': match.date,
                   'time': match.time,
                   'home': match.home,
                   'score': match.score,
                   'away': match.away,
                   }

        return render(request, 'schedule/kl1.html', context)

    def post(self, request):
        pass

class JulyView(View):
    def get(self, request):
            return render(request, 'schedule/july/july_all.html')

# K리그 일정 -> K리그 2(준비 중) 뷰
class KL2View(View):
    def get(self, request):
        return render(request, 'schedule/kl2.html')

    def post(self, request):
        pass
