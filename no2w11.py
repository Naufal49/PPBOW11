class Model(object):
    services = {
        'email': {'number': 1000, 'price': 2},
        'sms': {'number': 1000, 'price': 10},
        'voice': {'number': 1000, 'price': 15},
    }

class ViewEnglish(object):
    def list_services(self, services):
        print("Services Provided:")
        for svc in services:
            print(svc)

    def list_pricing(self, services):
        print("Pricing for Services:")
        for svc in services:
            print(f"For {Model.services[svc]['number']} {svc} message you pay $ {Model.services[svc]['price']}")

class ViewIndonesia(object):
    def list_services(self, services):
        print("Layanan yang disediakan:")
        for svc in services:
            print(svc)

    def list_pricing(self, services):
        print("Tarif tiap layanan:")
        for svc in services:
            print(f"Untuk setiap {Model.services[svc]['number']} {svc} anda membayar $ {Model.services[svc]['price']}")

class Controller(object):
    def __init__(self):
        self.model = Model()
        self.view = None

        lang = input("What language do you choose? [1]English [2]Indonesia: ")

        if lang == '1':
            self.view = ViewEnglish()
        elif lang == '2':
            self.view = ViewIndonesia()
        else:
            print("Error, choose the language number!")
            return  # Keluar dari konstruktor jika input salah

        self.get_services()
        self.get_pricing()

    def get_services(self):
        services = self.model.services.keys()
        self.view.list_services(services)

    def get_pricing(self):
        services = self.model.services.keys()
        self.view.list_pricing(services)

controller = Controller()

