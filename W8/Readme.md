# Praca z danymi w formacie JSON i CSV

 Pliki dostępne wykorzystywane w kodzie poniżej:<br><br>
 [JSON files](https://github.com/pkowalecki/machine-learning-piotr-kowalecki-175ic/tree/main/W8/json_file) <br>
 [CSV files](https://github.com/pkowalecki/machine-learning-piotr-kowalecki-175ic/tree/main/W8/csv_file) <br>

## Working With JSON Data in Python

Prosta serializacja, przekształcenie danych w format JSON<br>

```
data = {
    "student": {
        "name": "Piotr Kowalecki",
        "group": "175IC_B1"
    }
}
```

Zapisanie formatu JSON do pliku o nazwie data_file.json<br>

```
with open("json_file/data_file.json", "w") as write_file:
  json.dump(data, write_file)
```

Formatowanie tekstu. Dodanie wycięć podczas wyświetlania<br>

```
json.dumps(data, indent=3)
```

Deserializacja z pliku. Odczyt danych.<br>

```
with open("json_file/data_file_deserialization.json", "r") as read_file:
    data = json.load(read_file)
```

Deserializacja z URL<br>

```
response = requests.get("https://jsonplaceholder.typicode.com/posts")
posts = json.loads(response.text)
```

Wyświetlanie osób oraz ilość postów napisanych przez te osoby:

```
posts_by_user = {}

for post in posts:
  if post["id"]:
    try:
      posts_by_user[post["userId"]] += 1
    except KeyError:
      posts_by_user[post["userId"]] = 1

top_posts = sorted(posts_by_user.items(), 
                   key=lambda x: x[1], reverse=True)

print(f'Top postów: {top_posts}')
```

Wyświetlenie osób które mają największą ilość napisanych postów<br>
Na moje nieszczęście każda osoba ma napisane po 10 postów<br>
```
max_complete = top_posts[0][1]
users = []
for user, num_complete in top_posts:
    if num_complete < max_complete:
        break
    users.append(str(user))

max_users = ", ".join(users)

print(f'ID osób które mają najwięcej postów: {max_users}')
```

Wypisanie postów osób które mają ich najwięcej oraz zapis tych danych do pliku filtered_data_file.json<br>

```
def keep(post):
    is_complete = post["id"]
    has_max_count = str(post["userId"]) in users
    return is_complete and has_max_count

with open("json_file/filtered_data_file.json", "w") as data_file:
    filtered_posts = list(filter(keep, posts))
    json.dump(filtered_posts, data_file, indent=2)
```


Kodowanie i dekodowanie niestandardowych obiektów PYTHON<br>

```
def encode_complex(z):
    if isinstance(z, complex):
        return (z.real, z.imag)
    else:
        type_name = z.__class__.__name__
        raise TypeError(f"Object of type '{type_name}' is not JSON serializable")
```

Kodowanie z pomocą JSONEncoder<br>

```
class ComplexEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, complex):
            return (z.real, z.imag)
        else:
            return super().default(z)
```

Dekodowanie typów niestandardowych<br>

```
complex_json = json.dumps(4 + 17j, cls=ComplexEncoder)
print(f'json.loads: {json.loads(complex_json)}')
```

Dekodowanie klucza - definicja oraz odkodowanie<br>

```
def decode_complex(dct):
    if "__complex__" in dct:
        return complex(dct["real"], dct["imag"])
    return dct

with open("json_file/complex_data.json") as complex_data:
     data = complex_data.read()
     z = json.loads(data, object_hook=decode_complex)
```


## Reading and Writing CSV Files in Python

Czytanie plików CSV<br>

```
with open('csv_file/addresses.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} {row[1]} comes from {row[4]} and has post code {row[5]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')
```

Zapisywanie plików CSV<br>

```
with open('csv_file/addresses.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(['Name', 'Surname','Street','City','Nb','PostCode'])
    employee_writer.writerow(['John', 'Smith', 'Street', 'Tahoma','Th','0000000'])
```

Czytanie plików CSV z użyciem PANDAS<br>

```
df = pd.read_csv('csv_file/freshman_kgs.csv')
```

Zapis plików CSV z użyciem PANDAS oraz zamiana indeksu<br>

```
df = pd.read_csv('csv_file/freshman_kgs.csv', 
            index_col='"Weight (Sep)"', 
            parse_dates=['"Weight (Sep)"'],
            header=1, 
            names=['Sex','"Weight (Sep)"','"Weight (Apr)"','"BMI (Sep)"','"BMI (Apr)"'])
df.to_csv('csv_file/freshman_modified.csv')
```
