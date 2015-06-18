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
    'client_id': '8d2ddb72ef774dc6a472a4a2090ebbe1',
    'client_secret': 'b1871feaade14048b479907e02784883',
    'redirect_uri': 'http://127.0.0.1:8000/home'
}
unauthenticated_api = InstagramAPI(**CONFIG)

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


        code = request.GET.get("code")
        if not code:
            return HttpResponse('missing code')
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
            context_dict = {'access_token': access_token, 'photos': photos}
        except Exception as e:
            print(e)


        return render(request, 'home/index.html', context_dict)
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'home/index.html', {})