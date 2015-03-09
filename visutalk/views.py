from django.shortcuts import render_to_response, redirect, render
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect
from open_facebook import OpenFacebook
from social.apps.django_app.default.models import UserSocialAuth
from django.contrib.auth.models import User
from visutalk.models import UserKakaoAuth
from django.contrib.auth import login

User._meta.get_field('username')._unique = False

@csrf_protect
def home(request):
    user=request.user
    if request.method=="POST" and request.is_ajax():
        user_list=UserKakaoAuth.objects.all().filter(uid=request.POST["id"])
        if user_list:
            user=User.objects.get(id=user_list[0].user_id)
        else:
            username = request.POST["properties[nickname]"]
            user = User.objects.create_user(username)
            kakao_user = UserKakaoAuth(provider="kakao", uid=request.POST["id"],user_id=user.id)
            kakao_user.save()
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request,user)
    context = {'request': request,'user': user}
    return render(request,'home.html',
                            context)

def picture(request):
   user= UserSocialAuth.objects.get(user_id=request.user.id)
   facebook = OpenFacebook('422158497940047|5wSfOHT-9XlGJldHlXHPlImUMjI')
   ob=facebook.get(str(user.uid)+'/picture', height=99999,redirect=False)
   return render_to_response('picture.html',{'profile_pic':ob["data"]["url"]})
