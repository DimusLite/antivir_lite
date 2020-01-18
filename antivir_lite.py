HKCU_PATH = "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\\"
HKLM_PATH = "HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\\"
import tkinter as tk
root = tk.Tk()
root.title("antivir.lite")
root["bg"] = "#f0f0ed"

lbl_hkcu = tk.Label(root, font = ("Ubuntu", 20), text = HKCU_PATH+":", bg = "#f0f0ed", fg = "black", justify = "left")
lbl_hkcu.grid(row = 0, column = 0, sticky = tk.W, pady = 4, padx = 5)

lst_hkcu = tk.Listbox(root, width = 70, height = 5, bg = "white")
lst_hkcu.grid(row = 1, rowspan = 2, column = 0, padx = 5)

btn_refresh_hkcu = tk.Button(root, width = 15, height = 2, text = "Refresh", font = ("Ubuntu", 14))
btn_remove_hkcu = tk.Button(root, width = 15, height = 2, text = "Remove", font = ("Ubuntu", 14))
btn_refresh_hkcu.grid(row = 1, column = 1)
btn_remove_hkcu.grid(row = 2, column = 1, pady = 4)

lbl_hklm = tk.Label(root, font = ("Ubuntu", 20), text = HKCU_PATH+":", bg = "#f0f0ed", fg = "black", justify = "left")
lbl_hklm.grid(row = 3, column = 0, sticky = tk.W, pady = 4, padx = 5)

lst_hklm = tk.Listbox(root, width = 70, height = 5, bg = "white")
lst_hklm.grid(row = 4, rowspan = 2, column = 0, padx = 5)

btn_refresh_hklm = tk.Button(root, width = 15, height = 2, text = "Refresh", font = ("Ubuntu", 14))
btn_remove_hklm = tk.Button(root, width = 15, height = 2, text = "Remove", font = ("Ubuntu", 14))
btn_refresh_hklm.grid(row = 4, column = 1)
btn_remove_hklm.grid(row = 5, column = 1, pady = 4)

for el in ('first', 'second', 'third', 'fourth'):
    lst_hklm.insert(0, el)
    lst_hkcu.insert(1, el)
root.mainloop()