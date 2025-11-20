import tkinter as tk
from tkinter import ttk
from datetime import datetime

data=[]
error=[]

def buka_halaman2():
    halaman2.tkraise()

def buka_halaman3():
    halaman3.tkraise()

def pesanan():
    halaman4.tkraise()
    tampilan_pesanan()

def kembali():
    halaman1.tkraise()

def login():
    username=entry1.get()
    password=entry2.get()
    cbb=stuju.get()

    if username=="marvelle" and password=="1234":
        buka_halaman2()
    else:
        error_login.config(text="Username/Password Salah", foreground="red")
    if not cbb:
        error_login.config(text="Harap setuju dengan privacy dan policy")
    else:
        buka_halaman2()


def simpan_data():
    nama=entry3.get().strip()
    ci=entry4.get().strip()
    co=entry5.get().strip()
    tipe=tipe_kamar.get()

    if not nama or not ci or not co or not tipe:
        error.append("Masukkan semua data yang ada")
        
    if not nama:
        error.append("Masukkan nama anda")
        
    if not ci:
        error.append("Masukkan tanggal checkin anda dengan format yang disediakan")
        
    if not co:
        error.append("Masukkan tanggal checkin anda dengan format yang disediakan")
        
    if not tipe:
        error.append("Silahkan pilih tipe kamar yang anda mau")
    
        

    harga=0
    if tipe =="Standard":harga=300000
    if tipe =="Deluxe":harga=500000
    if tipe =="Suite":harga=800000

    
    try:
        t1=datetime.strptime(ci,"%d/%m/%y")
        t2=datetime.strptime(co,"%d/%m/%y")
        jumlah=(t2-t1).days
        if jumlah<=0:
            hasil.config(text="Tanggal tidak valid!", foreground="red")
            return
    except:
        hasil.config(text="Format tanggal salah!", foreground="red")
        return

    total_harga=jumlah*harga

    
    data.append((nama,ci,co,tipe,jumlah,total_harga))

    
    label_konf.config(text=
        f"Nama:{nama}\n"
        f"Check-in:{ci}\n"
        f"Check-out:{co}\n"
        f"Tipe kamar:{tipe}\n"
        f"Harga per malam: Rp{harga:,.0f}\n"
        f"Jumlah hari:{jumlah}\n"
        f"Total harga: Rp{total_harga:,.0f}"
    )
    buka_halaman3()


def tampilan_pesanan():
    for item in tree.get_children():
        tree.delete(item)
    for d in data:
        tree.insert("", tk.END, values=d)


def cari_data():
    keyword=entry_cari.get().strip().lower()

    for i in tree.get_children():
        tree.delete(i)

    hasil=[]
    for d in data:
        if keyword in d[0].lower() or keyword in d[3].lower():
            hasil.append(d)

    if hasil:
        for d in hasil:
            tree.insert("", tk.END, values=d)
    else:
        tree.insert("", tk.END, values=("Data tidak ditemukan","","","","",""))


def total():
    total_uang=sum([d[5] for d in data])

    label_total.config(text=f"Total pemasukan: Rp {total_uang:,.0f}")
    halaman5.tkraise()


root=tk.Tk()
root.title("Form Penginapan Hotel")
root.geometry("520x420")
root.configure(background="#BF1A1A")

halaman1=ttk.Frame(root)
halaman2=ttk.Frame(root)
halaman3=ttk.Frame(root)   
halaman4=ttk.Frame(root)
halaman5=ttk.Frame(root)

style=ttk.Style()
style.theme_use("clam")
style.configure("TFrame", background="#8BAE66")
style.configure("TLabel", background="#8BAE66", font=("Helvetica",10))
style.configure("TButton", font=("Helvetica",10,"bold"), padding=5)
style.configure("Treeview.Heading", font=("Helvetica",10,"bold"), background="#4682b4", foreground="white")
style.configure("Treeview", background="#fafafa", fieldbackground="#fafafa", foreground="black")

for frame in(halaman1,halaman2,halaman3,halaman4,halaman5):
    frame.place(relx=0, rely=0, relheight=1, relwidth=1)



ttk.Label(halaman1, text="Username").pack(pady=10)
entry1=ttk.Entry(halaman1, width=30)
entry1.pack()

ttk.Label(halaman1, text="Password").pack(pady=5)
entry2=ttk.Entry(halaman1, width=30, show="*")
entry2.pack()

stuju=tk.BooleanVar()
ttk.Checkbutton(halaman1, text="Setuju dengan Privacy dan Policy", variable=stuju).pack()

error_login=ttk.Label(halaman1, text="")
error_login.pack()

tk.Button(halaman1, text="Login", command=login, background="#BF092F").pack(pady=5)
tk.Button(halaman1, text="Keluar", command=root.destroy, background="white").pack()



ttk.Label(halaman2, text="Masukkan Nama Anda").pack(pady=10)
entry3=ttk.Entry(halaman2, width=30)
entry3.pack()

ttk.Label(halaman2, text="Tanggal Checkin (dd/mm/yy)").pack(pady=5)
entry4=ttk.Entry(halaman2, width=30)
entry4.pack()

ttk.Label(halaman2, text="Tanggal Checkout (dd/mm/yy)").pack(pady=5)
entry5=ttk.Entry(halaman2, width=30)
entry5.pack()

tipe_kamar=ttk.Combobox(halaman2, values=["Standard","Deluxe","Suite"], state="readonly")
tipe_kamar.pack(pady=5)

hasil=ttk.Label(halaman2, text="")
hasil.pack()

ttk.Button(halaman2, text="Simpan", command=simpan_data).pack(pady=5)
ttk.Button(halaman2, text="Lihat Data", command=pesanan).pack(pady=5)
ttk.Button(halaman2, text="Cari Data", command=pesanan).pack(pady=5)
tk.Button(halaman2, text="Keluar", command=root.destroy, background="#BF092F").pack(pady=5)



ttk.Label(halaman3, text="Konfirmasi Pesanan", font=("Helvetica",16,"bold")).pack(pady=10)
label_konf=ttk.Label(halaman3, text="", font=("Helvetica",10))
label_konf.pack(pady=10)
ttk.Button(halaman3, text="Kembali", command=buka_halaman2).pack(pady=10)



tree=ttk.Treeview(
    halaman4,
    columns=("Nama","Checkin","Checkout","Tipe","Jumlah Hari","Total Harga"),
    show="headings",
    height=8
)

tree.heading("Nama", text="Nama")
tree.heading("Checkin", text="Check-in")
tree.heading("Checkout", text="Check-out")
tree.heading("Tipe", text="Tipe Kamar")
tree.heading("Jumlah Hari", text="Jumlah")
tree.heading("Total Harga", text="Total Harga")

tree.pack(pady=10, fill="x", padx=10)

ttk.Label(halaman4, text="Cari Data").pack(pady=5)
entry_cari=ttk.Entry(halaman4, width=30)
entry_cari.pack(pady=5)

ttk.Button(halaman4, text="Cari", command=cari_data).pack(pady=5)
ttk.Button(halaman4, text="Kembali", command=buka_halaman2).pack(pady=5)



ttk.Label(halaman5, text="Total Pemasukan", font=("Helvetica",16,"bold")).pack(pady=10)
label_total=ttk.Label(halaman5, text="")
label_total.pack(pady=10)
ttk.Button(halaman5, text="Kembali", command=buka_halaman2).pack(pady=10)


halaman1.tkraise()
root.mainloop()

