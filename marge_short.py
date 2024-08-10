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


