class Curso:
    def __init__(self, nome, duracao):
        self.nome = nome
        self.duracao = duracao

    def detalhes_do_curso (self):
        return f"O nome do curso é  {self.nome} e o ano de duração {self.duracao}"


class Presencial (Curso):
    def __init__(self, nome, duracao, vagas):
        super().__init__(nome, duracao)
        self.vagas = vagas

    def detalhes_do_curso (self):
        info_curso = super().detalhes_do_curso
        return f"{info_curso}, numeros de vagas {self.vagas}"

class Online (Curso):
    def __init__(self, nome, duracao, plataforma):
        super().__init__(nome, duracao)
        self.plataforma = plataforma

    def detalhes_do_curso (self):
        info_curso = super().detalhes_do_curso
        return f"{info_curso}, numeros de vagas {self.plataforma}"



curso_p = Presencial("Analise", 2023, 5)
curso_o = Online ("Engenharia", 2024, "Google Meet")

print (curso_p.detalhes_do_curso())
print (curso_o.detalhes_do_curso())