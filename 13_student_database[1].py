ini_dict = {'Pradeep':{'Roll No':38, 'Division':'A'}, 'Firoz':{'Roll no':44, 'Division':'B'}, 
            'Pratham':{'Roll No':2, 'Division':'C'}, 'Prasad':{'Roll No':2, 'Division':'C'}}
  
# printing initial_dictionary
print ("initial dictionary", str(ini_dict))
  
# code to remove duplicates
result = {}
  
for key, value in ini_dict.items():
    if value not in result.values():
        result[key] = value
          
# printing result
print ("result", str(result))