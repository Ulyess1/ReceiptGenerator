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