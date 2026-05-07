"""
In this workshop, you are going to build a discount calculator that can apply different discount strategies to products.
The system will determine the best price for a customer based on multiple discount
"""

class DiscountStrategy:
    """Base class for discount strategies."""
    def apply_discount(self, price):
        raise NotImplementedError("Subclasses must implement this method")  
    
class PercentageDiscount(DiscountStrategy):
    """Applies a percentage discount to the price."""
    def __init__(self, percentage):
        self.percentage = percentage

    def apply_discount(self, price):
        return price * (1 - self.percentage / 100)
    
class FixedAmountDiscount(DiscountStrategy):
    """Applies a fixed amount discount to the price."""
    def __init__(self, amount):
        self.amount = amount

    def apply_discount(self, price):
        return max(0, price - self.amount)  
    
    
class Product:
    """Represents a product with a name and price."""
    def __init__(self, name, price):
        self.name = name
        self.price = price  
        
        
        
class DiscountCalculator:
    """Calculates the best price for a product based on multiple discount strategies."""
    def __init__(self, product):
        self.product = product
        self.discounts = []

    def add_discount(self, discount):
        if not isinstance(discount, DiscountStrategy):
            raise ValueError("Discount must be an instance of DiscountStrategy")
        self.discounts.append(discount)

    def calculate_best_price(self):
        best_price = self.product.price
        for discount in self.discounts:
            discounted_price = discount.apply_discount(self.product.price)
            best_price = min(best_price, discounted_price)
        return best_price               
    
    
# Example usage
if __name__ == "__main__":  
    product = Product("Laptop", 1000)
    calculator = DiscountCalculator(product)
    
    calculator.add_discount(PercentageDiscount(10))  # 10% off
    calculator.add_discount(FixedAmountDiscount(150))  # $150 off
    
    best_price = calculator.calculate_best_price()
    print(f"The best price for {product.name} is: ${best_price:.2f}")   