from django.shortcuts import render
from instagram.client import InstagramAPI
from django.http import HttpResponseRedirect, HttpResponse
from datetime import date, timedelta
from models import Popularity

# Create your views here.

session_opts = {
    'session.type': 'file',
    'session.data_dir': './session/',
    'session.auto': True,
}

CONFIG = {
    'client_id': '1affff744df74fd08d195007f0dca248',
    'client_secret': '25942534c36046909ad8278eb70eadcd',
    'redirect_uri': 'http://127.0.0.1:8000/home/'
}

unauthenticated_api = InstagramAPI(**CONFIG)


def calculate_popularity(times): ##receives array of datetimes!!!
    if len(times) < 10:
        return "low"

    tenth_photo_date = times[9].date()
    current_date = date.today()

    # print current_date
    # print current_date - timedelta(weeks=6*4)
    # print tenth_photo_date

    if (current_date - timedelta(weeks=1*4)) < tenth_photo_date:
        return "high"
    elif (current_date - timedelta(weeks=6*4)) < tenth_photo_date:
        return "med"
    else:
        return "low"

##popularity_list = Popularity.objects.order_by('-lat')
def index(request):
    if request.method == 'POST':
        context_dict = {}
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        lat = str(round(float(request.POST.get('lat')), 7))
        lng = str(round(float(request.POST.get('lng')), 7))
        access_token = request.POST.get('token')

        if access_token:
            try:
                api = InstagramAPI(access_token=access_token, client_secret=CONFIG['client_secret'])
                request.session['access_token'] = access_token

                print "Real ones ", lat, lng
                media_search = api.media_search(lat=lat, lng=lng, distance=100)
                photos = []
                times = []
                for media in media_search:
                    photos.append(media.get_standard_resolution_url())
                    times.append(media.created_time)
                location_popularity = calculate_popularity(times)

                p = Popularity.objects.get_or_create(lat=lat,lng=lng,pop=location_popularity)
                popularity_list = Popularity.objects.order_by('-lat')

                context_dict = {'access_token': access_token, 'photos': photos, 'popularity_list': popularity_list}

            except Exception as e:
                print(e)
        else:
            code = request.GET.get("code")
            if not code:
                return HttpResponse('missing code. \n Please ensure you are logged in instagram before searching for places!')
            try:
                access_token, user_info = unauthenticated_api.exchange_code_for_access_token(code)
                if not access_token:
                    return HttpResponse('Could not get access token')
                api = InstagramAPI(access_token=access_token, client_secret=CONFIG['client_secret'])
                request.session['access_token'] = access_token

                print "Real ones ", lat, lng
                media_search = api.media_search(lat=lat, lng=lng, distance=100)
                photos = []
                times = []
                for media in media_search:
                    photos.append(media.get_standard_resolution_url())
                    times.append(media.created_time)
                location_popularity = calculate_popularity(times)

                p = Popularity.objects.get_or_create(lat=lat,lng=lng,pop=location_popularity)
                popularity_list = Popularity.objects.order_by('-lat')

                context_dict = {'access_token': access_token, 'photos': photos, 'popularity_list': popularity_list}
            except Exception as e:
                print(e)

        return render(request, 'home/index.html', context_dict)
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        popularity_list = Popularity.objects.order_by('-lat')
        return render(request, 'home/index.html', {'popularity_list': popularity_list})