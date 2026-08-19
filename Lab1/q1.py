def capitalize(input_string):
    result = ""
    pre = " "
    for i in input_string:
        if pre == " " and i != " ":
            result = result + i.upper()
        else:
            result = result + i
        pre = i
    if result[-1]!= ".":
        result += "."
    return result
def main():
    t = input("Enter a sentence: ")
    print(capitalize(t))
    
if __name__ == "__main__":
    main()
