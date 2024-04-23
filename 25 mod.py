

# 1

class Avto:
    def init(self, model, rang, korobka, narh, kilometer=0):
        self.model = model
        self.rang = rang
        self.korobka = korobka
        self.narh = narh
        self.kilometer = kilometer

    def get_info(self):
        info = f"Model: {self.model}\nRang: {self.rang}\nKorobka: {self.korobka}\nNarh: {self.narh}\nKilometraj: {self.kilometer} km"
        return info

avto = Avto("Toyota Camry", "Oq", "Avtomatik", 25000)
print(avto.get_info())  # Avtomobilning ma'lumotini chiqaramiz



# 2



class Avto:
    def init(self, model, rang, korobka, narh, kilometer=0):
        self.model = model
        self.rang = rang
        self.korobka = korobka
        self.narh = narh
        self.kilometer = kilometer

    def get_info(self):
        info = f"Model: {self.model}\nRang: {self.rang}\nKorobka: {self.korobka}\nNarh: {self.narh}\nKilometraj: {self.kilometer} km"
        return info

    def update_info(self, model=None, rang=None, korobka=None, narh=None, kilometer=None):
        if model:
            self.model = model
        if rang:
            self.rang = rang
        if korobka:
            self.korobka = korobka
        if narh:
            self.narh = narh
        if kilometer is not None:
            self.kilometer = kilometer

avto = Avto("Toyota Camry", "Oq", "Avtomatik", 25000)
print(avto.get_info())  # Avtomobilning ma'lumotini chiqaramiz

avto.update_info(rang="Qora", korobka="Mexanika")
print(avto.get_info())  # Yangilangan ma'lumotni chiqaramiz

avto.update_info(kilometer=5000)
print(avto.get_info())  # Yangilangan ma'lumotni chiqaramiz


