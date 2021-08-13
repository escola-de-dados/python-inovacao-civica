# Sobreposição (slide 14)

class PaginaWeb:
    dominio = ""

    def __init__(self, href):
        self.href = href

    def url_completa(self):
        return f"www.{self.dominio}/{self.href}"

class PaginaWebSegura(PaginaWeb):
    def url_completa(self):
        return f"https://www.{self.dominio}/{self.href}"

class PaginaWebExemploSegura(PaginaWebSegura):
    dominio = "exemplo.com.br"

pagina_inicial = PaginaWebExemploSegura("home")
print(pagina_inicial.url_completa())
