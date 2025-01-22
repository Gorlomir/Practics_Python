import tkinter as tk
from tkinter import filedialog, messagebox


class TextEditor:
    def __init__(self, master):
        self.master = master
        master.title("Блокнот")
        master.geometry('800x600')

        # Создание текстового поля
        self.text_area = tk.Text(master, wrap='word', font=('Times New Roman', 12))
        self.text_area.pack(fill=tk.BOTH, expand=True)

        # Создание панели инструментов
        toolbar = tk.Frame(master, height=50)
        toolbar.pack(fill=tk.X)

        # Кнопка New
        tk.Button(toolbar, text="New", command=self.new_file).pack(side=tk.LEFT)

        # Кнопка Open
        tk.Button(toolbar, text="Open", command=self.open_file).pack(side=tk.LEFT)

        # Кнопка Save
        tk.Button(toolbar, text="Save", command=self.save_file).pack(side=tk.LEFT)

        # Кнопка Help
        tk.Button(toolbar, text="Help", command=self.show_help).pack(side=tk.LEFT)

        # Кнопка About
        tk.Button(toolbar, text="About", command=self.show_about).pack(side=tk.LEFT)

    def new_file(self):
        self.text_area.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(title="Выберите файл",
                                               filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, file.read())

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt")],
                                                 title="Сохранить как")
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.text_area.get(1.0, tk.END))

    def show_help(self):
        messagebox.showinfo("Помощь", "Эта программа - простой блокнот с функциями:\n"
                                      "- Создание нового файла\n"
                                      "- Открытие существующего текстового файла\n"
                                      "- Сохранение изменений в файле\n"
                                      "- Просмотр информации о программе")

    def show_about(self):
        messagebox.showinfo("О программе", "Блокнот\n"
                                           "Версия: 0.1\n"
                                           "Разработчик: Gorlomir")


root = tk.Tk()
app = TextEditor(root)
root.mainloop()