import customtkinter as ctk

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

class CalculatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Calculator")
        self.geometry("320x420")
        self.resizable(False, False)
        self.expression = ""

        self.entry = ctk.CTkEntry(
            self, font=("Segoe UI", 24), justify="right",
            corner_radius=10, height=60
        )
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")

        self.btn_7 = self.create_button("7", 1, 0)
        self.btn_8 = self.create_button("8", 1, 1)
        self.btn_9 = self.create_button("9", 1, 2)
        self.btn_div = self.create_button("/", 1, 3)

        self.btn_4 = self.create_button("4", 2, 0)
        self.btn_5 = self.create_button("5", 2, 1)
        self.btn_6 = self.create_button("6", 2, 2)
        self.btn_mul = self.create_button("*", 2, 3)

        self.btn_1 = self.create_button("1", 3, 0)
        self.btn_2 = self.create_button("2", 3, 1)
        self.btn_3 = self.create_button("3", 3, 2)
        self.btn_sub = self.create_button("-", 3, 3)

        self.btn_0 = self.create_button("0", 4, 0)
        self.btn_dot = self.create_button(".", 4, 1)
        self.btn_eq = self.create_button("=", 4, 2)
        self.btn_add = self.create_button("+", 4, 3)

        self.btn_clear = ctk.CTkButton(
            self, text="C", font=("Segoe UI", 18),
            width=60, height=60, corner_radius=15,
            fg_color="#d9d9d9", text_color="black", hover_color="#c0c0c0",
            command=lambda: self.on_click("C")
        )
        self.btn_clear.grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)

    def create_button(self, char, row, col):
        btn = ctk.CTkButton(
            self, text=char, font=("Segoe UI", 18),
            width=60, height=60, corner_radius=15,
            fg_color="#d9d9d9", text_color="black", hover_color="#c0c0c0",
            command=lambda: self.on_click(char)
        )
        btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
        return btn

    def on_click(self, char):
        if char == "C":
            self.expression = ""
        elif char == "=":
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "Error"
        else:
            self.expression += str(char)

        self.entry.delete(0, "end")
        self.entry.insert(0, self.expression)


if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()
