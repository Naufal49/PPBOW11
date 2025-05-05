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
    
        def show_bid_update(self):
            print("Price according to your bid:")
    
    class Controller(object):
        def __init__(self):
            self.model = Model()
            self.view = ViewEnglish()
    
            self.get_services()
            self.get_pricing()
            self.bid_price()  
    
        def get_services(self):
            services = self.model.services.keys()
            self.view.list_services(services)
    
        def get_pricing(self):
            services = self.model.services.keys()
            self.view.list_pricing(services)
    
        def bid_price(self):
            service = input("What service do you want to bid? email, sms, or voice : ").lower()
            if service not in self.model.services:
                print("Invalid service!")
                return
    
            try:
                price = float(input("Enter the price you want (in $): "))
            except ValueError:
                print("Invalid price input!")
                return
    
            self.model.services[service]['price'] = price
    
            self.view.show_bid_update()
            self.get_pricing()
    
    controller = Controller()
