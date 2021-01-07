import os
import requests
from django.conf import settings

def search_food(query):
    url = 'https://api.nal.usda.gov/fdc/v1/foods/search'
    r = requests.get(url, params={'api_key':settings.FDC_API_KEY, 'query':query, 'requireAllWords': 'true', 'dataType': 'Survey (FNDDS)'})
    print(r.url)
    # turns request into JSON
    food = r.json()
    
    return food











    # logic for only getting the wanted nutrients
    #food_test = []
    #nutrient_list = ['Protein', 'Total lipid (fat)', 'Carbohydrate, by difference', 'Energy', 'Fiber, total dietary', 
    #                 'Sugars, total including NLEA', 'Fatty acids, total monounsaturated', 'Fatty acids, total polyunsaturated', 'Fatty acids, total saturated', 
    #                 'Sodium, Na', 'Potassium, K', 'Magnesium, Mg', 'Iron, Fe', 'Calcium, Ca', 'Vitamin C, total ascorbic acid']
    #for j in range(int(food['totalHits'])):
    #    food_test.clear()
    #    for i in range(len(food['foods'][j]['foodNutrients'])):
    #        if food['foods'][j]['foodNutrients'][i]['nutrientName'].strip() in nutrient_list:
    #            food_test.append(food['foods'][j]['foodNutrients'][i])
    #    del food['foods'][j]['foodNutrients']
    #    food['foods'][j]['foodNutrients'] = food_test

    #print(food_test)



    #for i in range(len(food['foods'][0]['foodNutrients'])):

    #    if food['foods'][0]['foodNutrients'][i]['nutrientName'].strip() in nutrient_list:
    #        #print(True)
    #        food_test.append(food['foods'][0]['foodNutrients'][i])
    #    #else:
    #        #print(False)

    #del food['foods'][0]['foodNutrients']
    #food['foods'][0]['foodNutrients'] = food_test

