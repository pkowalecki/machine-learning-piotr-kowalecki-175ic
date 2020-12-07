# Praca z plikami
Pliki dostępne wykorzystywane w kodzie poniżej:<br><br>
[kowalecki_175ic_txt.txt](https://github.com/pkowalecki/machine-learning-piotr-kowalecki-175ic/blob/main/W6/kowalecki_175ic_txt.txt) <br>
[kowalecki_175ic_write.txt](https://github.com/pkowalecki/machine-learning-piotr-kowalecki-175ic/blob/main/W6/kowalecki_175ic_write.txt) <br>
[test.jpg](https://github.com/pkowalecki/machine-learning-piotr-kowalecki-175ic/blob/main/W6/test.jpg) <br>

### Wczytanie pliku

```
file = open('kowalecki_175ic_txt.txt')
```

### Otwieranie pliku oraz zamknięcie go w razie pojawienia się błędu
```
reader = open('kowalecki_175ic_txt.txt')
try:
  reader.read()
finally:
    reader.close()
```

### Uruchomienie pliku. Zamknięcie następuje po wyjściu z 'with'

```
with open('kowalecki_175ic_txt.txt') as reader:
    reader.read()
```

### Typy plików
```
print(type(open('kowalecki_175ic_txt.txt', 'r')))
print(type(open('kowalecki_175ic_txt.txt', 'rb')))
print(type(open('kowalecki_175ic_txt.txt', 'rb', buffering=0)))
```
Odpowiedź:
<br><class '_io.TextIOWrapper'>
<br><class '_io.BufferedReader'>
<br><class '_io.FileIO'>

### Czytanie pliku
```
with open('kowalecki_175ic_txt.txt', 'r') as reader:
  print(reader.read())
 ```
 Odpowiedź:
<br>Kowalecki 175IC
<br>Linia  2 
<br>Linia 3
<br>Linia 4

 
### Czytanie po 5 bajtów z pliku
```
with open('kowalecki_175ic_txt.txt', 'r') as reader:
  print(reader.readline(5))
  print(reader.readline(5))
  print(reader.readline(5))
 ```
  Odpowiedź:
<br>Kowal
<br>ecki 
<br>175IC

### Zwrócenie tekstu jako listę
```
f = open('kowalecki_175ic_txt.txt')
f.readlines()
```
Odpowiedź:
<br> ['Kowalecki 175IC\n', 'Linia  2 \n', 'Linia 3\n', 'Linia 4\n']

### Iterowanie po każdej linii w pliku na 3 różne sposoby

```
with open('kowalecki_175ic_txt.txt', 'r') as reader:
    line = reader.readline()
    while line != '':
         print(line, end='')
         line = reader.readline()
```
```
with open('kowalecki_175ic_txt.txt', 'r') as reader:
     for line in reader.readlines():
         print(line, end='')
```
```
with open('kowalecki_175ic_txt.txt', 'r') as reader:
     for line in reader:
         print(line, end='')
```
W każdym wypadku odpowiedź wygląda następująco:
<br>Kowalecki 175IC
<br>Linia  2 
<br>Linia 3
<br>Linia 4

### Zapis do pliku
```
with open('kowalecki_175ic_txt.txt', 'r') as reader:
    read_only_text = reader.readlines()

with open('kowalecki_175ic_write.txt', 'w') as writer:
    for text in reversed(read_only_text):
        writer.write(text)

with open('kowalecki_175ic_write.txt', 'r') as reader:
      print(reader.read())
```

Zapis do pliku odwrotnej zawartości i wyświetlenie jej:
<br>Linia 4
<br>Linia 3
<br>Linia  2 
<br>Kowalecki 175IC

### Praca z bajtami - wczytanie pliku
```
with open('kowalecki_175ic_write.txt', 'rb') as reader:
    print(reader.readline())
```
Odpowiedź:
<br>b'Linia 4\n'

### Wczytanie obrazu i wyświetlenie jego danych
```
with open('test.jpg', 'rb') as byte_reader:
     print(byte_reader.read(1))
     print(byte_reader.read(3))
     print(byte_reader.read(2))
     print(byte_reader.read(1))
     print(byte_reader.read(1))
```
Odpowiedź:
<br>b'\xff'
<br>b'\xd8\xff\xe0'
<br>b'\x00\x10'
<br>b'J'
<br>b'F'

