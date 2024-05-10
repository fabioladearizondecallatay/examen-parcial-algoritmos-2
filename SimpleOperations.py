import functools

class SimpleOperations:
    def apply_discount(self, price, discount):
        """Aplica un descuento al precio dado y retorna el nuevo precio."""
        discounted_price = price - (price * discount)
        return discounted_price

    def calculate_tax(self, price, tax_rate):
        """Calcula y agrega el impuesto al precio dado."""
        price_with_tax = price * (1 + tax_rate)
        return price_with_tax

# Crear una instancia de SimpleOperations
operations = SimpleOperations()

#solicita al usuario que ingrese un precio 
price = float(input("Ingrese el precio base: "))
discount_rate = float(input("Ingrese el porcentaje de descuento (como decimal): "))
tax_rate = float(input("Ingrese el porcentaje de impuesto (como decimal): "))


# Configurar funciones con descuentos y tasas de impuestos predefinidos utilizando functools.partial.
# twenty_percent_discount 
# vat_tax
twenty_percent_discount = functools.partial(operations.apply_discount, discount=discount_rate)
vat_tax = functools.partial(operations.calculate_tax, tax_rate=tax_rate)


final_price_with_discount = twenty_percent_discount(price)
final_price_with_tax = vat_tax(price)

print("Precio final con descuento:", final_price_with_discount)
print("Precio final con impuesto:", final_price_with_tax)