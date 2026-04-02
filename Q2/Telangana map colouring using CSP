districts = [
'Adilabad','Komaram Bheem','Nirmal','Mancherial','Nizamabad','Kamareddy',
'Karimnagar','Peddapalli','Jagitial','Rajanna','Medak','Siddipet',
'Sangareddy','Warangal Urban','Warangal Rural','Jangaon','Mahabubabad',
'Bhadradri','Khammam','Suryapet','Nalgonda','Yadadri','Medchal',
'Hyderabad','Rangareddy','Vikarabad','Mahabubnagar','Narayanpet',
'Wanaparthy','Jogulamba','Nagarkurnool'
]

neighbors = {
'Adilabad':['Komaram Bheem','Nirmal'],
'Komaram Bheem':['Adilabad','Mancherial'],
'Nirmal':['Adilabad','Nizamabad'],
'Mancherial':['Komaram Bheem','Peddapalli'],
'Nizamabad':['Nirmal','Kamareddy'],
'Kamareddy':['Nizamabad','Medak'],
'Karimnagar':['Jagitial','Peddapalli'],
'Peddapalli':['Karimnagar','Mancherial'],
'Jagitial':['Karimnagar','Rajanna'],
'Rajanna':['Jagitial','Siddipet'],
'Medak':['Kamareddy','Siddipet'],
'Siddipet':['Medak','Jangaon'],
'Sangareddy':['Medak','Medchal'],
'Warangal Urban':['Warangal Rural','Jangaon'],
'Warangal Rural':['Warangal Urban','Mahabubabad'],
'Jangaon':['Siddipet','Warangal Urban'],
'Mahabubabad':['Warangal Rural','Bhadradri'],
'Bhadradri':['Mahabubabad','Khammam'],
'Khammam':['Bhadradri','Suryapet'],
'Suryapet':['Khammam','Nalgonda'],
'Nalgonda':['Suryapet','Yadadri'],
'Yadadri':['Nalgonda','Medchal'],
'Medchal':['Yadadri','Hyderabad'],
'Hyderabad':['Medchal','Rangareddy'],
'Rangareddy':['Hyderabad','Vikarabad'],
'Vikarabad':['Rangareddy','Mahabubnagar'],
'Mahabubnagar':['Vikarabad','Narayanpet'],
'Narayanpet':['Mahabubnagar','Wanaparthy'],
'Wanaparthy':['Narayanpet','Jogulamba'],
'Jogulamba':['Wanaparthy','Nagarkurnool'],
'Nagarkurnool':['Jogulamba','Mahabubnagar']
}

colors = ['Red','Green','Blue','Yellow']

def valid(d, c, assign):
    for n in neighbors.get(d, []):
        if n in assign and assign[n] == c:
            return False
    return True

def solve(assign):
    if len(assign) == len(districts):
        return assign

    for d in districts:
        if d not in assign:
            break

    for c in colors:
        if valid(d, c, assign):
            assign[d] = c
            res = solve(assign)
            if res:
                return res
            del assign[d]

    return None

result = solve({})

print("\nTelangana Map Coloring:\n")
for d in result:
    print(d, "->", result[d])
