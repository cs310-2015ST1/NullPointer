from django.shortcuts import render
from instagram.client import InstagramAPI
from django.http import HttpResponseRedirect, HttpResponse
from login.models import Favorite
from home.models import Weather
from models import Popularity
from datetime import datetime, date, timedelta
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


def index(request):
    date = datetime.now()
    context_dict = {'weather' : Weather.objects.get(date_id=date), 'popularity_list' : Popularity.objects.all() }
    user = request.user
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception

        user_id_for_follow = request.POST.get('user_id_for_follow')

        if user_id_for_follow:
            print user_id_for_follow
            access_token = request.POST.get('token')
            if access_token:
                print "got access token"
            try:
                api = InstagramAPI(access_token=access_token, client_secret=CONFIG['client_secret'])
                request.session['access_token'] = access_token
                api.follow_user(user_id=str(user_id_for_follow))
                print "followed the poster"
                return render(request, 'home/index.html', {'weather' : Weather.objects.get(date_id=date),
                                                           'popularity_list' : Popularity.objects.all()})
            except Exception as e:
                    print('xxxx',e)
                    return HttpResponse(e)
        else:
            photo_id_for_like = request.POST.get('photo_id_for_like')

            if photo_id_for_like:
                print photo_id_for_like
                access_token = request.POST.get('token')
                if access_token:
                    print "got access token"
                try:
                    api = InstagramAPI(access_token=access_token, client_secret=CONFIG['client_secret'])
                    request.session['access_token'] = access_token
                    print "trying to like the photo"
                    api.like_media(media_id=photo_id_for_like)
                    print "liked the photo"

                    return render(request, 'home/index.html', {'weather' : Weather.objects.get(date_id=date)})
                except Exception as e:
                        print(e)
                        return HttpResponse(e)

            else:
                lat = request.POST.get('lat')
                lng = request.POST.get('lng')
                search_value = request.POST.get('search_value')
                bool_clear_search = request.POST.get('clear_history')
                access_token = request.POST.get('token')

                favorite_place_name = request.POST.get('favorite_place_name')
                # Add the search history to the user's history.
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
                        return render(request, 'home/index.html', {'weather' : Weather.objects.get(date_id=date),
                                                                   'popularity_list' : Popularity.objects.all()})

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
                        photos = {}
                        times = []
                        for media in media_search:
                            photos[media] = media.get_standard_resolution_url()
                            times.append(media.created_time)
                        location_popularity = calculate_popularity(times)
                        p = Popularity.objects.get_or_create(lat=lat,lng=lng,pop=location_popularity)
                        popularity_list = Popularity.objects.all()
                        context_dict = {'access_token': access_token, 'photos': photos,
                                        'weather' : Weather.objects.get(date_id=date), 'popularity_list': popularity_list}
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
                        photos = {}
                        times = []
                        for media in media_search:
                            photos[media] = media.get_standard_resolution_url()
                            times.append(media.created_time)
                        location_popularity = calculate_popularity(times)
                        p = Popularity.objects.get_or_create(lat=lat,lng=lng,pop=location_popularity)
                        popularity_list = Popularity.objects.all()

                        context_dict = {'access_token': access_token, 'photos': photos,
                                        'weather' : Weather.objects.get(date_id=date), 'popularity_list': popularity_list}
                    except Exception as e:
                        print(e)

                return render(request, 'home/index.html', context_dict)
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'home/index.html', context_dict)
    

