import requests
# recuerda instalar la libreria
#     Win: pip install requests
#     Mac: pip3 install requests

def get_json_from(uri):
    r = requests.get(uri)
    # print(r.status_code)
    # print(r.headers['content-type'])
    # print(r.encoding)
    # print(r.text)
    # print(r.json())

    return r.json()

def pretty(d, indent=0):
    for key, value in d.items():
        print('  ' * indent + str(key))
        if isinstance(value, dict):
            pretty(value, indent+1)
        else:
            print('\t' * (indent+1) + str(value))

def main():
    nombresito = generate_name_and_email()
    print(nombresito)
    
def generate_randomuser():
    results = "2"  # input("Cuantos quieres? ")
    uri = f'https://randomuser.me/api/?results={results}'
    randomuser = get_json_from(uri)
    
    return randomuser
    

def generate_name_and_email():
    randomuser = generate_randomuser()
    user = randomuser["results"][0]
    # user = generate_randomuser()["results"][0]  ----> se puede hacer asi para acortarlo
    return {
        "fullname" :f'{user["name"]["first"]} {user["name"]["last"]}',
        "email" : user["email"]
    }

if __name__ == "__main__":
    main()