# Vareleira

[![ORCID](https://img.shields.io/badge/ORCID-0009--0006--0765--4201-A6CE39?logo=orcid&logoColor=white)](https://orcid.org/0009-0006-0765-4201)
[![Código: MIT](https://img.shields.io/badge/C%C3%B3digo-MIT-yellow.svg)](LICENSES/MIT.txt)
[![Conteúdo: CC BY 4.0](https://img.shields.io/badge/Conte%C3%BAdo-CC%20BY%204.0-lightgrey.svg)](LICENSES/CC-BY-4.0.txt)
[![Validação e Pages](https://github.com/EdneiMonteiro/vareleira/actions/workflows/pages.yml/badge.svg)](https://github.com/EdneiMonteiro/vareleira/actions/workflows/pages.yml)
[![Último commit](https://img.shields.io/github/last-commit/EdneiMonteiro/vareleira)](https://github.com/EdneiMonteiro/vareleira/commits/main)

Site institucional de uma **seguradora fictícia**, usado como contexto para
mentorias, livros, manuais, cursos e laboratórios de inteligência
artificial (IA). Versão **0.1.0**, em português do Brasil, com cenário de referência
em **agosto de 2026**.

**Site:** [edneimonteiro.github.io/vareleira](https://edneimonteiro.github.io/vareleira/).
**Dúvidas e propostas:** [Discussions](https://github.com/EdneiMonteiro/vareleira/discussions).

O projeto oferece uma história comum para estudar consulta a apólices com
geração aumentada por recuperação e criação de um Centro de Excelência em IA.
As introduções estão disponíveis; os laboratórios executáveis permanecem
planejados. Consulte os [avisos de uso](DISCLAIMER.md).

## Abrir localmente

Abra `index.html` no navegador. As sete páginas e os arquivos locais funcionam
diretamente, sem instalação de pacotes ou servidor. Os links externos para o
playbook e o GitHub exigem internet.

Para verificar o site por um endereço local, use um servidor HTTP (*Hypertext
Transfer Protocol*, protocolo de transferência de páginas web). Essa alternativa
exige Python 3 instalado. Abra o PowerShell na pasta do projeto e execute:

```powershell
python -m http.server 8080 --bind 127.0.0.1
```

Acesse `http://127.0.0.1:8080` para abrir a página inicial. O servidor aceita apenas
conexões locais. Se a porta estiver ocupada, substitua `8080` por outra porta livre
no comando e no endereço. Ao terminar, encerre o servidor com `Ctrl+C`.

## Conteúdo

| Arquivo | Conteúdo |
|---|---|
| `index.html` | Apresentação institucional |
| `empresa.html` | História-base, personagens, cronologia e operação |
| `seguros.html` | Linhas fictícias residencial, automóvel e empresas |
| `labs.html` | Catálogo das duas jornadas educacionais |
| `rag.html` | Introdução ao futuro piloto interno do Assistente de Apólices |
| `coe.html` | Criação do Centro de Excelência em IA e avaliação de maturidade |
| `acervo.html` | Materiais disponíveis, planejados, fontes e condições de uso |
| `dados\contexto-v0.1.0.json` | Contexto estruturado em JSON (JavaScript Object Notation) |
| `assets\site.css` | Estilo compartilhado e responsividade |
| `assets\brasilia.svg` | Ilustração vetorial original, sem dependências externas |
| `assets\favicon.svg` | Marca gráfica inicial |

## Contribuição, suporte e citação

| Necessidade | Referência |
| --- | --- |
| Propor uma mudança ou enviar código | [CONTRIBUTING.md](CONTRIBUTING.md) |
| Consultar regras de convivência e moderação | [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) |
| Relatar um problema de conteúdo ou apresentação | [SUPPORT.md](SUPPORT.md) |
| Comunicar uma vulnerabilidade em privado | [SECURITY.md](SECURITY.md) |
| Entender escopo, garantias e privacidade | [DISCLAIMER.md](DISCLAIMER.md) |
| Consultar autoria e política de créditos | [CONTRIBUTORS.md](CONTRIBUTORS.md) |
| Identificar fontes e adaptações | [NOTICE.md](NOTICE.md) |
| Citar o projeto | [CITATION.cff](CITATION.cff) |
| Manter a publicação no GitHub Pages | [Publicação](docs/publicacao.md) |

Projeto pessoal, sem afiliação, endosso ou suporte oficial da Microsoft ou do
GitHub. O suporte é comunitário e não tem prazo garantido.

Discussions é o canal público de entrada. Issues e pull requests estão
temporariamente restritos a colaboradores com acesso `write`, conforme o prazo
registrado em [CONTRIBUTING.md](CONTRIBUTING.md). A branch `main` bloqueia
exclusão e force-push.

Referência sugerida:

> Monteiro, Ednei. *Vareleira: contexto fictício para educação em inteligência
> artificial*. Versão 0.1.0, 2026. https://github.com/EdneiMonteiro/vareleira

Indique também a revisão utilizada ao citar conteúdo que ainda não pertence a
uma release. O projeto não possui DOI próprio; os identificadores dos projetos
de referência não identificam a Vareleira.

## Fatos do cenário e origem da narrativa

- Fundação em 1994, de origem familiar, com sede em Brasília e atuação nacional.
- Aproximadamente 4.000 colaboradores no cenário de agosto de 2026.
- Personalidade tradicional em modernização, com sistemas legados e conflitos.
- Produtos fictícios: Vareleira Lar, Vareleira Auto e Vareleira Negócios.
- O patrocínio ao Centro de Excelência em IA (CoE de IA) começou em março de 2025.
- O piloto didático de geração aumentada por recuperação (RAG, do inglês
  Retrieval-Augmented Generation) é interno e anterior ao assistente externo
  registrado na avaliação de maturidade, chamada de *assessment* no playbook.
- Agosto de 2026 permanece como referência histórica: três soluções em produção,
  média bruta 2,52, nível final 2, cinco contenções e dois vetos operacionais.
- Os personagens, a fundação, a expansão e o piloto interno foram acrescentados
  à narrativa do site.
- Melhorias propostas em exercícios devem ser registradas como alternativas ou
  evoluções posteriores, preservando o marco de agosto de 2026.

Fonte do caso original: [assessment preenchido do AI CoE Playbook](https://github.com/EdneiMonteiro/ai-coe-playbook/blob/main/assessment/exemplo-preenchido.md).
Os materiais dessa fonte mantêm a licença Creative Commons Atribuição 4.0
Internacional (CC BY 4.0). A revisão de referência e as adaptações estão
registradas em [NOTICE.md](NOTICE.md).

Ao alterar a história, atualize as páginas afetadas e o arquivo JSON para manter
nomes, datas, responsabilidades e situações coerentes. Novos pacotes devem
identificar a versão do contexto e seu período narrativo. Preserve arquivos de
dados de versões já usadas em cursos e publique alterações em uma nova versão.

## Escopo desta versão

**Disponível:** páginas institucionais, introduções das duas jornadas, referências
do playbook e um arquivo de contexto para download.

**Planejado:** laboratórios executáveis, documentos sintéticos de apólices,
roteiros e conjuntos de perguntas de avaliação.

O site é estático, sem chatbot, formulários, contas, análise de visitantes ou
integrações com sistemas. Não oferece seguros nem recebe dados pessoais.
Use apenas dados e documentos sintéticos nos futuros ambientes de exercícios.

## Licenças

O **código** segue [MIT](LICENSES/MIT.txt). Os **textos, ilustrações e dados
sintéticos** seguem [CC BY 4.0](LICENSES/CC-BY-4.0.txt). O mapa de escopos está em
[LICENSE](LICENSE), incluindo o tratamento de páginas HTML que misturam código
e conteúdo.

As licenças permitem reutilização, inclusive comercial, respeitadas suas
condições. Preserve os avisos do código, atribua o conteúdo, forneça a licença
e identifique as adaptações. Materiais de terceiros mantêm os próprios termos.

## Validação e publicação

Requisito para a automação: Python 3.12 ou superior, somente biblioteca padrão.

```powershell
python scripts\site.py check
python -m unittest discover -s tests -v
python scripts\site.py build
```

O último comando cria `_site` em uma pasta nova. Se ela já existir, escolha outra
com `python scripts\site.py build --output _site-preview`; o comando preserva
diretórios existentes. O pacote inclui apenas páginas, ativos, dados e avisos
licenciados, sem scripts, testes ou arquivos internos do repositório.

Pull requests executam as verificações. Atualizações em `main` também geram o
pacote e publicam no GitHub Pages. Consulte [o procedimento de publicação](docs/publicacao.md)
para configuração, acompanhamento e recuperação.

`vareleira.com` e `vareleira.com.br` não são alterados por essa automação.
O artigo continua em [seu endereço atual](https://vareleira.com/artigos/coe-ia-playbook.html).
