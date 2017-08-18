from django.conf.urls import url
from . import views
from . import do_shit

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	url(r'^tak_blet/', do_shit.LOL)
]