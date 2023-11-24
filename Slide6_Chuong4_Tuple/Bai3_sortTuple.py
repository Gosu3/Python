my_tuple = (('Tom', '19', '80'), ('John', '17','91'), 
            ('John', '20', '90'),('Jony','17', '93'),
            ('Json', '21', '90'))

a = sorted(tuple, key=lambda tup:(tup[0],tup[1],tup[2]))
print(a)