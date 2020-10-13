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
  mylist = []
  noofresults = int(response['results'])
  for x in range(0, noofresults):
    mylist.append(response['response'][x]['country'])
  if request.method == 'POST':
    selectedcountry = request.POST['selectedcountry']
    print(selectedcountry)
    noofresults = int(response['results'])
    for x in range(0, noofresults): 
      if selectedcountry == response['response'][x]['country']:
        new = response['response'][x]['cases']['new']
        active = response['response'][x]['cases']['active']
        critical = response['response'][x]['cases']['critical']
        recovered = response['response'][x]['cases']['recovered']
        total = response['response'][x]['cases']['total']
        deaths = int(total) - int(active) - int(recovered)
    context ={
      'selectedcountry': selectedcountry,
      'mylist': mylist,
      'new': new,
      'active': active,
      'critical': critical,
      'recovered': recovered,
      'total': total,
      "deaths": deaths,
    }
    return render(request, 'helloworld.html', context)
  context = {'mylist': mylist}
  return render(request, 'helloworld.html', context)