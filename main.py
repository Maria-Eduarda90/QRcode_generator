from tkinter import *
import qrcode
from tkinter import messagebox, Tk, Label, Entry, Button

def generator_qr_code():
    url = website_entry.get()

    if len(url) == 0:
        messagebox.showinfo(
            title="Erro!",
            message="Favor insira uma URL válida"
        )
    else:
        opcao_escolhida = messagebox.askokcancel(
            title=url,
            message=f"O endereço URL é: \n"
                    f"Endereço: {url} \n"
                    f"Pronto para salvar?")
        
        if opcao_escolhida:
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(url)
            qr.make(fit=True)
            img = qr.make_image(fill_color='black', back_color='white')
            img.save('qrcode.png')

if __name__ == '__main__':
    window = Tk()
    window.title("Gerador de Código QRCode")
    window.config(padx=10, pady=100)

    website_label = Label(text="Digite uma URL", font=("Arial", 12))
    website_label.grid(row=0, column=0, columnspan=2)

    website_entry = Entry(width=35, font=("Arial", 12), bd=2, relief="groove")
    website_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
    website_entry.focus()
    
    add_button = Button(
        text="Gerar QR Code", 
        bg="black", fg="white", 
        font=("Arial", 10, "bold"),
        width=36, 
        command=generator_qr_code)
    add_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    window.mainloop()