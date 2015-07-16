from django.shortcuts import render
from instagram.client import InstagramAPI
from django.http import HttpResponseRedirect, HttpResponse

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

def index(request):
    if request.method == 'POST':
        context_dict = {}

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
                return render(request, 'home/index.html', {})
            except Exception as e:
                    print(e)
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
                    api.like_media(media_id=photo_id_for_like)
                    print "liked the photo"
                    return render(request, 'home/index.html', {})
                except Exception as e:
                        print(e)
                        return HttpResponse(e)
            else:
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
                        photos = {}
                        for media in media_search:
                            photos[media] = media.get_standard_resolution_url()
                        context_dict = {'access_token': access_token, 'photos': photos}
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
                        for media in media_search:
                            photos[media] = media.get_standard_resolution_url()
                        context_dict = {'access_token': access_token, 'photos': photos}
                    except Exception as e:
                        print(e)

                return render(request, 'home/index.html', context_dict)
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'home/index.html', {})

