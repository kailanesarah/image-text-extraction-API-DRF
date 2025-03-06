# Descrição do Projeto: API de Extração e Tradução de Texto de Imagens

## Objetivo

Esta API tem como objetivo:

1. **Extrair textos de imagens** enviadas pelos usuários.
2. **Traduzir o texto extraído**, caso o usuário deseje, para um idioma diferente.

---

## Tecnologias e Bibliotecas Utilizadas

1. **Django**: Framework para o desenvolvimento da API.
2. **Django REST Framework (DRF)**: Facilita a criação de APIs RESTful, fornecendo recursos como serializadores e views baseadas em classe.
3. **Pillow**: Biblioteca para processamento de imagens, permitindo manipulação como redimensionamento e conversão.
4. **OpenCV**: Usada para processar as imagens, convertendo-as para escala de cinza, facilitando a extração de texto.
5. **Tesseract**: Motor de OCR (Reconhecimento Óptico de Caracteres) utilizado para extrair texto das imagens.
6. **Google Translate ou outra API de Tradução**: Para traduzir o texto extraído para o idioma desejado pelo usuário.

---

## Fluxo de Funcionamento da API

### 1. Endpoint de Extração de Texto

- O usuário envia uma **imagem** (por upload ou URL) para a API.
- A API recebe a imagem e a **valida**.
- A imagem é processada:
    - **Pillow** para manipulação básica da imagem.
    - **OpenCV** é utilizado para converter a imagem em escala de cinza.
    - **Tesseract** extrai o texto da imagem.
- O texto extraído é retornado como resposta para o usuário.

### 2. Endpoint de Tradução

- O usuário fornece o **texto extraído** (recebido do primeiro endpoint) e o **idioma de destino**.
- A API então traduz o texto utilizando um serviço de tradução (como o Google Translate).
- A tradução é retornada como resposta para o usuário.

---

## Componentes do Sistema

### 1. Serializers

- São usados para validar e processar os dados enviados pelo usuário, como as imagens ou os textos a serem traduzidos.
- O **serializer** para o upload de imagens vai validar o arquivo da imagem e sua URL, além de garantir que o formato seja adequado.
- O **serializer** para a tradução validará o texto e o idioma desejado.

### 2. Views

- São responsáveis por tratar a lógica de cada funcionalidade.
- Uma view para **extrair o texto** da imagem e outra para **traduzir** o texto.
- A lógica de processamento da imagem e da tradução será separada em funções auxiliares para melhor organização do código.

---

## Como o Usuário Interage com a API

### 1. Envio de Imagem para Extração de Texto

- O usuário acessa o endpoint de extração de texto, enviando a imagem via **POST**.
- A API processa a imagem e retorna o texto extraído.

### 2. Envio de Texto para Tradução

- O usuário acessa o endpoint de tradução, enviando o texto extraído anteriormente e o idioma desejado.
- A API retorna o texto traduzido.

---

## Bibliotecas e Ferramentas Necessárias

1. **Django**: Para a criação do servidor e gerenciamento de rotas.
2. **Django REST Framework (DRF)**: Para simplificar a criação de APIs RESTful.
3. **Pillow**: Para processar as imagens (ex.: redimensionar, ajustar contraste, etc.).
4. **OpenCV**: Para converter a imagem em escala de cinza, uma etapa útil para melhorar a precisão do OCR.
5. **Tesseract**: Para realizar o OCR e extrair o texto da imagem.
6. **Google Translate API (ou alternativa)**: Para traduzir o texto extraído para o idioma desejado.

---

## Estrutura do Projeto

1. **views.py**: Contém as views para os endpoints de extração e tradução.
2. **serializers.py**: Contém os serializers para validar as imagens e os textos.
3. **urls.py**: Mapeia as rotas para os endpoints da API.
4. **models.py** (opcional): Pode ser utilizado para armazenar registros de imagens ou textos extraídos, caso necessário.
5. **settings.py**: Configurações do Django, incluindo chaves de API para Tesseract e Google Translate.

---
