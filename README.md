# 🐾 Sistema de Adoção de Animais – CLI / API Minimal

## 📌 Visão Geral

Este projeto consiste no desenvolvimento de um **sistema de linha de comando (CLI)** ou **API minimalista** (utilizando **FastAPI ou Flask**) para gerenciar de forma estruturada e orientada a objetos o processo completo de **adoção de animais**.

O sistema cobre desde o **cadastro e triagem de animais e adotantes**, passando por **reservas, adoções, devoluções e quarentena**, até a **geração de relatórios analíticos**, respeitando **políticas configuráveis**, **priorização por fila de espera** e **persistência desacoplada** via repositórios.

O foco do projeto é aplicar **conceitos sólidos de Programação Orientada a Objetos (POO)** aliados a regras de negócio realistas.

---

## 🎯 Objetivos

- Centralizar o fluxo de adoção de animais
- Garantir consistência de regras por meio de políticas configuráveis
- Aplicar padrões de projeto clássicos (Strategy, State, Repository, etc.)
- Manter domínio desacoplado da infraestrutura
- Facilitar testes, extensões e manutenção

---

## ⚙️ Funcionalidades Principais

### 1️⃣ Cadastro de Animais
- CRUD completo de animais
- Atributos:
  - espécie, raça, nome, sexo
  - idade (em meses)
  - porte (P / M / G)
  - temperamento (lista)
  - status
- Estados possíveis:
  - `DISPONIVEL`, `RESERVADO`, `ADOTADO`,
    `DEVOLVIDO`, `QUARENTENA`, `INADOTAVEL`
- Histórico completo de eventos (entrada, vacina, adoção, devolução, etc.)

---

### 2️⃣ Triagem de Adotantes
- Cadastro com:
  - nome, idade
  - tipo de moradia (casa/apartamento)
  - área útil
  - experiência com pets
  - crianças em casa
  - outros animais
- Validação automática de elegibilidade conforme políticas
- Cálculo de **pontuação de compatibilidade (0–100)** considerando:
  - porte × moradia
  - idade × nível de energia
  - experiência
  - presença de crianças

---

### 3️⃣ Reserva e Adoção
- Reserva temporária (padrão: 48h, configurável)
- Expiração automática via comando/job
- Adoção efetiva:
  - geração de contrato textual
  - cálculo de taxa de adoção por estratégia:
    - padrão
    - sênior (desconto)
    - filhote (custos de vacina)
    - cuidados especiais

---

### 4️⃣ Lista de Espera e Prioridade
- Fila por animal disputado
- Priorização baseada em:
  - pontuação de compatibilidade
  - tempo de espera
- Notificação interna (log/evento) ao expirar reserva

---

### 5️⃣ Devolução, Quarentena e Reavaliação
- Registro do motivo da devolução
- Alteração automática de status:
  - `DEVOLVIDO`
  - `QUARENTENA` (saúde/comportamento)
- Reavaliação pode resultar em:
  - `DISPONIVEL`
  - `INADOTAVEL`

---

### 6️⃣ Relatórios
- Top 5 animais mais adotáveis
- Taxa de adoções por espécie e porte
- Tempo médio entre entrada e adoção
- Devoluções e adoções canceladas por motivo

---

### 7️⃣ Configurações
Arquivo `settings.json` contendo:
- Idade mínima do adotante
- Regras moradia × porte
- Duração da reserva
- Pesos de compatibilidade
- Estratégia padrão de taxa de adoção

---

## 🧠 Requisitos Técnicos de POO

### 🔹 Modelagem e Herança
- `Animal` (classe abstrata)
  - `Cachorro`, `Gato`
- Atributos específicos:
  - necessidade de passeio
  - independência
- Herança múltipla com mixins:
  - `VacinavelMixin`
  - `AdestravelMixin`
- `Pessoa` → `Adotante`

---

### 🔹 Encapsulamento e Validação
- Uso de `@property` para atributos sensíveis
- Validações centralizadas no domínio
- Repositórios garantindo consistência transacional

---

### 🔹 Métodos Especiais
- `__str__`, `__repr__`
- `__eq__`, `__hash__` (identidade)
- `__lt__` (ordenação por data de entrada)
- `__iter__` (histórico de eventos)
- `FilaEspera.__len__` e comparadores de prioridade

---

### 🔹 Padrões de Projeto
- **Strategy** – cálculo de taxa de adoção
- **State / Enum** – estados e transições do animal
- **Specification (opcional)** – filtros combináveis
- **Observer (opcional)** – notificações internas

---

### 🔹 Tratamento de Erros
Exceções customizadas:
- `ReservaInvalidaError`
- `TransicaoDeEstadoInvalidaError`
- `PoliticaNaoAtendidaError`
- `RepositorioError`

---

### 🔹 Tipagem e Documentação
- Type hints em todo o código
- Docstrings padrão Google ou NumPy
- Compatível com `mypy`

---

### 🔹 Testes
- Framework: `pytest`
- Cobertura mínima:
  - políticas
  - expiração de reserva
  - compatibilidade
  - transições de estado
  - estratégias de taxa

---

## 🖥 Interface

### CLI (exemplo)
```bash
adocao cadastrar-animal
adocao reservar
adocao rodar-expiracao
adocao relatorio top
