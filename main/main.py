import json



myDict = dict(username='fakhodsadykov', password='redhat', email='farkhodsadykov@gmail.com', role='admin')
with open('./test.json', 'w') as file:
    json.dump(myDict, file, indent=2)
