import requests

class GeneradorDeNombre:

    def __init__(self):
        my_data_user = self.generate_name_and_email()
        self.name = my_data_user["fullname"]
        self.email = my_data_user["email"]

    def get_name(self):
        return self.name
    
    def get_email(self):
        return self.email

    def generate_name_and_email(self):
        results = "1"  # input("Cuantos quieres? ")
        uri = f'https://randomuser.me/api/?results={results}'
        r = requests.get(uri)
        randomuser = r.json()
        user = randomuser["results"][0]
        
        return {
            "fullname" :f'{user["name"]["first"]} {user["name"]["last"]}',
            "email" : user["email"]
        }

if __name__ == "__main__":
    gen = GeneradorDeNombre()
    my_data_user = gen.generate_name_and_email()
    print(my_data_user["fullname"])
    print(my_data_user["email"])
    print()
    print()
