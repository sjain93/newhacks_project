import json
import requests
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import random
import os
import ipdb

def solardata(requests, id):
    
