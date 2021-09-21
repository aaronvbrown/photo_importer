import tkinter as tk
from tkinter import scrolledtext as st
from tkinter.filedialog import askdirectory


import photo_importer as pi

## Main window setup

window = tk.Tk()
window.title('Photo and Movie Importer')

window.columnconfigure(0, weight=1)
window.rowconfigure(0, pad=0)
window.rowconfigure(1, pad=20)
window.rowconfigure(2, pad=10)


def set_import_folder():
    import_folder = askdirectory()
    if not import_folder:
        return
    ent_input_path.delete(0, tk.END)
    ent_input_path.insert(0, import_folder)
    st_input_files.delete("0.0", tk.END)
    for ind, file in enumerate(pi.get_list_of_images_to_import(import_folder)):
        st_input_files.insert(f"{ind}.0", f"{file}\n")

def set_output_folder():
    output_folder = askdirectory()
    if not output_folder:
        return
    ent_output_path.delete(0, tk.END)
    ent_output_path.insert(0, output_folder)

def update_list_of_images_to_import(import_folder):
    if import_folder:
        images_to_import = pi.get_list_of_images_to_import()
        pass
    

##  Build Detail Frame 
frm_detail = tk.Frame(master=window, borderwidth=1, relief=tk.RAISED)

frm_detail.columnconfigure(0, pad=20, weight=1)
frm_detail.columnconfigure(1, minsize=250, weight=5)
frm_detail.columnconfigure(2, weight=1)

# Input Path
lbl_input_path  = tk.Label(master=frm_detail, text="Input Path")
lbl_input_path.grid(row=0, column=0, sticky="nw")
ent_input_path = tk.Entry(master=frm_detail, bd=2, bg="White")
ent_input_path.grid(row=0, column=1, sticky="ew")
btn_input_path = tk.Button(master=frm_detail, text=f"Set Import Path", command=set_import_folder)
btn_input_path.grid(row=0, column=2, sticky="sew", padx=5, pady=5)

# Input Files
lbl_input_files = tk.Label(master=frm_detail, text="Input Files")
lbl_input_files.grid(row=1, column=0, sticky="nw")
st_input_files = st.ScrolledText(master=frm_detail, bg="White", height=10)
st_input_files.insert("1.0", "This is where the scrolled text belongs.")
st_input_files.grid(row=1, column=1)

# Output Path
lbl_output_path = tk.Label(master=frm_detail, text="Output Path")
lbl_output_path.grid(row=2, column=0, sticky="nw")
ent_output_path = tk.Entry(master=frm_detail, bd=2, bg="White")
ent_output_path.grid(row=2, column=1, sticky="ew")
btn_output_path = tk.Button(master=frm_detail, text=f"Update Output Folder", command=set_output_folder)
btn_output_path.grid(row=2, column=2, sticky="sew", padx=5, pady=5)

# Log
lbl_log         = tk.Label(master=frm_detail, text="Log")
lbl_log.grid(row=3, column=0, sticky="nw")
st_log = st.ScrolledText(master=frm_detail, bg="White", height=10)
st_log.grid(row=3, column=1)
st_log.insert("1.0", "Program hasn't run yet.")

frm_detail.grid(row=0, column=0, sticky="ew")


## Setup the actions frame.
frm_actions = tk.Frame(master=window, borderwidth=2, relief="flat")

btn_copy_files = tk.Button(master=frm_actions, text="Copy Files", borderwidth=1, relief="raised")
btn_copy_files.pack(side="right", ipadx=5, padx=5, pady=5, fill="x")

btn_move_files = tk.Button(master=frm_actions, text="Move Files", borderwidth=1, relief="raised")
btn_move_files.pack(side="right", ipadx=5, padx=5, pady=5, fill="x")

frm_actions.grid(row=1, column=0, sticky="EW")


window.mainloop()