# Publicação e manutenção do repositório

## Identificação

| Campo | Valor |
| --- | --- |
| Repositório | `EdneiMonteiro/vareleira` |
| Visibilidade | Público |
| Branch principal | `main` |
| Site | https://vareleira.com/ |
| About | Universo educacional de uma seguradora fictícia de Brasília para mentorias, cursos e laboratórios de IA, com contexto sintético, RAG e governança. |
| Tópicos | `artificial-intelligence`, `education`, `fictional-company`, `synthetic-data`, `insurance`, `rag`, `ai-governance`, `ai-coe`, `github-pages`, `portuguese` |
| Pages | Origem: GitHub Actions |

O About, os tópicos e a origem do Pages são configurações do GitHub. Arquivos de
documentação descrevem os valores; mudanças nesses arquivos não alteram as
configurações remotas automaticamente.

Discussions recebe publicamente dúvidas, propostas e relatos de erro.
Issues e pull requests estão restritos a colaboradores com acesso `write`
até **9 de abril de 2027, às 02:20:22 UTC**, por `collaborators_only`.
O limite expira automaticamente e exige renovação.

O ruleset **Main Branch Protection** está ativo na branch padrão, sem exceções
de bypass, com regras `deletion` e `non_fast_forward`. Ele bloqueia exclusão
e force-push. Não exige aprovação de pull requests ou verificações obrigatórias.

As categorias Q&A, Ideas e General têm formulários. A moderação pública segue
[CODE_OF_CONDUCT.md](../CODE_OF_CONDUCT.md); não há filtragem automática de spam.

## Verificar e renovar restrições

Com o GitHub CLI autenticado como administrador do repositório:

```powershell
gh api repos/EdneiMonteiro/vareleira/interaction-limits
gh api repos/EdneiMonteiro/vareleira/rulesets/24763521
```

Para renovar o limite de interações por seis meses:

```powershell
gh api --method PUT repos/EdneiMonteiro/vareleira/interaction-limits `
  -f limit=collaborators_only -f expiry=six_months
```

Confira `expires_at` na resposta e atualize a data neste documento e em
`CONTRIBUTING.md`. Essa operação afeta as interações abrangidas pelo limite;
Discussions continua como fórum público moderado.

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

Em 9 de outubro de 2026 (UTC), `vareleira.com` foi transferido das configurações
Pages do repositório `ai-coe-playbook` para `vareleira`, com HTTPS obrigatório.
O endereço `https://edneimonteiro.github.io/vareleira/` redireciona para o domínio.
Os registros DNS existentes foram mantidos.

A rota `https://vareleira.com/artigos/coe-ia-playbook.html` é atendida por uma
cópia integral e atribuída do artigo no pacote deste site. O gerador verifica
seu hash antes de publicar. Consulte [NOTICE.md](../NOTICE.md) para a origem
e o procedimento de atualização.

O repositório do playbook mantém sua publicação em
`https://edneimonteiro.github.io/ai-coe-playbook/`, sem domínio personalizado.
Seu arquivo `CNAME` foi removido. Este repositório usa Actions e configura o
domínio diretamente em Settings → Pages; não precisa de arquivo `CNAME`.

A consulta DNS durante a migração não encontrou o TXT convencional de
verificação de propriedade. Verifique o estado em configurações da conta →
Pages e, se necessário, adicione o TXT fornecido pelo GitHub. Isso protege
a associação do domínio contra uso por outras contas.

`vareleira.com.br` e `www.vareleira.com` não foram configurados nesta operação.
O redirecionamento do domínio brasileiro e o registro da variante `www`
devem ser tratados separadamente.

## Reutilizar esta estrutura

Ao adaptar o repositório, atualize nome, proprietário, URL, About, tópicos, badges,
citação, autoria e contatos. Escolha licenças compatíveis com os materiais.
Confira se Discussions e comunicação privada de vulnerabilidades estão
habilitados antes de publicar seus links.

Preserve somente informações verdadeiras do novo projeto. Não copie DOI, selo
de teste, situação de publicação, proteção de branch ou garantia de suporte
sem configurar e verificar o recurso correspondente.
