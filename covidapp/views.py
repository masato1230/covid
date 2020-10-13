from django.shortcuts import render
import requests
import json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "c6423465efmsh620fdeb33728c9dp187368jsnd1c18150f0b6"
    }

response = requests.request("GET", url, headers=headers).json()

def helloworldview(request):
  if request.method == 'POST':
    selectedcountry = request.POST['selectedcountry']
    print(selectedcountry)
  noofresults = int(response['results'])
  mylist = []
  for x in range(0, noofresults):
    mylist.append(response['response'][x]['country'])
  context = {'mylist': mylist}
  return render(request, 'helloworld.html', context)