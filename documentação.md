Visão Geral do Projeto
O projeto é uma aplicação Python Flask que oferece uma API para gerenciar informações sobre pessoas. O banco de dados é armazenado em um servidor MySQL. A aplicação é empacotada em um contêiner Docker, permitindo fácil implantação e escalabilidade.

Arquitetura da Solução
A arquitetura da solução inclui:

-Aplicação Flask: Responsável por fornecer uma API RESTful para gerenciar informações sobre pessoas.
-Banco de Dados MySQL: Armazena os dados sobre pessoas.
-Docker: Utilizado para empacotar a aplicação, facilitando a implantação em ambientes diferentes.
-Ferramentas Utilizadas
    Python e Flask: Para o desenvolvimento da aplicação.
    MySQL: Como banco de dados relacional.
    Docker: Para containerizar a aplicação.
    GitHub Actions: Como ferramenta de CI/CD para automatizar o pipeline.
    Swagger e flasgger: Para documentar a API.

Configuração e Execução do Pipeline

Passos para Configurar o Pipeline
Clone o Repositório:

git clone https://github.com/VictorLG21/finalDevOpss
Crie um Ambiente Virtual (Opcional, mas Recomendado):

baixe as dependencias necessarias, sendo elas o docker/docker-compose e execute-o

Execução do Pipeline
O pipeline é automatizado usando o GitHub Actions. Cada push para o repositório aciona o pipeline, que executa testes, constrói e empurra a imagem Docker, e implanta a aplicação.

Manual de Execução da Aplicação
Requisitos
Docker instalado
Docker-Compose instalado

Passos
Clone o Repositório:

git clone https://github.com/VictorLG21/finalDevOpss
acesse o diretorio do docker-compose 
rode o seguinte comando docker-compose -d up

Relatório de Desafios e Lições Aprendidas

Desafios
Configuração do MySQL: A configuração inicial do MySQL no Docker e no pipeline pode ser desafiadora devido a questões de autenticação e permissões.

Integração do Swagger: Integrar o Swagger pode exigir ajustes específicos, especialmente ao documentar endpoints mais complexos.

Segurança: implementação com segurança de todas as informações para que não fiquem publicas.

Configuração do yaml.

Lições Aprendidas
Automação do Pipeline: A automação do pipeline com o GitHub Actions simplifica o processo de CI/CD, proporcionando consistência e confiabilidade.
Testes Unitários: Reforçamos o conhecimento de testes unitarios num contexto de ci-cd.
Documentação Clara: A documentação clara, incluindo a API do Swagger, facilita o entendimento e uso da aplicação.

Reflexão sobre Práticas de DevOps
A aplicação de práticas de DevOps no projeto demonstrou benefícios significativos, incluindo:

Integração Contínua: Identificação rápida de problemas e garantia de que o código seja sempre implantável.

Entrega Contínua: Implantação automática e consistente da aplicação em ambientes diferentes.

Em conclusão, a aplicação de práticas de DevOps não apenas facilitou o desenvolvimento e a entrega contínua, mas também contribuiu para a eficiência e confiabilidade do projeto. O aprendizado contínuo e a adaptação às lições aprendidas são cruciais para a evolução contínua da prática de DevOps.