"""Praktikum Sesi 11: Pendaftaran Kegiatan Mahasiswa (Python + Tkinter)."""
import tkinter as tk
from tkinter import ttk, messagebox

KEGIATAN = {
    'Seminar Teknologi': 'Diskusi perkembangan teknologi dan penerapannya.',
    'Workshop Python': 'Latihan pemrograman Python melalui praktik langsung.',
    'Pelatihan Organisasi': 'Belajar kepemimpinan, komunikasi, dan kerja tim.',
    'Bakti Sosial': 'Kegiatan kepedulian dan pengabdian kepada masyarakat.',
}
PRODI = ('Teknik Informatika', 'Sistem Informasi', 'Manajemen', 'Akuntansi', 'Teknik Mesin')


class FormMahasiswa:
    def __init__(self, root):
        self.root = root
        self.about_window = None
        root.title('Pendaftaran Kegiatan Mahasiswa | Sesi 11')
        root.geometry('980x720')
        root.minsize(900, 680)
        root.configure(bg='#EFF6FF')
        root.columnconfigure(0, weight=1)
        root.rowconfigure(1, weight=1)
        style = ttk.Style(root)
        style.theme_use('clam')
        style.configure('TFrame', background='#EFF6FF')
        style.configure('TLabel', background='#EFF6FF', font=('Arial', 10))
        style.configure('TLabelframe', background='#EFF6FF')
        style.configure('TLabelframe.Label', background='#EFF6FF', font=('Arial', 11, 'bold'))
        style.configure('TCheckbutton', background='#EFF6FF', font=('Arial', 10))
        style.configure('TRadiobutton', background='#EFF6FF', font=('Arial', 10))
        style.configure('TButton', font=('Arial', 10), padding=8)
        style.configure('Primary.TButton', foreground='white', background='#1D4ED8')
        style.map('Primary.TButton', background=[('active', '#1E40AF')])

        menu = tk.Menu(root)
        file_menu = tk.Menu(menu, tearoff=False)
        file_menu.add_command(label='Keluar', command=root.destroy)
        menu.add_cascade(label='File', menu=file_menu)
        help_menu = tk.Menu(menu, tearoff=False)
        help_menu.add_command(label='About', command=self.about)
        menu.add_cascade(label='Bantuan', menu=help_menu)
        root.config(menu=menu)

        header = tk.Frame(root, bg='#1D4ED8', padx=24, pady=18)
        header.grid(row=0, column=0, sticky='ew')
        tk.Label(header, text='PENDAFTARAN KEGIATAN MAHASISWA', bg='#1D4ED8',
                 fg='white', font=('Arial', 18, 'bold')).pack(anchor='w')
        tk.Label(header, text='Praktikum Sesi 11  •  Advanced Widgets dan Event Handling',
                 bg='#1D4ED8', fg='#DBEAFE', font=('Arial', 10)).pack(anchor='w', pady=(6, 0))
        body = ttk.Frame(root, padding=20)
        body.grid(row=1, column=0, sticky='nsew')
        body.columnconfigure(0, weight=3)
        body.columnconfigure(1, weight=2)
        body.rowconfigure(0, weight=1)
        form = ttk.LabelFrame(body, text=' Identitas dan pilihan kegiatan ', padding=16)
        form.grid(row=0, column=0, sticky='nsew', padx=(0, 16))
        form.columnconfigure(1, weight=1)
        self.nama = tk.StringVar()
        self.nim = tk.StringVar()
        self.prodi = tk.StringVar()
        self.gender = tk.StringVar()
        self.pilihan = {name: tk.BooleanVar(value=False) for name in KEGIATAN}

        for row, label in enumerate(('Nama *', 'NIM (opsional)', 'Program studi *', 'Jenis kelamin *', 'Kegiatan *', 'Alasan mengikuti')):
            ttk.Label(form, text=label).grid(row=row, column=0, sticky='nw', padx=(0, 14), pady=9)
        self.input_nama = ttk.Entry(form, textvariable=self.nama, font=('Arial', 11))
        self.input_nama.grid(row=0, column=1, sticky='ew', pady=6, ipady=4)
        ttk.Entry(form, textvariable=self.nim, font=('Arial', 11)).grid(row=1, column=1, sticky='ew', pady=6, ipady=4)
        self.input_prodi = ttk.Combobox(form, textvariable=self.prodi, values=PRODI, state='readonly', font=('Arial', 10))
        self.input_prodi.grid(row=2, column=1, sticky='ew', pady=6, ipady=4)
        gender_frame = ttk.Frame(form)
        gender_frame.grid(row=3, column=1, sticky='w', pady=9)
        for col, value in enumerate(('Laki-laki', 'Perempuan')):
            ttk.Radiobutton(gender_frame, text=value, value=value, variable=self.gender).grid(row=0, column=col, padx=(0, 10))
        checks = ttk.Frame(form)
        checks.grid(row=4, column=1, sticky='w', pady=6)
        for row, (name, variable) in enumerate(self.pilihan.items()):
            ttk.Checkbutton(checks, text=name, variable=variable).grid(row=row, column=0, sticky='w', pady=3)
        self.alasan = tk.Text(form, height=4, width=25, font=('Arial', 11), wrap='word', relief='solid', bd=1)
        self.alasan.grid(row=5, column=1, sticky='ew', pady=6)
        ttk.Label(form, text='* Wajib diisi. Kegiatan boleh lebih dari satu.').grid(row=6, column=0, columnspan=2, sticky='w', pady=(12, 4))
        ttk.Label(form, text='Enter: Submit  |  Shift+Enter: baris baru pada alasan').grid(row=7, column=0, columnspan=2, sticky='w', pady=4)
        buttons = ttk.Frame(form)
        buttons.grid(row=8, column=0, columnspan=2, sticky='ew', pady=(14, 0))
        self.submit_button = ttk.Button(buttons, text='Submit', command=self.submit, style='Primary.TButton')
        self.submit_button.pack(side='left', fill='x', expand=True, padx=(0, 8))
        ttk.Button(buttons, text='Reset', command=self.reset).pack(side='left', fill='x', expand=True)

        right = ttk.Frame(body)
        right.grid(row=0, column=1, sticky='nsew')
        right.columnconfigure(0, weight=1)
        right.rowconfigure(1, weight=1)
        catalog = ttk.LabelFrame(right, text=' Daftar kegiatan ', padding=12)
        catalog.grid(row=0, column=0, sticky='ew', pady=(0, 14))
        catalog.columnconfigure(0, weight=1)
        self.daftar = tk.Listbox(catalog, height=4, exportselection=False, font=('Arial', 11), activestyle='none')
        self.daftar.grid(row=0, column=0, sticky='ew')
        for name in KEGIATAN:
            self.daftar.insert(tk.END, name)
        self.deskripsi = ttk.Label(catalog, text='Klik kegiatan untuk melihat deskripsi.\nCentang pilihan pada formulir untuk mendaftar.', wraplength=310)
        self.deskripsi.grid(row=1, column=0, sticky='w', pady=(10, 0))
        self.daftar.bind('<<ListboxSelect>>', self.show_activity)
        info = ttk.LabelFrame(right, text=' Ringkasan pendaftaran ', padding=12)
        info.grid(row=1, column=0, sticky='nsew')
        info.columnconfigure(0, weight=1)
        info.rowconfigure(0, weight=1)
        self.hasil = tk.Text(info, width=30, height=12, wrap='word', font=('Arial', 11), relief='flat', padx=10, pady=10)
        self.hasil.grid(row=0, column=0, sticky='nsew')
        scroll = ttk.Scrollbar(info, command=self.hasil.yview)
        scroll.grid(row=0, column=1, sticky='ns')
        self.hasil.config(yscrollcommand=scroll.set)
        self.set_result('Ringkasan akan muncul setelah Submit.\n\nData hanya ditampilkan selama aplikasi terbuka; tidak disimpan ke file atau database.')
        root.bind('<Return>', self.on_enter)
        root.bind('<KP_Enter>', self.on_enter)
        # Binding pada Text menghentikan newline bawaan ketika Submit.
        self.alasan.bind('<Return>', self.on_enter)
        self.alasan.bind('<Shift-Return>', self.newline)
        self.input_nama.focus_set()

    def set_result(self, text):
        self.hasil.config(state='normal')
        self.hasil.delete('1.0', tk.END)
        self.hasil.insert('1.0', text)
        self.hasil.config(state='disabled')

    def show_activity(self, event=None):
        selected = self.daftar.curselection()
        if selected:
            self.deskripsi.config(text=KEGIATAN[self.daftar.get(selected[0])])

    def submit(self):
        nama = self.nama.get().strip()
        selected = [name for name, value in self.pilihan.items() if value.get()]
        if not nama:
            messagebox.showwarning('Validasi', 'Nama tidak boleh kosong!', parent=self.root)
            self.input_nama.focus_set()
            return
        if not self.prodi.get():
            messagebox.showwarning('Validasi', 'Silakan pilih program studi!', parent=self.root)
            self.input_prodi.focus_set()
            return
        if not self.gender.get():
            messagebox.showwarning('Validasi', 'Silakan pilih jenis kelamin!', parent=self.root)
            return
        if not selected:
            messagebox.showwarning('Validasi', 'Pilih minimal satu kegiatan melalui kotak centang!', parent=self.root)
            return
        alasan = self.alasan.get('1.0', 'end-1c').strip()
        self.set_result(f'PENDAFTARAN BERHASIL\n\nNama: {nama}\nNIM: {self.nim.get().strip() or "-"}\n'
                        f'Program studi: {self.prodi.get()}\nJenis kelamin: {self.gender.get()}\n\n'
                        'Kegiatan yang dipilih:\n' + '\n'.join(f'• {name}' for name in selected)
                        + f'\n\nAlasan mengikuti:\n{alasan or "-"}')
        messagebox.showinfo('Berhasil', 'Pendaftaran berhasil diproses. Lihat ringkasan di sebelah kanan.', parent=self.root)

    def on_enter(self, event=None):
        if event is None or event.widget.winfo_toplevel() == self.root:
            self.submit()
        return 'break'

    def newline(self, event=None):
        self.alasan.insert(tk.INSERT, '\n')
        return 'break'

    def reset(self):
        for variable in (self.nama, self.nim, self.prodi, self.gender):
            variable.set('')
        for value in self.pilihan.values():
            value.set(False)
        self.alasan.delete('1.0', tk.END)
        self.daftar.selection_clear(0, tk.END)
        self.deskripsi.config(text='Klik kegiatan untuk melihat deskripsi.\nCentang pilihan pada formulir untuk mendaftar.')
        self.set_result('Formulir telah direset. Silakan isi pendaftaran baru.')
        self.input_nama.focus_set()

    def about(self):
        if self.about_window is not None and self.about_window.winfo_exists():
            self.about_window.lift()
            return
        window = tk.Toplevel(self.root)
        self.about_window = window
        window.title('About — Praktikum Sesi 11')
        window.geometry('440x250')
        window.resizable(False, False)
        window.transient(self.root)
        content = ttk.Frame(window, padding=22)
        content.pack(fill='both', expand=True)
        ttk.Label(content, text='Pendaftaran Kegiatan Mahasiswa', font=('Arial', 13, 'bold')).pack(anchor='w', pady=(0, 12))
        ttk.Label(content, text='Praktikum Sesi 11\nAdvanced Widgets dan Event Handling\n\nDibuat menggunakan Python dan Tkinter.\nData pendaftaran ditampilkan sementara di aplikasi.', wraplength=390).pack(anchor='w')
        ttk.Button(content, text='Tutup', command=window.destroy).pack(anchor='e', pady=(18, 0))
        window.bind('<Escape>', lambda event: window.destroy())


def main():
    root = tk.Tk()
    FormMahasiswa(root)
    root.mainloop()


if __name__ == '__main__':
    main()
