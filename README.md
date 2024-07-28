## API para Predição de Preço de Imóveis e Análise de Sentimentos 🏡💬

![Static Badge](https://img.shields.io/badge/Status-Finalizado-green)

## Descrição

Este projeto demonstra os conceitos básicos de desenvolvimento de APIs para modelos de Machine Learning utilizando Flask. Ele oferece dois endpoints principais:

- **Análise de Sentimentos:** Analisa o sentimento expresso em um texto, retornando a polaridade da frase.
- **Predição de Preço de Imóveis:** Prevê o preço de um imóvel com base em suas características (tamanho, ano de construção e número de vagas na garagem).

## Tecnologias Utilizadas

- Python
- Flask
- TextBlob
- Googletrans
- Scikit-learn (LinearRegression)
- Pickle
- Flask-BasicAuth

## Endpoints da API

### 1. Análise de Sentimentos

- **Rota:** `/sentimento/<frase>`
- **Método:** GET
- **Parâmetros:**
    - `frase`: Frase a ser analisada (string).
- **Retorno:** Polaridade da frase (número entre -1 e 1).

**Exemplo de Requisição:**
```
GET /sentimento/Este filme é incrível!
```

**Exemplo de Resposta:**
```
  polaridade: 0.8
```

### 2. Predição de Preço de Imóveis

- **Rota:** `/cotacao/`
- **Método:** POST
- **Autenticação:** Basic Auth (usuário: `user`, senha: `admin`)
- **Corpo da Requisição (JSON):**
```json
{
  "tamanho": 100,
  "ano": 2010,
  "garagem": 2
}
```
- **Retorno:** Preço previsto do imóvel (número).

**Exemplo de Requisição:**
```
POST /cotacao/
Content-Type: application/json

{
  "tamanho": 100,
  "ano": 2010,
  "garagem": 2
}
```

**Exemplo de Resposta:**
```json
{
  "preco": 550000.0
}
```
