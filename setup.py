from setuptools import setup, find_packages

# Nome do pacote
nome_pacote = 'dataprocessing'

# Versão do pacote
versao = '1.0.0'

# Descrição do pacote
descricao = 'Pacote personalizado para realização de web scraping e automação web'

# Autor
autor = 'Damodara Barbosa'

# Email do autor
email_autor = 'damodarabarbosa@gmail.com'

# URL do repositório do projeto
url_repositorio = 'https://github.com/DamodaraBarbosa/xbox_gamepass/tree/main/dataprocessing'

# Configuração do pacote
setup(
    name=nome_pacote,
    version=versao,
    description=descricao,
    author=autor,
    author_email=email_autor,
    url=url_repositorio,
    packages=find_packages(),  # Encontra automaticamente todos os pacotes do projeto
    install_requires=[
        'time', 'urllib', 'selenium', 'bs4',
        'zipfile', 'wget', 'os'
    ]  # Lista de dependências do pacote 
)
