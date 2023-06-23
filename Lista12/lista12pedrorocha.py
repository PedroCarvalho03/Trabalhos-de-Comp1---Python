import tkinter as tk

class somatorio():
    def __init__(self,janela) :
        self.janela = janela
        self.frame = tk.Frame(self.janela)
        self.frame.grid(row=0,column=0,rowspan=4,columnspan=2)
        
        self.entryNumeros = tk.Entry(self.frame)
        self.entryNumeros.grid(row=2,columnspan=2)
        
        self.LabelNumeros = tk.Label(self.frame,\
                                     text = '')
        self.LabelNumeros.grid(row=1,columnspan=2)
        
        self.butao1 = tk.Button(self.frame,\
                                text = '+',\
                                command = self.Mais)
        self.butao1.grid(row=3,column = 0)
        
        self.butao2 = tk.Button(self.frame,\
                                text = '=',\
                                command = self.Igual)
        self.butao2.grid(row=3,column = 1)
        
        
        self.LabelResultado = tk.Label(self.frame,\
                                       text = 'Resultado: ')
        self.LabelResultado.grid(row=4,columnspan=2)
        
        self.texto = ''
        self.soma = 0
    def Mais(self):
        self.LabelResultado['text'] = 'Resultado: '
        texto = (self.entryNumeros.get())
        valor = float(self.entryNumeros.get())
        if len(texto) != 0 :
            self.soma = valor + self.soma
            self.texto = self.texto + str(texto) + '+'
            self.LabelNumeros['text'] = self.texto
            self.entryNumeros.delete(0,'end')
        
    def Igual(self):
        valor = (self.entryNumeros.get())
        if len(valor) != 0:
            self.soma = self.soma + float(valor)
            self.entryNumeros.delete(0,'end')
            self.texto = ''
            self.LabelNumeros['text'] = ''
            self.LabelResultado['text'] = 'Resultado: ' + str(self.soma)
            self.soma = 0
            
        
if __name__ == '__main__':
    
    janelaPrincipal = tk.Tk()

    jogo = somatorio(janelaPrincipal)

    janelaPrincipal.mainloop()

