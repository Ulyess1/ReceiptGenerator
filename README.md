# 🧾 Receipt Generator

A clean and simple Python-based tool to generate professional receipts for small businesses, shops, and service providers — no extra libraries required.

---

## ✅ Features

- Professional, clean receipt formatting  
- Business and customer info input via terminal  
- Add multiple items with quantity and price  
- Auto subtotal, tax, and total calculation  
- Custom tax rates supported  
- Save receipts as `.txt` files  
- Interactive CLI mode + Python API available  

---
💱 Currency Support

This receipt generator supports over 30 international currencies with automatic formatting.

🔧 How to Change Currency

Open the script and look for the main() function. Then, change the currency code like this:

def main():
    CURRENCY = "EUR"  # Change this to your desired currency


✅ Popular Options

Currency         Code    Example
---------------- ------- -------------
US Dollar        USD     $10.99
Euro             EUR     €10.99
British Pound    GBP     £10.99
Japanese Yen     JPY     ¥1000
Indian Rupee     INR     ₹599.00
Canadian Dollar  CAD     C$20.00
Moroccan Dirham  MAD     MAD 150.00
Swedish Krona    SEK     99.00 kr

✅ Some currencies use symbols before the amount ($10.00),
others after (99.00 kr) — formatting is handled automatically.

➕ Add Your Own Currency

If your currency isn't listed, just open the script and add it
to the currency_symbols dictionary:

self.currency_symbols = {
    # ... existing entries ...
    'XYZ': '¤',  # Add your code and symbol here
}

## 💻 Getting Started

### Requirements
- Python 3.6 or higher  
- No dependencies (uses only the standard library)

### Run in Terminal

```bash
python receipt_generator.py
Follow the prompts to:

Enter business information

(Optionally) add customer details

Add items (name, quantity, price)

Set a tax rate

Generate and save the receipt
You can also use this as a Python module:

from receipt_generator import ReceiptGenerator

receipt = ReceiptGenerator()

receipt.set_business_info(name="Your Business Name")
receipt.set_customer_info(name="Customer Name")
receipt.add_item("Item Name", quantity=1, price=9.99)

receipt.generate_receipt(tax_rate=0.08)
receipt.save_receipt("receipt.txt")


Note: All values can be entered via terminal using the interactive mode.