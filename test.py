import requests


#vext api key to access llm pipeline
api_key = 'XjyKjf51.5yrjeLpBvnGvuQq28BwO36pjLw1EPdnN'
your_query = 'What is Ai'

#headers

headers ={
    'Content-Type' : 'application/json',
    'Apikey' : f'Api-Key {api_key}'
}

data ={
    "payload" : your_query
}

url = 'https://payload.vextapp.com/hook/E5GBCSEKCI/catch/$(pravin)'


response = requests.post(url, json=data, headers=headers)
print(response.text)
    