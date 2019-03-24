from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
import json
import requests
import ipdb

#Api call from Toronto Local data
url = "https://ckan0.cf.opendata.inter.sandbox-toronto.ca/download_resource/38dbdd62-70e7-43f7-b9a1-f770cd04c574?format=json"
res = requests.get(url)
body = json.loads(res.content)
address = []

#rendering data on home page
def home_page(request):
    for item in body:
        if item['STATUS'] == 'Closed':
            address.append("{} {} {}".format(item['STREET_NUM'],item['STREET_NAME'],item['STREET_TYPE']))
    context = {'data': address}
    # ipdb.set_trace()
    response = render(request, 'index.html', context)
    return HttpResponse(response)
