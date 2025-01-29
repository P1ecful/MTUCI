def file_read(var: int) -> str:
  try:
    match var:
        case 1:
            with open ("example.txt") as example:
                content = example.read()
                return content
    
        case 2:
            result = ""
            
            with open ("example.txt") as example:
                for line in example:
                    result += line
                    
                return result

  except FileNotFoundError:
    print("Такого файла не существует")

usrInput = int(input("Введите способо открытия файла(1, 2): "))
print(file_read(usrInput)) if usrInput == 1 or usrInput == 2 else print("Выбран ошибочный метод")
    
