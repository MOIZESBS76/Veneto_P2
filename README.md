🍕 Veneto Digital – Sistema de Gestão de Pedidos

O Veneto Digital é uma solução de software desenvolvida para a modernização dos processos de gestão da Pizzaria Veneto. 
O sistema substitui controles manuais por uma API escalável, seguindo rigorosos padrões de engenharia de software e arquitetura limpa.

🚀 Link do Sistema Publicado
Acesse a API aqui: https://veneto-p2.onrender.com/docs
(Documentação Swagger interativa disponível no link acima)

🛠️ Justificativa Técnica
A solução foi construída utilizando Python com o framework FastAPI, escolhido por sua alta performance assíncrona e geração automática de documentação. A persistência de dados utiliza MongoDB, oferecendo flexibilidade para o cardápio. A arquitetura foi desenhada para ser independente de frameworks e bancos de dados, facilitando a manutenção.

🏗️ Arquitetura e Organização (Clean Architecture)
O projeto respeita a divisão em camadas para garantir o desacoplamento (SOLID):
Domain: Entidades de negócio (entities.py) e interfaces abstratas (interfaces.py).
Application: Casos de uso que orquestram a lógica de negócio (use_cases.py).
Infrastructure: Implementações concretas de banco de dados (database.py) e repositórios (repositories.py).
API: Controladores e definição de rotas para comunicação externa.
Padrões de Projeto (Design Patterns) Implementados:
Singleton: Garante uma única instância da conexão com o banco de dados.
Repository: Abstrai a lógica de persistência.
Strategy: Cálculo dinâmico de preços (Taxas de final de semana vs. Dias úteis).
Factory: Centraliza a criação de estratégias de preço.

🧪 Qualidade e Testes
Clean Code: Nomes semânticos e funções de responsabilidade única.
TDD (Test Driven Development): Validação das regras de preço utilizando pytest.
BDD (Behavior Driven Development): Cenários de comportamento definidos para alinhar o técnico ao negócio.

📦 Infraestrutura e Deploy (Docker & Render)
O projeto utiliza Docker para garantir que o ambiente de execução seja idêntico em qualquer máquina.
Deploy Contínuo: O sistema está hospedado na plataforma Render, configurado para realizar deploy automático a partir do repositório GitHub utilizando o Dockerfile.
Execução Local:
docker-compose up --buildA 
API local estará em http://localhost:8000/docs.

👥 Autor:
Moizes Baptista da Silva
