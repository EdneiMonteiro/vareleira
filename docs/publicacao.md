# Publicação e manutenção do repositório

## Identificação

| Campo | Valor |
| --- | --- |
| Repositório | `EdneiMonteiro/vareleira` |
| Visibilidade | Público |
| Branch principal | `main` |
| Site | https://edneimonteiro.github.io/vareleira/ |
| About | Universo educacional de uma seguradora fictícia de Brasília para mentorias, cursos e laboratórios de IA, com contexto sintético, RAG e governança. |
| Tópicos | `artificial-intelligence`, `education`, `fictional-company`, `synthetic-data`, `insurance`, `rag`, `ai-governance`, `ai-coe`, `github-pages`, `portuguese` |
| Pages | Origem: GitHub Actions |

O About, os tópicos e a origem do Pages são configurações do GitHub. Arquivos de
documentação descrevem os valores; mudanças nesses arquivos não alteram as
configurações remotas automaticamente.

Discussions recebe dúvidas e propostas. Issues recebe erros reproduzíveis.
Pull requests permitem revisar alterações antes da incorporação. A política
não alega restrição técnica desses canais a colaboradores.

## Fluxo de publicação

O workflow `.github/workflows/pages.yml` executa em pull requests, atualizações
de `main` e acionamentos manuais. Usa Python 3.12, sem dependências adicionais.

1. A automação verifica os arquivos e executa os testes.
2. Em `main`, gera `_site` com uma lista explícita de arquivos públicos.
3. Envia o artefato ao GitHub Pages.
4. O job de publicação usa o ambiente `github-pages` e registra a URL.

Pull requests executam apenas verificações e não publicam. O job de publicação
tem permissões `pages: write` e `id-token: write`; o restante do workflow usa
somente leitura do conteúdo. As ações são fixadas por revisão.

## Conferir uma alteração

Execute na raiz do projeto:

```powershell
python scripts\site.py check
python -m unittest discover -s tests -v
python scripts\site.py build --output _site-preview
python -m http.server 8080 --bind 127.0.0.1 --directory _site-preview
```

A pasta de saída deve ser nova. Abra `http://127.0.0.1:8080`, confira as páginas
alteradas e encerre o servidor com `Ctrl+C`. Verifique também a apresentação em
tela pequena. O script confere links locais, mas não substitui revisão factual,
editorial ou inspeção visual.

Depois do envio a `main`, acompanhe
[Actions](https://github.com/EdneiMonteiro/vareleira/actions/workflows/pages.yml).
Considere a publicação concluída após o job terminar com sucesso e a página
pública apresentar a alteração.

## Falhas e recuperação

| Situação | Ação |
| --- | --- |
| Verificação local falhou | Corrija o arquivo indicado antes de enviar a alteração. |
| A pasta de saída já existe | Use outra pasta de saída; preserve a anterior enquanto precisar compará-la. |
| Pages não está habilitado | Em Settings → Pages, selecione GitHub Actions como origem. |
| O job de publicação está aguardando | Confira as regras do ambiente `github-pages` e a execução de Actions. |
| A URL retorna erro logo após o deploy | Confira o resultado do job e aguarde a propagação antes de repetir a publicação. |
| Conteúdo incorreto foi publicado | Faça um commit de reversão da alteração e publique pela mesma automação. Preserve o histórico. |

## Domínios existentes

A publicação inicial usa o endereço padrão do GitHub Pages. Este repositório
não contém `CNAME` e o workflow não modifica DNS.

Antes de migrar `vareleira.com`, preserve a rota
`https://vareleira.com/artigos/coe-ia-playbook.html`, hoje atendida pelo playbook.
A mudança exige escolher como servir ou redirecionar o artigo, verificar a
propriedade do domínio e configurar HTTPS. O redirecionamento de
`vareleira.com.br` deve ser planejado separadamente.

## Reutilizar esta estrutura

Ao adaptar o repositório, atualize nome, proprietário, URL, About, tópicos, badges,
citação, autoria e contatos. Escolha licenças compatíveis com os materiais.
Confira se Discussions e comunicação privada de vulnerabilidades estão
habilitados antes de publicar seus links.

Preserve somente informações verdadeiras do novo projeto. Não copie DOI, selo
de teste, situação de publicação, proteção de branch ou garantia de suporte
sem configurar e verificar o recurso correspondente.
