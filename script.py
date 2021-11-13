import json

class Art:
    def _init_(self,id,name):
        self.id =id
        self.name = name

    
    @classmethod(f)
    def from_json(cls, json_string):
        json_dict = json.loads(json_string)
        return cls(**json_disc)

    def _repr_(self):
        return f"<Art { self.name}>"

arts_list = []
with open("art.json", "r") as json_file:
     art_data = json.loads (json_file.read())
     for u in arts_data:
         users_list.append(Art(**u))

print (arts_list)         
           

