class Garage :
    garage = []
    def __init__(self, slot):
        self.slot = slot
        
        for index in range(slot):
            i = index + 1
            self.garage.append((i,''))
        print('Created parking lot with {} slots'.format(self.slot))


    def park(self, registration):
        try:
            result =[item for item in self.garage if item[1] == '']
            index = self.garage.index(result[0])
            if len(result) > 0:
                for x,y in self.garage:
                    if x == index+1:
                        self.garage[index] = (x,registration)
                        break
                print('Allocated slot number: {}'.format(index+1))
            else:
                print('Sorry, parking lot is full')
        except:
            if(len(self.garage) > 0):
                print('Sorry, parking lot is full')
            else:
                print('There\'s no parking lot')
        
    
    def leave(self, registration):
        try:
            result =[item for item in self.garage if item[1] == registration]
            index = self.garage.index(result[0])
            k,v = result[0]
            print('Registration number: {} with Slot number {} is free'.format(v,k))
            self.garage[index] = (k,'')
        except:
            print('Registration number {} not found'.format(registration))
            
    def status(self):
        print('Slot No. | Registration No.')
        for slot, car in self.garage:
            if car != '':
                print(str(slot)+ '  ' +car)
            
