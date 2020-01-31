string1 = input("Enter String:")    #input string
def string_alternative():
    string2 = " "
    for i in range(len(string1)):
        if(i%2 == 0):               #condition checking even index
            string2 = string2+string1[i]        #appending to string2
    print(string2)
string_alternative()