# Classes (slide 8)

class PaginaWebExemplo:
    dominio = "exemplo.com.br"

    def __init__(self, href):
        self.href = href

    def url_completa(self):
        return f"www.{self.dominio}/{self.href}"

pagina_inicial = PaginaWebExemplo("home")
print(pagina_inicial.url_completa())

pagina_sobre = PaginaWebExemplo("about")
print(pagina_sobre.url_completa())
