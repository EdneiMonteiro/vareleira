# Como contribuir

Proponha mudanças de escopo, história ou laboratórios em
[Discussions](https://github.com/EdneiMonteiro/vareleira/discussions) antes de
implementá-las. Correções pontuais podem ser enviadas por pull request, com
descrição do problema e da alteração. Consulte [SUPPORT.md](SUPPORT.md) para erros.

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
