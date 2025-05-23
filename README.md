# projeto-final-qa-Gabrielly-Bentivoglio-Negri

# Projeto de Quality Assurance (QA)

## 1. Apresentação

**Nome:** Gabrielly Bentivoglio Negri
**Curso:** Gestão da Tecnologia da Informação – 5°Semestre

Durante este semestre, tive a oportunidade de aprender na prática como aplicar conceitos de garantia da qualidade no desenvolvimento de software. A disciplina me proporcionou contato com ferramentas reais, criação de testes automatizados, planejamento de testes e uma visão mais clara sobre como a área de QA é essencial para entregar sistemas funcionais e confiáveis. Foi desafiador no início, mas muito gratificante ver os testes funcionando na prática com o auxílio de ferramentas como o Google Colab e o GitHub.

---

## 2. O que é Quality Assurance (QA)?

Quality Assurance, ou Garantia da Qualidade, é um conjunto de práticas e processos utilizados para garantir que um software funcione corretamente, sem erros, e atenda às necessidades dos usuários. É como uma inspeção que acontece durante todo o processo de desenvolvimento, e não só no final. O QA ajuda a evitar falhas, economiza tempo e dinheiro, e faz com que os usuários tenham uma boa experiência com o sistema. Pense como se fosse um "controle de qualidade" do software, igual ao que acontece em uma fábrica, só que voltado para sistemas e aplicativos.

---

## 3. Conceitos Aprendidos Durante o Semestre

Neste semestre, aprendi que qualidade em software vai além de apenas "funcionar"; envolve confiabilidade, desempenho, segurança e boa experiência do usuário. Compreendi diferentes tipos de testes: testes unitários (pequenos blocos de código), testes de integração (como os componentes interagem), testes de sistema, aceitação (validação com o cliente), regressão (evita que algo que funcionava quebre) e testes exploratórios (sem roteiro fixo). Aprendi também a planejar testes, criar critérios de aceitação, escrever planos e casos de teste. Utilizamos ferramentas como o Google Colab para programar em Python, GitHub para versionamento, e automatizamos testes com bibliotecas como `unittest`, `pytest`, `requests` e `selenium`. Também entendemos como a automação se conecta a pipelines CI/CD e como monitorar a qualidade com métricas e relatórios.

---

## 4. Ferramentas e Sites Utilizados

- [https://reqres.in/](https://reqres.in/) – API para testes  
- [https://colab.research.google.com/](https://colab.research.google.com/) – Ambiente para execução de scripts Python  
- [Notebook do projeto no Colab](https://colab.research.google.com/drive/1V3rM6U21n1mSrVT6CNlB_oZt7Bzqp8FK?usp=sharing) – Link direto para os testes automatizados desenvolvidos  
- [https://github.com/](https://github.com/) – Controle de versão e repositórios de código  
- [https://uptimerobot.com/](https://uptimerobot.com/) – Monitoramento de serviços web  
- [https://demoqa.com/automation-practice-form](https://demoqa.com/automation-practice-form) – Site usado para testes de formulários  
- [https://chatgpt.com/](https://chatgpt.com/) – Apoio para escrita de código e explicações  
- [https://www.deepseek.com/](https://www.deepseek.com/) – Pesquisa técnica com IA  
- **Visual Studio Code (VSCode)** – Editor de código usado durante o curso   
- **Katalon Recorder** – Extensão para gravar testes automatizados no navegador  
- **Ghost Inspector** – Extensão e plataforma para testes de interface e fluxos web  
- **Fake Filler** – Extensão para preenchimento automático de formulários  
- **WAVE (Web Accessibility Evaluation Tool)** – Ferramenta para avaliar acessibilidade de páginas web  

---

## 5. Explicação dos Testes Entregues

### ✅ Teste 01 – Verificação de status da API ReqRes
- **Biblioteca:** `requests`  
- **Objetivo:** Verificar se o endpoint da API retorna status HTTP 200  
- **Resultado esperado:** Teste passa com sucesso se o status for 200  
- **Arquivo:** `testes/teste_01.py`  

---

### ✅ Teste 02 – Teste Unitário de Soma
- **Biblioteca:** `unittest`  
- **Objetivo:** Validar o funcionamento de uma função de soma simples  
- **Resultado esperado:** Teste aprovado se a função retornar corretamente o resultado da soma  
- **Arquivo:** `testes/teste_02_unitario.py`  

---

### ✅ Teste 03 – Preenchimento de Formulário com Selenium
- **Biblioteca:** `selenium`, `unittest`  
- **Objetivo:** Preencher automaticamente o formulário do site DemoQA com os dados de Gabrielly (21 anos)  
- **Resultado esperado:** Teste passa se o modal "Thanks for submitting the form" for exibido  
- **Arquivo:** `testes/teste_03_selenium_formulario.py`  

---

Link para o Notebook no Google Colab:

🔗 [Acessar o notebook no Google Colab](https://colab.research.google.com/drive/1V3rM6U21n1mSrVT6CNlB_oZt7Bzqp8FK?usp=sharing)

---

## 6. Conclusão Final

O aprendizado mais importante que levo desta disciplina é que **testar é tão essencial quanto programar**. QA é uma área estratégica dentro de qualquer projeto de tecnologia, pois garante a entrega de valor ao usuário final. No futuro, pretendo aprofundar meus conhecimentos em automação de testes e integrar isso ao meu perfil profissional. A ferramenta que mais me chamou a atenção foram os **Testes Automatizados**, pois pude interagir com páginas reais e perceber o quanto a automação pode poupar tempo e reduzir erros humanos nos testes manuais.

---
