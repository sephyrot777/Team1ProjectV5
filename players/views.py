from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from players.models import Records, Soccers
from teams.models import Stadiums, Stadium
from django.core import serializers

# Create your views here.


# Player -> 선수1 감독 뷰


class CoachView(View):
    def get(self, request):
        form = request.GET.dict()
        tbs = Stadium.objects.all()

        if (form == {}):
            if request.session.get('myteam') is not None:
                pinfo = Soccers.objects.filter(team=request.session['myteam'])
            else:
                pinfo = Soccers.objects.filter(team='수원 삼성 블루윙즈')
        else:
            pinfo = Soccers.objects.filter(team=form['team'])



        context = {'pinfo': pinfo, 'tbs': tbs}
        return render(request, 'players/coach1.html', context)

    def post(self, request):
        pass


# Player -> 기록/순위 뷰
class RecordView(View):
    def get(self, request):
        form = request.GET.dict()
        pbs = Records.objects.all()

        if (form != {}):
            player = Records.objects.get(name=form['name'])
        else:
            player = Records.objects.get(name='무고사')
            print(player)
        pbs = Records.objects.all()

        context = {'pbs': pbs,
                   'rank': player.rank,
                   'name': player.name,
                   'team': player.team,
                   'goal': player.goal,
                   'assist': player.assist,
                   'attackpoint': player.attackpoint,
                   'losspoint': player.losspoint,
                   'cornerkick': player.cornerkick,
                   'foul': player.foul,
                   'shoot': player.shoot,
                   'offside': player.offside,
                   'warning': player.warning,
                   'exit': player.exit,
                   'norun': player.norun,
                   'trip': player.trip,
                   'replace': player.replace,
                   'matchpoint': player.matchpoint,
                   }



        return render(request, 'players/record.html', context)



    def post(self, request):
        pass


