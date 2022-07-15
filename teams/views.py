from django.shortcuts import render, redirect
from django.views import View
from teams.models import Stadiums, Stadium


# Create your views here.


class TeamsView(View):
    def get(self, request):
        form = request.GET.dict()
        tbs = Stadium.objects.all()

        if (form == {}):
            if request.session.get('myteam') is not None:
                team = Stadium.objects.get(hteam=request.session['myteam'])
            else:
                team = Stadium.objects.get(hteam='FC서울')
        else:
            team = Stadium.objects.get(hteam=form['hteam'])



        context = {'tbs': tbs,
                   'stname': team.stname,
                   'opdate': team.opdate,
                   'based': team.based,
                   'hteam': team.hteam,
                   'accnum': format(team.accnum, ','),
                   'addr': team.location,
                   'addrstmp': team.addrstmp,
                   'addrkey': team.addrkey,
                   'url': team.url,
                   }

        return render(request, 'teams/stadium.html', context)


class OrganizationView(View):
    def get(self, request):
        return render(request, 'teams/organization.html')
