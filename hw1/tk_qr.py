import qrcode
import pack
from customtkinter import *
from tkinter import *
from PIL import ImageTk


# по дефолту светлая тема
def main():
    current_theme = "light"

    # осуществление функционала кнопки для смены темы
    def theme_button_calllback():
        nonlocal current_theme
        new = pack.theme(current_theme)
        set_appearance_mode(new)
        current_theme = new

    # генерация и вывод кью ар кода
    def generate_qr():
        nonlocal current_theme  # получаем текущую тему
        back_color, fill_color = pack.generate_qr_theme(current_theme)

        link = entry.get()  # получаем введенный текст
        qr = qrcode.QRCode(version=15, box_size=10, border=5)
        qr.add_data(link)
        qr.make(fit=True)
        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        img = img.resize((300, 300))  # меняю размер чтобы красиво было
        img = ImageTk.PhotoImage(img)  # преобразуем в удобный формат
        label = CTkLabel(app, image=img, text="")
        label.place(relx=0.6, rely=0.25)  # постим на экран

        text = CTkLabel(master=app, text=link, text_color="grey")
        text.place(relx=0.6, rely=0.20)  # выводим текст над кью ар кодом

    # функционал кнобки эбаут
    def about_button_calllback():
        about_window = CTk()  # создаем второе окно
        about_window.geometry("600x300")
        info = CTkLabel(
            master=about_window,
            text=pack.text_about,
            font=("Arial", 12),
            fg_color="goldenrod1",
            anchor="center",
            text_color="black",
            corner_radius=6
        )
        info.place(relx=0.1, rely=0.1)
        about_window.mainloop()

    # создаем главное окно
    app = CTk()
    app.title("QR-Maker")
    set_appearance_mode("light")
    app.geometry("920x620")

    # делаем фрейм для удобного расположения элементов
    frame = CTkFrame(master=app)
    frame.place(relx=0, rely=0.1, relwidth=0.5, relheight=0.7)

    # это тот огромный текст по середине
    welcome_text = CTkLabel(
        master=frame,
        text="_put link below_",
        font=("Arial", 45, "bold"),
        fg_color=f"goldenrod1",
        text_color="black",
        anchor="center",
        corner_radius=6
    )
    welcome_text.place(relx=0.1, rely=0.3)

    # полее ввода для ссылки
    entry = CTkEntry(master=frame, width=300, height=30,
                     border_color="black",
                     placeholder_text="https://www.youtube.com/")  # текст заглушка, который видно по дефолту
    entry.place(relx=0.47, rely=0.6, anchor="center")

    # кнопка генерации кода
    button_gen = CTkButton(master=frame)
    button_gen.configure(fg_color="goldenrod1",
                         text="Generate QR code",
                         text_color="black",
                         hover_color="goldenrod2",
                         width=50,
                         height=30,
                         corner_radius=6,
                         border_width=1,
                         border_color="grey29",
                         command=generate_qr)
    button_gen.place(relx=0.47, rely=0.7, anchor="center")

    # кнопка эбаут
    button_about = CTkButton(master=app)
    button_about.configure(fg_color="goldenrod1",
                           text="About",
                           text_color="black",
                           hover_color="goldenrod2",
                           width=50,
                           height=30,
                           corner_radius=6,
                           border_width=1,
                           border_color="grey29",
                           command=about_button_calllback)
    button_about.pack(side='left', anchor='nw', padx=10, pady=10)

    # кнопка темы
    button_theme = CTkButton(master=app)
    button_theme.configure(fg_color="goldenrod1",
                           text="Theme",
                           text_color="black",
                           hover_color="goldenrod2",
                           width=50,
                           height=30,
                           corner_radius=6,
                           border_width=1,
                           border_color="grey29",
                           command=theme_button_calllback)
    button_theme.pack(side='right', anchor='nw', padx=10, pady=10)

    # мини текст снизу страницы
    author = CTkLabel(
        master=app,
        text="_by nik1t7n_",
        font=("Arial", 12),
        fg_color="transparent",
        anchor="center",
        text_color="grey"
    )
    author.place(relx=0.5, rely=0.95)

    app.mainloop()


if __name__ == "__main__":
    main()
