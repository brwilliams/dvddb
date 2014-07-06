from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
#from dvd.models import LIST MODELS I GUESS.  maybe I can just do import *?
from decimal import * #don't remember if I need this
# Create your views here.
