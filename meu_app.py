import customtkinter as ctk
from tkinter import filedialog
from rembg import remove
import os

# Configuração visual (O estilo All Black que você curte)
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("RemoveBG Tunado v1.0")
        self.geometry("400x250")

        self.label = ctk.CTkLabel(self, text="Selecione a pasta com as fotos", font=("Roboto", 16))
        self.label.pack(pady=20)

        self.btn_select = ctk.CTkButton(self, text="Escolher Pasta", command=self.processar)
        self.btn_select.pack(pady=10)

        self.status_label = ctk.CTkLabel(self, text="Status: Aguardando...", text_color="gray")
        self.status_label.pack(pady=20)

    def processar(self):
        pasta_origem = filedialog.askdirectory()
        if pasta_origem:
            pasta_destino = os.path.join(pasta_origem, "sem_fundo")
            if not os.path.exists(pasta_destino):
                os.makedirs(pasta_destino)
            
            self.status_label.configure(text="Processando... Olhe o CMD!", text_color="yellow")
            self.update()

            for arquivo in os.listdir(pasta_origem):
                if arquivo.lower().endswith(('.png', '.jpg', '.jpeg')):
                    with open(os.path.join(pasta_origem, arquivo), 'rb') as i:
                        input_data = i.read()
                        output_data = remove(input_data)
                        with open(os.path.join(pasta_destino, f"sem_{arquivo}.png"), 'wb') as o:
                            o.write(output_data)
            
            self.status_label.configure(text="✅ Concluído! Pasta 'sem_fundo' criada.", text_color="green")

if __name__ == "__main__":
    app = App()
    app.mainloop()