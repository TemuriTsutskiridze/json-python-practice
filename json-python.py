import json

# peope_string = '''
# {
#  "people": [
#      {
#       "name":"Elon Musk",
#       "phone":"369-169-136",
#       "emails":["elonmusk@btu.edu.ge","robot@tesla.com"],
#       "has_license":false
#       },
#      {
#       "name": "Nicola Tesla",
#       "phone": "777-777-777",
#       "emails":null,
#       "has_license": true
#       }
#      ]
#  }
# '''
# data = json.loads(peope_string)
# # print(type(data['people']))

# # for person in data['people']:
# #     print(person['name'])

# for person in data['people']:
#     del person['phone']
# sort_keys = True
# new_string = json.dumps(data, indent = 2, sort_keys=True)
# print(new_string)






# with open('states.json') as f:
#     data = json.load(f)
    
# for state in data['states']:
#     # print(state['name'], state['abbreviation'])
#     del state['area_codes']
    
    
# with open('new_states.json', 'w') as f:
#     json.dump(data, f, indent = 2)



# import json 
# from urllib.request import urlopen
# with urlopen("https://www.covid19dataportal.org/api/backend/viral-sequences/sequences?page=1&size=15") as response:
#     source = response.read()
# print(source)
# data = json.loads(source)
# print(json.dumps(data, indent=2))




# import requests
# response = requests.get("https://randomfox.ca/floof")
# print(response.text)
# fox = response.json()
# print(fox['image'])




import requests
import json 
bitcoin= '''
[
  {
    "userId": 1,
    "id": 1,
    "title": "Tesla",
    "completed": false
  },
  {
    "userId": 1,
    "id": 2,
    "title": "Linux",
    "completed": false
  },
  {
    "userId": 1,
    "id": 3,
    "title": "Cisco",
    "completed": false
  },
  {
    "userId": 1,
    "id": 4,
    "title": "Microsoft",
    "completed": true
  },
  {
    "userId": 1,
    "id": 5,
    "title": "Twitter",
    "completed": false
  },
  {
    "userId": 1,
    "id": 6,
    "title": "Github",
    "completed": false
  },
  {
    "userId": 1,
    "id": 7,
    "title": "Unix",
    "completed": false
  },
  {
    "userId": 1,
    "id": 8,
    "title": "MozillaLab",
    "completed": true
  },
  {
    "userId": 1,
    "id": 9,
    "title": "Python",
    "completed": false
  },
  {
    "userId": 1,
    "id": 10,
    "title": "OpenAI",
    "completed": true
  },
  {
    "userId": 1,
    "id": 11,
    "title": "Starlink",
    "completed": true
  },
  {
    "userId": 1,
    "id": 12,
    "title": "Bitcoin",
    "completed": true
  },
  {
    "userId": 1,
    "id": 13,
    "title": "SMS",
    "completed": false
  },
  {
    "userId": 1,
    "id": 14,
    "title": "Clubhouse",
    "completed": true
  },
  {
    "userId": 1,
    "id": 15,
    "title": "BTU",
    "completed": true
  },
  {
    "userId": 1,
    "id": 16,
    "title": "Android",
    "completed": true
  },
  {
    "userId": 1,
    "id": 17,
    "title": "Meta",
    "completed": true
  },
  {
    "userId": 1,
    "id": 18,
    "title": "Google",
    "completed": false
  },
  {
    "userId": 1,
    "id": 19,
    "title": "Apple",
    "completed": true
  },
  {
    "userId": 1,
    "id": 20,
    "title": "Dell",
    "completed": true
  }
]

'''


# json_file = open('json.txt', "r", encoding="utf-8")
# bitcoin = json.load(json_file)
# print(bitcoin)
# json_file.close()
response_json=json.loads(bitcoin)
# print(response_json['title'])
# print(response_json['id'])
print(response_json[0])
for tesla in response_json:
    if tesla['id'] == 5:
        print(tesla['title'])




