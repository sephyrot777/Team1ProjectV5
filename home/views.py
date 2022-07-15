from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.core import serializers
from urllib.parse import urlencode
from math import ceil
from board.models import News
from home.models import Standing
from join.models import Member

# Create your views here.

# 메인화면 뷰


class HomeView(View):
    def get(self, request, perPage = 8):
        form = request.GET.dict()
        sbs = Standing.objects.all()
        query = ''

        if (form != {}):
            stand = Standing.objects.get(rank=form['rank'])
        else:
            stand = Standing.objects.get(rank='1')


        if request.GET.get('keyword') is not None and request.GET.get('type') is not None:

            if form['type'] == 'title':
                announce_table = News.objects.select_related(). \
                    filter(category__contains='notice', title__contains=form['keyword'])
            elif form['type'] == 'content':
                announce_table = News.objects.select_related(). \
                    filter(category__contains='notice', content__contains=form['keyword'])


            query = urlencode({'type': form['type'], 'keyword': form['keyword']})

        else:
            announce_table = News.objects.select_related().filter(category__contains='notice')
            # announce_table = News.objects.select_related()


        pages = ceil(announce_table.count() / perPage)

        page = 1
        if request.GET.get('page') is not None:
            page = form['page']

        start = (int(page) - 1) * perPage
        end = start + perPage

        announce_table = announce_table[start:end]
        listPage = int((int(page) - 1) / 10) * 10 + 1

        context = {'sbs': sbs,
                   'rank': stand.rank,
                   'based': stand.based,
                   'team': stand.team,
                   'match': stand.match,
                   'wpoint': stand.wpoint,
                   'win': stand.win,
                   'draw': stand.draw,
                   'defeat': stand.defeat,
                   'goal': stand.goal,
                   'loss': stand.loss,
                   'gol': stand.gol,
                   'at': announce_table,
                   'pages': pages,
                   'range': range(listPage, listPage + 10),
                   'query': query
                   }



        return render(request, 'index.html', context)

    def post(self, request):
        pass

# 로그인 뷰
class LoginView(View):
    def post(self, request):
        form = request.POST.dict()

        returnPage = '/loginfail'
        isExisted = Member.objects.filter(userid=form['muserid'], passwd=form['mpasswd']).exists()


        if isExisted:
            user = Member.objects.get(userid=form['muserid'])

            request.session['myteam'] = str(user.team)
            print(request.session['myteam'])

            returnPage='/'

        return redirect(returnPage)


# 로그인 실패 뷰
class LoginfailView(View):
    def get(self, request):
        return render(request, 'loginfail.html')

# 로그아웃 뷰
class LogoutView(View):
    def get(self, request):
        request.session.flush()

        return redirect('/')

    def post(self, request):
        pass

# 사이트맵 뷰
class SitemapView(View):
    def get(self, request):
        return render(request, 'sitemap.html')

    def post(self, request):
        pass

# 마이페이지 뷰
class MypageView(View):
    def get(self, request):
        return render(request, 'mypage.html')

    def post(self, request):
        pass


class SearchIdView(View):
    def get(self, request):
        form = request.GET.dict()

        # 아이디를 찾기 위해 가입 때 입력한 이메일로 가입여부 조회

        # isExisted가 True면 DB에서 id를 찾아 context로 보내고, False면 error 내용을 context로 보낸다
        # m= Member.objects.select_related().get(email=form['email'])
        # context = {'member': m}
        # return render(request, 'layouts/modal.html', context)

        result= Member.objects.select_related().filter(email=form['email'])
        json_data = serializers.serialize('json', result)
        print(json_data, form['email'])


        return HttpResponse(json_data, content_type='application/json')


class StandingView(View):
    def get(self, request):
        form = request.GET.dict()
        sbs = Standing.objects.all()
        print(form)

        if (form != {}):
            stand = Standing.objects.get(rank=form['rank'])
        else:
            stand = Standing.objects.get(rank='1')


        context = {'sbs': sbs,
                   'rank': stand.rank,
                   'based': stand.based,
                   'team': stand.team,
                   'match': stand.match,
                   'wpoint': stand.wpoint,
                   'win': stand.win,
                   'draw': stand.draw,
                   'defeat': stand.defeat,
                   'goal': stand.goal,
                   'loss': stand.loss,
                   'gol': stand.gol,
                   }

        print(context)

        return render(request, 'index.html', context)