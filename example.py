import requests
url = 'https://httpbin.org/'

def ex1():
    res = requests.get(url + 'get')

    print(res.json())

def ex2():
    res = requests.post(url + 'post', json= {'Channel': 'ShandonCodes'})

    print(res.json())

def ex3():
    res = requests.post(url + 'post', json= {'Channel': 'ShandonCodes'}, headers={'TEST_HEADER': 'TEST'})

    print(res.json())
def ex4():
    res = requests.get(url + 'delay/10')

    print(res.json())

def ex5():
    try: 
        res = requests.get(url + 'delay/10', timeout=5)

        print(res.json())
    except requests.exceptions.ReadTimeout:
        print('Request did not complete in time.')

ex1()
ex2()
ex3()
ex4()
ex5()
