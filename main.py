from fastapi import FastAPI
import requests
import flask
import random

app = FastAPI()



class RequestAPI:
    url = 'https://dog-facts-api.herokuapp.com/api/v1/resources/dogs/all'
    
    def get_facts(self):
        result = requests.get(self.url).json()
        return result
    def get_fact(self):
        result2 = requests.get(self.url).json()
        i = random.randint(1, 50)
        return result2[i]['fact']

        
    def get_one_fact_for_name(self, name):
        return '%s, Do you know that, %s ?'%(name, self.get_fact())

@app.get('/')
def index():
    return 'Welcome to the main page of the site about the dog facts'
      
@app.get('/names')
def names():
    return 'Sasha, Masha, Dasha, Katya'

@app.get('/facts/list')
def all_facts():
    request = RequestAPI()
    return request.get_facts()

@app.get('/names/{name}')
def names_one(name):
     request_1 = RequestAPI()
     return request_1.get_one_fact_for_name(name)
    

@app.get('/facts/fact')
def get_one_fact():
    request_2 =  RequestAPI()
    return request_2.get_fact()


