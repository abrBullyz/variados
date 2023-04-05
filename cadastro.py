"""
1 import libs
2 interface
    nome do cao, raca, cor, dbo, pai, mae,
3


"""
import sqlite3
import pandas as pd
import tkinter as tk


conect = sqlite3.connect('db_dogsID.db')

# cur = conect.cursor()
#
# cur.execute(""" CREATE TABLE dogs (
#
#     nome_cao text,
#     raca text,
#     foto text,
#     cor text,
#     db0 text,
#     pai text,
#     mae text )
#
#
# """)
# conect.commit()
# conect.close()
janela = tk.Tk()
janela.title('Cadastro de cachorro')

label_nome = tk.Label(janela, text='nome')
label_nome.grid(row=0, colunum=0, padx=0, pady =10)
label_raca = tk.Label(janela, text='raca')
label_raca.grid(row=0, colunum=0, padx=0,pady =10)
label_cor = tk.Label(janela, text='cor')
label_cor.grid(row=0, colunum=0, padx=0,pady =10)
label_dbo = tk.Label(janela, text='dbo')
label_dbo.grid(row=0, colunum=0, padx=0,pady =10)
label_pai = tk.Label(janela, text='pai')
label_pai.grid(row=0, colunum=0, padx=0,pady =10)
label_mae = tk.Label(janela, text='mae')
label_mae.grid(row=0, colunum=0, padx=0,pady =10)

# entry_nome = tk.Entry(janela)
# entry_nome.grid(row=0, colunum=0, padx=0,pady =10)
# entry_raca = tk.Entry(janela, text='raca')
# entry_raca.grid(row=0, colunum=0, padx=0,pady =10)
# entry_cor = tk.Entry(janela, text='cor')
# entry_cor.grid(row=0, colunum=0, padx=0,pady =10)
# entry_dbo = tk.Entry(janela, text='dbo')
# entry_dbo.grid(row=0, colunum=0, padx=0,pady =10)
# entry_pai = tk.Entry(janela, text='pai')
# entry_pai.grid(row=0, colunum=0, padx=0,pady =10)
# entry_mae = tk.Entry(janela, text='mae')
# entry_mae.grid(row=0, colunum=0, padx=0,pady =10)

janela.mainloop()