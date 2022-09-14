import pickle
import json

store = [{"name": "pen", "price": 1.50, "quantity": 15},
         {"name": "pencil", "price": 0.99, "quantity": 30},
         {"name": "scissors", "price": 3.25, "quantity": 6}
         ]

with open('data.pickle', 'wb') as file:
    pickle.dump(store, file)

with open('data.pickle', 'rb') as file:
    content = pickle.load(file)
    with open('data.json', 'w') as jfile:
        json.dump(content, jfile)
