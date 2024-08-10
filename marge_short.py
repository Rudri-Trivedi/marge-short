array = []

while True: 
        print('\nadd - adding value.')
        print('q - recive shorted value.')

        user_input= input()

        if user_input == 'add':
            element = input('Entar a value. ')
            array.append(element)
            print(array)

        if user_input == 'q':
             break

def devide(a):
    if len(a) <= 1:
        return a
    
    mid = len(a)//2

    lefta = a[:mid]
    righta = a[mid:]

    devideleft = devide(lefta)
    devideright = devide(righta)


