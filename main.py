import csv
import datetime

class Pizza():
   def __init__(self, cost, description):
       self.cost = cost
       self.description = description

   def get_description(self):
        return self.description

   def get_cost(self):
       return self.cost



class ClasicPizza(Pizza):
    pass;

class MargheritaPizza(Pizza):
    pass;


class TurkPizza(Pizza):
    pass;

class PlainPizza(Pizza):
    pass;



class SaucePizza(Pizza):

    def __init__(self, cost, description, Pizza):
        super().__init__(cost, description)
        self.Pizza = Pizza

    def __call__(self, *args, **kwargs):
        self.Pizza(*args, **kwargs)

    def get_description(self):
        return self.description + ' ' + self.Pizza.get_description()

    def get_cost(self):
        return self.cost + self.Pizza.get_cost()




class OliveSauce(SaucePizza):
    pass


class MushroomSauce(SaucePizza):
    pass


class GoatCheesSauce(SaucePizza):
    pass


class MeatSauce(SaucePizza):
    pass


class OnionSauce(SaucePizza):
    pass


class SweetcornSauce(SaucePizza):
    pass




clasicPizza = ClasicPizza(10,"Leziz Pizza")
margheritaPizza = MargheritaPizza(12,"Çok Leziz Pizza")
turkPizza = TurkPizza(81, "Yerli Pizza")
plainPizza = PlainPizza(13, "Fenasal Leziz Pizza")

enumerateList = []
txtList = []
###
###

def choosePizza(typeOf):
    global typeOfPizza

    if typeOf == 1:
        typeOfPizza = clasicPizza
        return typeOfPizza
    elif typeOf == 2:
        typeOfPizza = margheritaPizza
        return typeOfPizza
    elif typeOf == 3:
        typeOfPizza = turkPizza
        return typeOfPizza
    elif typeOf == 4:
        typeOfPizza = plainPizza
        return typeOfPizza
    else:
        raise ValueError("Lütfen Geçerli Bir Numara Seçin!")

def chooseSouce(typeOf):
    global pizza

    if typeOf == 11:
        pizza = OliveSauce(1, "Leziz Sos",typeOfPizza)
        return pizza
    elif typeOf == 12:
        pizza = MushroomSauce(2, "Çok Leziz Sos",typeOfPizza)
        return  pizza
    elif typeOf == 13:
        pizza = GoatCheesSauce(3, "Ronaldomsu Sos",typeOfPizza)
        return pizza
    elif typeOf == 14:
        pizza = MeatSauce(4, "Baya Leziz Sos",typeOfPizza)
        return pizza
    elif typeOf == 15:
        pizza = OnionSauce(5, "Fenasal Leziz Sos",typeOfPizza)
        return pizza
    elif typeOf == 16:
        pizza = SweetcornSauce(5, "Herhangi Bir Sos",typeOfPizza)
        return pizza
    else:
        raise ValueError("Lütfen Geçerli Bir Numara Seçin!")


def getInformation():
    global price
    global description
    global name
    global id
    global creditCardNumber
    global creditCardPassword
    global hour

    typeOfPizza = int(input("Lütfen İstediğiniz Pizza Numarasını Seçiniz!:"))
    typeOfSauce = int(input("Lütfen İstediğiniz Sos Numarasını Seçiniz!:"))
    choosePizza(typeOfPizza)
    chooseSouce(typeOfSauce)
    price = pizza.get_cost()
    description = pizza.get_description()
    name = str(input("Lütfen isminizi giriniz:"))
    id = int(input("Lütfen TC kimlik numaranızı giriniz:"))
    creditCardNumber = int(input("Lütfen kredi kartı numaranızı giriniz:"))
    creditCardPassword = int(input("Lütfen kredi kartı şifrenizi numaranızı giriniz:"))

    now = datetime.datetime.now()
    # Zaman formatını belirle
    time_format = '%H:%M:%S'
    # Saat bilgisini al ve yazdır
    hour = now.strftime(time_format)

def writeToCsv():
    with open('Orders_Database.csv', mode='a', newline='') as file:
        # CSV dosyasına yazmak için bir yazar nesnesi oluşturun
        writer = csv.writer(file)
        # Verileri yazın
        writer.writerow([f'{name}, {id}, {creditCardNumber}, {description}, {hour}, {creditCardPassword}'])


class main():
    with open(r"Menu.txt", "r", encoding="UTF-8") as f:
        readList = f.readlines()

    with open('Orders_Database.csv', mode='w', newline='') as file:
        # CSV dosyasına yazmak için bir yazar nesnesi oluşturun
        writer = csv.writer(file)

        writer.writerow(['Ad', 'Tc Kimlik', 'Kredi Kartı Numarası', 'Sipariş Açıklaması', 'Sipariş Zamanı', 'Kredi Kartı Şifresi'])

    for line in readList:
        print(line,end="")

    print("\n")

    flag = True

    while(flag):
        getInformation()
        writeToCsv()
        question = str(input("Başka Bir Sipariş Verecek Misiniz?(evet/hayır):"))
        question = question.lower()
        print(question)
        if question == "evet":
            pass
        else:
            flag = False




