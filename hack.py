from fuzzywuzzy import fuzz
from fuzzywuzzy import process
class eventObj:
    def __init__(self):
        self.name = input('name: ')
        self.typee = input('type: ')
        self.theme = input('theme: ')
        
class vacebularry:
    def __init__(self):
        self.name=[]
        self.typee=[]
        self.theme=[]
        f = open('vac.dat')
        i=0
        for line in f:
            if i==0:
                if line==']\n':
                    i+=1
                else:
                    self.name.append(line)
            elif i==1:
                if line==']\n':
                    i+=1
                else:
                    self.typee.append(line)
                
            elif i==2:
                if line==']\n':
                    i+=1
                else:
                    self.theme.append(line)
        f.close()
    def compairing(self, event):
        res=0
        j=0
        for i in range(len(self.name)):
            if fuzz.partial_ratio(self.name[i], event.name)>j:
                j=fuzz.partial_ratio(self.name[i], event.name)
        print(j)
        res+=j/100
        j=0
        for i in range(len(self.typee)):
            if fuzz.partial_ratio(self.typee[i], event.typee)>j:
                j=fuzz.partial_ratio(self.typee[i], event.typee)
        print(j)
        res+=j/100
        j=0
        for i in range(len(self.theme)):
            if fuzz.partial_ratio(self.theme[i], event.theme)>j:
                j=fuzz.partial_ratio(self.theme[i], event.theme)
        print(j)
        return (res+j/100)/3
    def close(self):
        f = open('vac.dat', 'w')
        for i in range(len(self.name)):
            f.write(self.name[i])
        for i in range(len(self.typee)):
            f.write(self.typee[i])
        for i in range(len(self.theme)):
            f.write(self.theme[i])

try:
    event = eventObj()
    vac = vacebularry()
    print(vac.compairing(event)*100, '%')
except Exception as e:
    raise e
    vac.close()

