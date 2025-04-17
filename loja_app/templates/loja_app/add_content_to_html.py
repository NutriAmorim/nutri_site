import os

# Defina o diretório onde estão os arquivos HTML
diretorio = r'C:\Users\iagom\nutri_site_backup\loja_app\templates\loja_app'

# Conteúdo a ser adicionado em cada arquivo HTML
template = '''{% extends 'base.html' %}

{% block content %}
<h1>{}</h1>
<p>Conteúdo em construção. Em breve teremos novidades por aqui!</p>
{% endblock %}
'''

# Função para adicionar conteúdo aos arquivos HTML
def adicionar_conteudo():
    # Itera sobre todos os arquivos no diretório
    for nome_arquivo in os.listdir(diretorio):
        if nome_arquivo.endswith('.html'):  # Filtra apenas arquivos .html
            caminho_arquivo = os.path.join(diretorio, nome_arquivo)
            
            # Verifica se o arquivo está vazio
            if os.path.getsize(caminho_arquivo) == 0:
                # Nome do arquivo sem extensão para usar no título
                titulo = nome_arquivo.replace('.html', '').replace('_', ' ').title()

                # Conteúdo formatado sem usar .format() para o template
                conteudo = template.replace("{}", titulo)
                
                # Abre o arquivo e escreve o conteúdo
                with open(caminho_arquivo, 'w', encoding='utf-8') as file:
                    file.write(conteudo)
                print(f'Conteúdo adicionado em {nome_arquivo}')
            else:
                print(f'O arquivo {nome_arquivo} não está vazio, portanto não foi modificado.')

# Chama a função para adicionar o conteúdo
adicionar_conteudo()
