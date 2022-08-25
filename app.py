
import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk



def connection():
    conn = pymysql.connect(
        host='localhost',
        user='root', 
        password='',
        db='estudantes_db',
    )
    return conn

def refreshTable():
    for data in my_tree.get_children():
        my_tree.delete(data)

    for array in read():
        my_tree.insert(parent='', index='end', iid=array, text="", values=(array), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE', font=('Arial', 12))
    my_tree.grid(row=8, column=0, columnspan=5, rowspan=11, padx=10, pady=20)

root = Tk()
root.title("Cadastro de estudantes")
root.geometry("1100x790")
my_tree = ttk.Treeview(root)

ph1 = tk.StringVar()
ph2 = tk.StringVar()
ph3 = tk.StringVar()
ph4 = tk.StringVar()
ph5 = tk.StringVar()


def setph(word,num):
    if num ==1:
        ph1.set(word)
    if num ==2:
        ph2.set(word)
    if num ==3:
        ph3.set(word)
    if num ==4:
        ph4.set(word)
    if num ==5:
        ph5.set(word)

def read():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM estudantes")
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results

cad_icone = PhotoImage(file='D:\\tkinter_projeto\\icon.png')
atualizar_icone = PhotoImage(file='D:\\tkinter_projeto\\atualizar.png')
deletar_icone = PhotoImage(file='D:\\tkinter_projeto\\deletar.png')
pesquisar_icone = PhotoImage(file='D:\\tkinter_projeto\\pesquisar.png')
resetar_icone = PhotoImage(file='D:\\tkinter_projeto\\resetar.png')
selecionar_icone = PhotoImage(file='D:\\tkinter_projeto\\selecionar.png')



def read():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM estudantes")
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results


def cadastrar():
    estid = str(estidEntry.get())
    nome = str(nomeEntry.get())
    s_nome = str(s_nomeEntry.get())
    endereco = str(enderecoEntry.get())
    telefone = str(telefoneEntry.get())

    if (estid == "" or estid == " ") or (nome == "" or nome == " ") or (s_nome == "" or s_nome == " ") or (endereco == "" or endereco == " ") or (telefone == "" or telefone == " "):
        messagebox.showinfo("Error", "VOCE DEVE PREENCHER TODOS OS CAMPOS EM BRANCO")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO estudantes VALUES ('"+estid+"','"+nome+"','"+s_nome+"','"+endereco+"','"+telefone+"') ")
            conn.commit()
            conn.close()
           
            
        except:
            messagebox.showinfo("Error", "ESTE ESTUDANTE JA EXISTE NO BANCO DE DADOS COM ESTE ID")
            return
        

    refreshTable()
    
    

def resetar():
    decision = messagebox.askquestion("Warning!!", "DELETAR TODOS DADOS?")
    if decision != "yes":
        return 
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM estudantes")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "DESCULPE ALGUM ERRO OCORREU")
            return

        refreshTable()


def Limpar():
      estidEntry.delete(0,'end')
      nomeEntry.delete(0,'end')
      s_nomeEntry.delete(0,'end')
      enderecoEntry.delete(0,'end')
      telefoneEntry.delete(0,'end')
      estidEntry.focus_set()



      
def deletar():

    resposta = messagebox.askquestion("CUIDADO!!", "DELETAR A SESSAO DE DADOS?")
    if resposta != "yes":
        return

    else:
        selected_item = my_tree.selection()[0]
        deleteData = str(my_tree.item(selected_item)['values'][0])


        try:

            conn = connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM estudantes WHERE ESTID='"+str(deleteData)+"'")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "DESCULPE ALGUM ERRO OCORRIDO")
            return

        refreshTable()

def selecionar():
    try:
        selected_item = my_tree.selection()[0]
        estid = str(my_tree.item(selected_item)['values'][0])
        nome = str(my_tree.item(selected_item)['values'][1])
        s_nome = str(my_tree.item(selected_item)['values'][2])
        endereco = str(my_tree.item(selected_item)['values'][3])
        telefone = str(my_tree.item(selected_item)['values'][4])

        setph(estid,1)
        setph(nome,2)
        setph(s_nome,3)
        setph(endereco,4)
        setph(telefone,5)

        
    except:
        messagebox.showinfo("Error", "VOCE TEM QUE SELECIONAR UM CADASTRO OU LINHA")

def pesquisar():
    estid = str(estidEntry.get())
    nome = str(nomeEntry.get())
    s_nome = str(s_nomeEntry.get())
    endereco = str(enderecoEntry.get())
    telefone = str(telefoneEntry.get())

    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM estudantes WHERE ESTID='"+
    estid+"' or NOME='"+
    nome+"' or S_NOME='"+
    s_nome+"' or ENDERECO='"+
    endereco+"' or TELEFONE='"+
    telefone+"' ")
    
    try:
        result = cursor.fetchall()

        for num in range(0,5):
            setph(result[0][num],(num+1))

        conn.commit()
        conn.close()
    except:
        messagebox.showinfo("Error", "CADASTRO NAO ENCONTRADO")

def atualizar():
    selectedEstid = ""

    try:
        selected_item = my_tree.selection()[0]
        selectedEstid = str(my_tree.item(selected_item)['values'][0])
    except:
        messagebox.showinfo("Error", "FAVOR SELECIONAR UM CADASTRO")

    estid = str(estidEntry.get())
    nome = str(nomeEntry.get())
    s_nome = str(s_nomeEntry.get())
    endereco = str(enderecoEntry.get())
    telefone = str(telefoneEntry.get())

    if (estid == "" or estid == " ") or (nome == "" or nome == " ") or (s_nome == "" or s_nome == " ") or (endereco == "" or endereco == " ") or (telefone == "" or telefone == " "):
        messagebox.showinfo("Error", "FAVOR PREENCHER TODOS OS CAMPOS EM BRACO")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE estudantes SET ESTID='"+
            estid+"', NOME='"+
            nome+"', S_NOME='"+
            s_nome+"', ENDERECO='"+
            endereco+"', TELEFONE='"+
            telefone+"' WHERE ESTID='"+
            selectedEstid+"' ")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "ESTE st ID JA EXISTE")
            return

    refreshTable()

label = Label(root, text="CADASTRO DE ESTUDANTES", font=('Arial Bold', 30))
label.grid(row=0, column=0, columnspan=8, rowspan=2, padx=50, pady=40)

estidLabel = Label(root, text="Estudante ID :", font=('Arial', 15))
nomeLabel = Label(root, text="Nome :", font=('Arial', 15))
s_nomeLabel = Label(root, text="S_Nome :", font=('Arial', 15))
enderecoLabel = Label(root, text="Endereco :", font=('Arial', 15))
telefoneLabel = Label(root, text="Telefone:", font=('Arial', 15))

estidLabel.grid(row=3, column=0, columnspan=1, padx=50, pady=5)
nomeLabel.grid(row=4, column=0, columnspan=1, padx=50, pady=5)
s_nomeLabel.grid(row=5, column=0, columnspan=1, padx=50, pady=5)
enderecoLabel.grid(row=6, column=0, columnspan=1, padx=50, pady=5)
telefoneLabel.grid(row=7, column=0, columnspan=1, padx=50, pady=5)

estidEntry = Entry(root, width=55, bd=1, font=('Arial', 15), textvariable = ph1)
nomeEntry = Entry(root, width=55, bd=1, font=('Arial', 15), textvariable = ph2)
s_nomeEntry = Entry(root, width=55, bd=1, font=('Arial', 15), textvariable = ph3)
enderecoEntry = Entry(root, width=55, bd=1, font=('Arial', 15), textvariable = ph4)
telefoneEntry = Entry(root, width=55, bd=1, font=('Arial', 15), textvariable = ph5)

estidEntry.grid(row=3, column=1, columnspan=4, padx=5, pady=0)
nomeEntry.grid(row=4, column=1, columnspan=4, padx=5, pady=0)
s_nomeEntry.grid(row=5, column=1, columnspan=4, padx=5, pady=0)
enderecoEntry.grid(row=6, column=1, columnspan=4, padx=5, pady=0)
telefoneEntry.grid(row=7, column=1, columnspan=4, padx=5, pady=0)

LimparBtn = Button(
    root, text="Limpar Campos", padx=50, pady=5, width=8,
    bd=1, font=('Arial', 15), bg="#F4FE82",  command=Limpar)
LimparBtn.grid(row=0, column=5, columnspan=1, rowspan=2)




cadastrarBtn = Button(
    root, text="Cadastrar",anchor="center", width=98,
    bd=1, font=('Arial', 15), bg="#84F894",compound = TOP,image=cad_icone,command=lambda:[cadastrar(),Limpar()])  

atualizarBtn = Button(
    root, text="Atualizar",anchor="center", width=98,
    bd=1, font=('Arial', 15), bg="#84E8F8",compound = TOP,image=atualizar_icone,command=atualizar)

deletarBtn = Button(
    root, text="Deletar",anchor="center", width=98,
    bd=1, font=('Arial', 15), bg="#FF9999",compound = TOP,image=deletar_icone,command=deletar)

pesquisarBtn = Button(
    root, text="Pesquisar",anchor="center", width=98,
    bd=1, font=('Arial', 15), bg="#F4FE82",compound = TOP,image=pesquisar_icone,command=pesquisar)
resetarBtn = Button(

    root, text="Resetar",anchor="center", width=98,
    bd=1, font=('Arial', 15), bg="#F398FF",compound = TOP,image=resetar_icone,command=resetar)

selecionarBtn = Button(
    root, text="Selecionar",anchor="center", width=98,
    bd=1, font=('Arial', 15), bg="#EEEEEE",compound = TOP,image=selecionar_icone,command=selecionar)

cadastrarBtn.grid(row=3, column=5, columnspan=1, rowspan=2)
atualizarBtn.grid(row=5, column=5, columnspan=1, rowspan=2)
deletarBtn.grid(row=7, column=5, columnspan=1, rowspan=2)
pesquisarBtn.grid(row=9, column=5, columnspan=1, rowspan=2)
resetarBtn.grid(row=11, column=5, columnspan=1, rowspan=2)
selecionarBtn.grid(row=13, column=5, columnspan=1, rowspan=2)



style = ttk.Style()
style.configure("Treeview.Heading",font=('Arial Bold', 15,))

my_tree['columns'] = ("Est ID","Nome","S_Nome","Endereco","Telefone")

my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Est ID", anchor=W, width=170)
my_tree.column("Nome", anchor=W, width=150)
my_tree.column("S_Nome", anchor=W, width=150)
my_tree.column("Endereco", anchor=W, width=165)
my_tree.column("Telefone", anchor=W, width=150)

my_tree.heading("Est ID", text="Estudante ID", anchor=W)
my_tree.heading("Nome", text="Nome", anchor=W)
my_tree.heading("S_Nome", text="S_Nome", anchor=W)
my_tree.heading("Endereco", text="Endereco", anchor=W)
my_tree.heading("Telefone", text="Telefone", anchor=W)



refreshTable()
font1=('Times',10,'normal')

label_rodape = Label(root,text="CRIADO E DESENVOLVIDO POR SANGIORGIOVBA@GMAIL.COM",font=font1,height=1,width=95)
label_rodape.grid(row=15,column=0,columnspan=85,padx=0,pady=5)


root.mainloop()
