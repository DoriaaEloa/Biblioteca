class Livro:
    def _init_(self, titulo):
        self.titulo = titulo
        self.disponivel = True

    def _str_(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"{self.titulo} - {status}"

class Biblioteca:
    def _init_(self):
        self.livros = []

    def adicionar_livro(self, titulo):
        self.livros.append(Livro(titulo))
        print(f"Livro '{titulo}' adicionado com sucesso.")

    def emprestar(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo and livro.disponivel:
                livro.disponivel = False
                print(f"'{titulo}' emprestado com sucesso.")
                return
        print("Livro indisponível.")

    def devolver(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo and not livro.disponivel:
                livro.disponivel = True
                print(f"'{titulo}' devolvido com sucesso.")
                return
        print("Livro não encontrado ou já disponível.")

    def listar_livros(self):
        if not self.livros:
            print("Nenhum livro cadastrado.")
        else:
            for livro in self.livros:
                print(livro)

# --- Interface com input() ---
biblioteca = Biblioteca()

while True:
    print("\n--- Menu da Biblioteca ---")
    print("1. Adicionar Livro")
    print("2. Emprestar Livro")
    print("3. Devolver Livro")
    print("4. Listar Livros")
    print("5. Sair")

    opcao = input("Escolha uma opção (1-5): ")

    if opcao == "1":
        titulo = input("Digite o Título do Livro: ")
        biblioteca.adicionar_livro(titulo)
    elif opcao == "2":
        titulo = input("Digite o Título para Emprestar o Livro: ")
        biblioteca.emprestar(titulo)
    elif opcao == "3":
        titulo = input("Digite o Título do Livro para Devolver: ")
        biblioteca.devolver(titulo)
    elif opcao == "4":
        biblioteca.listar_livros()
    elif opcao == "5":
        print("Saindo da biblioteca. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")

