import tkinter as tk
from gui import AplikasiPerpustakaanGUI

def main():
    root = tk.Tk()
    app = AplikasiPerpustakaanGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()