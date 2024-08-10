array = []
while True: 
        print('\nadd - adding value.')
        print('q - recive shorted value.')

        user_input= input()

        if user_input == 'add':
            element = input('Entar a value. ')
            array.append(int(element))
            print(array)

        if user_input == 'q':
             break

def devide(array):
    if len(array) <= 1:
        return array
    
    mid = len(array)//2

    lefta = array[:mid]
    righta = array[mid:]

    devide_left = devide(lefta)
    devide_right = devide(righta)

    return marge_short(devide_left,devide_right)

def marge_short(leftarray,rightarray):
     result = []

     i , j = 0 , 0
     while i < len(leftarray) and j < len(rightarray):
          if leftarray[i] < rightarray[j]:
               result.append(leftarray[i])
               i += 1

          else:
               result.append(rightarray[j])
               j += 1

     result.extend(leftarray[i:])
     result.extend(rightarray[j:])

     return result

shorted_array = devide(array)
print(shorted_array)
