import customtkinter as ctk  # Mengimpor library customtkinter untuk GUI
import mysql.connector  # Mengimpor library mysql.connector untuk koneksi database MySQL

class CalculatorApp:
    def __init__(self, root):
        self.root = root  # Menyimpan referensi ke window utama
        self.root.title('Kalkulator LSP UNS')  # Menetapkan judul window
        self.root.geometry('400x450')  # Menetapkan ukuran window
        self.root.resizable(False, False)  # Menonaktifkan perubahan ukuran window

        ctk.set_appearance_mode('dark')  # Mengatur mode tampilan gelap untuk customtkinter

        # Setup database connection
        self.db = mysql.connector.connect(
            host="localhost",  # Host database
            user="root",  # Nama pengguna database
            password="",  # Kata sandi database
            database="calculator_db"  # Nama database
        )
        self.cursor = self.db.cursor()  # Membuat objek cursor untuk eksekusi query

        # Create table if not exists
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS riwayat (
                id INT AUTO_INCREMENT PRIMARY KEY,  # Kolom ID sebagai primary key
                expression VARCHAR(255),  # Kolom untuk menyimpan expression kalkulasi
                result VARCHAR(255)  # Kolom untuk menyimpan hasil kalkulasi
            )
        """)

        self.histories = self.fetch_riwayat()  # Mengambil riwayat dari database
        self.expression = ''  # Inisialisasi string expression

        # UI setup
        self.setup_ui()  # Menyiapkan ui pengguna

    def fetch_riwayat(self):
        self.cursor.execute("SELECT expression, result FROM riwayat ORDER BY id DESC")  # Mengambil data riwayat dari database
        return self.cursor.fetchall()  # Mengembalikan hasil sebagai daftar tuple

    def insert_riwayat(self, expression, result):
        self.cursor.execute("INSERT INTO riwayat (expression, result) VALUES (%s, %s)", (expression, result))  # Menyimpan riwayat ke database
        self.db.commit()  # Menyimpan perubahan ke database

    def delete_all_riwayat(self):
        self.cursor.execute("DELETE FROM riwayat")  # Menghapus semua entri riwayat dari database
        self.db.commit()  # Menyimpan perubahan ke database
        self.histories = []  # Mengosongkan daftar riwayat
        self.update_riwayat_expression('')  # Memperbarui tampilan expression riwayat
        self.update_expression('')  # Memperbarui tampilan expression kalkulasi

    def update_expression(self, new_expression):
        self.expression_label.configure(text=new_expression)  # Memperbarui label expression dengan expression baru
        self.expression = new_expression  # Menyimpan expression baru

    def update_riwayat_expression(self, new_riwayat_expression):
        self.riwayat_expression_label.configure(text=new_riwayat_expression)  # Memperbarui label expression riwayat dengan teks baru

    def calculate_expression(self, expression):
        try:
            # Mengganti '%' dengan '/100' dan menangani operasi yang melibatkan '%'
            if '%' in expression:
                expression = expression.replace('%', '/100')

            # Hitung hasil expression
            result = str(eval(expression.replace('x', '*')))
            if result.endswith('.0'):  # Hapus '.0' dari hasil jika ada
                result = result[:-2]
            self.update_expression(result)  # Perbarui tampilan expression dengan hasil
            self.update_riwayat_expression(expression)  # Perbarui tampilan expression riwayat
            self.histories.insert(0, (expression, result))  # Tambahkan expression dan hasil baru ke daftar riwayat
            self.insert_riwayat(expression, result)  # Simpan expression dan hasil ke database
        except Exception as e:
            print(e)  # Cetak kesalahan jika terjadi

    def button_action(self, button_value):
        if button_value == 'AC':
            if self.expression == '':
                self.delete_all_riwayat()  # Menghapus semua riwayat jika expression kosong dan tombol 'AC' ditekan
            self.expression = ''  # Mengosongkan expression
            self.update_expression(self.expression)  # Memperbarui tampilan expression
        elif button_value == '<':
            self.expression = self.expression[:-1]  # Menghapus karakter terakhir dari expression
            self.update_expression(self.expression)  # Memperbarui tampilan expression
        elif button_value == '=':
            self.calculate_expression(self.expression)  # Menghitung hasil expression jika tombol '=' ditekan
        else:
            self.expression += button_value  # Menambahkan nilai tombol ke expression
            self.update_expression(self.expression)  # Memperbarui tampilan expression

    def show_riwayat(self):
        riwayat_window = ctk.CTkToplevel(self.root)  # Membuat window baru untuk menampilkan riwayat
        riwayat_window.title('Riwayat')  # Menetapkan judul window
        riwayat_window.geometry('300x400')  # Menetapkan ukuran window
        riwayat_window.resizable(False, False)  # Menonaktifkan perubahan ukuran window

        main_frame = ctk.CTkScrollableFrame(riwayat_window, bg_color='#676767', fg_color='#676767')  # Frame scrollable untuk riwayat
        main_frame.pack(expand=True, fill='both')  # Memastikan frame dapat mengisi ruang yang tersedia
        main_frame.grid_columnconfigure(0, weight=1)  # Mengatur kolom frame untuk menyesuaikan ukuran

        def button_action(x):
            self.update_expression(x)  # Memperbarui expression dengan nilai yang dipilih dari riwayat
            riwayat_window.destroy()  # Menutup window riwayat

        for i, (expr, result) in enumerate(self.histories):  # Membuat tombol untuk setiap entri riwayat
            expr_label = ctk.CTkButton(main_frame, text=f'{expr} = ', width=0, font=('Arial', 12, 'bold'), command=lambda x=expr: button_action(x), fg_color='#4b4b4b', text_color='#ffffff')
            expr_label.grid(row=i, column=0, pady=2, sticky='e')  # Menempatkan label expression pada frame
            result_button = ctk.CTkButton(main_frame, text=result, width=0, font=('Arial', 12, 'bold'), command=lambda x=result: button_action(x), fg_color='#4b4b4b', text_color='#ffffff')
            result_button.grid(row=i, column=1, padx=(0, 5), pady=2, sticky='w')  # Menempatkan tombol hasil pada frame
        
        riwayat_window.transient(self.root)  # Menjadikan window riwayat sebagai window anak
        riwayat_window.grab_set()  # Mengambil kontrol input dari window utama
        riwayat_window.focus()  # Memastikan window riwayat mendapatkan fokus
        self.root.wait_window(riwayat_window)  # Menunggu hingga window riwayat ditutup

    def setup_ui(self):
        container_frame = ctk.CTkFrame(self.root, bg_color='#3b3b3b', fg_color='#3b3b3b')  # Frame utama dengan warna latar belakang
        container_frame.pack(expand=True, fill='both')  # Memastikan frame dapat mengisi ruang yang tersedia

        riwayat_expression_frame = ctk.CTkFrame(container_frame, bg_color='#3b3b3b', fg_color='#3b3b3b')  # Frame untuk menampilkan expression riwayat
        riwayat_expression_frame.pack(fill='x')  # Memastikan frame mengisi lebar container

        expression_frame = ctk.CTkFrame(container_frame, bg_color='#3b3b3b', fg_color='#3b3b3b')  # Frame untuk menampilkan expression kalkulasi
        expression_frame.pack(expand=True, fill='both')  # Memastikan frame dapat mengisi ruang yang tersedia

        button_frame = ctk.CTkFrame(container_frame, bg_color='#3b3b3b', fg_color='#3b3b3b')  # Frame untuk tombol kalkulator
        button_frame.pack(fill='x', padx=5, pady=5)  # Memastikan frame mengisi lebar container dan memberikan padding
        button_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)  # Mengatur kolom frame untuk menyesuaikan ukuran

        # Label
        button_riwayat = ctk.CTkButton(
            riwayat_expression_frame, text='Riwayat', anchor='w', width=0,
            font=('Arial', 12, 'bold'), command=self.show_riwayat,
            fg_color='#565656', text_color='#ffffff'
        )
        button_riwayat.pack(side='left', padx=10, pady=(10, 5))  # Menempatkan tombol riwayat di sebelah kiri frame dengan padding

        self.riwayat_expression_label = ctk.CTkLabel(
            riwayat_expression_frame, text='', font=('Arial', 14, 'bold'),
            anchor='e', text_color='#e0e0e0'
        )
        self.riwayat_expression_label.pack(side='right', padx=10, pady=(10, 5))  # Menempatkan label expression riwayat di sebelah

        self.expression_label = ctk.CTkLabel(
            expression_frame, text='', font=('Arial', 18, 'bold'),
            anchor='e', text_color='#e0e0e0'
        )
        self.expression_label.pack(expand=True, fill='both', padx=10)

        # Buttons
        buttons = [
            'AC', '<', '%', '/',
            '7', '8', '9', 'x',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', '=',
        ]

        row, col = 0, 0
        for button in buttons:
            btn = ctk.CTkButton(
                button_frame, text=button, font=('Arial', 16, 'bold'),
                fg_color='#4b4b4b', text_color='#e0e0e0',
                command=lambda x=button: self.button_action(x)
            )
            if button == '0':
                btn.grid(row=row, column=col, columnspan=2, padx=2, pady=2, ipady=10, sticky='we')
                col += 1
            else:
                btn.grid(row=row, column=col, padx=2, pady=2, ipady=10, sticky='we')
            col += 1
            if col == 4:
                col = 0
                row += 1

    def close(self):
        self.db.close()

if __name__ == '__main__':
    root = ctk.CTk()
    app = CalculatorApp(root)
    root.mainloop()
    app.close()
