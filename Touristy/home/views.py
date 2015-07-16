from django.shortcuts import render
from instagram.client import InstagramAPI
from django.http import HttpResponseRedirect, HttpResponse
from login.models import Favorite
from home.models import Weather
from datetime import datetime 
# Create your views here.

session_opts = {
    'session.type': 'file',
    'session.data_dir': './session/',
    'session.auto': True,
}

CONFIG = {
    'client_id': '8d2ddb72ef774dc6a472a4a2090ebbe1',
    'client_secret': 'b1871feaade14048b479907e02784883',
    'redirect_uri': 'http://128.189.139.253/'
}



unauthenticated_api = InstagramAPI(**CONFIG)

def index(request):
    date = datetime.now()
    context_dict = {'weather' : Weather.objects.get(date_id=date) }
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        lat = request.POST.get('lat')
        lng = request.POST.get('lng')
        search_value = request.POST.get('search_value')
        bool_clear_search = request.POST.get('clear_history')
        access_token = request.POST.get('token')

        favorite_place_name = request.POST.get('favorite_place_name')
        # Add the search history to the user's history.
        user = request.user
        if user.is_anonymous():
            print "Anonymous user detected, breaking early."
        else:
            profile = user.userprofile
            if search_value:
                profile.history = search_value + '\n' + profile.history
            elif bool_clear_search:
                profile.history = ""
                print "cleared history!!"
                profile.save()
                return render(request, 'home/index.html', {'weather' : Weather.objects.get(date_id=date)})

            if favorite_place_name != "":
                favorite_place_name = request.POST.get('favorite_place_name')
                favorite_place_content_string = request.POST.get('favorite_place_content_string')
                #fav = user.entry_set.create(user_profile=user, place_name=favorite_place_name, lat=lat, lng=lng, content_string=favorite_place_content_string)
                fav = Favorite.objects.get_or_create(user_profile=user, place_name=favorite_place_name, lat=lat, lng=lng, content_string=favorite_place_content_string)
                print fav
                print 'Favorite printed!'
            else:
                print "Not favorited!"

            if profile:
                print "There's a profile!"
                print user.username
                print profile.history
                profile.save()
            else:
                print "NO profile.. no login, no history."

            

        if access_token:
            try:
                api = InstagramAPI(access_token=access_token, client_secret=CONFIG['client_secret'])
                request.session['access_token'] = access_token

                print "Real ones ", lat, lng
                media_search = api.media_search(lat=lat, lng=lng, distance=100)
                photos = []
                for media in media_search:
                    photos.append(media.get_standard_resolution_url())
                context_dict = {'access_token': access_token, 'photos': photos, 'weather' : Weather.objects.get(date_id=date)}
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
                for media in media_search:
                    photos.append(media.get_standard_resolution_url())
                context_dict = {'access_token': access_token, 'photos': photos, 'weather' : Weather.objects.get(date_id=date)}
            except Exception as e:
                print(e)

        return render(request, 'home/index.html', context_dict)
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'home/index.html', {'weather' : Weather.objects.get(date_id=date)})
    

