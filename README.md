Projeto Atualizado – Sistema de Controle Financeiro Pessoal Inteligente
🧩 1. Definição do Escopo do Projeto

Objetivo Geral:
Desenvolver um app que permita ao usuário controlar suas finanças pessoais com registro automático e manual, incluindo captura de contas por foto, registro de renda mensal, e integração automática com extratos bancários para facilitar o acompanhamento das faturas pagas. Inteligencia Artificial para recomendações de investimentos e alertas para nao estrapolar o limite posto pelo usuario

⚙️ 2. Requisitos Funcionais (RF)

RF01 – Cadastro e login de usuários.

RF02 – Registro manual de receitas e despesas.

RF03 – Captura de imagens de contas a pagar e contas pagas:
O usuário poderá tirar fotos das contas e o sistema fará o reconhecimento dos dados (OCR) para registrar automaticamente as despesas.

RF04 – Registro da renda mensal (salário):
O usuário poderá informar sua renda mensal para acompanhamento do orçamento.

RF05 – Integração com bancos (API bancária) para importação automática das faturas pagas e movimentações:
O sistema irá sincronizar automaticamente os dados financeiros, reduzindo o trabalho manual do usuário.

RF06 – Categorizar transações automaticamente e manualmente.

RF07 – Mostrar saldo atualizado e relatórios financeiros.

RF08 – Definir e acompanhar metas de economia.

RF09 – Editar e excluir transações.

🛡️ 3. Requisitos Não Funcionais (RNF)

RNF01 – Sistema disponível 24/7.

RNF02 – Resposta rápida (menos de 2 segundos).

RNF03 – Aplicação responsiva para smartphones.

RNF04 – Dados protegidos com autenticação forte e criptografia.

RNF05 – Alta disponibilidade e segurança na integração bancária, respeitando padrões de segurança (ex: OAuth, PCI-DSS).

RNF06 – OCR com alta precisão para leitura de contas.

🖼️ 4. Protótipo (novas telas e funcionalidades)

Tela de captura de conta via câmera.

Tela de revisão dos dados extraídos do OCR para confirmação.

Tela de integração bancária com autorização do usuário.

Tela de registro de renda mensal.

Dashboard atualizado com receitas, despesas e saldo automático.

📌 5. Considerações Finais

Projeto incorpora tecnologias modernas (OCR, integração bancária) para facilitar a vida do usuário.

Aumenta a automação e reduz erros manuais.

Pode ser base para futuros recursos como previsão financeira e análise de crédito.

🛠️ 6. Próximos Passos

Pesquisa e escolha da API bancária adequada (ex: Plaid, API dos bancos locais).

Desenvolvimento do módulo OCR (bibliotecas como Tesseract, Google Vision API).

Protótipo da captura e reconhecimento de contas.

Definição das políticas de segurança para integração bancária.
