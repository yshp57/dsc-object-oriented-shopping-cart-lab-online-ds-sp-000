class ShoppingCart:
    # write your code here
    
    def __init__(self, total=0, emp_discount=None, items=[]):
        self.total = total
        self.employee_discount = emp_discount
        self.items = items
        
    def add_item(self, name, price, quantity=1):
        self.total += (price*quantity)
        self.items.append({'n': name, 'p': price, 'q':quantity})
        return self.total
        
    def mean_item_price(self):
        totalprice = 0
        totalitems = 0
        for item in self.items:
            totalprice += (item['p']*item['q'])
            totalitems += item['q']
        return totalprice/totalitems

    def median_item_price(self):
        prices = []
        for item in self.items:
            amount = 0
            while amount != item['q']:
                prices.append(item['p'])
                amount +=1
        prices = sorted(prices)
        if len(prices)%2 == 1:
            return prices[int((len(prices)-1)/2)]
        else:
            return (prices[int((len(prices)/2)-1)]+prices[int(len(prices)/2)])/2

    def apply_discount(self):
        if self.employee_discount:
            total = self.total*(100 - self.employee_discount) *.01
            return total
        else:
            return "Sorry, there is no discount to apply to your cart :("

    def void_last_item(self):
        self.items = self.items.pop(-1)