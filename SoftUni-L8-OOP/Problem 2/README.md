### Задача: 2. Разширете програмата от предишната задача така, че да може да чете различни входни формати


Програмата от предишната задача зарежда данните от JSON файл.

По подобие на метода, който използвахме за чертане на различни фигури, разширете програмата така, че да може да чете входните си данни от файлове с различни формати - както JSON, така и YAML.

За да решите задачата, е необходимо:

- Да създадете базов клас - например Loader, който:
  * да приема име на файл в конструктора си.
  * да има метод ```load()```, който за този клас е празен; припомняме, че реализацията ще бъде в наследниците, и ще бъде специфична за съответните формати

```python
import os

class Loader:
    def __init__(self, filename):
        # base validations
        if os.access(filename, os.R_OK) and os.path.isfile(filename):
            self.filename = filename
        else:
            raise ValueError("Inaccessible file '{}'".format(filename))

    def load(self):
        raise NotImplementedError()
```

- Да създадете клас JSONLoader, който наследява Loader, и да реализирате метода ```load()```

```python
class JSONLoader(Loader):

    def load():
        with open(self.input_filename) as f:
            input_data = json.load(f)
            return input_data
```

- Да промените функцията ```load_input_data()``` от главния файл:

```python
from loaders import JSONLoader

def load_input_data(input_filename):
    # os.path.splitext връща tuple с 2 стойности - име и разширение на файла
    filename, extension = os.path.splitext(input_filename)
    loader = None
    if extension == '.json':
        loader = JSONLoader(input_filename)
    elif extension == '.yaml':
        # ... тук по същия начин ще се добави обработване на YAML файлове
        pass

    if loader is not None:
        return loader.load()
    else:
        raise ValueError("Unsupported file format: {}".format(extension))
```

### Работа с YAML в Python
YAML e лек, удобен и лесно четим файлов формат, при който излишните символи са сведени до минимум.

За да можете да работите с YAML, трябва да инсталирате пакет ```PyYAML```:

```python
pip3 install PyYAML
```

След като сте инсталирали пакета ```PyYAML```, в Python можете да заредите YAML файл по почти същия начин, както зареждате и JSON файл:

```python
import yaml

...

with open('input-file.yaml') as f:
    input_data = yaml.load(f)

print(input_data)
```

Примерен файл 'input-file.yaml':

```
- type: square
  center_x: 0
  center_y: 0
  side: 2
  color: black

- type: square
  center_x: 0
  center_y: 0
  side: 100
  color: red

- type: square
  center_x: 0
  center_y: 0
  side: 200
  color: blue

- type: circle
  center_x: 0
  center_y: 0
  radius: 50
  color: blue

- type: circle
  center_x: 0
  center_y: 0
  radius: 100
  color: red
```
