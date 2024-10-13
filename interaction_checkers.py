import json

def load_database():
    try:
        with open('data/drugs_database.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Database file not found.")
        return {}

def check_interaction(drug1, drug2):
    database = load_database()
    drug_pair = tuple(sorted([drug1, drug2]))
    
    return database.get(drug_pair, None)
