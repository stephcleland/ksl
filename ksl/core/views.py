import json

from django.http import HttpResponse
from django.shortcuts import render

import models

def index(request):
    context = {}
    return render(request, 'index.html', context)

def sync_db(incoming):
    ''' 
    Accepts an incoming JSON bytestring with incoming changes and returns a
    JSON bytestring with a list of changes to the database since the last
    sync. 
    The incoming JSON bytestring should contain a single dictionary with the
    following elements:
        (1) The date of last sync as a string (YYYY-MM-DD HH:MM)
        (2) An array of new words to add to the database.
        (3) An array of new keywords keywords to add to the database.
        (4) An array of new video metadata.
        (5) An array of new word-keyword relations (as arrays).
        (6) An array of new word-video relations (as arrays).
    The outgoing bytestring will contain the same elements.
    e.g. 
    {"time-updated": "2014-01-01 12:00",
     "words": [ "cow", "egg", ],
     "keywords": [ "biology" ],
     "videos": ["cow-sign0", "cow-sign1", "egg-sign0"],
     "word-keyword": [ ["cow", "biology"], ["egg", "biology"] ],
     "word-video": [ ["cow", "cow-sign0"], ["cow", "cow-sign1"],
                     ["egg", "egg-sign0"] ]
    }
    '''
    ## Parse the incoming JSON
    #data = json.decode(incoming)
    ## Enter the incoming data into the database
    #models.add_words(data[words])
    #models.add_keywords(data[keywords])
    #models.add_
    ## Query the database for recently changed data
    ## Construct and return a JSON string

def update(request):
    return sync_db(request.body)
