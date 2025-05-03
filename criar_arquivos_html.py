import os

# Lista de nomes dos arquivos HTML
arquivos_html = [
    "creatinas.html", "pre_treino.html", "emagrecedores.html", 
    "acessorios.html", "bcaa.html", "albumina.html", "aumento_testosterona.html", 
    "bebidas.html", "ciclistas.html", "coffee.html", "colageno.html", "dose_unica.html", 
    "melatonina.html", "omega3.html", "forca_energia.html", "vitaminas.html", 
    "aumentar_massa_muscular.html", "aminoacidos.html", "articulacoes_saudaveis.html", 
    "barras_de_proteinas.html", "antioxidantes.html", "carboidratos.html", "glutaminas.html", 
    "pastas_de_amendoim.html", "caldas_e_molhos.html", "snacks_doces.html", "combos.html"
]

# Caminho da pasta onde os arquivos serão criados
caminho = 'loja_app/templates/loja_app/'

# Verifique se o diretório existe, se não, crie-o
if not os.path.exists(caminho):
    os.makedirs(caminho)

# Código HTML base
conteudo_html = """{% extends 'base.html' %} 
{% load static %}

{% block content %}
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Produtos - Loja Nutri</title>
        <link rel="stylesheet" href="{% static 'css/styles.css' %}">
    </head>

    <main>
        <h1>Produtos</h1>

        {% comment %} Lista de Produtos {% endcomment %}
        <section class="produtos-container">
            <!-- Produto 1 -->
            <article class="produto-item">
                <img src="{% static 'img/ebook1.jpg' %}" alt="Abcesso - Definição e Causas" class="produto-imagem">
                <div class="produto-info">
                    <h2>Abcesso - Definição e Causas</h2>
                    <p><strong>Preço:</strong> R$ 19,90</p>
                    <p>Este ebook aborda as principais causas e definições sobre abcessos e suas implicações na saúde.</p>
                    <a href="{% static 'pdf/Abcesso-Definicao-e-Causas.pdf' %}" target="_blank"><button>Ver Detalhes</button></a>
                    <button onclick="adicionarAoCarrinho('Abcesso - Definição e Causas', 19.90)">Adicionar ao Carrinho</button>
                </div>
            </article>
            <!-- Mais produtos aqui -->
        </section>

        <script>
            function adicionarAoCarrinho(produto, preco) {
                alert(`${produto} foi adicionado ao carrinho! Preço: R$ ${preco.toFixed(2)}`);
            }
        </script>
    </main>
{% endblock %}
"""

# Criando os arquivos HTML
for arquivo in arquivos_html:
    with open(os.path.join(caminho, arquivo), 'w') as file:
        file.write(conteudo_html)
    print(f"Arquivo '{arquivo}' criado com sucesso!")
