from tkinter import Tk
import vista
import observador

class Controller:

    def __init__(self, root):
        self.root_controller = root
        self.objeto_vista = vista.InterfazGrafica(self.root_controller)
        self.el_observador = observador.ObservadorA(self.objeto_vista.base)

if __name__ == "__main__":
    root_tk = Tk()
    aplicacion = Controller(root_tk)


root_tk.mainloop()