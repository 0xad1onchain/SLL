inp = eval(input("Enter the comma seperated values: "))
print ('Original list: ',inp)
even_list = [i for i in inp if i%2 == 0.0]
print ('Even list : ',even_list)
print ('Reversed list : ',even_list[::-1])