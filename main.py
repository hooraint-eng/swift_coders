import csv

total_family_member= {}

with open ("family_size.csv","r") as csvfile:
    
    personal_info = list(csv.reader(csvfile,delimiter=","))
    
    person_num = 1
    
    for person in personal_info:
        
        print(f"Person # {person_num}:{person}")
        
        person_num +=1

    for row in personal_info [1:]:
        
        name = row[0]

        age = row[1]
        
        value = [int(cell) for cell in row [2:5]]
        
        total = sum(value)
        
        total_family_member[name]= total
      
        
    for person_name, total in total_family_member.items():
            
        print(f"{person_name} has total family memeber of {total}")
        

