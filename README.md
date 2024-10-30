# Projeto de Estudo de Inglês com Crianças

Este projeto é uma ferramenta para ajudar crianças a estudar inglês através de séries com legendas.

## Índice
- [Descrição do Projeto](#descrição-do-projeto)
- [Como Configurar o Ambiente](#como-configurar-o-ambiente)
- [Executando o Código](#executando-o-código)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Contribuição](#contribuição)

## Descrição do Projeto
Este projeto foi desenvolvido como parte de um trabalho de extensão para ajudar crianças a estudar inglês de forma prática e interativa. Ele utiliza uma interface gráfica simples, escrita em Python com a biblioteca `Tkinter`, e inclui funções para tradução de legendas e síntese de fala. O objetivo principal é tornar o aprendizado do inglês mais acessível e envolvente.

## Como Configurar o Ambiente

### 1. Pré-requisitos
- **Python 3.x**: Certifique-se de que Python está instalado em sua máquina. [Instale o Python](https://www.python.org/downloads/)
- **Git**: Para clonar o repositório. [Instale o Git](https://git-scm.com/)

### 2. Clonando o Repositório
Abra o terminal e clone o repositório com o comando:
```bash
git clone https://github.com/Carlos-1981/programa-estudo-ingles.git
cd programa-estudo-ingles
```

### 3. Instalando as Dependências
Para rodar o projeto, você precisará instalar as dependências listadas no arquivo `requirements.txt`. Execute o comando abaixo:
```bash
pip install -r requirements.txt
```

## Executando o Código
Depois de instalar as dependências, você pode rodar o programa com o seguinte comando:
```bash
python cod_revisado_completamente.py
```

**Nota**: Certifique-se de que o arquivo `Legendas reduzidas ep 10.txt` esteja presente no mesmo diretório para ser carregado pelo programa.

## Funcionalidades
- **Tradução de Legendas**: O programa permite a tradução automática das legendas utilizando a API do DeepL.
- **Interface Gráfica Simples**: Criada com `Tkinter`, fácil de usar para crianças, para interagir com as funcionalidades do programa.
- **Síntese de Fala**: Utiliza a biblioteca `pyttsx3` para reproduzir frases em inglês, ajudando na prática da pronúncia.
- **Marcação de Frases Difíceis**: As crianças podem marcar frases difíceis para revisá-las posteriormente.

## Tecnologias Utilizadas
- **Python**: Linguagem principal do projeto.
- **Tkinter**: Para criar a interface gráfica.
- **DeepL API**: Para tradução automática das legendas.
- **pyttsx3**: Para síntese de fala offline.

## Contribuição
Sinta-se à vontade para contribuir com o projeto. Para isso, faça um fork deste repositório, crie uma branch para a sua feature e abra um pull request.

1. Faça um **fork** do projeto.
2. Crie uma **branch** para sua feature:
   ```bash
   git checkout -b minha-feature
   ```
3. **Commit** suas mudanças:
   ```bash
   git commit -m "Adicionando minha feature"
   ```
4. Faça o **push** para a branch:
   ```bash
   git push origin minha-feature
   ```
5. Abra um **pull request**.

## Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.





