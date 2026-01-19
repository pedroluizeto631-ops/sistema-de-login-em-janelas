import tkinter as tk
from tkinter import messagebox

# ================== JANELA PRINCIPAL ==================
janela = tk.Tk()
janela.title("Sistema de Login")
janela.geometry("420x320")
janela.resizable(False, False)
janela.configure(bg="#1e1e1e")  # Fundo escuro da janela

# Aqui eu defini o tamanho, o título e ativei o modo escuro usando configure(bg)


# ================== FRAMES (TELAS) ==================
frame_registro = tk.Frame(janela, bg="#1e1e1e")
frame_login = tk.Frame(janela, bg="#1e1e1e")

for frame in (frame_registro, frame_login):
    frame.grid(row=0, column=0, sticky="nsew")

# Cada Frame é uma tela diferente, ambos ocupam o mesmo espaço e ficam sobrepostos.


# ================== TELA DE REGISTRO ==================
tk.Label(frame_registro, text="REGISTRO", fg="white", bg="#1e1e1e",
         font=("Arial", 14, "bold")).pack(pady=12)

tk.Label(frame_registro, text="Usuário", fg="white", bg="#1e1e1e").pack()
entrada_reg_user = tk.Entry(frame_registro)
entrada_reg_user.pack(pady=4)

tk.Label(frame_registro, text="Senha", fg="white", bg="#1e1e1e").pack()
entrada_reg_senha = tk.Entry(frame_registro, show="*")
entrada_reg_senha.pack(pady=4)

def registrar():
    messagebox.showinfo("Registro", "Usuário registrado ")

tk.Button(frame_registro, text="Registrar",
          width=20, pady=6,
          bg="#333333", fg="white",
          command=registrar).pack(pady=10)

tk.Button(frame_registro, text="Ir para Login",
          width=16, pady=4,
          bg="#444444", fg="white",
          command=lambda: frame_login.tkraise()).pack()

# Aqui eu criei os campos e botões do registro, todos centralizados usando pack().


# ================== TELA DE LOGIN ==================
tk.Label(frame_login, text="LOGIN", fg="white", bg="#1e1e1e",
         font=("Arial", 14, "bold")).pack(pady=12)

tk.Label(frame_login, text="Usuário", fg="white", bg="#1e1e1e").pack()
entrada_log_user = tk.Entry(frame_login)
entrada_log_user.pack(pady=4)

tk.Label(frame_login, text="Senha", fg="white", bg="#1e1e1e").pack()
entrada_log_senha = tk.Entry(frame_login, show="*")
entrada_log_senha.pack(pady=4)

resultado = tk.Label(frame_login, text="", fg="white", bg="#1e1e1e")
resultado.pack(pady=8)

def logar():
    user = entrada_log_user.get()
    senha = entrada_log_senha.get()
    if user == "admin" and senha == "123":
        resultado.config(text="Login OK ✅")
    else:
        resultado.config(text="Usuário ou senha incorretos ❌")

tk.Button(frame_login, text="Entrar",
          width=20, pady=6,
          bg="#333333", fg="white",
          command=logar).pack(pady=10)

tk.Button(frame_login, text="Voltar",
          width=16, pady=4,
          bg="#444444", fg="white",
          command=lambda: frame_registro.tkraise()).pack()

# Aqui fica toda a lógica e interface da tela de login, também centralizada.


# ================== INICIALIZAÇÃO ==================
frame_registro.tkraise()
janela.mainloop()

# Aqui eu escolho qual tela aparece primeiro e inicio o programa.
