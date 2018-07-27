from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
# from models import *
from django.core import serializers
import json
from stattlepy import Stattleship

def index(request):
  New_query = Stattleship()
  Token = New_query.set_token('4d4437ec2f26e8f8a489979d0f528f11')
  players = New_query.ss_get_results(sport="baseball",ep="players", league='mlb', season_id='mlb-2017', ) 
  #print(players[0]) 
  #print(type(players))
  parsed_json = players.pop()
  #print(parsed_json.get('players')[0].get('first_name'))
  #print(type(parsed_json))

  return render(request, 'index.html', {'players': parsed_json.get('players')})

def b(request):
  New_query = Stattleship()
  Token = New_query.set_token('4d4437ec2f26e8f8a489979d0f528f11')
  players = New_query.ss_get_results(sport="baseball",ep="players", league='mlb', season_id='mlb-2017', )
  parsed_json = players.pop('b')

  return render(request, 'index.html', {'players': parsed_json.get('players')})


def hitter(request):
  return render(request,'index.html')

def pitchers(request):
  return render(request,'index.html')

def users_api(request):
    # users = User.objects.filter(first_name__startswith=request.POST['starts_with'])
    return render(request, 'user_login/index.html')

def users_api_json(request):
    # users = User.objects.filter(first_name__startswith=request.POST['starts_with'])
    return HttpResponse(serializers.serialize("json"), content_type='application/json')


    # ,season_id='mlb-2017',player_id='mlb-manny-machado'





# API Info

# App Name
# lovedteacher
# Client Id
# dc73b5528c54c70cc0a987215e465ed9
# Client Secret
# f357f52bd1edfa4b8b56b05eeedc40322e0cb62650606427954ffd0b562d2aa6
# Access Token

# 4d4437ec2f26e8f8a489979d0f528f11
