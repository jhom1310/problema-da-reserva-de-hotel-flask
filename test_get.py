import requests

def test_hoteis_1():
    url = 'http://127.0.0.1:5000/api/v1/cheapest/Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)'
   
    valor = {"cheapest": "Lakewood"}

    response = requests.get(url)
    response_dict = response.json()    

    assert response_dict == valor

def test_hoteis_2(): 
    url = 'http://127.0.0.1:5000/api/v1/cheapest/Regular: 20Mar2009(fri), 21Mar2009(sat), 22Mar2009(sun)'

    valor = {"cheapest": "Bridgewood"}
     
    response = requests.get(url)
    response_dict = response.json()    

    assert response_dict == valor

def test_hoteis_3():
    url = 'http://127.0.0.1:5000/api/v1/cheapest/Reward: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)'

    valor = {"cheapest": "Ridgewood"}
     
    response = requests.get(url)
    response_dict = response.json()    

    assert response_dict == valor

