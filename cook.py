import io, json
f = io.open('/Users/carlosgoncalves/Documents/development/nutrition/foods.js','w', encoding='utf-8')
with open('/Users/carlosgoncalves/Documents/development/nutrition/FoodData_Central_foundation_food_json_2025-04-24.json', 'r') as file:
        master_data = json.load(file)
f.write("let FOODS = {\n")
data =  master_data['FoundationFoods']
n = len(data)
id_list = []
for i in range(n):
    description = data[i]['description']
    id= str(data[i]['fdcId'])
    description = description.replace('"','\\"')
    f.write("\""+description+"\": \""+id+"\",\n")
    if 'wild caught' in description.lower():
        print("#"+description+"#")
        nutrients = data[i]['foodNutrients']
        nn = len(nutrients)
        for j in range(nn):
            try:
                print(nutrients[j]['nutrient']['name'], nutrients[j]['amount'], nutrients[j]['nutrient']['unitName'])
            except:
                print(nutrients[j]['nutrient']['name'], "amount not found")
        if 'wild caught' in description.lower():
            print("#"+description+"#")
            for key in data[i].keys():
                value = str(data[i][key])
                if len(value) > 20:
                    value = value[:20]+"..."
                print(f"{key}: {value}")
print("Total of different fdcIds: ", sorted(set(id_list)))
print("Total of different food: ",n)
f.write("}")
f.close()