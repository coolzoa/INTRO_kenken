#modulos
import ast
from ast import*
import tkinter
from tkinter import*
import threading
import time
import subprocess
import itertools
from itertools import*
import os
import platform


#funcion de tomar captura de pantalla
def tomar():
    if nombre.get() != '':
        so = platform.system()
        if so == 'Darwin':
            os.system("screencapture "+str(nombre.get())+".png")
        else:
            messagebox.showinfo(None,'Esta funcionalidad solo sirve para sistema operativo OS X')
            return
    else:
        messagebox.showinfo(None,'Debe ingresar el nombre del jugador')

#funcion de cargar juego
def cargar():
    global jugados
    global hacer,rehacer
    global horas,minutos,segundos
    global horas2,minutos2,segundos2
    global board,tablero
    global multiniv,ya,inicio
    ya = False
    inicio = '*'
    archi = open('kenken_juegoactual.dat','r')
    texto = archi.read()
    if len(texto) == 0:
        messagebox.showinfo(None,'No hay juegos salvados')
        return
    else:
        texto = ast.literal_eval(texto)
        archi.close
        indice = texto[0]
        jugados[indice] = False
        largo = texto[1]
        if largo == 3:
            x3.select()
        elif largo == 4:
            x4.select()
        elif largo == 5:
            x5.select()
        elif largo == 6:
            x6.select()
        elif largo == 7:
            x7.select()
        elif largo == 8:
            x8.select()
        elif largo == 9:
            x9.select()
        else:
            x10.select()
            multiniv = texto[14]
        relo = texto[2]
        if relo == 1:
            rs.select()
        elif relo == 2:
            rn.select()
        else:
            rt.select()
        lado = texto[3]
        if lado == 1:
            ld.select()
        else:
            li.select()
        soni = texto[4]
        if soni == 1:
            ss.select()
        else:
            sn.select()
        name = texto[5]
        nombre.set(name)
        nom.config(state='readonly')
        hacer = texto[6]
        rehacer = texto[7]
        horas = texto[8]
        minutos = texto[9]
        segundos = texto[10]
        horas2 = texto[11]
        minutos2 = texto[12]
        segundos2 = texto[13]
        creapartida()
        for i in hacer:
            if len(i) == 3:
                i[2] = str(i[2])
                board[i[0]][i[1]].config(text=i[2],compound='center')
                tablero[i[0]][i[1]] = i[2]
            else:
                board[i[0]][i[1]].config(text=i[2] + '\n' + str(i[3]))
                tablero[i[0]][i[1]] = i[3]
        return
        
        
        
        

# funcion de guardar juego
def guardar():
    global jugando,juegos
    global horas,minutos,segundos
    global horas2,minutos2,segundos2
    global hacer,rehacer
    global multiniv
    indice = juegos.index(jugando)
    largo = largotabla.get()
    relo = relojsi.get()
    lad = lado.get()
    son = soni.get()
    nom = nombre.get()
    a = [indice,largo,relo,lad,son,nom,hacer,rehacer,horas,minutos,segundos,horas2,minutos2,segundos2,multiniv]
    archivo = open('kenken_juegoactual.dat','w')
    archivo.write(str(a))
    messagebox.showinfo(None,'El juego fue guardado con exito!')
    archivo.close()
    
    
    
    
#funcion de deshacer
def undo():
    global hacer,tablero,board,rehacer,inicio
    if inicio == False:
        messagebox.showinfo(None,'El juego no ha empezado')
        return
    elif hacer == []:
        messagebox.showinfo(None,'No hay jugadas que se pueden deshacer')
        return
    else:
        if len(hacer) == 1:
            a = hacer.pop()
            rehacer.append(a)
            if len(a) == 3:
                board[a[0]][a[1]].config(text='')
                tablero[a[0]][a[1]] = 0
            else:
                board[a[0]][a[1]].config(text=a[2])
                tablero[a[0]][a[1]] = 0
        else:
            a = hacer.pop()
            rehacer.append(a)
            if len(a) == 3:
                for i in hacer[::-1]:
                    if len(i) == 3:
                        if i[0:2] == a[0:2]:
                            if i[2] == '':
                                board[i[0]][i[1]].config(text=i[2])
                                tablero[i[0]][i[1]] = 0
                                return
                            else:
                                board[i[0]][i[1]].config(text=i[2])
                                tablero[i[0]][i[1]] = i[2]
                                return
                        else:
                            pass
                    else:
                        pass
                else:
                    board[a[0]][a[1]].config(text='')
                    tablero[a[0]][a[1]] = 0           
            else:
                for j in hacer[::-1]:
                    if len(j) == 4:
                        if j[0:3] == a[0:3]:
                            if j[3] == '':
                                board[j[0]][j[1]].config(text=j[2])
                                tablero[j[0]][j[1]] = 0
                                return
                            else:
                                board[j[0]][j[1]].config(text=j[2] + '\n' + str(j[3]))
                                tablero[j[0]][j[1]] = j[3]
                                return                                                        
                        else:
                            pass
                    else:
                        pass
                else:
                    board[a[0]][a[1]].config(text=a[2])
                    tablero[a[0]][a[1]] = 0

#funcion de rehacer
def redo():
    global board,tablero,hacer,rehacer,inicio
    if inicio == False:
        messagebox.showinfo(None,'El juego no ha empezado')
        return
    elif rehacer == []:
        messagebox.showinfo(None,'No hay jugadas por rehacer')
        return
    else:
        a = rehacer[0]
        rehacer = rehacer[1:]
        hacer.append(a)
        if len(a) == 3:
            if a[2] == '':
                board[a[0]][a[1]].config(text=a[2])
                tablero[a[0]][a[1]] = 0
                return
            else:
                board[a[0]][a[1]].config(text=a[2])
                tablero[a[0]][a[1]] = a[2]
                return
        else:
            if a[3] == '':
                board[j[0]][j[1]].config(text=a[2])
                tablero[a[0]][a[1]] = 0
                return
            else:
                board[a[0]][a[1]].config(text=a[2] + '\n' + str(a[3]))
                tablero[a[0]][a[1]] = a[3]
                return
            
#funcion de ayuda
def ayudame():
    so = platform.system()
    if so == 'Darwin':
        messagebox.showinfo(title='Programa de juegos kenken',message='Autor: Jose Pablo Murillo\n'
                                                                                'Fecha: Junio 2014\n'
                                                                                'Este programa sirve para jugar kenken.')
        os.system('open kenken_manual_de_usuario.pdf')
    elif so == 'Windows':
        messagebox.showinfo(title='Programa de juegos kenken',message='Autor: Jose Pablo Murillo\n'
                                                                            'Fecha: Junio 2014\n'
                                                                            'Este programa sirve para jugar kenken.')
        os.startfile('enken_manual_de_usuario.pdf')
    else:
        messagebox.showinfo(title='Programa de juegos kenken',message='La funcion de abrir el pdf no esta posible en tu sistema operativo, debe abrir el archivo de manera manual')
        return
    
#funcion que cierra ventana principal
def adios():
    de = messagebox.askquestion(title='Ventana de salir',message='Seguro que desea salir?')
    if de == 'yes':
        messagebox.showinfo(title=None,message='Gracias por haber jugado Ken Ken v1.0')
        menu.destroy()
        return


#funcion para salir de ventana de juego
def nosalir():
    messagebox.showinfo(title=None,message='Debe salir usando los botones que estan en la ventana excepto el de la "x" arriba en la ventana')
    return

#funcion que modifica tiempo sugerido en caso de que haya reloj y cambie el largo de tabla
def moditiempo():
    if relojsi.get() == 3:
        n = largotabla.get()
        if n == 3:
            tiemposugerido.set('5')
        elif n == 4:
            tiemposugerido.set('15')
        elif n == 5:
            tiemposugerido.set('20')
        elif n == 6:
            tiemposugerido.set('30')
        elif n == 7:
            tiemposugerido.set('40')
        elif n == 8:
            tiemposugerido.set('50')
        elif n == 9:
            tiemposugerido.set('60')
        else:
            tiemposugerido.set('120')
    else:
        tiemposugerido.set('')
        l.grid_forget()
        
#funcion que borra tiempo sugerido
def borraopcion():
    e.grid_forget()
    l.grid_forget()
    global reloj,tempo
    reloj = False
    tempo = False
    
    
#funcion que deshabilita entrada de tiemposugerido
def sireloj():
    tiemposugerido.set('')
    l.grid_forget()
    e.grid_forget()
    global reloj,tempo
    reloj = True
    tempo = False


#funcion que aparece tiempos sugeridos de timer
def apareceopcion():
    l.grid(row=1,column=2)
    global tempo,reloj
    tempo = True
    reloj = False
    e.config(textvariable=tiemposugerido)
    e.grid(row=2,column=2)
    n = largotabla.get()
    if n == 3:
        tiemposugerido.set('5')
    elif n == 4:
        tiemposugerido.set('15')
    elif n == 5:
        tiemposugerido.set('20')
    elif n == 6:
        tiemposugerido.set('30')
    elif n == 7:
        tiemposugerido.set('40')
    elif n == 8:
        tiemposugerido.set('50')
    elif n == 9:
        tiemposugerido.set('60')
    else:
        tiemposugerido.set('120')


#funcion para salir de ventana de configuracion
def saliconfig():

    if largotabla.get() == 10:
        if relojsi.get() != 3:
            messagebox.showinfo(None,'Debe seleccionar el temporizador para multinivel')
            return
    if relojsi.get() == 3:
        try:
            int(tiemposugerido.get())
            if int(tiemposugerido.get()) <= 0:
                messagebox.showerror(None,'La cantidad de minutos debe ser mayor a 0')
                return
            else:
                configuracion.withdraw()
                menu.deiconify()
        except ValueError:
            messagebox.showinfo(title=None,message='El temporizador solo usa una cantidad numerica de minutos')
            tiemposugerido.set('')
            return
    else:
        configuracion.withdraw()
        menu.deiconify()

#funcion para llamar ventana de configuracion
def aparececonfig():
    menu.withdraw()
    configuracion.deiconify()

#funcion de empezar el temporizador
def empezartempo():
    global inicio,horas,minutos,segundos,horas2,minutos2,segundos2,mulniv
    minutos = int(tiemposugerido.get())
    if minutos == 60:
        hor = 1
        minutos = 0
    elif minutos > 60:
        hor = minutos//60
        minutos = minutos - hor*60
        while hor >= 0:
            while minutos >= 0:
                while segundos >= 0:
                    if inicio == True:
                        hori.config(text=hor)
                        minu.config(text=minutos)
                        segu.config(text=segundos)
                        segundos -= 1
                        segundos2 += 1
                        time.sleep(1)
                    elif inicio == False:
                        hori.config(text=hor)
                        minu.config(text=minutos)
                        segu.config(text=segundos)
                        time.sleep(1)
                    else:
                        if mulniv == True:
                            inicio = True
                        else:
                            return
                minutos -= 1
                segundos = 59
                segundos2 = 0
                minutos2 += 1
            hor -= 1
            minutos = 59
            segundos = 59
            horas2 += 1
            minutos2 = 0
            segundos2 = 0
    while minutos >= 0:
        while segundos >= 0:
            minu.config(text=minutos)
            segu.config(text=segundos)
            segundos -= 1
            segundos2 += 1
            time.sleep(1)
        minutos -= 1
        segundos = 59
        segundos2 = 0
        minutos2 += 1
    de = messagebox.askquestion(None,'El tiempo se acabo, desea seguir jugando?')
    if de == 'yes':
        rs.select()
        segundos2 = 0
        minutos2 = 0
        horas2 = 0
        segundos = 0
        minutos = int(tiemposugerido.get())
        if minutos == 60:
            horas = 1
            minutos = 0
        elif minutos > 60:
            horas = minutos//60
            minutos = minutos - hor*60
            
        
        return llamareloj()
    else:
        return terminar()

def empezareloj():
    global inicio,horas,minutos,segundos
    while horas <= 24:
        while minutos <= 59:
            while segundos <= 59:
                if inicio == True:
                    hori.config(text=horas)
                    minu.config(text=minutos)
                    segu.config(text=segundos)
                    segundos += 1
                    time.sleep(1)
                elif inicio == False:
                    hori.config(text=horas)
                    minu.config(text=minutos)
                    segu.config(text=segundos)
                    time.sleep(1)
                else:
                    return
            minutos += 1
            segundos = 0
        horas += 1
        minutos = 0
        segundos = 0
    messagebox.showinfo(None,'El tiempo ha superado el tiempo maximo')
    return terminar()


#funcion que llama a temporizador
def llamartempo():
    tempor = threading.Thread(target=empezartempo)
    tempor.start()

#funcion que llama a reloj
def llamareloj():
    relo = threading.Thread(target=empezareloj)
    relo.start()

#funcion de seleccionar un boton
def seleccionar(a,b):
    global board,elegido,posicion,especial,inicio
    if inicio == False:
        messagebox.showinfo(None,'No ha iniciado el juego')
        return
    elif elegido == True:
        messagebox.showinfo(None,'Debe seleccionar un numero a ingresar en la casilla seleccionada antes de \n seleccionar otra casilla')
        return
    elif especial == True:
        elegido = True
        especial = False
    else:
        elegido = True
        especial = False
        posicion = [a,b]
    board[a][b].config(image=normal)

#funcion que dice que no puede modificar celdas predefinidas de un valor
def nopuede():
    messagebox.showinfo(None,'Esta casilla tiene un valor predefinido que no se puede cambiar')
    return

    

#funcion que agarra numero de operacion en celdas con operacion
def seleccionarespecial(a,b,t):
    global operacion,elegido,board,posicion,especial,inicio
    if inicio == False:
        messagebox.showinfo(None,'No ha iniciado el juego')
        return
    elif elegido == True:
        messagebox.showinfo(None,'Debe seleccionar un numero a ingresar antes de seleccionar otra casilla')
        return
    else:
        posicion = [a,b]
        operacion = str(t)
        elegido = True
        especial = True
        board[a][b].config(image=elegida)

#funcion de borrar texto en casilla
def borrar():
    global inicio,operacion,posicion,especial,elegido,board,tablero,hacer
    if inicio == False:
        messagebox.showinfo(None,'No ha iniciado el juego')
        return
    elif elegido == False:
        messagebox.showinfo(None,'Debe seleccionar una casilla')
        return
    elif operacion == '':
        if especial == True:
            board[posicion[0]][posicion[1]].config(text='',image=jaula)
            tablero[posicion[0]][posicion[1]] = [0]
            hacer.append([posicion[0],posicion[1],''])
            elegido = False
            especial = False
        else:
            board[posicion[0]][posicion[1]].config(text='',image=casilla)
            tablero[posicion[0]][posicion[1]] = [0]
            hacer.append([posicion[0],posicion[1],''])
            elegido = False
            especial = False
    else:
        board[posicion[0]][posicion[1]].config(text=operacion,image=jaula)
        tablero[posicion[0]][posicion[1]] = [0]
        hacer.append([posicion[0],posicion[1],operacion,''])
        elegido = False
        especial = False
        operacion = ''
        

#funcion para habilitar chat
def chatear():
    messagebox.showinfo(None,'Envie mensajes a traves de IDLE de Python')
    import client

#funcion que cambia imagen de celdas que no tienen texto de operacion
def seleccionarespecial2(a,b):
    global elegido,board,posicion,especial,operacion,inicio
    if inicio == False:
        messagebox.showinfo(None,'No ha iniciado el juego')
        return
    elif elegido == True:
        messagebox.showinfo(None,'Debe seleccionar un numero a ingresar antes de seleccionar otra casilla')
        return
    else:
        posicion = [a,b]
        elegido = True
        especial = True
        operacion = ''
        board[a][b].config(image=elegida)

        

#funcion de colocar numero en casilla
def colocar(num):
    global posicion,elegido,board,tablero,operacion,especial,hacer
    if elegido == False:
        messagebox.showinfo(None,'Debe seleccionar una casilla antes de colocar un numero')
        return
    elif operacion == '':
        if especial == False:
            board[posicion[0]][posicion[1]].config(image=casilla,text='')
            board[posicion[0]][posicion[1]].config(image=casilla,text=num,compound='center')
            tablero[posicion[0]][posicion[1]] = num
            hacer.append([posicion[0],posicion[1],num])
            elegido = False
            especial = False
        else:
            board[posicion[0]][posicion[1]].config(image=jaula,text='')
            board[posicion[0]][posicion[1]].config(image=jaula,text=num,compound='center')
            tablero[posicion[0]][posicion[1]] = num
            hacer.append([posicion[0],posicion[1],num])
            elegido = False
            especial = False
    else:
        board[posicion[0]][posicion[1]].config(image=jaula,text=operacion+'\n'+str(num),compound='center')
        tablero[posicion[0]][posicion[1]] = num
        hacer.append([posicion[0],posicion[1],operacion,num])
        elegido = False
        especial = False
        operacion = ''


#funcion que inicia juego
def iniciar():
    global inicio,ya
    if nombre.get() == '':
        messagebox.showinfo(None,'Debe ingresar su nombre antes de empezar')
        return
    elif len(nombre.get()) < 3 or len(nombre.get())>30:
        messagebox.showinfo(None,'El nombre debe ser entre 3 y 30 caracteres')
        return
    else:
        ini.config(state='disabled')
        inicio = True
        nom.config(state='readonly')
        if relojsi.get() == 3:
            if ya == False:
                return llamartempo()
            else:
                pass
        elif relojsi.get() == 1:
            if ya == False:
                return llamareloj()
        else:
            pass

#funcion para continuar juego ya empezado
def continuar():
    global inicio
    inicio = True
    pau.config(text='Pausa',command=pausa)
    
#funcion que pausa tiempo
def pausa():
    global inicio
    inicio = False
    pau.config(text='Continuar',command=continuar)

#funcion para salir de ventana de top10 a principal
def adiostop10():
    lisb.delete(1,11)
    topd.withdraw()

#funcion para salir de ventana de top10 a ventana de juego
def adiostopdiez():
    global inicio
    inicio = True
    lisb.delete(1,11)
    topd.withdraw()

#funcion para imprimir records en un archivo
def imprima():
    archivo = open('posiciones.dat','r')
    archi = open('imprimir.dat','w')
    record = []
    todo = []
    archi.write('-----Record de jugadores KenKen-----\n')
    archi.write('(Posicion,(Tiempo,nombre,tabla))\n')
    for i in archivo:
        if int(i[-3]) == largotabla.get():
            record.append (i)
            todo.append(i)
        else:
            todo.append(i)
    record.sort()
    todo.sort()
    posi = 1
    indice = 0
    if len(record) < 10:
        if len(todo) < 10:
            for i in todo:
                archi.write(str((posi,ast.literal_eval(i)))+'\n')
                posi += 1
        else:
            while posi != 11:
                archi.write(str((posi,ast.literal_eval(todo[indice])))+'\n')
                posi += 1
                indice += 1
    else:
        for i in record:
            while posi != 11:
                archi.write(str((posi,ast.literal_eval(record[inidice])))+'\n')
                posi += 1
                indice += 1
    messagebox.showinfo(None,'Los marcadores han sido guardados')
    archivo.close()
    archi.close()


#funcion para ver top 10 desde ventana principal
def top10():
    archivo = open('posiciones.dat','r')
    b.config(command=adiostop10)
    record = []
    for i in archivo:
        record.append(i)
    record.sort()
    posi = 1
    indice = 0
    if len(record) < 10:
        for i in record:
            lisb.insert(END,(posi,eval(i)))
            posi += 1
    else:
        while posi != 11:
            lisb.insert(END,(posi,eval(record[indice])))
            posi += 1
            indice += 1
    lisb.pack()
    archivo.close()
    topd.deiconify()

#funcion para ver top 10 desde ventana de juego
def topdiez():
    b.config(command=adiostopdiez)
    archivo = open('posiciones.dat','r')
    record = []
    todo = []
    for i in archivo:
        if int(i[-3]) == largotabla.get():
            record.append(i)
            todo.append(i)
        else:
            todo.append(i)
    record.sort()
    todo.sort()
    posi = 1
    indice = 0
    if len(record) < 10:
        if len(todo) < 10:
            for i in todo:
                lisb.insert(END,(posi,eval(i)))
                posi += 1
        else:
            while posi != 11:
                lisb.insert(END,(posi,eval(todo[indice])))
                posi += 1
                indice += 1
    else:
        for i in record:
            while posi != 11:
                lisb.insert(END,(posi,eval(record[indice])))
                posi += 1
                indice += 1
    lisb.pack()
    archivo.close()
    topd.deiconify()
            
#funcion de agregar marcador a archivo
def agregar_marcador():
    global segundos,minutos,horas,horas2,minutos2,segundos2
    global multiniv,mulniv,solucionado
    if solucionado == True:
        if mulniv == False:
            return
        else:
            solucionado = False
            menu.withdraw()
            if multiniv == 9:
                messagebox.showinfo(None,'El ultimo nivel de multinivel ha sido completado!')
                multiniv = 3
                x10.select()
                mulniv = False
                x6.select()
                if soni.get() == 1:
                    subprocess.call(["afplay",'aplausos.wav'])
                return
            else:
                multiniv += 1
                x10.select()
                terminar()
                return creapartida()
            
    name = nombre.get()
    modo = largotabla.get()
    if relojsi.get() == 2:
        return terminar()
    elif relojsi.get() == 1:
        tiempo = str(horas)+':'+str(minutos)+':'+str(segundos)
    else:
        tiempo = str(horas2)+':'+str(minutos2)+':'+str(segundos2)

    archivo = open('posiciones.dat','a')
    archivo.write(str((tiempo,name,modo))+'\n')
    archivo.close()
    messagebox.showinfo(None,'El marcador ha sido guardado')
    return

#funcion que valida que operaciones de tablero esten correctas
def valida_op():
    global jugando,tablero,board
    global multiniv
    malo = False
    for i in list(jugando.keys()):
        opera = list(jugando[i])
        try:
            int(opera[0])
        except ValueError:
            valores = ''
            operacion = opera[0][-1]
            if operacion == 'x':
                operacion ='*'
            else:
                pass
            resul = int(opera[0][0:-1])
            for j in opera:
                if type(j) == str:
                    pass
                else:
                    valores += str(tablero[j[0]][j[1]]) + operacion
            valores = valores[0:-1]
            if eval(valores) == resul:
                pass
            else:
                malo = True
                for m in opera:
                    if type(m) == str:
                        pass
                    else:
                        board[j[0]][j[1]].config(image=error)
                        messagebox.showinfo(None,'Los valores en las jaulas no dan el resultado especificado')
                        return
    if malo == False:
        messagebox.showinfo(None,'Felicitaciones, has ganado!')
        if soni.get() == 1:
            subprocess.call(["afplay",'aplausos.wav'])
        else:
            pass
        return agregar_marcador()
    else:
        messagebox.showinfo(None,'No has ganado :(')
        if soni.get() == 1:
            subprocess.call(["afplay",'wua.wav'])
        else:
            pass
                                    
#funcion que valida que el tablero este correcto
def validar():
    global tablero,board
    malo = False
    #validar 0
    for i in range(0,len(tablero)):
        for j in range(0,len(tablero[0])):
            if tablero[i][j] == 0:
                board[i][j].config(image=error)
                malo = True
            else:
                pass
    #validar horizontal
    for i in tablero:
        for j in range(1,len(tablero)+1):
            if i.count(j) == 1:
                pass
            else:
                indice1 = tablero.index(i)
                for m in range(0,len(i)):
                    if tablero[indice1][m] == j:
                        board[indice1][m].config(image=error)
                        malo = True
                    else:
                        pass
    #validar vertical
    temporal = list(zip(*tablero))
    for i in range(0,len(temporal)):
        for j in range(0,len(temporal[0])):
            if tablero[i][j] == 0:
                board[i][j].config(image=error)
                malo = True
            else:
                pass
    for j in temporal:
        for m in range(1,len(temporal[0])+1):
            if j.count(m) == 1:
                pass
            else:
                indice2 = temporal.index(j)
                for n in range(0,len(j)):
                    if temporal[indice2][n] == m:
                        board[n][indice2].config(image=error)
                        malo = True
                    else:
                        pass
    if malo == True:
        messagebox.showinfo(None,'Aun tiene casillas con numeros repetidos')
        return
    else:
        return valida_op()

#funcion para terminar el juego
def terminar():
    global inicio,ya
    global board,jugando,tablero,valores,alfabeto,juegos,ini,pau
    global horas, minutos, segundos
    global horas2,minutos2,segundos2
    global hacer, rehacer
    global error2,mulniv
    global flag, solucionado,flag,error2
    if mulniv == True:
        solucionado = False
        glag = False
        error2 = 0
        ken.withdraw()
        tiemposugerido.set(str(horas*60+minutos+segundos%60))
        nombre.set(nombre.get())
        inicio = True
        ya = True
        pau.config(text='pausa',command = pausa)
        for i in range(0,len(board)):
            for j in range(0,len(board)):
                board[i][j].grid_forget()
            board = list()
            tablero = list()
            valores = list()
            alfabeto = list()
            hacer = list()
            rehacer = list()
        dic = jugando
        for i in list(dic.keys()):
            temp = []
            for j in list(dic[i]):
                if type(j) == str:
                    temp.append(j)
                elif type(j) == tuple:
                    j = list(j)
                    j[0] += 1
                    j[1] += 1
                    j = tuple(j)
                    temp.append(j)                       
                dic[i] = tuple(temp)
        dic = jugando
        for i in valores:
            i.grid_forget()
        vali.grid_forget()
        otro.grid_forget()
        reini.grid_forget()
        termi.grid_forget()
        top.grid_forget()
        chat.grid_forget()
        pau.grid_forget()
        sav.grid_forget()
        resol.grid_forget()
        sol.grid_forget()
        pic.grid_forget()
        l.grid_forget()
        e.grid_forget()
        borr.grid_forget()
    else:
        de = messagebox.askquestion(None,'Desea terminar el juego?')
        if de == 'no':
            return
        else:
            ken.withdraw()

            solucionado = False
            flag = False
            error2 = 0
            if relojsi.get() == 2:
                pass
            elif relojsi.get() == 1:
                horas = 0
                minutos = 0
                segundos = 0
                horas2 = 0
                minutos2 = 0
                segundos2 = 0
                hori.config(text='')
                minu.config(text='')
                segu.config(text='')
            elif relojsi.get() == 3:
                segundos = 0
                minutos = 0
                horas = 0
                horas2 = 0
                minutos2 = 0
                segundos2 = 0
                hori.config(text='')
                minu.config(text='')
                segu.config(text='')
            else:
                pass
            inicio = '*'
            ya = True
            ini.config(state='normal')
            pau.config(text='pausa',command=pausa)
            for i in range(0,len(board)):
                for j in range(0,len(board[0])):
                    board[i][j].grid_forget()
            board = list()
            tablero = list()
            valores = list()
            alfabeto = list()
            hacer = list()
            rehacer = list()
            dic = jugando
            for i in list(dic.keys()):
                temp = []
                for j in list(dic[i]):
                    if type(j) == str:
                        temp.append(j)
                    elif type(j) == tuple:
                        j = list(j)
                        j[0] += 1
                        j[1] += 1
                        j = tuple(j)
                        temp.append(j)
                dic[i] = tuple(temp)
                temp = []
            for i in valores:
                i.grid_forget()
            nom.config(state='normal')
            nombre.set('')
            hori.grid_forget()
            minu.grid_forget()
            segu .grid_forget()
            vali.grid_forget()
            otro.grid_forget()
            reini.grid_forget()
            termi.grid_forget()
            top.grid_forget()
            pau.grid_forget()
            l.grid_forget()
            e.grid_forget()
            borr.grid_forget()
            menu.deiconify()
            sav.grid_forget()
            resol.grid_forget()
            sol.grid_forget()
            pic.grid_forget()
            menu.deiconify()
                       
#funcion para llamar a un nuevo juego
def nuevo():
    global inicio,ya
    global board,jugando,tablero,valores,alfabeto,juegos,ini,pau,malo
    global horas, minutos, segundos
    global hacer, rehacer
    if inicio == False:
        messagebox.showerror(None,'El juego no ha iniciado')
        return
    de = messagebox.askquestion(None,'Seguro que quiere empezar otro juego?')
    if de == 'no':
        return
    if relojsi.get() == 1:
        horas = 0
        minutos = 0
        segundos = 0
    elif relojsi.get() == 3:
        segundos = 0
        minutos = int(tiemposugerido.get())
        horas = minutos//10
        minutos = minutos - horas*60
    inicio = False
    ya = True
    ini.config(state='normal')
    pau.config(text='Pausa',command=pausa)
    board = list()
    tablero = list()
    valores = list()
    alfabeto = list()
    hacer = list()
    rehacer = list()
    malo = False
    indice = juegos.index(jugando)
    dic = juegos[indice]
    for i in list(dic.keys()):
        temp = []
        for j in list(dic[i]):
            if type(j) == str:
                temp.append(j)
            elif type(j) == tuple:
                j = list(j)
                j[0] += 1
                j[1] += 1
                j = tuple(j)
                temp.append(j)
            else:
                pass
        dic[i] = tuple(temp)
        temp = []

    hori.grid_forget()
    minu.grid_forget()
    segu .grid_forget()
    ini.grid_forget()
    vali.grid_forget()
    otro.grid_forget()
    reini.grid_forget()
    termi.grid_forget()
    top.grid_forget()
    pau.grid_forget()
    ken.withdraw()
    l.grid_forget()
    e.grid_forget()
    borr.grid_forget()
    sav.grid_forget()
    resol.grid_forget()
    sol.grid_forget()
    pic.grid_forget()
    return creapartida()

#funcion de reiniciar
def reiniciar():
    global inicio,ya
    if inicio == False:
        messagebox.showinfo(None,'El juego no ha empezado')
        return
    de = messagebox.askquestion(None,'Desea reiniciar el juego?')
    if de == 'no':
        return
    else:
        global jugados,jugando,juegos,jugados,minutos,segundos,horas
        global horas2,minutos2,segundos2
        global hacer,rehacer
        indice = juegos.index(jugando)
        dic = juegos[indice]
        jugados[indice] = False
        for i in list(dic.keys()):
            temp = []
            for j in list(dic[i]):
                if type(j) == str:
                    temp.append(j)
                elif type(j) == tuple:
                    j = list(j)
                    j[0] += 1
                    j[1] += 1
                    j = tuple(j)
                    temp.append(j)
                else:
                    pass
            dic[i] = tuple(temp)
            temp = []
        if relojsi.get() == 1:
            horas = 0
            minutos = 0
            segundos = 0
            horas2 = 0
            minutos2 = 0
            segundos2 = 0
        elif relojsi.get() == 3:
            segundos = 0
            minutos = int(tiemposugerido.get())
            horas = minutos//10
            minutos = minutos - horas*60
            horas2 = 0
            minutos2 = 0
            segundos2 = 0
    hacer = list()
    rehacer = list()
    inicio = False
    ini.config(state='normal')
        
    ya = True
    return creapartida()

#funcion para salir de ventana de soluciones
def salirsolu():
    solulb.delete(0,END)
    solu.withdraw()
    

#funcion para agregar soluciones a tablero
def agregarsolucion():
    global posicion, jugando,board,tablero
    poner = eval(solulb.get(solulb.curselection()[0]))
    for i in list(jugando.keys()):
        if posicion in list(jugando[i]):
            posiciones = list(jugando[i])[1:]
            cont = 0
            for i in posiciones:
                board[i[0]][i[1]].invoke()
                colocar(poner[0][cont])
                cont +=1
            messagebox.showinfo(None,'La solucion ha sido implementada')
            solu.withdraw()
            solulb.delete(0,END)
        else:
            pass
            
    
#funcion que pone soluciones posibles en ventana de soluciones
def ponersoluciones(posibles):
    for i in posibles:
        solulb.insert(END,i)
    solu.deiconify()
    messagebox.showinfo(None,'Seleccione la solucion que desea ingresar')
    return

#funcion que genera soluciones posibles de juego       
def soluciones():
    global inicio,alfabeto,jugando,elegido,posicion,board,elegido
    if inicio == False:
        messagebox.showinfo(None,'El juego no ha empezado')
        return
    elif elegido == False:
        messagebox.showinfo(None,'Debe seleccionar una celda de una jaula')
        return
    else:
        board[posicion[0]][posicion[1]].config(image=jaula)
        elegido = False
        posicion = tuple(posicion)
        for i in list(jugando.keys()):
            if posicion in list(jugando[i]):
                if len(list(jugando[i])) == 2:
                    messagebox.showinfo(None,'No hay soluciones posibles para jaulas con numeros preestablecidos')
                    return
                else:
                    num = int(list(jugando[i])[0][0:-1])
                    operacion = (jugando[i][0][-1])
                    if operacion == 'x' or posicion == 'X':
                        operacion = '*'
                    cant = len(list(jugando[i]))-1
                    posibles = []
                    todos = list(itertools.product(alfabeto,repeat=cant))
                                
                    for i in todos:
                        resuelva = ''
                        for j in i:
                            resuelva +=(str(j)+operacion)
                        resuelva = resuelva[0:-1]
                        if eval(resuelva) == num:
                            posibles.append([i])
                        else:
                            pass
                    return ponersoluciones(posibles)              
            else:
                pass
                                    
    

#funcion para multinivel
def multi():
    global multiniv,mulniv
    mulniv = True
    if multiniv == 3:
        largotabla.set(3)
    elif multiniv == 4:
        largotabla.set(4)
    elif multiniv == 5:
        largotabla.set(5)
    elif multiniv == 6:
        largotabla.set(6)
    elif multiniv == 7:
        largotabla.set(7)
    elif multiniv == 8:
        largotabla.set(8)
    elif multiniv == 9:
        largotabla.set(9)
    return creapartida()

SudokuBoard=[]

flag = False   

#verifica si hay 0 en el tablero
def es_correcto(board):
    global error2
    
    inicio_de_validacion(board)

    if error2 ==1:
        error2=0
        return False
    elif error2==0:
        return True
    
def inicio_de_validacion(board):
    global jugando
    a=jugando
    for i in a.values():
        validar_de_verdad(i,board)
    return
#agrara un elemento del diccionario y separa el operador del numero, tambien agarra los valores de la matriz en la tuple de la llave#
def validar_de_verdad(i,board):
        opera=""
        numero=""
        resul=[]
        lugar=[]
        for j in i:
            if type(j)==str:
                if operador(j)!="":
                    opera=operador(j)
                    numero=obtener_numero(j)
                else:
                    opera="#"
                    numero=obtener_numero(j)
            elif type(j)==tuple:
                lugar+=[j]
                resul+=[board[j[0]][j[1]]]
            
        resul.sort(reverse=True)
        return comprobar(resul,lugar,numero,opera,board)

#obtiene el numero de in string#
def obtener_numero(string):
    resul=""
    for j in string:
        if j=="0" or j=="1" or j=="2" or j=="3" or j=="4" or j=="5" or j=="6" or j=="7" or j=="8" or j=="9":
            resul+=j
    return resul
    
                
            

#saca el operador de un string#    
def operador(string):
    resul=""
    for i in string:
        if i=="+":
            resul="+"
        elif i=="/":
            resul="/"
        elif i=="x":
            resul="x"
        elif i=="-":
            resul="-"
    return resul
#esta funcion agarra los valoresde la matriz y ve que si operados dan el numero#
def comprobar(resultados,lugar,numero,oper,board):
    global error2
    if oper=="-":
        final=0
        for i in resultados:
            final-=int(i)
            final=abs(final)
        if int(final)==int(numero):
            pass
        else:
            error2=1
    
    elif oper=="+":
        final=0
        for i in resultados:
            final+=i
        if int(final)==int(numero):
            pass
        else:
            error2=1
        
    elif oper=="x":
        final=1
        
        for i in resultados:
            final*=i
        
        if int(final)==int(numero):
            pass
        else:
            
            error2=1
            
        
    elif oper=="/":
        if 0 in resultados:
            error2=1
        else:
            final=0
        
            for i in resultados:
                if final==0:
                    final+=int(i)
                else:
                    final/=int(i)
            
            if final==int(numero):
                pass
            else:
                error2=1
    elif oper=="#":
        final=0
        i=lugar[0][0]
        j=lugar[0][1]
        final=board[i][j]
        if int(final)==int(numero):
            pass
        else:
            error=1

#funcion que verifica si tablero esta lleno               
def isFull(board) :
    for x in range(0, len(board)):
        for y in range (0, len(board)):
            if board[x][y] == 0:
                return False
    return True
    
# funcion que encuentra posibles soluciones que cumplan con reglas de tablero
def possibleEntries(board, i, j):
    
    possibilityArray = {}
    
    for x in range (1, len(board)+1):
        possibilityArray[x] = 0
    
    #For horizontal entries
    for y in range (0, len(board)):
        if not board[i][y] == 0: 
            possibilityArray[board[i][y]] = 1
     
    #For vertical entries
    for x in range (0, len(board)):
        if not board[x][j] == 0: 
            possibilityArray[board[x][j]] = 1
            
       
    
    for x in range (1, len(board)+1):
        if possibilityArray[x] == 0:
            possibilityArray[x] = x
        else:
            possibilityArray[x] = 0
    
    return possibilityArray

 

#funcion qe despliega matriz resuelta
def resuelto():
    global tablero,board,solucionado,inicio
    for i in range(0,len(tablero)):
        for j in range(0,len(tablero)):
            inicio = True
            board[i][j].invoke()
            colocar(tablero[i][j])
            inicio = False
    messagebox.showinfo(None,'Juego resuelto')
    solucionado = True
    return agregar_marcador()

#funcion que resuelve juego recursivamente
def sudokuSolver(board):
    global flag
    if flag == True:
        return tablero
    
    i = 0
    j = 0
    
    possiblities = {}
    
    if isFull(board) and es_correcto(board):
        for i in range(0,len(board)):
            for j in range(0,len(board)):
                tablero[i][j]=board[i][j]
        flag = True
        return resuelto()   
    else:
        for x in range (0, len(board)):
            for y in range (0,len(board)):
                if board[x][y] == 0:
                    i = x
                    j = y
                    break
            else:
                continue
            break
        
        possiblities = possibleEntries(board, i, j)
        
        for x in range (1, len(board)+1):
            if not possiblities[x] == 0:
                board[i][j] = possiblities[x]
                #file.write(printFileBoard(board))
                sudokuSolver(board)
        # backtrack
        board[i][j] = 0

def main():
    global SudokuBoard,tablero,inicio
    if inicio == False:
        messagebox.showinfo(None,'El juego debe estar corriendo')
        return
    pausa()
    SudokuBoard = list(tablero)
    for i in range(0,len(SudokuBoard)):
        for j in range(0,len(SudokuBoard)):
            SudokuBoard[i][j] = 0
    

    return sudokuSolver(SudokuBoard)
        
            
        
   
    
#funcion de crear tablero de juego
def creapartida():
    menu.withdraw()
    global maximos,juegos,jugados,matriz,tablero,valores,alfabeto,board,jugando
    tabla = largotabla.get()
    colores = ['black','green','blue','yellow','orange','purple']
    if tabla == 10:
        return multi()
    elif tabla not in maximos:
        messagebox.showerror(title=None,message='No existen juegos para ese nivel de dificultad, cambie el nivel de dificultad')
        return
    else:
        cont = 0
        while cont != len(maximos):
            if maximos[cont] == tabla:
                if  jugados[cont] == False:
                    jugados[cont] = True
                    dic = juegos[cont]
                    for i in list(dic.keys()):
                        temp = []
                        for j in list(dic[i]):
                            if type(j) == str:
                                temp.append(j)
                            elif type(j) == tuple:
                                j = list(j)
                                j[0] -= 1
                                j[1] -= 1
                                j = tuple(j)
                                temp.append(j)
                            else:
                                pass
                        dic[i] = tuple(temp)
                        temp = []
                    jugando = dict(juegos[cont])
                    board = list(matriz)
                    if len(board) == tabla and len(board[0]) == tabla:
                        pass                       
                    else:
                        while len(board[0]) != tabla:
                            for i in board:
                                i.append([])
                        while len(board) != tabla:
                            board.append([[]]*tabla)

                    fil = 0
                    col = 0
                    for i in range(0,len(board)):
                        for j in range(0,len(board[0])):
                            board[i][j] = Button(ken,image=casilla,command = lambda a = i,b=j: seleccionar(a,b))
                            board[i][j].grid(row=i,column=j,sticky=W+E+N+S)
                    while len(tablero) != tabla:
                        tablero.append([0]*tabla)

                    contcolor = 0
                    for i in list(juegos[cont].values()):
                        for j in i:
                            if contcolor+1 == len(colores):
                                contcolor = 0
                            else:
                                pass
                            if type(j) == str:
                                contcolor += 1
                                texto = str(j)
                                lugar = tuple(i[1])
                                try:
                                    int(texto)
                                    tablero[lugar[0]][lugar[1]] = int(texto)
                                    board[lugar[0]][lugar[1]].config(width=1,height=1,text=texto,image=jaula,compound='center',state=DISABLED)
                                except ValueError:
                                    board[lugar[0]][lugar[1]].config(width=1,height=1,text=texto,image=jaula,compound='center',highlightbackground=colores[contcolor],command=lambda a=lugar[0],b=lugar[1],t=texto: seleccionarespecial(a,b,t))
                            elif type(j) == tuple:
                                if j == lugar:
                                    pass
                                else:
                                    board[j[0]][j[1]].config(image=jaula,highlightbackground=colores[contcolor],command=lambda a = j[0],b=j[1]: seleccionarespecial2 (a,b))

                    if tabla == 3:
                        valores = [1,2,3]
                    elif tabla == 4:
                        valores = [1,2,3,4]
                    elif tabla == 5:
                        valores = [1,2,3,4,5]
                    elif tabla == 6:
                        valores = [1,2,3,4,5,6]
                    elif tabla == 7:
                        valores = [1,2,3,4,5,6,7]
                    elif tabla == 8:
                        valores = [1,2,3,4,5,6,7,8]
                    else:
                        valores = list(alfabeto)
                        
                    fil = 0
                    col = len(tablero)
                    alfabeto = list(valores)
                    for i in valores:
                        i = Button(ken,text=str(i),image=bola,compound='center',command=lambda num=i: colocar (num))
                        i.grid(row=fil,column=col,sticky=W+E+N+S)
                        if lado.get() == 2:
                            pass
                        else:
                            i.grid(row=fil,column=3)
                        fil += 1
                    borr.config(image=borrador,command=borrar)
                    borr.grid(row=fil,column=col,sticky=W+E+N+S)
                    col = 0
                    ini.config(text='Iniciar Juego',command=iniciar)
                    ini.grid(row=fil+1,column=col)
                    vali.config(text='Validar Juego',command=validar)
                    vali.grid(row=fil+1,column=col+1)
                    otro.config(text='Otro Juego',command=nuevo)
                    otro.grid(row = fil+1,column=col+2)
                    reini.config(text='Reiniciar juego',command=reiniciar)
                    reini.grid(row=fil+1,column=col+3)
                    termi.config(text='Terminar juego',command=terminar)
                    termi.grid(row=fil+1,column=col+4)
                    top.config(text='Top 10',command=topdiez)
                    top.grid(row=fil+1,column=col+5)
                    sol.config(text='Soluciones posibles',command=soluciones)
                    sol.grid(row=fil+1,column=col+6)
                    pic.config(text='Tomar foto',command=tomar)
                    pic.grid(row=fil+1,column=col+7)
                    chat.config(text='Chatear',command=chatear)
                    chat.grid(row=fil+1,column=col+8)
                    resol.config(text='Solucionar juego',command=main)
                    resol.grid(row=fil+2,column=col+3)
                    l = Label(ken,text='Nombre de jugador')
                    l.grid(row=+fil+2,column=col)
                    nom.grid(row=fil+2,column=col+1)
                    sav.config(text='Salvar juego',command=guardar)
                    sav.grid(row=fil+2,column=col+2)
                    col = fil + 1
                    if relojsi.get() == 3:
                        lb = Label(ken,text='Tiempo restante:')
                        lb.grid(row=0,column=col)
                        lb2 = Label(ken,text='Horas:')
                        lb2.grid(row=1,column=col)
                        lb3 = Label(ken,text='Minutos:')
                        lb3.grid(row=1,column=col+1)
                        lb4 = Label(ken,text='Segundos:')
                        lb4.grid(row=1,column=col+2)
                        hori.grid(row=2,column=col)
                        minu.grid(row=2,column=col+1)
                        segu.grid(row=2,column=col+2)
                        pau.config(text='Pausa',command=pausa)
                        pau.grid(row=3,column=col)
                    elif relojsi.get() == 1:
                        lb = Label(ken,text='Tiempo transcurrido:')
                        lb.grid(row=0,column=col)
                        lb2 = Label(ken,text='Horas:')
                        lb2.grid(row=1,column=col)
                        lb3 = Label(ken,text='Minutos:')
                        lb3.grid(row=1,column=col+1)
                        lb4 = Label(ken,text='Segundos:')
                        lb4.grid(row=1,column=col+2)
                        hori.grid(row=2,column=col)
                        minu.grid(row=2,column=col+1)
                        segu.grid(row=2,column=col+2)
                        pau.config(text='Pausa',command=pausa)
                        pau.grid(row=3,column=col)
                    else:
                        pass
                        
                    if lado.get() == 2:
                        pass
                    else:
                        if relojsi.get() == 1 or relojsi.get() == 3:
                            lb.grid(row=0,column=0)
                            lb2.grid(row=1,column=0)
                            lb3.grid(row=1,column=1)
                            lb4.grid(row=1,column=2)
                            pau.grid(row=3,column=0)
                            hori.grid(row=2,column=0)
                            minu.grid(row=2,column=1)
                            segu.grid(row=2,column=2)
                        
                        
                            
                        fil = 0
                        col = 4
                        for i in range(0,len(board)):
                            for j in range(0,len(board[0])):
                                board[i][j].grid(row=fil,column=col)
                                col += 1
                            else:
                                col = 4
                                fil += 1
                        borr.grid(row=fil,column=3)
                    ken.deiconify()
                    return
                else:
                    cont += 1
            else:
                cont += 1
        for i in range(0,len(jugados)):
            jugados[i] = False
        return creapartida()

#ventanas

#ventana principal

menu = tkinter.Tk()

#imagenes
logo = PhotoImage(file='kenken_logo.gif')
jaula = PhotoImage(file='jaula.gif')
casilla = PhotoImage(file='casilla.gif')
elegida = PhotoImage(file='casillaelegida.gif')
bola = PhotoImage(file='bolita.gif')
normal = PhotoImage(file='elegida.gif')
borrador = PhotoImage(file='borrador.gif')
error = PhotoImage(file='error.gif')
#Variables
largotabla = IntVar()
relojsi = IntVar()
tiemposugerido = StringVar()
lado = IntVar()
soni = IntVar()
nombre = StringVar()

#imagenes

#globales
indice1 = 0
indice2 = 0
horas = 0
minutos = 0
segundos = 0
horas2 = 0
minutos2 = 0
segundos2 = 0
error2 = 0
multiniv = 3
diccionario = {}
jugando = {}
inicio = False
reloj = False
tempo = False
elegido = False
especial = False
ya = False
mulniv = False
solucionado = False
posicion = list()
juegos = list()
jugados = list()
maximos = list()
maximotempo = list()
matriz = [[[],[],[]],
          [[],[],[]],
          [[],[],[]]]
tablero = []
board = list()
hacer = list()
rehacer = list()
valores = []
alfabeto = [1,2,3,4,5,6,7,8,9]
operacion = ''
kenkentabla = list()

#Agarrar juegos de archivo

#abrir archivo y agregar todos los juegos
archivo = open('kenken_juegos.dat','r')
texto = archivo.read()
while indice2 != len(texto):
    if texto[indice2] != '}':
        indice2 += 1
    else:
        indice2 += 1
        juego = texto[indice1:indice2]
        diccionario = ast.literal_eval(juego)
        juegos.append(diccionario)
        indice1 = indice2

for i in juegos:
    juegotem = list(i.values())
    for j in juegotem:
        for l in j[1:]:
            maximotem = max(l)
            maximotempo.append(maximotem)
    maximos.append(max(maximotempo))
    maximotempo = []
    
for i in range(0,len(juegos)):
    jugados.append(False)
archivo.close()
    
##GUI
menu.title('Menu principal')
menu.geometry('550x550')
l1 = Label(menu,image=logo).pack()
l2 = Label(menu,text='Un juego de aritmetica!',font=("Times New Roman",24)).pack()
b1 = Button(menu,text='Configuracion',font=("Times New Roman",20),command=aparececonfig).pack()
b2 = Button(menu,text='Nueva partida',font=("Times New Roman",20),command=creapartida).pack()
b3 = Button(menu,text='Top 10 mejores',command=top10,font=("Times New Roman",20)).pack()
b4 = Button(menu,text='Cargar juego',font=("Times New Roman",20),command=cargar).pack()
b5 = Button(menu,text='Ayuda',font=("Times New Roman",20),command=ayudame).pack()
b6 = Button(menu,text='Salir',command=adios,font=("Times New Roman",20)).pack()



#ventana de configuracion

configuracion = Toplevel()
configuracion.geometry('680x550')
configuracion.title('Configuracion')
c = Label(configuracion,text='Configuracion de juego:',font=("Times New Roman",20)).grid(row=0,column=1)
l2 = Label(configuracion,text='Nivel de dificultad:',font=("Times New Roman",14))
l2.grid(row=1,column=0)
x3 = Radiobutton(configuracion,value=3,text='3x3',variable=largotabla,command=moditiempo)
x3.grid(row=2,column=0)
x4 = Radiobutton(configuracion,value=4,text='4x4',variable=largotabla,command=moditiempo)
x4.grid(row=3,column=0)
x5 = Radiobutton(configuracion,value=5,text='5x5',variable=largotabla,command=moditiempo)
x5.grid(row=4,column=0)
x6 = Radiobutton(configuracion,value=6,text='6x6',variable=largotabla,command=moditiempo)
x6.select()
x6.grid(row=5,column=0)
x7 = Radiobutton(configuracion,value=7,text='7x7',variable=largotabla,command=moditiempo)
x7.grid(row=6,column=0)
x8 = Radiobutton(configuracion,value=8,text='8x8',variable=largotabla,command=moditiempo)
x8.grid(row=7,column=0)
x9 = Radiobutton(configuracion,value=9,text='9x9',variable=largotabla,command=moditiempo)
x9.grid(row=8,column=0)

x10 = Radiobutton(configuracion,value=10,text='Multinivel',variable=largotabla,command=moditiempo)
x10.grid(row=9,column=0)

r = Label(configuracion,text='Uso de reloj:',font=("Times New Roman",14)).grid(row=1,column=1)
rs = Radiobutton(configuracion,value=1,text='Si',variable=relojsi,command=sireloj)
rs.select()
rs.grid(row=2,column=1)
rn = Radiobutton(configuracion,value=2,text='No',font=("Times New Roman",14),variable=relojsi,command=borraopcion)
rn.grid(row=3,column=1)
rt = Radiobutton(configuracion,value=3,text='Timer',font=("Times New Roman",14),variable=relojsi,command=apareceopcion)
rt.grid(row=4,column=1)

l3 = Label(configuracion,text='Posicion de panel de numeros y borrador:',font=("Times New Roman",14)).grid(row=5,column=1)
ld = Radiobutton(configuracion,value=1,text='Derecha',font=("Times New Roman",14),variable=lado)
ld.grid(row=6,column=1)
ld.select()
li = Radiobutton(configuracion,value=2,text='Izquierda',font=("Times New Roman",14),variable=lado)
li.grid(row=7,column=1)
s = Label(configuracion,text='Sonido cuando gana el juego:',font=("Times New Roman",14)).grid(row=8,column=1)
ss = Radiobutton(configuracion,value=1,text='Si',variable=soni)
ss.grid(row=9,column=1)
sn = Radiobutton(configuracion,value=2,text='No',variable=soni)
sn.grid(row=10,column=1)
sn.select()
          
lis = Button(configuracion,text='Listo',command=saliconfig)
lis.grid(row=11,column=1)

l = Label(configuracion,text='Tiempos recomendados en minutos (puede modificarlo):',font=("Times New Roman",14))
e = Entry(configuracion)
configuracion.protocol('WM_DELETE_WINDOW',nosalir)
configuracion.withdraw()

#ventana del juego
ken = Toplevel()
ken.title('Ken Ken')
ken.protocol('WM_DELETE_WINDOW',nosalir)
barraMenu = Menu(ken)
menuEditar = Menu(barraMenu)
menuEditar.add_command(label='Deshacer',command=undo)
menuEditar.add_command(label='Rehacer',command=redo)
barraMenu.add_cascade(label='Editar',menu=menuEditar)
ken.config(menu=barraMenu)
hori = Label(ken)
minu = Label(ken)
segu = Label(ken)
ini = Button(ken)
vali = Button(ken)
otro = Button(ken)
reini = Button(ken)
termi = Button(ken)
top = Button(ken)
pau = Button(ken)
sol = Button(ken)
pic = Button(ken)
sav = Button(ken)
borr = Button(ken)
chat = Button(ken)
resol = Button(ken)
nom = Entry(ken,textvariable=nombre)
ken.withdraw()

#ventana de top10
topd = Toplevel()
topd.title('Top 10 jugadores')
topd.protocol('WM_DELETE_WINDOW',nosalir)
b = Button(topd,text='Listo',command=adiostop10)
prin = Button(topd,text='Imprimir',command=imprima)
lisb = Listbox(topd)
lisb.insert(END,('posicion','tie','nom','tabla'))
b.pack()
prin.pack()
topd.withdraw()

#ventana de soluciones posibles
solu = Toplevel()
solu.title('Soluciones posibles')
solu.protocol('WM_DELETE_WINDOW',nosalir)
soluf = Frame(solu)
sols = Scrollbar(soluf)
sols.pack(side=RIGHT,fill=Y)
solulb = Listbox(soluf,selectmode=SINGLE)
sols['command'] = solulb.yview()
solulb['yscrollcommand'] = sols.set
sl = Label(solu,text='Estas son las soluciones posibles').pack()
soluf.pack()
solulb.pack()
solub = Button(solu,text='Poner solucion',command=agregarsolucion)
solub.pack()
solub2 = Button(solu,text='Listo',command=salirsolu)
solub2.pack()
solu.withdraw()

menu.mainloop()

