import tkinter as tk
from tkinter import scrolledtext, messagebox
from deep_translator import GoogleTranslator

# Função para traduzir
def traduzir():
    texto = entrada_texto.get("1.0", tk.END).strip()
    if not texto:
        messagebox.showwarning("Aviso", "Digite um texto para traduzir!")
        return
    
    idioma_origem = idioma_var.get()
    
    saida_texto.config(state=tk.NORMAL)
    saida_texto.delete("1.0", tk.END)
    
    try:
        if idioma_origem == "hr":  # Croata para outros
            idiomas = {
                "pt": "Português (Brasil)",
                "es": "Espanhol",
                "en": "Inglês"
            }
            for codigo, nome in idiomas.items():
                traducao = GoogleTranslator(source="hr", target=codigo).translate(texto)
                saida_texto.insert(tk.END, f"{nome}: {traducao}\n\n")
        
        else:  # Outro idioma para croata
            traducao = GoogleTranslator(source=idioma_origem, target="hr").translate(texto)
            saida_texto.insert(tk.END, f"Croata: {traducao}\n\n")
    
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")
    
    saida_texto.config(state=tk.DISABLED)

# Criar janela
janela = tk.Tk()
janela.title("Tradutor Croata ↔ PT / ES / EN")
janela.geometry("520x480")

# Menu de seleção do idioma de origem
tk.Label(janela, text="Selecione o idioma de origem:").pack(pady=5)
idioma_var = tk.StringVar(value="hr")
opcoes_idiomas = {
    "Croata": "hr",
    "Português (Brasil)": "pt",
    "Espanhol": "es",
    "Inglês": "en"
}
tk.OptionMenu(janela, idioma_var, *opcoes_idiomas.values()).pack()

# Entrada de texto
tk.Label(janela, text="Digite o texto:").pack(pady=5)
entrada_texto = scrolledtext.ScrolledText(janela, wrap=tk.WORD, width=55, height=5)
entrada_texto.pack(pady=5)

# Botão
tk.Button(janela, text="Traduzir", command=traduzir).pack(pady=10)

# Saída de texto
tk.Label(janela, text="Resultado:").pack(pady=5)
saida_texto = scrolledtext.ScrolledText(janela, wrap=tk.WORD, width=55, height=10, state=tk.DISABLED)
saida_texto.pack(pady=5)

janela.mainloop()
