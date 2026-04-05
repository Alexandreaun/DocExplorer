# DocExplorer
Agente para interagir via chat com assuntos baseados no documento PDF sobre Criptografia.

# Variáveis de ambiente:
No arquivo .env.example coloque a sua chave de API da OPENAI

# Rodar Postgres
Rodar no terminal: docker compose up -d
Para subir o banco de dados Postgres

# Para fazer a ingestão de documentos:
Rodar no terminal: 
./ingest
O comando irá fazer a ingestão do document.pdf do projeto no Postgres

# Para interagir com o Chat:
Rodar no terminal:
./chat