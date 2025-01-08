def file_read(var: int) -> str:
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
            
usrInput = int(input("Введите способо открытия файла(1, 2): "))

print(file_read(usrInput))