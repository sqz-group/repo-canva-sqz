# repo-canva-sqz

Repositório público controlado para hospedar arquivos sanitizados usados na importação de designs editáveis no Canva pelo OpenSquad/SQZ.

## Uso

Arquivos publicados aqui devem ser acessíveis por HTTPS público, por exemplo:

```text
https://raw.githubusercontent.com/sqz-group/repo-canva-sqz/main/imports/<arquivo>.html
```

Esse tipo de URL pode ser usado pelo Canva MCP com `import-design-from-url`.

## O que pode entrar

- HTML estático preparado para importação no Canva.
- ZIPs com HTML/assets públicos e sanitizados.
- PDFs/PPTXs sem dados sensíveis.
- Imagens públicas/autorizadas para uso em peças.

## O que NÃO pode entrar

- `.env`, tokens, cookies, credenciais ou chaves.
- Browser profiles, sessões, local storage.
- Memórias internas do OpenSquad/SQZ.
- Outputs operacionais com dados sensíveis, PII ou contexto interno.
- Documentos internos não aprovados para publicação.

## Convenção para HTML importável

Para páginas fixas importáveis no Canva, cada página deve usar:

```html
<section data-document-role="page" data-label="Nome da página" data-speaker-notes="Notas opcionais">
  ...
</section>
```

Não aninhe elementos com `data-document-role="page"` dentro de outra página.

## Estrutura

```text
imports/        arquivos finais para importação Canva
assets/         imagens/assets públicos usados pelos imports
examples/       exemplos seguros de referência
scripts/        utilitários locais sem segredos
```
