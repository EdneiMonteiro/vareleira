# Como contribuir

Proponha mudanças de escopo, história ou laboratórios em
[Discussions](https://github.com/EdneiMonteiro/vareleira/discussions) antes de
implementá-las. Discussions é o canal público para propostas, correções e dúvidas.
Consulte [SUPPORT.md](SUPPORT.md) para relatar problemas.

## Acesso e proteção

A criação de issues e pull requests e as demais interações abrangidas pelo
limite do GitHub estão restritas a colaboradores com acesso `write`. A restrição
`collaborators_only` está configurada até **9 de abril de 2027, às 02:20:22 UTC**.
O GitHub expira esse limite automaticamente; o mantenedor precisa renová-lo
para manter a restrição após essa data.

Quem não tem acesso de escrita deve iniciar uma Discussion. O mantenedor pode
incorporar a contribuição e creditá-la ou avaliar uma solicitação de colaboração.
Colaboradores podem enviar correções por pull request, com descrição do problema
e da alteração.

A branch `main` está protegida contra exclusão e force-push, pelo ruleset
**Main Branch Protection**. A regra não exige aprovação obrigatória de pull
request nem impede atualizações diretas autorizadas.

## Moderação de Discussions

Discussions permanece pública, conforme o [código de conduta](CODE_OF_CONDUCT.md).
Use Q&A para dúvidas, Ideas para propostas e General para outros assuntos do
projeto. Os formulários dessas categorias ajudam a descrever o contexto e
evitar o compartilhamento de informações sensíveis.

O mantenedor pode editar ou remover conteúdo inadequado, bloquear conversas e
denunciar abuso conforme os recursos do GitHub. A moderação é manual, sem
garantia de resposta imediata; formulários não bloqueiam spam automaticamente.
Vulnerabilidades devem seguir o canal privado de [SECURITY.md](SECURITY.md).

## Conteúdo e consistência

Preserve o cenário de agosto de 2026 e seus resultados. Mantenha nomes,
responsabilidades, números e situações coerentes entre páginas e dados
estruturados. Separe os acontecimentos da ficção das referências técnicas.
Identifique materiais planejados e entregas disponíveis.

Escreva em português profissional, com títulos informativos e verbos concretos.
Explique siglas no primeiro uso e use links descritivos. Revise a categoria
inteira ao encontrar slogans, repetições ou ressalvas dispensáveis.
Preserve condições técnicas, restrições e avisos de ficção.

Use dados sintéticos e declare a origem dos materiais externos. Não inclua
segredos, dados pessoais ou arquivos de configuração do seu ambiente.

## Antes de enviar

Prepare o ambiente com Python 3.12 ou superior e
`python -m pip install -r requirements-build.txt`.

1. Execute `python scripts\site.py check` com Python 3.12 ou superior.
2. Abra as páginas alteradas e confira navegação, textos e apresentação em
   telas grandes e pequenas.
3. Atualize a documentação, a atribuição e os dados afetados pela mudança.
4. Descreva o resultado no modelo de pull request.

A automação verifica arquivos e referências locais. Afirmações técnicas,
referências externas, qualidade editorial e aparência exigem revisão humana.
A geração para publicação usa `python scripts\site.py build`.

## Créditos e licenças

Contribuições aceitas são creditadas conforme [CONTRIBUTORS.md](CONTRIBUTORS.md).
Ao contribuir, você disponibiliza o código sob MIT e o conteúdo sob CC BY 4.0,
conforme os escopos de [LICENSE](LICENSE), e confirma que tem os direitos necessários.
Materiais externos devem manter sua atribuição e licença compatível.

O mantenedor pode solicitar alterações ou recusar propostas que ampliem o
escopo sem documentação, introduzam riscos ou prejudiquem a consistência do caso.
