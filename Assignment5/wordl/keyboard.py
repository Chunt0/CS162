# Christopher Hunt
# CS162
# keyboard.py

import tkinter as tk

class Keyboard(tk.Label):
    """
    A bunch of labels that correspond with the QWERTY keyboard. Also
    all of the labels in a dictionary called key_matrix.
    """
    def __init__(self, COL, ROW):
        self.Q = tk.Label(text="Q", bg="black", fg="white", font=("Helvetica", 48, "bold"))
        self.Q.grid(column=COL,row=ROW)
        self.W = tk.Label(text="W", bg="black", fg="white", font=("Helvetica", 48, "bold"))
        self.W.grid(column=COL+1,row=ROW)
        self.E = tk.Label(text="E", bg="black", fg="white", font=("Helvetica", 48, "bold"))
        self.E.grid(column=COL+2,row=ROW)
        self.R = tk.Label(text="R", bg="black", fg="white", font=("Helvetica", 48, "bold"))
        self.R.grid(column=COL+3,row=ROW)
        self.T = tk.Label(text="T", bg="black", fg="white", font=("Helvetica", 48, "bold"))
        self.T.grid(column=COL+4,row=ROW)
        self.Y = tk.Label(text="Y", bg="black", fg="white", font=("Helvetica", 48, "bold"))
        self.Y.grid(column=COL+5,row=ROW)
        self.U = tk.Label(text="U", bg="black", fg="white", font=("Helvetica", 48, "bold"))
        self.U.grid(column=COL+6,row=ROW)
        self.I = tk.Label(text="I", bg="black", fg="white", font=("Helvetica", 48, "bold"))
        self.I.grid(column=COL+7,row=ROW)
        self.O = tk.Label(text="O", bg="black", fg="white", font=("Helvetica", 48, "bold"))
        self.O.grid(column=COL+8,row=ROW)
        self.P = tk.Label(text="P", bg="black", fg="white", font=("Helvetica", 48, "bold"))
        self.P.grid(column=COL+9,row=ROW)

        self.A = tk.Label(text="A", bg="black", fg="white", font=("Helvetica", 48, "bold"))
        self.A.grid(column=COL,row=ROW+1)
        self.S = tk.Label(text="S", bg="black", fg="white", font=("Helvetica", 48, "bold"))
        self.S.grid(column=COL+1,row=ROW+1)
        self.D = tk.Label(text="D", bg="black", fg="white", font=("Helvetica", 48, "bold"))
        self.D.grid(column=COL+2,row=ROW+1)
        self.F = tk.Label(text="F", bg="black", fg="white", font=("Helvetica", 48, "bold"))
        self.F.grid(column=COL+3,row=ROW+1)
        self.G = tk.Label(text="G", bg="black", fg="white", font=("Helvetica", 48, "bold"))
        self.G.grid(column=COL+4,row=ROW+1)
        self.H = tk.Label(text="H", bg="black", fg="white", font=("Helvetica", 48, "bold"))
        self.H.grid(column=COL+5,row=ROW+1)
        self.J = tk.Label(text="J", bg="black", fg="white", font=("Helvetica", 48, "bold"))
        self.J.grid(column=COL+6,row=ROW+1)
        self.K = tk.Label(text="K", bg="black", fg="white", font=("Helvetica", 48, "bold"))
        self.K.grid(column=COL+7,row=ROW+1)
        self.L = tk.Label(text="L", bg="black", fg="white", font=("Helvetica", 48, "bold"))
        self.L.grid(column=COL+8,row=ROW+1)

        self.Z = tk.Label(text="Z", bg="black", fg="white", font=("Helvetica", 48, "bold"))
        self.Z.grid(column=COL,row=ROW+2)
        self.X = tk.Label(text="X", bg="black", fg="white", font=("Helvetica", 48, "bold"))
        self.X.grid(column=COL+1,row=ROW+2)
        self.C = tk.Label(text="C", bg="black", fg="white", font=("Helvetica", 48, "bold"))
        self.C.grid(column=COL+2,row=ROW+2)
        self.V = tk.Label(text="V", bg="black", fg="white", font=("Helvetica", 48, "bold"))
        self.V.grid(column=COL+3,row=ROW+2)
        self.B = tk.Label(text="B", bg="black", fg="white", font=("Helvetica", 48, "bold"))
        self.B.grid(column=COL+4,row=ROW+2)
        self.N = tk.Label(text="N", bg="black", fg="white", font=("Helvetica", 48, "bold"))
        self.N.grid(column=COL+5,row=ROW+2)
        self.M = tk.Label(text="M", bg="black", fg="white", font=("Helvetica", 48, "bold"))
        self.M.grid(column=COL+6,row=ROW+2)

        self.key_matrix={\
                'A' : self.A,\
                'B' : self.B,\
                'C' : self.C,\
                'D' : self.D,\
                'E' : self.E,\
                'F' : self.F,\
                'G' : self.G,\
                'H' : self.H,\
                'I' : self.I,\
                'J' : self.J,\
                'K' : self.K,\
                'L' : self.L,\
                'M' : self.M,\
                'N' : self.N,\
                'O' : self.O,\
                'P' : self.P,\
                'Q' : self.Q,\
                'R' : self.R,\
                'S' : self.S,\
                'T' : self.T,\
                'U' : self.U,\
                'V' : self.V,\
                'W' : self.W,\
                'X' : self.X,\
                'Y' : self.Y,\
                'Z' : self.Z,\
                }
