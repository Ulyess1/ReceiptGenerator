import datetime
from typing import List, Dict

class ReceiptGenerator:
    def __init__(self):
        self.items = []
        self.business_info = {}
        self.customer_info = {}
        
    def set_business_info(self, name: str, address: str = "", phone: str = ""):
        """Set business information for the receipt header"""
        self.business_info = {
            'name': name,
            'address': address,
            'phone': phone
        }
    
    def set_customer_info(self, name: str = "", email: str = ""):
        """Set customer information (optional)"""
        self.customer_info = {
            'name': name,
            'email': email
        }
    
    def add_item(self, name: str, quantity: int, price: float):
        """Add an item to the receipt"""
        item = {
            'name': name,
            'quantity': quantity,
            'price': price,
            'total': quantity * price
        }
        self.items.append(item)
    
    def calculate_subtotal(self) -> float:
        """Calculate subtotal of all items"""
        return sum(item['total'] for item in self.items)
    
    def calculate_tax(self, tax_rate: float = 0.08) -> float:
        """Calculate tax amount"""
        return self.calculate_subtotal() * tax_rate
    
    def calculate_total(self, tax_rate: float = 0.08) -> float:
        """Calculate final total including tax"""
        return self.calculate_subtotal() + self.calculate_tax(tax_rate)
    
    def generate_receipt(self, tax_rate: float = 0.08) -> str:
        """Generate formatted receipt string"""
        receipt_width = 50
        receipt = []
        
        receipt.append("=" * receipt_width)
        if self.business_info.get('name'):
            receipt.append(f"{self.business_info['name']:^{receipt_width}}")
        if self.business_info.get('address'):
            receipt.append(f"{self.business_info['address']:^{receipt_width}}")
        if self.business_info.get('phone'):
            receipt.append(f"{self.business_info['phone']:^{receipt_width}}")
        receipt.append("=" * receipt_width)
        
        now = datetime.datetime.now()
        receipt.append(f"Date: {now.strftime('%Y-%m-%d %H:%M:%S')}")
        receipt.append("")
        
        if self.customer_info.get('name'):
            receipt.append(f"Customer: {self.customer_info['name']}")
        if self.customer_info.get('email'):
            receipt.append(f"Email: {self.customer_info['email']}")
        if self.customer_info.get('name') or self.customer_info.get('email'):
            receipt.append("")
        
        receipt.append(f"{'Item':<20} {'Qty':>5} {'Price':>8} {'Total':>10}")
        receipt.append("-" * receipt_width)
        
        for item in self.items:
            name = item['name'][:20]  # Truncate if too long
            receipt.append(f"{name:<20} {item['quantity']:>5} ${item['price']:>7.2f} ${item['total']:>9.2f}")
        
        receipt.append("-" * receipt_width)
        
        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax(tax_rate)
        total = self.calculate_total(tax_rate)
        
        receipt.append(f"{'Subtotal:':<30} ${subtotal:>9.2f}")
        receipt.append(f"{'Tax (' + str(int(tax_rate * 100)) + '%):':.<30} ${tax:>9.2f}")
        receipt.append("=" * receipt_width)
        receipt.append(f"{'TOTAL:':<30} ${total:>9.2f}")
        receipt.append("=" * receipt_width)
        receipt.append("")
        receipt.append("Thank you for your business!".center(receipt_width))
        receipt.append("=" * receipt_width)
        
        return "\n".join(receipt)
    
    def save_receipt(self, filename: str = None, tax_rate: float = 0.08):
        """Save receipt to a text file"""
        if filename is None:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"receipt_{timestamp}.txt"
        
        with open(filename, 'w') as f:
            f.write(self.generate_receipt(tax_rate))
        
        print(f"Receipt saved to {filename}")
    
    def clear_receipt(self):
        """Clear all items and start a new receipt"""
        self.items = []
        self.customer_info = {}

def main():
    """Interactive receipt generator"""
    generator = ReceiptGenerator()
    
    print("=== Receipt Generator ===\n")
    
    business_name = input("Enter business name: ").strip()
    business_address = input("Enter business address (optional): ").strip()
    business_phone = input("Enter business phone (optional): ").strip()
    generator.set_business_info(business_name, business_address, business_phone)
    
    customer_name = input("Enter customer name (optional): ").strip()
    customer_email = input("Enter customer email (optional): ").strip()
    if customer_name or customer_email:
        generator.set_customer_info(customer_name, customer_email)
    
    print("\n--- Add Items ---")
    while True:
        item_name = input("Enter item name (or 'done' to finish): ").strip()
        if item_name.lower() == 'done':
            break
        
        try:
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price per item: $"))
            generator.add_item(item_name, quantity, price)
            print(f"Added: {quantity}x {item_name} @ ${price:.2f} each\n")
        except ValueError:
            print("Please enter valid numbers for quantity and price.\n")
    
    try:
        tax_rate = float(input("Enter tax rate (e.g., 0.08 for 8%, default 8%): ") or "0.08")
    except ValueError:
        tax_rate = 0.08
    
    print("\n" + "="*50)
    print("GENERATED RECEIPT:")
    print("="*50)
    print(generator.generate_receipt(tax_rate))
    
    save = input("\nSave receipt to file? (y/n): ").strip().lower()
    if save == 'y':
        filename = input("Enter filename (or press Enter for auto-generated name): ").strip()
        generator.save_receipt(filename if filename else None, tax_rate)

if __name__ == "__main__":
    main()