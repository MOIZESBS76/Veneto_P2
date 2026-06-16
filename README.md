🍕 Veneto Digital – Sistema de Gestão de PedidosO Veneto Digital é uma solução de software desenvolvida para a modernização dos processos de gestão da Pizzaria Veneto. O sistema substitui controles manuais por uma API escalável, seguindo rigorosos padrões de engenharia de software e arquitetura limpa.
🚀 Link do Sistema Publicado

🛠️ Justificativa Técnica
A solução foi construída utilizando Python com o framework FastAPI, escolhido por sua alta performance assíncrona e geração automática de documentação (Swagger). A persistência de dados utiliza MongoDB, oferecendo a flexibilidade necessária para um cardápio dinâmico. A arquitetura foi desenhada para ser independente de frameworks e bancos de dados, facilitando a manutenção e evolução do sistema.
🏗️ Arquitetura e Organização (Clean Architecture)
O projeto respeita a divisão em camadas para garantir o desacoplamento (SOLID):
Domain: Entidades de negócio (entities.py) e interfaces abstratas (interfaces.py).
Application: Casos de uso que orquestram a lógica de negócio (use_cases.py).
Infrastructure: Implementações concretas de banco de dados (database.py) e repositórios (repositories.py).
API: Controladores e definição de rotas para comunicação externa.
Padrões de Projeto (Design Patterns) Implementados:
Singleton: Garante uma única instância da conexão com o banco de dados.
Repository: Abstrai a lógica de persistência, permitindo trocar o banco de dados sem afetar o domínio.
Strategy: Define diferentes algoritmos para cálculo de preços (Taxas de final de semana vs. Dias úteis).
Factory: Centraliza a criação de estratégias de preço com base em condições de negócio.
🧪 Qualidade e Testes
Clean Code: Aplicação de nomes semânticos, funções de responsabilidade única e baixo acoplamento.
TDD (Test Driven Development): Desenvolvimento orientado por testes utilizando pytest para validar as regras de cálculo de preço.
BDD (Behavior Driven Development): Cenários de comportamento definidos para garantir que o software atenda às expectativas de negócio.
📦 Infraestrutura e Execução (Docker)
O projeto está totalmente conteinerizado, garantindo que o ambiente de execução seja idêntico em qualquer máquina.
Para rodar localmente:
docker-compose up --build
A API estará disponível em http://localhost:8000 e a documentação interativa em http://localhost:8000/docs.

👥 Autor
Moizes Baptista da Silva
