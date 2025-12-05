import tkinter as tk
from tkinter import messagebox


class SimpleTaskShop:
    def __init__(self):
        self.products = [
            {"id": "1", "name": "Plantilla Excel", "price": 9.99},
            {"id": "2", "name": "Curso Python", "price": 29.99},
            {"id": "3", "name": "Recarga Premium", "price": 5.00},
        ]
        self.cart = []

        self.window = tk.Tk()
        self.window.title("TaskShop - Tienda Simple")
        self.window.geometry("500x400")
        self.setup_ui()

    def setup_ui(self):
        title = tk.Label(self.window, text="🛒 TASK SHOP", font=("Arial", 20))
        title.pack(pady=10)

        tk.Label(self.window, text="Productos Disponibles:", font=("Arial", 12)).pack()

        self.products_listbox = tk.Listbox(self.window, width=50, height=6)
        for product in self.products:
            self.products_listbox.insert(
                tk.END, f"{product['name']} - ${product['price']}"
            )
        self.products_listbox.pack(pady=5)

        buttons_frame = tk.Frame(self.window)
        buttons_frame.pack(pady=10)

        tk.Button(
            buttons_frame,
            text="Agregar al Carrito",
            command=self.add_to_cart,
            bg="lightblue",
        ).pack(side=tk.LEFT, padx=5)
        tk.Button(
            buttons_frame, text="Ver Carrito", command=self.show_cart, bg="lightgreen"
        ).pack(side=tk.LEFT, padx=5)
        tk.Button(
            buttons_frame, text="Comprar", command=self.checkout, bg="orange"
        ).pack(side=tk.LEFT, padx=5)
        tk.Button(
            buttons_frame, text="Salir", command=self.window.quit, bg="red", fg="white"
        ).pack(side=tk.LEFT, padx=5)

        self.status_label = tk.Label(
            self.window, text="Carrito vacío", font=("Arial", 10)
        )
        self.status_label.pack(pady=10)

    def add_to_cart(self):
        try:
            index = self.products_listbox.curselection()[0]
            product = self.products[index]
            self.cart.append(product)
            self.status_label.config(
                text=f"✅ {product['name']} agregado. Carrito: {len(self.cart)} items"
            )
        except IndexError:
            messagebox.showwarning("Selecciona", "Por favor, selecciona un producto")

    def show_cart(self):
        if not self.cart:
            messagebox.showinfo("Carrito", "Tu carrito está vacío")
            return

        cart_window = tk.Toplevel(self.window)
        cart_window.title("Tu Carrito")
        cart_window.geometry("400x300")

        tk.Label(cart_window, text="🛍️ Tu Carrito", font=("Arial", 14)).pack(pady=10)

        total = 0
        for i, item in enumerate(self.cart, 1):
            tk.Label(cart_window, text=f"{i}. {item['name']} - ${item['price']}").pack()
            total += item["price"]

        tk.Label(
            cart_window,
            text=f"Total: ${total:.2f}",
            font=("Arial", 12, "bold"),
            fg="green",
        ).pack(pady=10)

    def checkout(self):
        if not self.cart:
            messagebox.showwarning(
                "Carrito vacío", "Agrega productos al carrito primero"
            )
            return

        total = sum(item["price"] for item in self.cart)
        response = messagebox.askyesno(
            "Confirmar Compra", f"Total: ${total:.2f}\n\n¿Confirmar compra?"
        )

        if response:
            messagebox.showinfo(
                "¡Compra Exitosa!", f"✅ Compra realizada por ${total:.2f}\nGracias!"
            )
            self.cart = []
            self.status_label.config(text="✅ Compra completada. Carrito vacío")

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = SimpleTaskShop()
    app.run()
