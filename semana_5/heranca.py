# Herança (slide 11)

class PaginaWebExemplo:
    dominio = "exemplo.com.br"

    def __init__(self, href):
        self.href = href

    def url_completa(self):
        return f"www.{self.dominio}/{self.href}"

class PaginaWebExemploSeguro(PaginaWebExemplo):
    def url_completa_segura(self):
        return f"https://www.{self.dominio}/{self.href}"

pagina_inicial = PaginaWebExemploSeguro("home")
print(pagina_inicial.url_completa_segura())
