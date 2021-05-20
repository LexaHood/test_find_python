#   🐍Unix 'find' on Python

* **📓Описание**

    Простая реализация команды find. 
    Поиск производится рекурсивно. 
    Не взаимодействует с директорииями. 
    Может делать:

    *    Рекурсивно искать файлы в заданной директории
    *    Искать файлы по заданному шаблону
    *    Удалаять файлы  


* **💻Как использовать**

    ```
    ❯ python ./find.py -h

    usage: find.py [-h] [--path PATH] [--name NAME] [--delete] [--info]

    optional arguments:
    -h, --help            show this help message and exit
    --path PATH, -p PATH  directory path
    --name NAME, -n NAME  file name
    --delete, -d          delete found files
    --info, -i            debug information
    ``` 

* **📮Типы аргументов**

    `path` | `name` | `delete` | `info`

    * **Аргумент `--path`**
        <br>Позволяет явно указать директорию поиска. <b>Задается в кавычках.</b> Вернет найденные файлы в указанной директории</br>

        ```bash
        ❯ python ./find.py -p '/home/alexey/Project/Test-py/' 
        found: /home/alexey/Project/Test-py/Pipfile 
        ``` 
        
        <br>Если аргумент `--path` не указывать, то поиск будет произведен из текущей директории. Вернет найденные файлы из текущей директории</br>

        ```bash
        ❯ python ./find.py 
        found: /media/alexey/NAS/programming/test-find-program/.gitignore
        found: /media/alexey/NAS/programming/test-find-program/find.py
        found: /media/alexey/NAS/programming/test-find-program/Pipfile
        found: /media/alexey/NAS/programming/test-find-program/README.md
        found: /media/alexey/NAS/programming/test-find-program/test.py
        found: /media/alexey/NAS/programming/test-find-program/.git/description
        ... 
        ```
        <br>Если указанная директория не будет найдена, программа выведет соответсвующее сообщение</br>

        ```bash
        ❯ python ./find.py -p '/home/alexey/Project/dfdffd/' 
        path not available 
        ```
    <br></br>  
    * **Аргумент `--name`**
        <br>Позволяет явно указать шаблон поиска. <b>Задается в кавычках.</b></br> Шаблон поддерживает 
        | Шаблон        | Соответсвует  |
        | ------------- |:-------------:|
        | *             | соответствует всему|
        | ?     | соответствует любому одиночному символу      |
        | [seq] | соответствует любому символу в seq     |
        | [!seq] | соответствует любому символу не в seq |

        
        см.подрорбнее: (https://docs.python.org/3.8/library/fnmatch.html)

        ```bash
        ❯ python ./find.py -n '*.??'
        found: /media/alexey/NAS/programming/test-find-program/find.py
        found: /media/alexey/NAS/programming/test-find-program/README.md
        found: /media/alexey/NAS/programming/test-find-program/test.py 
        ``` 
        
        <br>Если аргумент `--name` не указывать, поиск будет произведен по универсальному ключу `'*'`</br>

        ```bash
        ❯ python ./find.py
        found: /media/alexey/NAS/programming/test-find-program/.gitignore
        found: /media/alexey/NAS/programming/test-find-program/find.py
        found: /media/alexey/NAS/programming/test-find-program/Pipfile
        found: /media/alexey/NAS/programming/test-find-program/README.md
        found: /media/alexey/NAS/programming/test-find-program/test.py
        found: /media/alexey/NAS/programming/test-find-program/.git/description
        ... 
        ```
        <br>Если по указанному шаблону файлов не будет найдено, программа выведет соответсвующее сообщение</br>

        ```bash
        ❯ python ./find.py -n '*fg'
        nothing was found
        ``` 
    
    <br></br>  
    * **Аргумент `--delete`**
        <br>Позволяет удалять найденные файлы. <b>Задавать значение параметра не нужно</b></br>

        ```bash
        ❯ python ./find.py -p '/home/alexey/Project/Test-py/' -d
        deleted: /home/alexey/Project/Test-py/file-T
        deleted: /home/alexey/Project/Test-py/file-O
        deleted: /home/alexey/Project/Test-py/file-E
        deleted: /home/alexey/Project/Test-py/file-V
        deleted: /home/alexey/Project/Test-py/file-A
        deleted: /home/alexey/Project/Test-py/file-F
        deleted: /home/alexey/Project/Test-py/file-S
        deleted: /home/alexey/Project/Test-py/file-U
        deleted: /home/alexey/Project/Test-py/file-X
        deleted: /home/alexey/Project/Test-py/file-Q
        deleted: /home/alexey/Project/Test-py/file-W
        deleted: /home/alexey/Project/Test-py/file-D
        deleted: /home/alexey/Project/Test-py/file-K
        deleted: /home/alexey/Project/Test-py/file-J
        deleted: /home/alexey/Project/Test-py/file-B
        deleted: /home/alexey/Project/Test-py/file-Y
        deleted: /home/alexey/Project/Test-py/file-Z
        deleted: /home/alexey/Project/Test-py/file-I
        deleted: /home/alexey/Project/Test-py/file-N
        deleted: /home/alexey/Project/Test-py/file-G
        deleted: /home/alexey/Project/Test-py/file-M
        deleted: /home/alexey/Project/Test-py/file-C
        deleted: /home/alexey/Project/Test-py/file-H
        deleted: /home/alexey/Project/Test-py/file-R
        deleted: /home/alexey/Project/Test-py/file-L
        deleted: /home/alexey/Project/Test-py/file-P
        ``` 
        
        <br>Если аргумент `--delete` не указывать, Удаление файлов выполняться не будет</br>

        ```bash
        ❯ python ./find.py
        found: /media/alexey/NAS/programming/test-find-program/.gitignore
        found: /media/alexey/NAS/programming/test-find-program/find.py
        found: /media/alexey/NAS/programming/test-find-program/Pipfile
        found: /media/alexey/NAS/programming/test-find-program/README.md
        found: /media/alexey/NAS/programming/test-find-program/test.py
        found: /media/alexey/NAS/programming/test-find-program/.git/description
        ... 
        ```
        <br>Если файл удалить не удалось. Программа выведет соответсвующее сообщение, вместе с возвращенной ошибкой</br>

        ```bash
        ❯ python ./find.py -p '/home/alexey/Project/Test-py/' -d
        failed to delete file
        OS error: [Errno 1] Operation not permitted: '/home/alexey/Project/Test-py/test.txt'
        ```
    <br></br>  
    * **Аргумент `--info`**
        <br>Выводит дебаг информацию. <b>Задавать значение параметра не нужно</b></br>

        ```bash
        ❯ python ./find.py -p '/home/alexey/Project/Test-py/' -i
        found: /home/alexey/Project/Test-py/test.txt
        Namespace(delete=False, info=True, name='*', path='/home/alexey/Project/Test-py')
        {'exsist': True, 'record': True}
        ```