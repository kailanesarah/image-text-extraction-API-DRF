# API de Extração de Texto de Imagens - DRF

⚠️ **Este projeto está sendo refatorado** ⚠️

A **API de Extração de Texto de Imagens - DRF** é uma API de OCR (Reconhecimento Óptico de Caracteres) construída com Django REST Framework. Seu objetivo é extrair texto legível de imagens, servindo como base para aplicações como automação de dados, análise de documentos e ferramentas de acessibilidade.

---

## Metodologia STAR

### Situação
Extrair manualmente texto de imagens, como documentos escaneados, recibos ou carteiras de identidade, é um processo demorado e sujeito a erros.

### Tarefa
Desenvolver uma API REST que receba uma imagem e retorne automaticamente o texto extraído utilizando tecnologias de OCR.

### Ação
- Construção da API REST com Django REST Framework.
- Implementação do Tesseract como motor OCR.
- Estruturação dos endpoints para futura integração com um frontend em React.
- Preparação da base para autenticação e controle de acesso.

### Resultado
- A API já consegue processar imagens por meio de um endpoint e retornar o texto extraído.
- Pronta para integração com aplicações web.
- Escalável para futuras melhorias como autenticação, permissões e recursos avançados.

---

## 🚀 Como Executar o Projeto

### 1.  Clonar o Repositório

```bash
git clone https://github.com/kailanesarah/image-text-extraction-API-DRF.git
cd image-text-extraction-API-DRF
```

### 2. Configurar Variáveis de Ambiente

```bash
DJANGO_SECRET_KEY='sua_chave_secreta'
DB_NAME='nome_do_banco'
DB_USER='usuario_do_banco'
DB_PASSWORD='senha_do_banco'

```

### 3. Instalar Dependências
```bash
pip install -r requirements.txt

```

### 4. Aplicar Migrações
```bash
python manage.py migrate

```

### 5. Iniciar o Servidor
```bash
python manage.py runserver
#Acesse o projeto em: http://127.0.0.1:8000/
```

## Endpoints Disponíveis (em desenvolvimento)

### Extração de Texto com OCR

Este endpoint permite o envio de uma imagem para que o texto contido nela seja automaticamente extraído utilizando tecnologia OCR (Reconhecimento Óptico de Caracteres).

| Método | Endpoint             | Descrição                                       |
|--------|----------------------|-------------------------------------------------|
| POST   | `/ocr/extract-text/` | Recebe uma imagem e retorna o texto reconhecido. |


---

## Refatoração e melhorias em progresso

O projeto está passando por uma fase de refatoração para tornar o código mais limpo, modular e escalável. As principais melhorias em andamento incluem:

- **Modularização do código**: separação das responsabilidades em serviços, utilitários e views para facilitar manutenção e testes.
- **Limpeza e organização**: remoção de redundâncias e reestruturação do código para maior legibilidade.
- **Migração para PostgreSQL**: substituição do banco SQLite pelo PostgreSQL, garantindo maior robustez, segurança e compatibilidade com ambientes de produção.
- **Melhoria no tratamento de imagem**:
  - Redimensionamento e conversão padronizada antes do processamento.
  - Detecção de arquivos inválidos ou corrompidos.
  - Melhor integração com o Tesseract para resultados mais precisos.
- **Validações aprimoradas**: verificação do tipo e conteúdo da imagem enviada antes de processar.
- **Preparação para testes automatizados**: estrutura base para testes unitários e de integração com `pytest` ou `unittest`.
- **Base para autenticação JWT**: preparando o sistema para autenticação segura com níveis de acesso diferenciados.
- **Preparação para deploy**: ajustes na estrutura do projeto e arquivos como `Dockerfile` e `Procfile` para facilitar deploy em serviços como Heroku, Railway ou Render.

Essas melhorias visam deixar o projeto mais robusto e pronto para ambientes de produção e escalabilidade futura.

---

## ⚖Licença

Este projeto está licenciado sob a [Creative Commons Attribution-NonCommercial 4.0 International](https://creativecommons.org/licenses/by-nc/4.0/deed.pt-br).

Você pode:
- Usar o código para fins pessoais e educacionais.
- Estudar, modificar e compartilhar com créditos à autora.
- Contribuir para o projeto via pull requests.

**Não é permitido:**
- Usar o código para fins comerciais.
- Vender, sublicenciar ou distribuir este projeto com fins lucrativos.

> © 2025 [Kailane Sarah](https://github.com/kailanesarah) – Compartilhe conhecimento, mas com respeito! 💜

