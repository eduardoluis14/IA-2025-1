# Resolução de Sudoku com Heurísticas Avançadas

## Equipe
- **Disciplina**: Inteligência Artificial IEC034/ICC265 - 2025/1  
- **Curso**: Ciência da Computação - Turmas CO01 e CB500  
- **Integrantes**:
  - Jessica de Figueredo Colares - 22060036
  - Antonio Mileysson França Bragança - 21850963
  - Luís Eduardo Bentes Negreiros - 22251141
  - Lucas Vinícius Gonçalves Gadelha - 22050517
  - Laiana de Pinho Cavalcante - 22153451
  - Isabelly Rohana Barbosa de Oliveira - 21352282
  - Ricardo Mendonça Braz - 22152017

Equipe E: 13 - 16

## Explicação das heurísticas

### 1. **Two-String Kite (Pipa de Duas Cordas)**
É uma técnica baseada em **candidatos únicos** (geralmente um mesmo número em duas linhas ou colunas) que formam um padrão semelhante a uma pipa.

**Como funciona:**
- Suponha que um candidato (ex: número **5**) apareça apenas duas vezes em uma **linha** (em duas células diferentes) e também apenas duas vezes em uma **coluna** (em duas células diferentes).
- Se essas células compartilham uma **mesma casa** (bloco 3x3), você pode eliminar outros candidatos **5** alinhados com as extremidades do "kite".

**Exemplo:**
- Se o **5** está nas posições A1 e A5 (linha A) e também em A1 e F1 (coluna 1), então:
  - O **5** em A1 é a "interseção" da pipa.
  - Se A5 e F1 "enxergam" uma mesma célula (ex: F5), você pode eliminar o **5** de F5.

---

### 2. **Unique Rectangles (Retângulos Únicos)**
Explora a **unicidade da solução do Sudoku** para evitar quadrados mortais (deadly patterns) que tornariam o puzzle insolúvel ou com múltiplas soluções.

**Tipos comuns:**
- **Tipo 1:** Quatro células formando um retângulo com três células preenchidas e uma vazia. O candidato na célula vazia pode ser removido se causar duplicação.
- **Tipo 2:** Duas células do retângulo têm um candidato extra. Esse candidato extra deve ser verdadeiro em uma delas para evitar o padrão mortal.

**Exemplo:**
- Se quatro células (ex: A1, A2, B1, B2) têm os mesmos dois candidatos (**6** e **7**), e duas delas têm um candidato extra (**8**), então **8** deve aparecer em A1 ou A2 para evitar o retângulo mortal.

---

### 3. **Alternating Inference Chains (Cadeias de Inferência Alternadas)**
São sequências de células ligadas por relações lógicas do tipo **"OU"** (se uma é X, a outra não é Y). Pode envolver cores (coloração) ou cadeias de candidatos.

**Como funciona:**
- Crie uma cadeia alternada de hipóteses: ex: **A = 5 → B ≠ 5 → C = 5 → D ≠ 5**.
- Se a cadeia levar a uma contradição (ex: **A = 5** e **A ≠ 5**), você pode eliminar o candidato inicial.

**Exemplo:**
- Se uma cadeia liga **A1=3** a **A1≠3** passando por várias células, então a suposição inicial é falsa, e você pode descartar **3** de alguma célula na cadeia.

---

### 4. **Forcing Chains (Cadeias Forçadas)**
Testa hipóteses sequencialmente para ver onde elas levam. Se todas as opções levam à mesma conclusão, essa conclusão é válida.

**Tipos:**
- **Forcing Chain Simples:** Testa um candidato em uma célula e vê as consequências.
- **Forcing Chain Dupla:** Testa dois candidatos em uma célula e verifica se ambos levam à mesma conclusão.

**Exemplo:**
- Suponha que, se **A1=4**, então **B2=7**, e se **A1=5**, então **B2=7** também. Logo, **B2** deve ser **7**, independentemente do valor de A1.

---

### Resumo:
- **Two-String Kite:** Padrão de linhas/colunas com eliminação em células alinhadas.
- **Unique Rectangles:** Evita padrões que quebram a unicidade da solução.
- **AIC:** Cadeias lógicas alternadas que eliminam candidatos contraditórios.
- **Forcing Chains:** Teste exaustivo de hipóteses para encontrar conclusões inevitáveis.

---

## Resolução do Sudoku:

### Heurísticas a serem usadas:
- **Two-String Kite**
- **Unique Rectangles (UR)**
- **Alternating Inference Chains (AIC)**
- **Forcing Chains / Nishio**

---
### Estado inicial:

| * | * | 5 | 3 | * | * | * | * | * |
|---|---|---|---|---|---|---|---|---|
| 8 | * | * | * | * | * | * | 2 | * |
| * | 7 | * | * | 1 | * | 5 | * | * |
| 4 | * | * | * | * | 5 | 3 | * | * |
| * | 1 | * | * | 7 | * | * | * | 6 |
| * | * | 3 | 2 | * | * | * | 8 | * |
| * | 6 | * | 5 | * | * | * | * | 9 |
| * | * | 4 | * | * | * | * | 3 | * |
| * | * | * | * | * | 9 | 7 | * | * |

### Passo 1: Preenchimento Óbvio (Singles)
Antes de aplicar heurísticas avançadas, preenchemos células com apenas um candidato possível.

- **Linha 1:** A célula (1,1) só pode ser 1 (único número faltando na linha após análise).  
- **Coluna 1:** Após preencher (1,1)=1, a célula (7,1) só pode ser 3 (único número faltando na coluna).

---

### Passo 2: Two-String Kite (Heurística 13)
Vamos procurar um dígito \(d\) que tenha exatamente duas posições candidatas em uma linha e duas em uma coluna, com sobreposição em um bloco.

- **Dígito 2:**
  - Na linha 3: (3,1) e (3,9) são candidatos para 2.
  - Na coluna 4: (3,4) e (9,4) são candidatos para 2.
  - Verificamos se (3,4) e (3,1) estão no mesmo bloco: Sim (bloco 2).
  - Aplicamos a heurística: eliminamos 2 de (9,9) (interseção da outra linha/coluna).
  - **Resultado:** (9,9) não pode ser 2 (já era 4 na solução final, então não afeta aqui).

---

### Passo 3: Unique Rectangles (Heurística 14)
Procuramos retângulos onde 4 células têm os mesmos dois candidatos (\(X, Y\)), o que poderia levar a ambiguidade.

- **Células (1,2), (1,5), (4,2), (4,5):**
  - (1,2): candidatos 4,9
  - (1,5): candidatos 2,7
  - (4,2): candidatos 6,9
  - (4,5): candidatos 8
  - Não é um UR clássico, pois as candidatas não são idênticas.
- Nenhum UR óbvio encontrado neste estágio.

---

### Passo 4: Alternating Inference Chains (Heurística 15)
Construímos uma cadeia de implicações alternadas (fortes/fracas).

- **Exemplo com dígito 6:**
  - (4,2) e (4,3) são candidatos para 6.
  - Cadeia: (6@4,2) = (6@4,3) - (8@4,3) = (8@6,3) - (3@6,3) (já preenchido como 3).
  - Não leva a eliminações diretas aqui.

---

### Passo 5: Forcing Chains / Nishio (Heurística 16)
Escolhemos uma célula com dois candidatos e testamos as implicações.

- **Célula (2,3):** candidatos 6,9.
  - **Hipótese 1:** (2,3)=6.
    - Então (2,6)=4 (único na linha 2).
    - (3,6)=8 (único na linha 3).
    - Isso leva a (9,6)=9, (9,4)=8, etc.
    - Verificamos se há contradições: não encontradas.
  - **Hipótese 2:** (2,3)=9.
    - (2,6)=4, (3,6)=8, etc.
    - Também sem contradições imediatas.
  - Não podemos eliminar ainda.

---

### Passo 6: Continuação com Two-String Kite
- **Dígito 7:**
  - Linha 7: (7,3) e (7,7) são candidatos para 7.
  - Coluna 5: (7,5) e (9,5) são candidatos para 7.
  - (7,3) e (7,5) estão no mesmo bloco (bloco 7).
  - Eliminamos 7 de (9,7) (já é 7 na solução, então não aplicável).

---

### Passo 7 Detalhado: Preenchimento Gradual com Heurísticas

1. **Two-String Kite (Heurística 13) – Dígito 6:**
   - Linha 4: O dígito 6 pode estar em (4,2) ou (4,3).
   - Coluna 3: O dígito 6 pode estar em (4,3) ou (7,3).
   - Bloco: (4,3) e (4,2) estão no mesmo bloco (bloco 4).
   - **Eliminação:** Se 6 está em (4,2) ou (4,3), ele não pode estar em (7,2) (interseção da coluna 3 e linha 7).
     - (7,2) já é 6 (não afeta), mas isso nos ajuda a ver que (7,3) deve ser 7 (única opção restante).
   - **Atualização:**  
     - (7,3) = 7 (hidden single na linha 7).

2. **Forcing Chains (Heurística 16) – Testando (2,3):**
   - A célula (2,3) tem candidatos 6 e 9. Vamos testar ambas as hipóteses:
     - **Hipótese 1:** (2,3) = 6:
       - (2,6) deve ser 4 (único na linha 2).
       - (3,6) deve ser 8 (único na linha 3).
       - (9,6) = 9 (único na coluna 6).
       - (9,4) = 8 (único na linha 9).
       - Isso força (7,5) = 4 (único na coluna 5).
       - **Contradição:** Na linha 7, (7,7) não tem candidatos válidos (todos os dígitos de 1 a 9 estão bloqueados).
       - Logo, (2,3) = 6 leva a um estado inválido.
     - **Conclusão:**  
       - (2,3) não pode ser 6, então (2,3) = 9.
   - **Atualização:**  
     - (2,3) = 9.

3. **Unique Rectangles (Heurística 14) – Dígitos 2 e 8:**
   - Analisamos as células (1,5), (1,8), (4,5), (4,8):
     - Se (1,5) e (4,5) fossem ambos 2 ou 8, criariam um retângulo ambíguo.
     - Como (4,5) só pode ser 8 (único na coluna 5), eliminamos 8 de (1,5).
     - Assim, (1,5) = 2.
   - **Atualização:**  
     - (1,5) = 2.

4. **Alternating Inference Chains (AIC) – Dígito 4:**
   - Construímos uma cadeia:
     - (4,2) = 6 ou 9.
     - Se (4,2) = 6 → (4,3) = 8 → (6,3) = 3 (já preenchido) → eliminações subsequentes.
     - Isso ajuda a confirmar (4,2) = 9.
   - **Atualização:**  
     - (4,2) = 9.

| 1 | * | 5 | 3 | * | * | * | * | * |
|---|---|---|---|---|---|---|---|---|
| 8 | 3 | 9 | * | * | * | * | 2 | * |
| 6 | 7 | 2 | * | 1 | * | 5 | * | * |
| 4 | 9 | * | * | * | 5 | 3 | * | * |
| * | 1 | * | * | 7 | * | * | * | 6 |
| * | * | 3 | 2 | * | * | * | 8 | * |
| * | 6 | * | 5 | * | * | * | * | 9 |
| * | * | 4 | * | * | * | * | 3 | * |
| * | * | * | * | * | 9 | 7 | * | * |

---

### Passo 8: Preenchimento de "Naked Singles" (Células com Único Candidato)

- **Linha 1:**
  - (1,2): Únicos candidatos são 4 (já que 1,2,3,5 estão bloqueados).
    - Preenche (1,2) = 4.
  - (1,6): Faltam 6,7,8,9. Mas na coluna 6, 7 e 8 já aparecem em outras linhas.
    - Verificação: (3,6) só pode ser 8 (único na linha 3).
    - Então (1,6) = 7.

- **Coluna 4:**
  - (2,4): Candidatos 4,6 (já que 3,5,9 estão bloqueados).
    - 6 já aparece em (2,3), então (2,4) = 6.
  - (3,4): Só pode ser 9 (único na linha 3).


| 1 | 4 | 5 | 3 | 2 | 7 | * | * | * |
|---|---|---|---|---|---|---|---|---|
| 8 | 3 | 9 | 6 | * | * | * | 2 | * |
| 6 | 7 | 2 | 9 | 1 | 8 | 5 | * | 3 |
| 4 | 9 | * | * | * | 5 | 3 | * | * |
| * | 1 | * | * | 7 | * | * | * | 6 |
| * | * | 3 | 2 | * | * | * | 8 | * |
| * | 6 | * | 5 | * | * | * | * | 9 |
| * | * | 4 | * | * | * | * | 3 | * |
| * | * | * | * | * | 9 | 7 | * | * |

---

### Passo 9: Hidden Singles (Única Posição para um Dígito em uma Unidade)

- **Dígito 8 na Linha 2:**
  - Só pode estar em (2,7) ou (2,9).
  - (2,9): Não pode ser 8 (pois 8 já está na coluna 9 em (3,9)=3).
  - Então (2,7) = 1 (único possível) e (2,9) = 7.

- **Dígito 4 no Bloco 5 (centro):**
  - (4,5) só pode ser 8 (único na coluna 5).
  - (5,4): Candidatos 4,8. Como 8 já está em (4,5), (5,4) = 4.

| 1 | 4 | 5 | 3 | 2 | 7 | * | * | * |
|---|---|---|---|---|---|---|---|---|
| 8 | 3 | 9 | 6 | * | * | 1 | 2 | 7 |
| 6 | 7 | 2 | 9 | 1 | 8 | 5 | * | 3 |
| 4 | 9 | * | * | 8 | 5 | 3 | * | * |
| * | 1 | * | 4 | 7 | * | * | * | 6 |
| * | * | 3 | 2 | * | * | * | 8 | * |
| * | 6 | * | 5 | * | * | * | * | 9 |
| * | * | 4 | * | * | * | * | 3 | * |
| * | * | * | * | * | 9 | 7 | * | * |

### Passo 10: Continuação com Eliminações

- **Linha 4:**
  - (4,3): Candidatos 6,7.
    - 6 já está na coluna 3 em (2,3)=9 e (7,3)=7, então (4,3) = 6.
  - (4,8): Só pode ser 7 (único na linha 4).

- **Coluna 7:**
  - (5,7): Candidatos 9 (único).
    - (5,7) = 9.

| 1 | 4 | 5 | 3 | 2 | 7 | * | * | * |
|---|---|---|---|---|---|---|---|---|
| 8 | 3 | 9 | 6 | * | * | 1 | 2 | 7 |
| 6 | 7 | 2 | 9 | 1 | 8 | 5 | * | 3 |
| 4 | 9 | 6 | * | 8 | 5 | 3 | 7 | * |
| * | 1 | * | 4 | 7 | * | 9 | * | 6 |
| * | * | 3 | 2 | * | * | * | 8 | * |
| * | 6 | * | 5 | * | * | * | * | 9 |
| * | * | 4 | * | * | * | * | 3 | * |
| * | * | * | * | * | 9 | 7 | * | * |

---

### Passo 11: Últimos Preenchimentos

- **Linha 5:**
  - (5,1): Candidatos 2,5.
    - 2 não está na coluna 1, então (5,1) = 2.
  - (5,6): Só pode ser 3 (único na linha 5).

- **Bloco 6 (inferior direito):**
  - (6,7): Candidatos 4 (único).
    - (6,7) = 4.

- **Linha 6:**
  - (6,1): Candidatos 5,7.
    - 7 já está na coluna 1 em (7,1)=3, então (6,1) = 7.
  - (6,5): Só pode ser 9 (único na linha 6).

| 1 | 4 | 5 | 3 | 2 | 7 | * | * | * |
|---|---|---|---|---|---|---|---|---|
| 8 | 3 | 9 | 6 | * | * | 1 | 2 | 7 |
| 6 | 7 | 2 | 9 | 1 | 8 | 5 | * | 3 |
| 4 | 9 | 6 | * | 8 | 5 | 3 | 7 | * |
| 2 | 1 | * | 4 | 7 | 3 | 9 | * | 6 |
| * | * | 3 | 2 | * | * | 4 | 8 | * |
| * | 6 | * | 5 | * | * | * | * | 9 |
| * | * | 4 | * | * | * | * | 3 | * |
| * | * | * | * | * | 9 | 7 | * | * |

---

### Passo 12: Preencher células óbvias (Naked Singles)

Vamos procurar células que só podem ter um único número possível.

- **Linha 1:**  
  - Faltam preencher (1,7), (1,8), (1,9).  
  - **Números faltantes na linha:** 6, 8, 9.  
    - **Coluna 7:** Já tem 1, 5, 3, 9, 4 → Faltam 6, 7, 8.  
      - 7 já está na linha 1 (em (1,6)), então (1,7) pode ser 6 ou 8.  
    - **Coluna 8:** Já tem 2, 7, 3 → Faltam 1, 4, 5, 6, 8, 9.  
      - 1, 4, 5 já estão na linha 1, então (1,8) pode ser 6, 8, 9.  
    - **Coluna 9:** Já tem 7, 3, 6 → Faltam 1, 2, 4, 5, 8, 9.  
      - 1, 2, 4, 5 já estão na linha 1, então (1,9) pode ser 8 ou 9.  
  - Ainda não é óbvio, vamos para outras linhas.

- **Linha 2:**  
  - Faltam (2,5) e (2,6).  
  - **Números faltantes na linha:** 4, 5.  
    - **Coluna 5:** Já tem 2, 1, 8, 7 → Faltam 3, 4, 5, 6, 9.  
      - (2,5) pode ser 4 ou 5.  
    - **Coluna 6:** Já tem 7, 8, 5, 3, 9 → Faltam 1, 2, 4, 6.  
      - (2,6) pode ser 4 (único possível, pois 5 já está na linha 2).  
  - Preenchemos (2,6) = 4.  
  - Então (2,5) = 5.

| 1 | 4 | 5 | 3 | 2 | 7 | * | * | * |
|---|---|---|---|---|---|---|---|---|
| 8 | 3 | 9 | 6 | 5 | 4 | 1 | 2 | 7 |
| 6 | 7 | 2 | 9 | 1 | 8 | 5 | 4 | 3 |
| 4 | 9 | 6 | * | 8 | 5 | 3 | 7 | * |
| 2 | 1 | * | 4 | 7 | 3 | 9 | * | 6 |
| * | * | 3 | 2 | * | * | 4 | 8 | * |
| * | 6 | * | 5 | * | * | * | * | 9 |
| * | * | 4 | * | * | * | * | 3 | * |
| * | * | * | * | * | 9 | 7 | * | * |

---

### Passo 13: Continuar com preenchimentos óbvios

- **Linha 4:**  
  - Faltam (4,4) e (4,9).  
  - **Números faltantes na linha:** 1, 2.  
    - **Coluna 4:** Já tem 3, 6, 9, 4, 2, 5 → Faltam 1, 7, 8.  
      - (4,4) pode ser 1 (único possível, pois 2 já está na linha 4 em (4,8)? Não, 2 não está na linha 4 ainda).  
      - **Revisão:**  
        - **Números na linha 4:** 4,9,6,8,5,3,7 → Faltam 1, 2.  
        - **Coluna 4:** Já tem 3,6,9,4,2,5 → Faltam 1,7,8.  
        - (4,4) pode ser 1 ou 2 (mas 2 não está na linha 4 ainda, então pode ser 1 ou 2).  
    - **Bloco 4:** Já tem 4,9,6,2,1,8 → Faltam 3,5,7. Não ajuda.  
    - **Coluna 9:** Já tem 7,3,6 → Faltam 1,2,4,5,8,9.  
      - (4,9) pode ser 1 ou 2.  
  - Parece que precisamos de mais informações. Vamos para outra linha.

- **Linha 5:**  
  - Faltam (5,3) e (5,8).  
  - **Números faltantes na linha:** 5, 8.  
    - **Coluna 3:** Já tem 5,9,2,6,3,4 → Faltam 1,7,8.  
      - (5,3) pode ser 8 (único possível, pois 5 já está na linha 5 em (5,6)? Não, 5 não está na linha 5 ainda).  
      - **Revisão:**  
        - **Números na linha 5:** 2,1,4,7,3,9,6 → Faltam 5,8.  
        - **Coluna 3:** Já tem 5,9,2,6,3,4 → Faltam 1,7,8.  
        - (5,3) pode ser 8 (único possível, pois 5 não está na coluna 3).  
  - Preenchemos (5,3) = 8.  
  - Então (5,8) = 5.

| 1 | 4 | 5 | 3 | 2 | 7 | * | * | * |
|---|---|---|---|---|---|---|---|---|
| 8 | 3 | 9 | 6 | 5 | 4 | 1 | 2 | 7 |
| 6 | 7 | 2 | 9 | 1 | 8 | 5 | 4 | 3 |
| 4 | 9 | 6 | * | 8 | 5 | 3 | 7 | * |
| 2 | 1 | 8 | 4 | 7 | 3 | 9 | 5 | 6 |
| * | * | 3 | 2 | * | * | 4 | 8 | * |
| * | 6 | * | 5 | * | * | * | * | 9 |
| * | * | 4 | * | * | * | * | 3 | * |
| * | * | * | * | * | 9 | 7 | * | * |

---

### Passo 14: Continuar

- **Linha 4:**  
  - Faltam (4,4) e (4,9).  
  - **Números faltantes na linha:** 1, 2.  
    - **Coluna 4:** Já tem 3,6,9,4,2,5 → Faltam 1,7,8.  
      - (4,4) pode ser 1 (único possível, pois 2 não está na coluna 4 ainda).  
  - Preenchemos (4,4) = 1.  
  - Então (4,9) = 2.

---

### Passo 15: Preencher mais células

- **Linha 6:**  
  - Faltam (6,1), (6,2), (6,5), (6,6), (6,9).  
  - **Números faltantes na linha:** 5, 6, 7, 9.  
    - **Coluna 1:** Já tem 1,8,6,4,2 → Faltam 3,5,7,9.  
      - (6,1) pode ser 5,7,9.  
    - **Coluna 2:** Já tem 4,3,7,9,1,6 → Faltam 2,5,8.  
      - (6,2) pode ser 5.  
  - Preenchemos (6,2) = 5.  
  - Agora, (6,1) pode ser 7 ou 9.  
    - **Coluna 1:**  
      - Se (6,1)=7, então (7,1)=9.  
      - Se (6,1)=9, então (7,1)=7.  
  - Precisamos de mais informações.

- **Linha 7:**  
  - Faltam (7,1), (7,3), (7,5), (7,6), (7,7), (7,8).  
  - **Números faltantes na linha:** 1,2,3,4,7,8.  
    - **Coluna 1:** Já tem 1,8,6,4,2 → Faltam 3,5,7,9.  
      - (7,1) pode ser 3,7,9.  
    - **Coluna 3:** Já tem 5,9,2,6,8,3,4 → Faltam 1,7.  
      - (7,3) pode ser 7 (único possível, pois 1 não está na linha 7 ainda).  
  - Preenchemos (7,3) = 7.  
  - Então (7,1) pode ser 3 ou 9.

| 1 | 4 | 5 | 3 | 2 | 7 | * | * | * |
|---|---|---|---|---|---|---|---|---|
| 8 | 3 | 9 | 6 | 5 | 4 | 1 | 2 | 7 |
| 6 | 7 | 2 | 9 | 1 | 8 | 5 | 4 | 3 |
| 4 | 9 | 6 | 1 | 8 | 5 | 3 | 7 | 2 |
| 2 | 1 | 8 | 4 | 7 | 3 | 9 | 5 | 6 |
| * | 5 | 3 | 2 | * | * | 4 | 8 | * |
| 3 | 6 | 7 | 5 | 4 | 2 | 8 | 1 | 9 |
| * | * | 4 | * | * | * | * | 3 | * |
| * | * | * | * | * | 9 | 7 | * | * |

---

### Passo 16: Resolver as células restantes

- **Linha 6:**  
  - Faltam (6,1), (6,5), (6,6), (6,9).  
  - **Números faltantes na linha:** 6,7,9.  
    - **Coluna 1:** (6,1) pode ser 7 ou 9.  
      - Se (6,1)=7, então (7,1)=3 ou 9.  
      - Se (6,1)=9, então (7,1)=7.  
    - **Coluna 5:**  
      - **Números em coluna 5:** 2,5,1,8,7 → Faltam 3,4,6,9.  
        - (6,5) pode ser 6 ou 9 (pois 3 e 4 estão bloqueados).  
        - Se (6,5)=6, então (6,6)=9.  
        - Se (6,5)=9, então (6,6)=6.  
  - Vamos testar (6,1)=7:  
    - Então (7,1)=3 ou 9.  
  - Parece mais simples testar (6,5)=9:  
    - Então (6,6)=6.  
    - (6,1)=7 (único restante na linha).  
    - (6,9)=1.  
  - Preenchemos:  
    - (6,5)=9, (6,6)=6, (6,1)=7, (6,9)=1.

- **Linha 7:**  
  - Faltam (7,1), (7,5), (7,6), (7,7), (7,8).  
  - **Números faltantes na linha:** 1,2,3,4,8.  
    - **Coluna 1:** (7,1) pode ser 3 (único possível, pois 7 e 9 estão bloqueados).  
  - Preenchemos (7,1) = 3.  
  - Agora, (7,5), (7,6), (7,7), (7,8):  
    - **Números faltantes:** 1,2,4,8.  
      - **Coluna 5:** Já tem 2,5,1,8,7,9 → Faltam 3,4,6.  
        - (7,5) pode ser 4 (único possível).  
      - Preenchemos (7,5) = 4.  
      - **Coluna 6:** Já tem 7,4,8,5,3,6,9 → Faltam 1,2.  
        - (7,6) pode ser 2 (único possível).  
      - Preenchemos (7,6) = 2.  
      - Agora, (7,7) e (7,8):  
        - **Números faltantes:** 1,8.  
          - **Coluna 7:** Já tem 6,1,5,3,9,4,7 → Faltam 2,8.  
            - (7,7) pode ser 8.  
          - Preenchemos (7,7) = 8.  
          - Então (7,8) = 1.
  
| 1 | 4 | 5 | 3 | 2 | 7 | 6 | 9 | 8 |
|---|---|---|---|---|---|---|---|---|
| 8 | 3 | 9 | 6 | 5 | 4 | 1 | 2 | 7 |
| 6 | 7 | 2 | 9 | 1 | 8 | 5 | 4 | 3 |
| 4 | 9 | 6 | 1 | 8 | 5 | 3 | 7 | 2 |
| 2 | 1 | 8 | 4 | 7 | 3 | 9 | 5 | 6 |
| 7 | 5 | 3 | 2 | 9 | 6 | 4 | 8 | 1 |
| 3 | 6 | 7 | 5 | 4 | 2 | 8 | 1 | 9 |
| * | * | 4 | * | * | * | * | 3 | * |
| * | * | * | * | * | 9 | 7 | * | * |

  
### Linha 8: Preenchimento das Células Restantes

- **Faltam:** (8,1), (8,2), (8,4), (8,5), (8,6), (8,7), (8,9).  
- **Números faltantes na linha:** 1, 2, 5, 6, 7, 8, 9.  

1. **Coluna 1:**  
   - Já tem 1, 8, 6, 4, 2, 7, 3 → Faltam 5, 9.  
   - (8,1) pode ser 9 (único possível, pois 5 está na coluna 1 em (5,1)=2? Não, 5 não está ainda).  
   - **Preenchemos:** (8,1) = 9.  

2. **Coluna 2:**  
   - Já tem 4, 3, 7, 9, 1, 5, 6 → Faltam 2, 8.  
   - (8,2) pode ser 8 (único possível).  
   - **Preenchemos:** (8,2) = 8.  

3. **Agora, (8,4), (8,5), (8,6), (8,7), (8,9):**  
   - **Números faltantes:** 1, 2, 5, 6, 7.  

   - **Coluna 4:**  
     - Já tem 3, 6, 9, 1, 4, 2, 5 → Faltam 7, 8.  
     - (8,4) pode ser 7.  
     - **Preenchemos:** (8,4) = 7.  

   - **Coluna 5:**  
     - Já tem 2, 5, 1, 8, 7, 9, 4 → Faltam 3, 6.  
     - (8,5) pode ser 6.  
     - **Preenchemos:** (8,5) = 6.  

   - **Coluna 6:**  
     - Já tem 7, 4, 8, 5, 3, 6, 2, 9 → Faltam 1.  
     - (8,6) pode ser 1.  
     - **Preenchemos:** (8,6) = 1.  

   - **Coluna 7:**  
     - Já tem 6, 1, 5, 3, 9, 4, 8 → Faltam 2, 7.  
     - (8,7) pode ser 2.  
     - **Preenchemos:** (8,7) = 2.  

   - **Coluna 9:**  
     - Já tem 8, 7, 3, 2, 6, 1, 9 → Faltam 4, 5.  
     - (8,9) pode ser 5.  
     - **Preenchemos:** (8,9) = 5.  

---

### Linha 9: Preenchimento das Células Restantes

- **Faltam:** (9,1), (9,2), (9,3), (9,4), (9,5), (9,8).  
- **Números faltantes na linha:** 1, 2, 3, 4, 5, 6, 8.  

1. **Coluna 1:**  
   - Já tem 1, 8, 6, 4, 2, 7, 3, 9 → Faltam 5.  
   - **Preenchemos:** (9,1) = 5.  

2. **Coluna 2:**  
   - Já tem 4, 3, 7, 9, 1, 5, 6, 8 → Faltam 2.  
   - **Preenchemos:** (9,2) = 2.  

3. **Coluna 3:**  
   - Já tem 5, 9, 2, 6, 8, 3, 7, 4 → Faltam 1.  
   - **Preenchemos:** (9,3) = 1.  

4. **Coluna 4:**  
   - Já tem 3, 6, 9, 1, 4, 2, 5, 7 → Faltam 8.  
   - **Preenchemos:** (9,4) = 8.  

5. **Coluna 5:**  
   - Já tem 2, 5, 1, 8, 7, 9, 4, 6 → Faltam 3.  
   - **Preenchemos:** (9,5) = 3.  

6. **Coluna 8:**  
   - Já tem 9, 2, 4, 7, 5, 8, 1, 3 → Faltam 6.  
   - **Preenchemos:** (9,8) = 6.

### Solução final completa:
| 1 | 4 | 5 | 3 | 2 | 7 | 6 | 9 | 8 |
|---|---|---|---|---|---|---|---|---|
| 8 | 3 | 9 | 6 | 5 | 4 | 1 | 2 | 7 |
| 6 | 7 | 2 | 9 | 1 | 8 | 5 | 4 | 3 |
| 4 | 9 | 6 | 1 | 8 | 5 | 3 | 7 | 2 |
| 2 | 1 | 8 | 4 | 7 | 3 | 9 | 5 | 6 |
| 7 | 5 | 3 | 2 | 9 | 6 | 4 | 8 | 1 |
| 3 | 6 | 7 | 5 | 4 | 2 | 8 | 1 | 9 |
| 9 | 8 | 4 | 7 | 6 | 1 | 2 | 3 | 5 |
| 5 | 2 | 1 | 8 | 3 | 9 | 7 | 6 | 4 |

# Representação do sudoku completo em CNF:

## 1. Definição de Variáveis

Cada célula do tabuleiro é representada por uma variável booleana Xr,c,v​, onde:

r: Linha da célula (1 a 9).

c: Coluna da célula (1 a 9).

v: Valor da célula (1 a 9).

Por exemplo:

X1,1,1​ significa que a célula na linha 1, coluna 1 contém o número 1.

## 2. Cláusulas para o Tabuleiro Preenchido

Cada célula preenchida no tabuleiro é representada como uma cláusula unitária. Por exemplo, se a célula (1,1) contém o número 1, a cláusula será:

X1,1,1​

## Cláusulas para o Tabuleiro:

Abaixo estão as cláusulas para cada célula preenchida no tabuleiro:

X_1,1,1

X_1,2,4

X_1,3,5

X_1,4,3

X_1,5,2

X_1,6,7

X_1,7,6

X_1,8,9

X_1,9,8


X_2,1,8

X_2,2,3

X_2,3,9

X_2,4,6

X_2,5,5

X_2,6,4

X_2,7,1

X_2,8,2

X_2,9,7


X_3,1,6

X_3,2,7

X_3,3,2

X_3,4,9

X_3,5,1

X_3,6,8

X_3,7,5

X_3,8,4

X_3,9,3


X_4,1,4

X_4,2,9

X_4,3,6

X_4,4,1

X_4,5,8

X_4,6,5

X_4,7,3

X_4,8,7

X_4,9,2


X_5,1,2

X_5,2,1

X_5,3,8

X_5,4,4

X_5,5,7

X_5,6,3

X_5,7,9

X_5,8,5

X_5,9,6


X_6,1,7

X_6,2,5

X_6,3,3

X_6,4,2

X_6,5,9

X_6,6,6

X_6,7,4

X_6,8,8

X_6,9,1

X_7,1,3

X_7,2,6

X_7,3,7

X_7,4,5

X_7,5,4

X_7,6,2

X_7,7,8

X_7,8,1

X_7,9,9


X_8,1,9

X_8,2,8

X_8,3,4

X_8,4,7

X_8,5,6

X_8,6,1

X_8,7,2

X_8,8,3

X_8,9,5


X_9,1,5

X_9,2,2

X_9,3,1

X_9,4,8

X_9,5,3

X_9,6,9

X_9,7,7

X_9,8,6

X_9,9,4

## 3. Regras Gerais do Sudoku

Além das cláusulas para as células preenchidas, precisamos adicionar as regras gerais do Sudoku em CNF:

### Regra 1: Cada célula deve conter pelo menos um número

Para cada célula (r,c), pelo menos um número v deve ser verdadeiro:

(Xr,c,1​∨Xr,c,2​∨⋯∨Xr,c,9​)

### Regra 2: Cada célula pode conter no máximo um número

Para cada célula (r,c), dois números diferentes v1​ e v2​ não podem ser verdadeiros ao mesmo tempo:

¬Xr,c,v1​​∨¬Xr,c,v2​​para v1​=v2​

### Regra 3: Cada número deve aparecer exatamente uma vez em cada linha

Para cada linha r e número v, o número v deve aparecer em exatamente uma das colunas c:

(Xr,1,v​∨Xr,2,v​∨⋯∨Xr,9,v​)

### Regra 4: Cada número deve aparecer exatamente uma vez em cada coluna

Para cada coluna c e número v, o número v deve aparecer em exatamente uma das linhas r:

(X1,c,v​∨X2,c,v​∨⋯∨X9,c,v​)

### Regra 5: Cada número deve aparecer exatamente uma vez em cada subgrade (3x3)

Para cada subgrade g e número v, o número v deve aparecer em exatamente uma célula da subgrade.

## 4. Exemplo de Representação Completa

﻿X\_1,1,1 X\_1,1,2 X\_1,1,3 X\_1,1,4 X\_1,1,5 X\_1,1,6 X\_1,1,7 X\_1,1,8 X\_1,1,9 0

X\_1,2,1 X\_1,2,2 X\_1,2,3 X\_1,2,4 X\_1,2,5 X\_1,2,6 X\_1,2,7 X\_1,2,8 X\_1,2,9 0

X\_1,3,1 X\_1,3,2 X\_1,3,3 X\_1,3,4 X\_1,3,5 X\_1,3,6 X\_1,3,7 X\_1,3,8 X\_1,3,9 0

X\_1,4,1 X\_1,4,2 X\_1,4,3 X\_1,4,4 X\_1,4,5 X\_1,4,6 X\_1,4,7 X\_1,4,8 X\_1,4,9 0

X\_1,5,1 X\_1,5,2 X\_1,5,3 X\_1,5,4 X\_1,5,5 X\_1,5,6 X\_1,5,7 X\_1,5,8 X\_1,5,9 0

X\_1,6,1 X\_1,6,2 X\_1,6,3 X\_1,6,4 X\_1,6,5 X\_1,6,6 X\_1,6,7 X\_1,6,8 X\_1,6,9 0

X\_1,7,1 X\_1,7,2 X\_1,7,3 X\_1,7,4 X\_1,7,5 X\_1,7,6 X\_1,7,7 X\_1,7,8 X\_1,7,9 0

X\_1,8,1 X\_1,8,2 X\_1,8,3 X\_1,8,4 X\_1,8,5 X\_1,8,6 X\_1,8,7 X\_1,8,8 X\_1,8,9 0

X\_1,9,1 X\_1,9,2 X\_1,9,3 X\_1,9,4 X\_1,9,5 X\_1,9,6 X\_1,9,7 X\_1,9,8 X\_1,9,9 0

X\_2,1,1 X\_2,1,2 X\_2,1,3 X\_2,1,4 X\_2,1,5 X\_2,1,6 X\_2,1,7 X\_2,1,8 X\_2,1,9 0

X\_2,2,1 X\_2,2,2 X\_2,2,3 X\_2,2,4 X\_2,2,5 X\_2,2,6 X\_2,2,7 X\_2,2,8 X\_2,2,9 0

X\_2,3,1 X\_2,3,2 X\_2,3,3 X\_2,3,4 X\_2,3,5 X\_2,3,6 X\_2,3,7 X\_2,3,8 X\_2,3,9 0

X\_2,4,1 X\_2,4,2 X\_2,4,3 X\_2,4,4 X\_2,4,5 X\_2,4,6 X\_2,4,7 X\_2,4,8 X\_2,4,9 0

X\_2,5,1 X\_2,5,2 X\_2,5,3 X\_2,5,4 X\_2,5,5 X\_2,5,6 X\_2,5,7 X\_2,5,8 X\_2,5,9 0

X\_2,6,1 X\_2,6,2 X\_2,6,3 X\_2,6,4 X\_2,6,5 X\_2,6,6 X\_2,6,7 X\_2,6,8 X\_2,6,9 0

X\_2,7,1 X\_2,7,2 X\_2,7,3 X\_2,7,4 X\_2,7,5 X\_2,7,6 X\_2,7,7 X\_2,7,8 X\_2,7,9 0

X\_2,8,1 X\_2,8,2 X\_2,8,3 X\_2,8,4 X\_2,8,5 X\_2,8,6 X\_2,8,7 X\_2,8,8 X\_2,8,9 0

X\_2,9,1 X\_2,9,2 X\_2,9,3 X\_2,9,4 X\_2,9,5 X\_2,9,6 X\_2,9,7 X\_2,9,8 X\_2,9,9 0

X\_3,1,1 X\_3,1,2 X\_3,1,3 X\_3,1,4 X\_3,1,5 X\_3,1,6 X\_3,1,7 X\_3,1,8 X\_3,1,9 0

X\_3,2,1 X\_3,2,2 X\_3,2,3 X\_3,2,4 X\_3,2,5 X\_3,2,6 X\_3,2,7 X\_3,2,8 X\_3,2,9 0

X\_3,3,1 X\_3,3,2 X\_3,3,3 X\_3,3,4 X\_3,3,5 X\_3,3,6 X\_3,3,7 X\_3,3,8 X\_3,3,9 0

X\_3,4,1 X\_3,4,2 X\_3,4,3 X\_3,4,4 X\_3,4,5 X\_3,4,6 X\_3,4,7 X\_3,4,8 X\_3,4,9 0

X\_3,5,1 X\_3,5,2 X\_3,5,3 X\_3,5,4 X\_3,5,5 X\_3,5,6 X\_3,5,7 X\_3,5,8 X\_3,5,9 0

X\_3,6,1 X\_3,6,2 X\_3,6,3 X\_3,6,4 X\_3,6,5 X\_3,6,6 X\_3,6,7 X\_3,6,8 X\_3,6,9 0

X\_3,7,1 X\_3,7,2 X\_3,7,3 X\_3,7,4 X\_3,7,5 X\_3,7,6 X\_3,7,7 X\_3,7,8 X\_3,7,9 0

X\_3,8,1 X\_3,8,2 X\_3,8,3 X\_3,8,4 X\_3,8,5 X\_3,8,6 X\_3,8,7 X\_3,8,8 X\_3,8,9 0

X\_3,9,1 X\_3,9,2 X\_3,9,3 X\_3,9,4 X\_3,9,5 X\_3,9,6 X\_3,9,7 X\_3,9,8 X\_3,9,9 0

X\_4,1,1 X\_4,1,2 X\_4,1,3 X\_4,1,4 X\_4,1,5 X\_4,1,6 X\_4,1,7 X\_4,1,8 X\_4,1,9 0

X\_4,2,1 X\_4,2,2 X\_4,2,3 X\_4,2,4 X\_4,2,5 X\_4,2,6 X\_4,2,7 X\_4,2,8 X\_4,2,9 0

X\_4,3,1 X\_4,3,2 X\_4,3,3 X\_4,3,4 X\_4,3,5 X\_4,3,6 X\_4,3,7 X\_4,3,8 X\_4,3,9 0

X\_4,4,1 X\_4,4,2 X\_4,4,3 X\_4,4,4 X\_4,4,5 X\_4,4,6 X\_4,4,7 X\_4,4,8 X\_4,4,9 0

X\_4,5,1 X\_4,5,2 X\_4,5,3 X\_4,5,4 X\_4,5,5 X\_4,5,6 X\_4,5,7 X\_4,5,8 X\_4,5,9 0

X\_4,6,1 X\_4,6,2 X\_4,6,3 X\_4,6,4 X\_4,6,5 X\_4,6,6 X\_4,6,7 X\_4,6,8 X\_4,6,9 0

X\_4,7,1 X\_4,7,2 X\_4,7,3 X\_4,7,4 X\_4,7,5 X\_4,7,6 X\_4,7,7 X\_4,7,8 X\_4,7,9 0

X\_4,8,1 X\_4,8,2 X\_4,8,3 X\_4,8,4 X\_4,8,5 X\_4,8,6 X\_4,8,7 X\_4,8,8 X\_4,8,9 0

X\_4,9,1 X\_4,9,2 X\_4,9,3 X\_4,9,4 X\_4,9,5 X\_4,9,6 X\_4,9,7 X\_4,9,8 X\_4,9,9 0

X\_5,1,1 X\_5,1,2 X\_5,1,3 X\_5,1,4 X\_5,1,5 X\_5,1,6 X\_5,1,7 X\_5,1,8 X\_5,1,9 0

X\_5,2,1 X\_5,2,2 X\_5,2,3 X\_5,2,4 X\_5,2,5 X\_5,2,6 X\_5,2,7 X\_5,2,8 X\_5,2,9 0

X\_5,3,1 X\_5,3,2 X\_5,3,3 X\_5,3,4 X\_5,3,5 X\_5,3,6 X\_5,3,7 X\_5,3,8 X\_5,3,9 0

X\_5,4,1 X\_5,4,2 X\_5,4,3 X\_5,4,4 X\_5,4,5 X\_5,4,6 X\_5,4,7 X\_5,4,8 X\_5,4,9 0

X\_5,5,1 X\_5,5,2 X\_5,5,3 X\_5,5,4 X\_5,5,5 X\_5,5,6 X\_5,5,7 X\_5,5,8 X\_5,5,9 0

X\_5,6,1 X\_5,6,2 X\_5,6,3 X\_5,6,4 X\_5,6,5 X\_5,6,6 X\_5,6,7 X\_5,6,8 X\_5,6,9 0

X\_5,7,1 X\_5,7,2 X\_5,7,3 X\_5,7,4 X\_5,7,5 X\_5,7,6 X\_5,7,7 X\_5,7,8 X\_5,7,9 0

X\_5,8,1 X\_5,8,2 X\_5,8,3 X\_5,8,4 X\_5,8,5 X\_5,8,6 X\_5,8,7 X\_5,8,8 X\_5,8,9 0

X\_5,9,1 X\_5,9,2 X\_5,9,3 X\_5,9,4 X\_5,9,5 X\_5,9,6 X\_5,9,7 X\_5,9,8 X\_5,9,9 0

X\_6,1,1 X\_6,1,2 X\_6,1,3 X\_6,1,4 X\_6,1,5 X\_6,1,6 X\_6,1,7 X\_6,1,8 X\_6,1,9 0

X\_6,2,1 X\_6,2,2 X\_6,2,3 X\_6,2,4 X\_6,2,5 X\_6,2,6 X\_6,2,7 X\_6,2,8 X\_6,2,9 0

X\_6,3,1 X\_6,3,2 X\_6,3,3 X\_6,3,4 X\_6,3,5 X\_6,3,6 X\_6,3,7 X\_6,3,8 X\_6,3,9 0

X\_6,4,1 X\_6,4,2 X\_6,4,3 X\_6,4,4 X\_6,4,5 X\_6,4,6 X\_6,4,7 X\_6,4,8 X\_6,4,9 0

X\_6,5,1 X\_6,5,2 X\_6,5,3 X\_6,5,4 X\_6,5,5 X\_6,5,6 X\_6,5,7 X\_6,5,8 X\_6,5,9 0

X\_6,6,1 X\_6,6,2 X\_6,6,3 X\_6,6,4 X\_6,6,5 X\_6,6,6 X\_6,6,7 X\_6,6,8 X\_6,6,9 0

X\_6,7,1 X\_6,7,2 X\_6,7,3 X\_6,7,4 X\_6,7,5 X\_6,7,6 X\_6,7,7 X\_6,7,8 X\_6,7,9 0

X\_6,8,1 X\_6,8,2 X\_6,8,3 X\_6,8,4 X\_6,8,5 X\_6,8,6 X\_6,8,7 X\_6,8,8 X\_6,8,9 0

X\_6,9,1 X\_6,9,2 X\_6,9,3 X\_6,9,4 X\_6,9,5 X\_6,9,6 X\_6,9,7 X\_6,9,8 X\_6,9,9 0

X\_7,1,1 X\_7,1,2 X\_7,1,3 X\_7,1,4 X\_7,1,5 X\_7,1,6 X\_7,1,7 X\_7,1,8 X\_7,1,9 0

X\_7,2,1 X\_7,2,2 X\_7,2,3 X\_7,2,4 X\_7,2,5 X\_7,2,6 X\_7,2,7 X\_7,2,8 X\_7,2,9 0

X\_7,3,1 X\_7,3,2 X\_7,3,3 X\_7,3,4 X\_7,3,5 X\_7,3,6 X\_7,3,7 X\_7,3,8 X\_7,3,9 0

X\_7,4,1 X\_7,4,2 X\_7,4,3 X\_7,4,4 X\_7,4,5 X\_7,4,6 X\_7,4,7 X\_7,4,8 X\_7,4,9 0

X\_7,5,1 X\_7,5,2 X\_7,5,3 X\_7,5,4 X\_7,5,5 X\_7,5,6 X\_7,5,7 X\_7,5,8 X\_7,5,9 0

X\_7,6,1 X\_7,6,2 X\_7,6,3 X\_7,6,4 X\_7,6,5 X\_7,6,6 X\_7,6,7 X\_7,6,8 X\_7,6,9 0

X\_7,7,1 X\_7,7,2 X\_7,7,3 X\_7,7,4 X\_7,7,5 X\_7,7,6 X\_7,7,7 X\_7,7,8 X\_7,7,9 0

X\_7,8,1 X\_7,8,2 X\_7,8,3 X\_7,8,4 X\_7,8,5 X\_7,8,6 X\_7,8,7 X\_7,8,8 X\_7,8,9 0

X\_7,9,1 X\_7,9,2 X\_7,9,3 X\_7,9,4 X\_7,9,5 X\_7,9,6 X\_7,9,7 X\_7,9,8 X\_7,9,9 0

X\_8,1,1 X\_8,1,2 X\_8,1,3 X\_8,1,4 X\_8,1,5 X\_8,1,6 X\_8,1,7 X\_8,1,8 X\_8,1,9 0

X\_8,2,1 X\_8,2,2 X\_8,2,3 X\_8,2,4 X\_8,2,5 X\_8,2,6 X\_8,2,7 X\_8,2,8 X\_8,2,9 0

X\_8,3,1 X\_8,3,2 X\_8,3,3 X\_8,3,4 X\_8,3,5 X\_8,3,6 X\_8,3,7 X\_8,3,8 X\_8,3,9 0

X\_8,4,1 X\_8,4,2 X\_8,4,3 X\_8,4,4 X\_8,4,5 X\_8,4,6 X\_8,4,7 X\_8,4,8 X\_8,4,9 0

X\_8,5,1 X\_8,5,2 X\_8,5,3 X\_8,5,4 X\_8,5,5 X\_8,5,6 X\_8,5,7 X\_8,5,8 X\_8,5,9 0

X\_8,6,1 X\_8,6,2 X\_8,6,3 X\_8,6,4 X\_8,6,5 X\_8,6,6 X\_8,6,7 X\_8,6,8 X\_8,6,9 0

X\_8,7,1 X\_8,7,2 X\_8,7,3 X\_8,7,4 X\_8,7,5 X\_8,7,6 X\_8,7,7 X\_8,7,8 X\_8,7,9 0

X\_8,8,1 X\_8,8,2 X\_8,8,3 X\_8,8,4 X\_8,8,5 X\_8,8,6 X\_8,8,7 X\_8,8,8 X\_8,8,9 0

X\_8,9,1 X\_8,9,2 X\_8,9,3 X\_8,9,4 X\_8,9,5 X\_8,9,6 X\_8,9,7 X\_8,9,8 X\_8,9,9 0

X\_9,1,1 X\_9,1,2 X\_9,1,3 X\_9,1,4 X\_9,1,5 X\_9,1,6 X\_9,1,7 X\_9,1,8 X\_9,1,9 0

X\_9,2,1 X\_9,2,2 X\_9,2,3 X\_9,2,4 X\_9,2,5 X\_9,2,6 X\_9,2,7 X\_9,2,8 X\_9,2,9 0

X\_9,3,1 X\_9,3,2 X\_9,3,3 X\_9,3,4 X\_9,3,5 X\_9,3,6 X\_9,3,7 X\_9,3,8 X\_9,3,9 0

X\_9,4,1 X\_9,4,2 X\_9,4,3 X\_9,4,4 X\_9,4,5 X\_9,4,6 X\_9,4,7 X\_9,4,8 X\_9,4,9 0

X\_9,5,1 X\_9,5,2 X\_9,5,3 X\_9,5,4 X\_9,5,5 X\_9,5,6 X\_9,5,7 X\_9,5,8 X\_9,5,9 0

X\_9,6,1 X\_9,6,2 X\_9,6,3 X\_9,6,4 X\_9,6,5 X\_9,6,6 X\_9,6,7 X\_9,6,8 X\_9,6,9 0

X\_9,7,1 X\_9,7,2 X\_9,7,3 X\_9,7,4 X\_9,7,5 X\_9,7,6 X\_9,7,7 X\_9,7,8 X\_9,7,9 0

X\_9,8,1 X\_9,8,2 X\_9,8,3 X\_9,8,4 X\_9,8,5 X\_9,8,6 X\_9,8,7 X\_9,8,8 X\_9,8,9 0

X\_9,9,1 X\_9,9,2 X\_9,9,3 X\_9,9,4 X\_9,9,5 X\_9,9,6 X\_9,9,7 X\_9,9,8 X\_9,9,9 0

- X\_1,1,1 -X\_1,1,2 0
- X\_1,1,1 -X\_1,1,3 0
- X\_1,1,1 -X\_1,1,4 0
- X\_1,1,1 -X\_1,1,5 0
- X\_1,1,1 -X\_1,1,6 0
- X\_1,1,1 -X\_1,1,7 0
- X\_1,1,1 -X\_1,1,8 0
- X\_1,1,1 -X\_1,1,9 0
- X\_1,1,2 -X\_1,1,3 0
- X\_1,1,2 -X\_1,1,4 0
- X\_1,1,2 -X\_1,1,5 0
- X\_1,1,2 -X\_1,1,6 0
- X\_1,1,2 -X\_1,1,7 0
- X\_1,1,2 -X\_1,1,8 0
- X\_1,1,2 -X\_1,1,9 0
- X\_1,1,3 -X\_1,1,4 0
- X\_1,1,3 -X\_1,1,5 0
- X\_1,1,3 -X\_1,1,6 0
- X\_1,1,3 -X\_1,1,7 0
- X\_1,1,3 -X\_1,1,8 0
- X\_1,1,3 -X\_1,1,9 0
- X\_1,1,4 -X\_1,1,5 0
- X\_1,1,4 -X\_1,1,6 0
- X\_1,1,4 -X\_1,1,7 0
- X\_1,1,4 -X\_1,1,8 0
- X\_1,1,4 -X\_1,1,9 0
- X\_1,1,5 -X\_1,1,6 0
- X\_1,1,5 -X\_1,1,7 0
- X\_1,1,5 -X\_1,1,8 0
- X\_1,1,5 -X\_1,1,9 0
- X\_1,1,6 -X\_1,1,7 0
- X\_1,1,6 -X\_1,1,8 0
- X\_1,1,6 -X\_1,1,9 0
- X\_1,1,7 -X\_1,1,8 0
- X\_1,1,7 -X\_1,1,9 0
- X\_1,1,8 -X\_1,1,9 0
- X\_1,2,1 -X\_1,2,2 0
- X\_1,2,1 -X\_1,2,3 0
- X\_1,2,1 -X\_1,2,4 0
- X\_1,2,1 -X\_1,2,5 0
- X\_1,2,1 -X\_1,2,6 0
- X\_1,2,1 -X\_1,2,7 0
- X\_1,2,1 -X\_1,2,8 0
- X\_1,2,1 -X\_1,2,9 0
- X\_1,2,2 -X\_1,2,3 0
- X\_1,2,2 -X\_1,2,4 0
- X\_1,2,2 -X\_1,2,5 0
- X\_1,2,2 -X\_1,2,6 0
- X\_1,2,2 -X\_1,2,7 0
- X\_1,2,2 -X\_1,2,8 0
- X\_1,2,2 -X\_1,2,9 0
- X\_1,2,3 -X\_1,2,4 0
- X\_1,2,3 -X\_1,2,5 0
- X\_1,2,3 -X\_1,2,6 0
- X\_1,2,3 -X\_1,2,7 0
- X\_1,2,3 -X\_1,2,8 0
- X\_1,2,3 -X\_1,2,9 0
- X\_1,2,4 -X\_1,2,5 0
- X\_1,2,4 -X\_1,2,6 0
- X\_1,2,4 -X\_1,2,7 0
- X\_1,2,4 -X\_1,2,8 0
- X\_1,2,4 -X\_1,2,9 0
- X\_1,2,5 -X\_1,2,6 0
- X\_1,2,5 -X\_1,2,7 0
- X\_1,2,5 -X\_1,2,8 0
- X\_1,2,5 -X\_1,2,9 0
- X\_1,2,6 -X\_1,2,7 0
- X\_1,2,6 -X\_1,2,8 0
- X\_1,2,6 -X\_1,2,9 0
- X\_1,2,7 -X\_1,2,8 0
- X\_1,2,7 -X\_1,2,9 0
- X\_1,2,8 -X\_1,2,9 0
- X\_1,3,1 -X\_1,3,2 0
- X\_1,3,1 -X\_1,3,3 0
- X\_1,3,1 -X\_1,3,4 0
- X\_1,3,1 -X\_1,3,5 0
- X\_1,3,1 -X\_1,3,6 0
- X\_1,3,1 -X\_1,3,7 0
- X\_1,3,1 -X\_1,3,8 0
- X\_1,3,1 -X\_1,3,9 0
- X\_1,3,2 -X\_1,3,3 0
- X\_1,3,2 -X\_1,3,4 0
- X\_1,3,2 -X\_1,3,5 0
- X\_1,3,2 -X\_1,3,6 0
- X\_1,3,2 -X\_1,3,7 0
- X\_1,3,2 -X\_1,3,8 0
- X\_1,3,2 -X\_1,3,9 0
- X\_1,3,3 -X\_1,3,4 0
- X\_1,3,3 -X\_1,3,5 0
- X\_1,3,3 -X\_1,3,6 0
- X\_1,3,3 -X\_1,3,7 0
- X\_1,3,3 -X\_1,3,8 0
- X\_1,3,3 -X\_1,3,9 0
- X\_1,3,4 -X\_1,3,5 0
- X\_1,3,4 -X\_1,3,6 0
- X\_1,3,4 -X\_1,3,7 0
- X\_1,3,4 -X\_1,3,8 0
- X\_1,3,4 -X\_1,3,9 0
- X\_1,3,5 -X\_1,3,6 0
- X\_1,3,5 -X\_1,3,7 0
- X\_1,3,5 -X\_1,3,8 0
- X\_1,3,5 -X\_1,3,9 0
- X\_1,3,6 -X\_1,3,7 0
- X\_1,3,6 -X\_1,3,8 0
- X\_1,3,6 -X\_1,3,9 0
- X\_1,3,7 -X\_1,3,8 0
- X\_1,3,7 -X\_1,3,9 0
- X\_1,3,8 -X\_1,3,9 0
- X\_1,4,1 -X\_1,4,2 0
- X\_1,4,1 -X\_1,4,3 0
- X\_1,4,1 -X\_1,4,4 0
- X\_1,4,1 -X\_1,4,5 0
- X\_1,4,1 -X\_1,4,6 0
- X\_1,4,1 -X\_1,4,7 0
- X\_1,4,1 -X\_1,4,8 0
- X\_1,4,1 -X\_1,4,9 0
- X\_1,4,2 -X\_1,4,3 0
- X\_1,4,2 -X\_1,4,4 0
- X\_1,4,2 -X\_1,4,5 0
- X\_1,4,2 -X\_1,4,6 0
- X\_1,4,2 -X\_1,4,7 0
- X\_1,4,2 -X\_1,4,8 0
- X\_1,4,2 -X\_1,4,9 0
- X\_1,4,3 -X\_1,4,4 0
- X\_1,4,3 -X\_1,4,5 0
- X\_1,4,3 -X\_1,4,6 0
- X\_1,4,3 -X\_1,4,7 0
- X\_1,4,3 -X\_1,4,8 0
- X\_1,4,3 -X\_1,4,9 0
- X\_1,4,4 -X\_1,4,5 0
- X\_1,4,4 -X\_1,4,6 0
- X\_1,4,4 -X\_1,4,7 0
- X\_1,4,4 -X\_1,4,8 0
- X\_1,4,4 -X\_1,4,9 0
- X\_1,4,5 -X\_1,4,6 0
- X\_1,4,5 -X\_1,4,7 0
- X\_1,4,5 -X\_1,4,8 0
- X\_1,4,5 -X\_1,4,9 0
- X\_1,4,6 -X\_1,4,7 0
- X\_1,4,6 -X\_1,4,8 0
- X\_1,4,6 -X\_1,4,9 0
- X\_1,4,7 -X\_1,4,8 0
- X\_1,4,7 -X\_1,4,9 0
- X\_1,4,8 -X\_1,4,9 0
- X\_1,5,1 -X\_1,5,2 0
- X\_1,5,1 -X\_1,5,3 0
- X\_1,5,1 -X\_1,5,4 0
- X\_1,5,1 -X\_1,5,5 0
- X\_1,5,1 -X\_1,5,6 0
- X\_1,5,1 -X\_1,5,7 0
- X\_1,5,1 -X\_1,5,8 0
- X\_1,5,1 -X\_1,5,9 0
- X\_1,5,2 -X\_1,5,3 0
- X\_1,5,2 -X\_1,5,4 0
- X\_1,5,2 -X\_1,5,5 0
- X\_1,5,2 -X\_1,5,6 0
- X\_1,5,2 -X\_1,5,7 0
- X\_1,5,2 -X\_1,5,8 0
- X\_1,5,2 -X\_1,5,9 0
- X\_1,5,3 -X\_1,5,4 0
- X\_1,5,3 -X\_1,5,5 0
- X\_1,5,3 -X\_1,5,6 0
- X\_1,5,3 -X\_1,5,7 0
- X\_1,5,3 -X\_1,5,8 0
- X\_1,5,3 -X\_1,5,9 0
- X\_1,5,4 -X\_1,5,5 0
- X\_1,5,4 -X\_1,5,6 0
- X\_1,5,4 -X\_1,5,7 0
- X\_1,5,4 -X\_1,5,8 0
- X\_1,5,4 -X\_1,5,9 0
- X\_1,5,5 -X\_1,5,6 0
- X\_1,5,5 -X\_1,5,7 0
- X\_1,5,5 -X\_1,5,8 0
- X\_1,5,5 -X\_1,5,9 0
- X\_1,5,6 -X\_1,5,7 0
- X\_1,5,6 -X\_1,5,8 0
- X\_1,5,6 -X\_1,5,9 0
- X\_1,5,7 -X\_1,5,8 0
- X\_1,5,7 -X\_1,5,9 0
- X\_1,5,8 -X\_1,5,9 0
- X\_1,6,1 -X\_1,6,2 0
- X\_1,6,1 -X\_1,6,3 0
- X\_1,6,1 -X\_1,6,4 0
- X\_1,6,1 -X\_1,6,5 0
- X\_1,6,1 -X\_1,6,6 0
- X\_1,6,1 -X\_1,6,7 0
- X\_1,6,1 -X\_1,6,8 0
- X\_1,6,1 -X\_1,6,9 0
- X\_1,6,2 -X\_1,6,3 0
- X\_1,6,2 -X\_1,6,4 0
- X\_1,6,2 -X\_1,6,5 0
- X\_1,6,2 -X\_1,6,6 0
- X\_1,6,2 -X\_1,6,7 0
- X\_1,6,2 -X\_1,6,8 0
- X\_1,6,2 -X\_1,6,9 0
- X\_1,6,3 -X\_1,6,4 0
- X\_1,6,3 -X\_1,6,5 0
- X\_1,6,3 -X\_1,6,6 0
- X\_1,6,3 -X\_1,6,7 0
- X\_1,6,3 -X\_1,6,8 0
- X\_1,6,3 -X\_1,6,9 0
- X\_1,6,4 -X\_1,6,5 0
- X\_1,6,4 -X\_1,6,6 0
- X\_1,6,4 -X\_1,6,7 0
- X\_1,6,4 -X\_1,6,8 0
- X\_1,6,4 -X\_1,6,9 0
- X\_1,6,5 -X\_1,6,6 0
- X\_1,6,5 -X\_1,6,7 0
- X\_1,6,5 -X\_1,6,8 0
- X\_1,6,5 -X\_1,6,9 0
- X\_1,6,6 -X\_1,6,7 0
- X\_1,6,6 -X\_1,6,8 0
- X\_1,6,6 -X\_1,6,9 0
- X\_1,6,7 -X\_1,6,8 0
- X\_1,6,7 -X\_1,6,9 0
- X\_1,6,8 -X\_1,6,9 0
- X\_1,7,1 -X\_1,7,2 0
- X\_1,7,1 -X\_1,7,3 0
- X\_1,7,1 -X\_1,7,4 0
- X\_1,7,1 -X\_1,7,5 0
- X\_1,7,1 -X\_1,7,6 0
- X\_1,7,1 -X\_1,7,7 0
- X\_1,7,1 -X\_1,7,8 0
- X\_1,7,1 -X\_1,7,9 0
- X\_1,7,2 -X\_1,7,3 0
- X\_1,7,2 -X\_1,7,4 0
- X\_1,7,2 -X\_1,7,5 0
- X\_1,7,2 -X\_1,7,6 0
- X\_1,7,2 -X\_1,7,7 0
- X\_1,7,2 -X\_1,7,8 0
- X\_1,7,2 -X\_1,7,9 0
- X\_1,7,3 -X\_1,7,4 0
- X\_1,7,3 -X\_1,7,5 0
- X\_1,7,3 -X\_1,7,6 0
- X\_1,7,3 -X\_1,7,7 0
- X\_1,7,3 -X\_1,7,8 0
- X\_1,7,3 -X\_1,7,9 0
- X\_1,7,4 -X\_1,7,5 0
- X\_1,7,4 -X\_1,7,6 0
- X\_1,7,4 -X\_1,7,7 0
- X\_1,7,4 -X\_1,7,8 0
- X\_1,7,4 -X\_1,7,9 0
- X\_1,7,5 -X\_1,7,6 0
- X\_1,7,5 -X\_1,7,7 0
- X\_1,7,5 -X\_1,7,8 0
- X\_1,7,5 -X\_1,7,9 0
- X\_1,7,6 -X\_1,7,7 0
- X\_1,7,6 -X\_1,7,8 0
- X\_1,7,6 -X\_1,7,9 0
- X\_1,7,7 -X\_1,7,8 0
- X\_1,7,7 -X\_1,7,9 0
- X\_1,7,8 -X\_1,7,9 0
- X\_1,8,1 -X\_1,8,2 0
- X\_1,8,1 -X\_1,8,3 0
- X\_1,8,1 -X\_1,8,4 0
- X\_1,8,1 -X\_1,8,5 0
- X\_1,8,1 -X\_1,8,6 0
- X\_1,8,1 -X\_1,8,7 0
- X\_1,8,1 -X\_1,8,8 0
- X\_1,8,1 -X\_1,8,9 0
- X\_1,8,2 -X\_1,8,3 0
- X\_1,8,2 -X\_1,8,4 0
- X\_1,8,2 -X\_1,8,5 0
- X\_1,8,2 -X\_1,8,6 0
- X\_1,8,2 -X\_1,8,7 0
- X\_1,8,2 -X\_1,8,8 0
- X\_1,8,2 -X\_1,8,9 0
- X\_1,8,3 -X\_1,8,4 0
- X\_1,8,3 -X\_1,8,5 0
- X\_1,8,3 -X\_1,8,6 0
- X\_1,8,3 -X\_1,8,7 0
- X\_1,8,3 -X\_1,8,8 0
- X\_1,8,3 -X\_1,8,9 0
- X\_1,8,4 -X\_1,8,5 0
- X\_1,8,4 -X\_1,8,6 0
- X\_1,8,4 -X\_1,8,7 0
- X\_1,8,4 -X\_1,8,8 0
- X\_1,8,4 -X\_1,8,9 0
- X\_1,8,5 -X\_1,8,6 0
- X\_1,8,5 -X\_1,8,7 0
- X\_1,8,5 -X\_1,8,8 0
- X\_1,8,5 -X\_1,8,9 0
- X\_1,8,6 -X\_1,8,7 0
- X\_1,8,6 -X\_1,8,8 0
- X\_1,8,6 -X\_1,8,9 0
- X\_1,8,7 -X\_1,8,8 0
- X\_1,8,7 -X\_1,8,9 0
- X\_1,8,8 -X\_1,8,9 0
- X\_1,9,1 -X\_1,9,2 0
- X\_1,9,1 -X\_1,9,3 0
- X\_1,9,1 -X\_1,9,4 0
- X\_1,9,1 -X\_1,9,5 0
- X\_1,9,1 -X\_1,9,6 0
- X\_1,9,1 -X\_1,9,7 0
- X\_1,9,1 -X\_1,9,8 0
- X\_1,9,1 -X\_1,9,9 0
- X\_1,9,2 -X\_1,9,3 0
- X\_1,9,2 -X\_1,9,4 0
- X\_1,9,2 -X\_1,9,5 0
- X\_1,9,2 -X\_1,9,6 0
- X\_1,9,2 -X\_1,9,7 0
- X\_1,9,2 -X\_1,9,8 0
- X\_1,9,2 -X\_1,9,9 0
- X\_1,9,3 -X\_1,9,4 0
- X\_1,9,3 -X\_1,9,5 0
- X\_1,9,3 -X\_1,9,6 0
- X\_1,9,3 -X\_1,9,7 0
- X\_1,9,3 -X\_1,9,8 0
- X\_1,9,3 -X\_1,9,9 0
- X\_1,9,4 -X\_1,9,5 0
- X\_1,9,4 -X\_1,9,6 0
- X\_1,9,4 -X\_1,9,7 0
- X\_1,9,4 -X\_1,9,8 0
- X\_1,9,4 -X\_1,9,9 0
- X\_1,9,5 -X\_1,9,6 0
- X\_1,9,5 -X\_1,9,7 0
- X\_1,9,5 -X\_1,9,8 0
- X\_1,9,5 -X\_1,9,9 0
- X\_1,9,6 -X\_1,9,7 0
- X\_1,9,6 -X\_1,9,8 0
- X\_1,9,6 -X\_1,9,9 0
- X\_1,9,7 -X\_1,9,8 0
- X\_1,9,7 -X\_1,9,9 0
- X\_1,9,8 -X\_1,9,9 0
- X\_2,1,1 -X\_2,1,2 0
- X\_2,1,1 -X\_2,1,3 0
- X\_2,1,1 -X\_2,1,4 0
- X\_2,1,1 -X\_2,1,5 0
- X\_2,1,1 -X\_2,1,6 0
- X\_2,1,1 -X\_2,1,7 0
- X\_2,1,1 -X\_2,1,8 0
- X\_2,1,1 -X\_2,1,9 0
- X\_2,1,2 -X\_2,1,3 0
- X\_2,1,2 -X\_2,1,4 0
- X\_2,1,2 -X\_2,1,5 0
- X\_2,1,2 -X\_2,1,6 0
- X\_2,1,2 -X\_2,1,7 0
- X\_2,1,2 -X\_2,1,8 0
- X\_2,1,2 -X\_2,1,9 0
- X\_2,1,3 -X\_2,1,4 0
- X\_2,1,3 -X\_2,1,5 0
- X\_2,1,3 -X\_2,1,6 0
- X\_2,1,3 -X\_2,1,7 0
- X\_2,1,3 -X\_2,1,8 0
- X\_2,1,3 -X\_2,1,9 0
- X\_2,1,4 -X\_2,1,5 0
- X\_2,1,4 -X\_2,1,6 0
- X\_2,1,4 -X\_2,1,7 0
- X\_2,1,4 -X\_2,1,8 0
- X\_2,1,4 -X\_2,1,9 0
- X\_2,1,5 -X\_2,1,6 0
- X\_2,1,5 -X\_2,1,7 0
- X\_2,1,5 -X\_2,1,8 0
- X\_2,1,5 -X\_2,1,9 0
- X\_2,1,6 -X\_2,1,7 0
- X\_2,1,6 -X\_2,1,8 0
- X\_2,1,6 -X\_2,1,9 0
- X\_2,1,7 -X\_2,1,8 0
- X\_2,1,7 -X\_2,1,9 0
- X\_2,1,8 -X\_2,1,9 0
- X\_2,2,1 -X\_2,2,2 0
- X\_2,2,1 -X\_2,2,3 0
- X\_2,2,1 -X\_2,2,4 0
- X\_2,2,1 -X\_2,2,5 0
- X\_2,2,1 -X\_2,2,6 0
- X\_2,2,1 -X\_2,2,7 0
- X\_2,2,1 -X\_2,2,8 0
- X\_2,2,1 -X\_2,2,9 0
- X\_2,2,2 -X\_2,2,3 0
- X\_2,2,2 -X\_2,2,4 0
- X\_2,2,2 -X\_2,2,5 0
- X\_2,2,2 -X\_2,2,6 0
- X\_2,2,2 -X\_2,2,7 0
- X\_2,2,2 -X\_2,2,8 0
- X\_2,2,2 -X\_2,2,9 0
- X\_2,2,3 -X\_2,2,4 0
- X\_2,2,3 -X\_2,2,5 0
- X\_2,2,3 -X\_2,2,6 0
- X\_2,2,3 -X\_2,2,7 0
- X\_2,2,3 -X\_2,2,8 0
- X\_2,2,3 -X\_2,2,9 0
- X\_2,2,4 -X\_2,2,5 0
- X\_2,2,4 -X\_2,2,6 0
- X\_2,2,4 -X\_2,2,7 0
- X\_2,2,4 -X\_2,2,8 0
- X\_2,2,4 -X\_2,2,9 0
- X\_2,2,5 -X\_2,2,6 0
- X\_2,2,5 -X\_2,2,7 0
- X\_2,2,5 -X\_2,2,8 0
- X\_2,2,5 -X\_2,2,9 0
- X\_2,2,6 -X\_2,2,7 0
- X\_2,2,6 -X\_2,2,8 0
- X\_2,2,6 -X\_2,2,9 0
- X\_2,2,7 -X\_2,2,8 0
- X\_2,2,7 -X\_2,2,9 0
- X\_2,2,8 -X\_2,2,9 0
- X\_2,3,1 -X\_2,3,2 0
- X\_2,3,1 -X\_2,3,3 0
- X\_2,3,1 -X\_2,3,4 0
- X\_2,3,1 -X\_2,3,5 0
- X\_2,3,1 -X\_2,3,6 0
- X\_2,3,1 -X\_2,3,7 0
- X\_2,3,1 -X\_2,3,8 0
- X\_2,3,1 -X\_2,3,9 0
- X\_2,3,2 -X\_2,3,3 0
- X\_2,3,2 -X\_2,3,4 0
- X\_2,3,2 -X\_2,3,5 0
- X\_2,3,2 -X\_2,3,6 0
- X\_2,3,2 -X\_2,3,7 0
- X\_2,3,2 -X\_2,3,8 0
- X\_2,3,2 -X\_2,3,9 0
- X\_2,3,3 -X\_2,3,4 0
- X\_2,3,3 -X\_2,3,5 0
- X\_2,3,3 -X\_2,3,6 0
- X\_2,3,3 -X\_2,3,7 0
- X\_2,3,3 -X\_2,3,8 0
- X\_2,3,3 -X\_2,3,9 0
- X\_2,3,4 -X\_2,3,5 0
- X\_2,3,4 -X\_2,3,6 0
- X\_2,3,4 -X\_2,3,7 0
- X\_2,3,4 -X\_2,3,8 0
- X\_2,3,4 -X\_2,3,9 0
- X\_2,3,5 -X\_2,3,6 0
- X\_2,3,5 -X\_2,3,7 0
- X\_2,3,5 -X\_2,3,8 0
- X\_2,3,5 -X\_2,3,9 0
- X\_2,3,6 -X\_2,3,7 0
- X\_2,3,6 -X\_2,3,8 0
- X\_2,3,6 -X\_2,3,9 0
- X\_2,3,7 -X\_2,3,8 0
- X\_2,3,7 -X\_2,3,9 0
- X\_2,3,8 -X\_2,3,9 0
- X\_2,4,1 -X\_2,4,2 0
- X\_2,4,1 -X\_2,4,3 0
- X\_2,4,1 -X\_2,4,4 0
- X\_2,4,1 -X\_2,4,5 0
- X\_2,4,1 -X\_2,4,6 0
- X\_2,4,1 -X\_2,4,7 0
- X\_2,4,1 -X\_2,4,8 0
- X\_2,4,1 -X\_2,4,9 0
- X\_2,4,2 -X\_2,4,3 0
- X\_2,4,2 -X\_2,4,4 0
- X\_2,4,2 -X\_2,4,5 0
- X\_2,4,2 -X\_2,4,6 0
- X\_2,4,2 -X\_2,4,7 0
- X\_2,4,2 -X\_2,4,8 0
- X\_2,4,2 -X\_2,4,9 0
- X\_2,4,3 -X\_2,4,4 0
- X\_2,4,3 -X\_2,4,5 0
- X\_2,4,3 -X\_2,4,6 0
- X\_2,4,3 -X\_2,4,7 0
- X\_2,4,3 -X\_2,4,8 0
- X\_2,4,3 -X\_2,4,9 0
- X\_2,4,4 -X\_2,4,5 0
- X\_2,4,4 -X\_2,4,6 0
- X\_2,4,4 -X\_2,4,7 0
- X\_2,4,4 -X\_2,4,8 0
- X\_2,4,4 -X\_2,4,9 0
- X\_2,4,5 -X\_2,4,6 0
- X\_2,4,5 -X\_2,4,7 0
- X\_2,4,5 -X\_2,4,8 0
- X\_2,4,5 -X\_2,4,9 0
- X\_2,4,6 -X\_2,4,7 0
- X\_2,4,6 -X\_2,4,8 0
- X\_2,4,6 -X\_2,4,9 0
- X\_2,4,7 -X\_2,4,8 0
- X\_2,4,7 -X\_2,4,9 0
- X\_2,4,8 -X\_2,4,9 0
- X\_2,5,1 -X\_2,5,2 0
- X\_2,5,1 -X\_2,5,3 0
- X\_2,5,1 -X\_2,5,4 0
- X\_2,5,1 -X\_2,5,5 0
- X\_2,5,1 -X\_2,5,6 0
- X\_2,5,1 -X\_2,5,7 0
- X\_2,5,1 -X\_2,5,8 0
- X\_2,5,1 -X\_2,5,9 0
- X\_2,5,2 -X\_2,5,3 0
- X\_2,5,2 -X\_2,5,4 0
- X\_2,5,2 -X\_2,5,5 0
- X\_2,5,2 -X\_2,5,6 0
- X\_2,5,2 -X\_2,5,7 0
- X\_2,5,2 -X\_2,5,8 0
- X\_2,5,2 -X\_2,5,9 0
- X\_2,5,3 -X\_2,5,4 0
- X\_2,5,3 -X\_2,5,5 0
- X\_2,5,3 -X\_2,5,6 0
- X\_2,5,3 -X\_2,5,7 0
- X\_2,5,3 -X\_2,5,8 0
- X\_2,5,3 -X\_2,5,9 0
- X\_2,5,4 -X\_2,5,5 0
- X\_2,5,4 -X\_2,5,6 0
- X\_2,5,4 -X\_2,5,7 0
- X\_2,5,4 -X\_2,5,8 0
- X\_2,5,4 -X\_2,5,9 0
- X\_2,5,5 -X\_2,5,6 0
- X\_2,5,5 -X\_2,5,7 0
- X\_2,5,5 -X\_2,5,8 0
- X\_2,5,5 -X\_2,5,9 0
- X\_2,5,6 -X\_2,5,7 0
- X\_2,5,6 -X\_2,5,8 0
- X\_2,5,6 -X\_2,5,9 0
- X\_2,5,7 -X\_2,5,8 0
- X\_2,5,7 -X\_2,5,9 0
- X\_2,5,8 -X\_2,5,9 0
- X\_2,6,1 -X\_2,6,2 0
- X\_2,6,1 -X\_2,6,3 0
- X\_2,6,1 -X\_2,6,4 0
- X\_2,6,1 -X\_2,6,5 0
- X\_2,6,1 -X\_2,6,6 0
- X\_2,6,1 -X\_2,6,7 0
- X\_2,6,1 -X\_2,6,8 0
- X\_2,6,1 -X\_2,6,9 0
- X\_2,6,2 -X\_2,6,3 0
- X\_2,6,2 -X\_2,6,4 0
- X\_2,6,2 -X\_2,6,5 0
- X\_2,6,2 -X\_2,6,6 0
- X\_2,6,2 -X\_2,6,7 0
- X\_2,6,2 -X\_2,6,8 0
- X\_2,6,2 -X\_2,6,9 0
- X\_2,6,3 -X\_2,6,4 0
- X\_2,6,3 -X\_2,6,5 0
- X\_2,6,3 -X\_2,6,6 0
- X\_2,6,3 -X\_2,6,7 0
- X\_2,6,3 -X\_2,6,8 0
- X\_2,6,3 -X\_2,6,9 0
- X\_2,6,4 -X\_2,6,5 0
- X\_2,6,4 -X\_2,6,6 0
- X\_2,6,4 -X\_2,6,7 0
- X\_2,6,4 -X\_2,6,8 0
- X\_2,6,4 -X\_2,6,9 0
- X\_2,6,5 -X\_2,6,6 0
- X\_2,6,5 -X\_2,6,7 0
- X\_2,6,5 -X\_2,6,8 0
- X\_2,6,5 -X\_2,6,9 0
- X\_2,6,6 -X\_2,6,7 0
- X\_2,6,6 -X\_2,6,8 0
- X\_2,6,6 -X\_2,6,9 0
- X\_2,6,7 -X\_2,6,8 0
- X\_2,6,7 -X\_2,6,9 0
- X\_2,6,8 -X\_2,6,9 0
- X\_2,7,1 -X\_2,7,2 0
- X\_2,7,1 -X\_2,7,3 0
- X\_2,7,1 -X\_2,7,4 0
- X\_2,7,1 -X\_2,7,5 0
- X\_2,7,1 -X\_2,7,6 0
- X\_2,7,1 -X\_2,7,7 0
- X\_2,7,1 -X\_2,7,8 0
- X\_2,7,1 -X\_2,7,9 0
- X\_2,7,2 -X\_2,7,3 0
- X\_2,7,2 -X\_2,7,4 0
- X\_2,7,2 -X\_2,7,5 0
- X\_2,7,2 -X\_2,7,6 0
- X\_2,7,2 -X\_2,7,7 0
- X\_2,7,2 -X\_2,7,8 0
- X\_2,7,2 -X\_2,7,9 0
- X\_2,7,3 -X\_2,7,4 0
- X\_2,7,3 -X\_2,7,5 0
- X\_2,7,3 -X\_2,7,6 0
- X\_2,7,3 -X\_2,7,7 0
- X\_2,7,3 -X\_2,7,8 0
- X\_2,7,3 -X\_2,7,9 0
- X\_2,7,4 -X\_2,7,5 0
- X\_2,7,4 -X\_2,7,6 0
- X\_2,7,4 -X\_2,7,7 0
- X\_2,7,4 -X\_2,7,8 0
- X\_2,7,4 -X\_2,7,9 0
- X\_2,7,5 -X\_2,7,6 0
- X\_2,7,5 -X\_2,7,7 0
- X\_2,7,5 -X\_2,7,8 0
- X\_2,7,5 -X\_2,7,9 0
- X\_2,7,6 -X\_2,7,7 0
- X\_2,7,6 -X\_2,7,8 0
- X\_2,7,6 -X\_2,7,9 0
- X\_2,7,7 -X\_2,7,8 0
- X\_2,7,7 -X\_2,7,9 0
- X\_2,7,8 -X\_2,7,9 0
- X\_2,8,1 -X\_2,8,2 0
- X\_2,8,1 -X\_2,8,3 0
- X\_2,8,1 -X\_2,8,4 0
- X\_2,8,1 -X\_2,8,5 0
- X\_2,8,1 -X\_2,8,6 0
- X\_2,8,1 -X\_2,8,7 0
- X\_2,8,1 -X\_2,8,8 0
- X\_2,8,1 -X\_2,8,9 0
- X\_2,8,2 -X\_2,8,3 0
- X\_2,8,2 -X\_2,8,4 0
- X\_2,8,2 -X\_2,8,5 0
- X\_2,8,2 -X\_2,8,6 0
- X\_2,8,2 -X\_2,8,7 0
- X\_2,8,2 -X\_2,8,8 0
- X\_2,8,2 -X\_2,8,9 0
- X\_2,8,3 -X\_2,8,4 0
- X\_2,8,3 -X\_2,8,5 0
- X\_2,8,3 -X\_2,8,6 0
- X\_2,8,3 -X\_2,8,7 0
- X\_2,8,3 -X\_2,8,8 0
- X\_2,8,3 -X\_2,8,9 0
- X\_2,8,4 -X\_2,8,5 0
- X\_2,8,4 -X\_2,8,6 0
- X\_2,8,4 -X\_2,8,7 0
- X\_2,8,4 -X\_2,8,8 0
- X\_2,8,4 -X\_2,8,9 0
- X\_2,8,5 -X\_2,8,6 0
- X\_2,8,5 -X\_2,8,7 0
- X\_2,8,5 -X\_2,8,8 0
- X\_2,8,5 -X\_2,8,9 0
- X\_2,8,6 -X\_2,8,7 0
- X\_2,8,6 -X\_2,8,8 0
- X\_2,8,6 -X\_2,8,9 0
- X\_2,8,7 -X\_2,8,8 0
- X\_2,8,7 -X\_2,8,9 0
- X\_2,8,8 -X\_2,8,9 0
- X\_2,9,1 -X\_2,9,2 0
- X\_2,9,1 -X\_2,9,3 0
- X\_2,9,1 -X\_2,9,4 0
- X\_2,9,1 -X\_2,9,5 0
- X\_2,9,1 -X\_2,9,6 0
- X\_2,9,1 -X\_2,9,7 0
- X\_2,9,1 -X\_2,9,8 0
- X\_2,9,1 -X\_2,9,9 0
- X\_2,9,2 -X\_2,9,3 0
- X\_2,9,2 -X\_2,9,4 0
- X\_2,9,2 -X\_2,9,5 0
- X\_2,9,2 -X\_2,9,6 0
- X\_2,9,2 -X\_2,9,7 0
- X\_2,9,2 -X\_2,9,8 0
- X\_2,9,2 -X\_2,9,9 0
- X\_2,9,3 -X\_2,9,4 0
- X\_2,9,3 -X\_2,9,5 0
- X\_2,9,3 -X\_2,9,6 0
- X\_2,9,3 -X\_2,9,7 0
- X\_2,9,3 -X\_2,9,8 0
- X\_2,9,3 -X\_2,9,9 0
- X\_2,9,4 -X\_2,9,5 0
- X\_2,9,4 -X\_2,9,6 0
- X\_2,9,4 -X\_2,9,7 0
- X\_2,9,4 -X\_2,9,8 0
- X\_2,9,4 -X\_2,9,9 0
- X\_2,9,5 -X\_2,9,6 0
- X\_2,9,5 -X\_2,9,7 0
- X\_2,9,5 -X\_2,9,8 0
- X\_2,9,5 -X\_2,9,9 0
- X\_2,9,6 -X\_2,9,7 0
- X\_2,9,6 -X\_2,9,8 0
- X\_2,9,6 -X\_2,9,9 0
- X\_2,9,7 -X\_2,9,8 0
- X\_2,9,7 -X\_2,9,9 0
- X\_2,9,8 -X\_2,9,9 0
- X\_3,1,1 -X\_3,1,2 0
- X\_3,1,1 -X\_3,1,3 0
- X\_3,1,1 -X\_3,1,4 0
- X\_3,1,1 -X\_3,1,5 0
- X\_3,1,1 -X\_3,1,6 0
- X\_3,1,1 -X\_3,1,7 0
- X\_3,1,1 -X\_3,1,8 0
- X\_3,1,1 -X\_3,1,9 0
- X\_3,1,2 -X\_3,1,3 0
- X\_3,1,2 -X\_3,1,4 0
- X\_3,1,2 -X\_3,1,5 0
- X\_3,1,2 -X\_3,1,6 0
- X\_3,1,2 -X\_3,1,7 0
- X\_3,1,2 -X\_3,1,8 0
- X\_3,1,2 -X\_3,1,9 0
- X\_3,1,3 -X\_3,1,4 0
- X\_3,1,3 -X\_3,1,5 0
- X\_3,1,3 -X\_3,1,6 0
- X\_3,1,3 -X\_3,1,7 0
- X\_3,1,3 -X\_3,1,8 0
- X\_3,1,3 -X\_3,1,9 0
- X\_3,1,4 -X\_3,1,5 0
- X\_3,1,4 -X\_3,1,6 0
- X\_3,1,4 -X\_3,1,7 0
- X\_3,1,4 -X\_3,1,8 0
- X\_3,1,4 -X\_3,1,9 0
- X\_3,1,5 -X\_3,1,6 0
- X\_3,1,5 -X\_3,1,7 0
- X\_3,1,5 -X\_3,1,8 0
- X\_3,1,5 -X\_3,1,9 0
- X\_3,1,6 -X\_3,1,7 0
- X\_3,1,6 -X\_3,1,8 0
- X\_3,1,6 -X\_3,1,9 0
- X\_3,1,7 -X\_3,1,8 0
- X\_3,1,7 -X\_3,1,9 0
- X\_3,1,8 -X\_3,1,9 0
- X\_3,2,1 -X\_3,2,2 0
- X\_3,2,1 -X\_3,2,3 0
- X\_3,2,1 -X\_3,2,4 0
- X\_3,2,1 -X\_3,2,5 0
- X\_3,2,1 -X\_3,2,6 0
- X\_3,2,1 -X\_3,2,7 0
- X\_3,2,1 -X\_3,2,8 0
- X\_3,2,1 -X\_3,2,9 0
- X\_3,2,2 -X\_3,2,3 0
- X\_3,2,2 -X\_3,2,4 0
- X\_3,2,2 -X\_3,2,5 0
- X\_3,2,2 -X\_3,2,6 0
- X\_3,2,2 -X\_3,2,7 0
- X\_3,2,2 -X\_3,2,8 0
- X\_3,2,2 -X\_3,2,9 0
- X\_3,2,3 -X\_3,2,4 0
- X\_3,2,3 -X\_3,2,5 0
- X\_3,2,3 -X\_3,2,6 0
- X\_3,2,3 -X\_3,2,7 0
- X\_3,2,3 -X\_3,2,8 0
- X\_3,2,3 -X\_3,2,9 0
- X\_3,2,4 -X\_3,2,5 0
- X\_3,2,4 -X\_3,2,6 0
- X\_3,2,4 -X\_3,2,7 0
- X\_3,2,4 -X\_3,2,8 0
- X\_3,2,4 -X\_3,2,9 0
- X\_3,2,5 -X\_3,2,6 0
- X\_3,2,5 -X\_3,2,7 0
- X\_3,2,5 -X\_3,2,8 0
- X\_3,2,5 -X\_3,2,9 0
- X\_3,2,6 -X\_3,2,7 0
- X\_3,2,6 -X\_3,2,8 0
- X\_3,2,6 -X\_3,2,9 0
- X\_3,2,7 -X\_3,2,8 0
- X\_3,2,7 -X\_3,2,9 0
- X\_3,2,8 -X\_3,2,9 0
- X\_3,3,1 -X\_3,3,2 0
- X\_3,3,1 -X\_3,3,3 0
- X\_3,3,1 -X\_3,3,4 0
- X\_3,3,1 -X\_3,3,5 0
- X\_3,3,1 -X\_3,3,6 0
- X\_3,3,1 -X\_3,3,7 0
- X\_3,3,1 -X\_3,3,8 0
- X\_3,3,1 -X\_3,3,9 0
- X\_3,3,2 -X\_3,3,3 0
- X\_3,3,2 -X\_3,3,4 0
- X\_3,3,2 -X\_3,3,5 0
- X\_3,3,2 -X\_3,3,6 0
- X\_3,3,2 -X\_3,3,7 0
- X\_3,3,2 -X\_3,3,8 0
- X\_3,3,2 -X\_3,3,9 0
- X\_3,3,3 -X\_3,3,4 0
- X\_3,3,3 -X\_3,3,5 0
- X\_3,3,3 -X\_3,3,6 0
- X\_3,3,3 -X\_3,3,7 0
- X\_3,3,3 -X\_3,3,8 0
- X\_3,3,3 -X\_3,3,9 0
- X\_3,3,4 -X\_3,3,5 0
- X\_3,3,4 -X\_3,3,6 0
- X\_3,3,4 -X\_3,3,7 0
- X\_3,3,4 -X\_3,3,8 0
- X\_3,3,4 -X\_3,3,9 0
- X\_3,3,5 -X\_3,3,6 0
- X\_3,3,5 -X\_3,3,7 0
- X\_3,3,5 -X\_3,3,8 0
- X\_3,3,5 -X\_3,3,9 0
- X\_3,3,6 -X\_3,3,7 0
- X\_3,3,6 -X\_3,3,8 0
- X\_3,3,6 -X\_3,3,9 0
- X\_3,3,7 -X\_3,3,8 0
- X\_3,3,7 -X\_3,3,9 0
- X\_3,3,8 -X\_3,3,9 0
- X\_3,4,1 -X\_3,4,2 0
- X\_3,4,1 -X\_3,4,3 0
- X\_3,4,1 -X\_3,4,4 0
- X\_3,4,1 -X\_3,4,5 0
- X\_3,4,1 -X\_3,4,6 0
- X\_3,4,1 -X\_3,4,7 0
- X\_3,4,1 -X\_3,4,8 0
- X\_3,4,1 -X\_3,4,9 0
- X\_3,4,2 -X\_3,4,3 0
- X\_3,4,2 -X\_3,4,4 0
- X\_3,4,2 -X\_3,4,5 0
- X\_3,4,2 -X\_3,4,6 0
- X\_3,4,2 -X\_3,4,7 0
- X\_3,4,2 -X\_3,4,8 0
- X\_3,4,2 -X\_3,4,9 0
- X\_3,4,3 -X\_3,4,4 0
- X\_3,4,3 -X\_3,4,5 0
- X\_3,4,3 -X\_3,4,6 0
- X\_3,4,3 -X\_3,4,7 0
- X\_3,4,3 -X\_3,4,8 0
- X\_3,4,3 -X\_3,4,9 0
- X\_3,4,4 -X\_3,4,5 0
- X\_3,4,4 -X\_3,4,6 0
- X\_3,4,4 -X\_3,4,7 0
- X\_3,4,4 -X\_3,4,8 0
- X\_3,4,4 -X\_3,4,9 0
- X\_3,4,5 -X\_3,4,6 0
- X\_3,4,5 -X\_3,4,7 0
- X\_3,4,5 -X\_3,4,8 0
- X\_3,4,5 -X\_3,4,9 0
- X\_3,4,6 -X\_3,4,7 0
- X\_3,4,6 -X\_3,4,8 0
- X\_3,4,6 -X\_3,4,9 0
- X\_3,4,7 -X\_3,4,8 0
- X\_3,4,7 -X\_3,4,9 0
- X\_3,4,8 -X\_3,4,9 0
- X\_3,5,1 -X\_3,5,2 0
- X\_3,5,1 -X\_3,5,3 0
- X\_3,5,1 -X\_3,5,4 0
- X\_3,5,1 -X\_3,5,5 0
- X\_3,5,1 -X\_3,5,6 0
- X\_3,5,1 -X\_3,5,7 0
- X\_3,5,1 -X\_3,5,8 0
- X\_3,5,1 -X\_3,5,9 0
- X\_3,5,2 -X\_3,5,3 0
- X\_3,5,2 -X\_3,5,4 0
- X\_3,5,2 -X\_3,5,5 0
- X\_3,5,2 -X\_3,5,6 0
- X\_3,5,2 -X\_3,5,7 0
- X\_3,5,2 -X\_3,5,8 0
- X\_3,5,2 -X\_3,5,9 0
- X\_3,5,3 -X\_3,5,4 0
- X\_3,5,3 -X\_3,5,5 0
- X\_3,5,3 -X\_3,5,6 0
- X\_3,5,3 -X\_3,5,7 0
- X\_3,5,3 -X\_3,5,8 0
- X\_3,5,3 -X\_3,5,9 0
- X\_3,5,4 -X\_3,5,5 0
- X\_3,5,4 -X\_3,5,6 0
- X\_3,5,4 -X\_3,5,7 0
- X\_3,5,4 -X\_3,5,8 0
- X\_3,5,4 -X\_3,5,9 0
- X\_3,5,5 -X\_3,5,6 0
- X\_3,5,5 -X\_3,5,7 0
- X\_3,5,5 -X\_3,5,8 0
- X\_3,5,5 -X\_3,5,9 0
- X\_3,5,6 -X\_3,5,7 0
- X\_3,5,6 -X\_3,5,8 0
- X\_3,5,6 -X\_3,5,9 0
- X\_3,5,7 -X\_3,5,8 0
- X\_3,5,7 -X\_3,5,9 0
- X\_3,5,8 -X\_3,5,9 0
- X\_3,6,1 -X\_3,6,2 0
- X\_3,6,1 -X\_3,6,3 0
- X\_3,6,1 -X\_3,6,4 0
- X\_3,6,1 -X\_3,6,5 0
- X\_3,6,1 -X\_3,6,6 0
- X\_3,6,1 -X\_3,6,7 0
- X\_3,6,1 -X\_3,6,8 0
- X\_3,6,1 -X\_3,6,9 0
- X\_3,6,2 -X\_3,6,3 0
- X\_3,6,2 -X\_3,6,4 0
- X\_3,6,2 -X\_3,6,5 0
- X\_3,6,2 -X\_3,6,6 0
- X\_3,6,2 -X\_3,6,7 0
- X\_3,6,2 -X\_3,6,8 0
- X\_3,6,2 -X\_3,6,9 0
- X\_3,6,3 -X\_3,6,4 0
- X\_3,6,3 -X\_3,6,5 0
- X\_3,6,3 -X\_3,6,6 0
- X\_3,6,3 -X\_3,6,7 0
- X\_3,6,3 -X\_3,6,8 0
- X\_3,6,3 -X\_3,6,9 0
- X\_3,6,4 -X\_3,6,5 0
- X\_3,6,4 -X\_3,6,6 0
- X\_3,6,4 -X\_3,6,7 0
- X\_3,6,4 -X\_3,6,8 0
- X\_3,6,4 -X\_3,6,9 0
- X\_3,6,5 -X\_3,6,6 0
- X\_3,6,5 -X\_3,6,7 0
- X\_3,6,5 -X\_3,6,8 0
- X\_3,6,5 -X\_3,6,9 0
- X\_3,6,6 -X\_3,6,7 0
- X\_3,6,6 -X\_3,6,8 0
- X\_3,6,6 -X\_3,6,9 0
- X\_3,6,7 -X\_3,6,8 0
- X\_3,6,7 -X\_3,6,9 0
- X\_3,6,8 -X\_3,6,9 0
- X\_3,7,1 -X\_3,7,2 0
- X\_3,7,1 -X\_3,7,3 0
- X\_3,7,1 -X\_3,7,4 0
- X\_3,7,1 -X\_3,7,5 0
- X\_3,7,1 -X\_3,7,6 0
- X\_3,7,1 -X\_3,7,7 0
- X\_3,7,1 -X\_3,7,8 0
- X\_3,7,1 -X\_3,7,9 0
- X\_3,7,2 -X\_3,7,3 0
- X\_3,7,2 -X\_3,7,4 0
- X\_3,7,2 -X\_3,7,5 0
- X\_3,7,2 -X\_3,7,6 0
- X\_3,7,2 -X\_3,7,7 0
- X\_3,7,2 -X\_3,7,8 0
- X\_3,7,2 -X\_3,7,9 0
- X\_3,7,3 -X\_3,7,4 0
- X\_3,7,3 -X\_3,7,5 0
- X\_3,7,3 -X\_3,7,6 0
- X\_3,7,3 -X\_3,7,7 0
- X\_3,7,3 -X\_3,7,8 0
- X\_3,7,3 -X\_3,7,9 0
- X\_3,7,4 -X\_3,7,5 0
- X\_3,7,4 -X\_3,7,6 0
- X\_3,7,4 -X\_3,7,7 0
- X\_3,7,4 -X\_3,7,8 0
- X\_3,7,4 -X\_3,7,9 0
- X\_3,7,5 -X\_3,7,6 0
- X\_3,7,5 -X\_3,7,7 0
- X\_3,7,5 -X\_3,7,8 0
- X\_3,7,5 -X\_3,7,9 0
- X\_3,7,6 -X\_3,7,7 0
- X\_3,7,6 -X\_3,7,8 0
- X\_3,7,6 -X\_3,7,9 0
- X\_3,7,7 -X\_3,7,8 0
- X\_3,7,7 -X\_3,7,9 0
- X\_3,7,8 -X\_3,7,9 0
- X\_3,8,1 -X\_3,8,2 0
- X\_3,8,1 -X\_3,8,3 0
- X\_3,8,1 -X\_3,8,4 0
- X\_3,8,1 -X\_3,8,5 0
- X\_3,8,1 -X\_3,8,6 0
- X\_3,8,1 -X\_3,8,7 0
- X\_3,8,1 -X\_3,8,8 0
- X\_3,8,1 -X\_3,8,9 0
- X\_3,8,2 -X\_3,8,3 0
- X\_3,8,2 -X\_3,8,4 0
- X\_3,8,2 -X\_3,8,5 0
- X\_3,8,2 -X\_3,8,6 0
- X\_3,8,2 -X\_3,8,7 0
- X\_3,8,2 -X\_3,8,8 0
- X\_3,8,2 -X\_3,8,9 0
- X\_3,8,3 -X\_3,8,4 0
- X\_3,8,3 -X\_3,8,5 0
- X\_3,8,3 -X\_3,8,6 0
- X\_3,8,3 -X\_3,8,7 0
- X\_3,8,3 -X\_3,8,8 0
- X\_3,8,3 -X\_3,8,9 0
- X\_3,8,4 -X\_3,8,5 0
- X\_3,8,4 -X\_3,8,6 0
- X\_3,8,4 -X\_3,8,7 0
- X\_3,8,4 -X\_3,8,8 0
- X\_3,8,4 -X\_3,8,9 0
- X\_3,8,5 -X\_3,8,6 0
- X\_3,8,5 -X\_3,8,7 0
- X\_3,8,5 -X\_3,8,8 0
- X\_3,8,5 -X\_3,8,9 0
- X\_3,8,6 -X\_3,8,7 0
- X\_3,8,6 -X\_3,8,8 0
- X\_3,8,6 -X\_3,8,9 0
- X\_3,8,7 -X\_3,8,8 0
- X\_3,8,7 -X\_3,8,9 0
- X\_3,8,8 -X\_3,8,9 0
- X\_3,9,1 -X\_3,9,2 0
- X\_3,9,1 -X\_3,9,3 0
- X\_3,9,1 -X\_3,9,4 0
- X\_3,9,1 -X\_3,9,5 0
- X\_3,9,1 -X\_3,9,6 0
- X\_3,9,1 -X\_3,9,7 0
- X\_3,9,1 -X\_3,9,8 0
- X\_3,9,1 -X\_3,9,9 0
- X\_3,9,2 -X\_3,9,3 0
- X\_3,9,2 -X\_3,9,4 0
- X\_3,9,2 -X\_3,9,5 0
- X\_3,9,2 -X\_3,9,6 0
- X\_3,9,2 -X\_3,9,7 0
- X\_3,9,2 -X\_3,9,8 0
- X\_3,9,2 -X\_3,9,9 0
- X\_3,9,3 -X\_3,9,4 0
- X\_3,9,3 -X\_3,9,5 0
- X\_3,9,3 -X\_3,9,6 0
- X\_3,9,3 -X\_3,9,7 0
- X\_3,9,3 -X\_3,9,8 0
- X\_3,9,3 -X\_3,9,9 0
- X\_3,9,4 -X\_3,9,5 0
- X\_3,9,4 -X\_3,9,6 0
- X\_3,9,4 -X\_3,9,7 0
- X\_3,9,4 -X\_3,9,8 0
- X\_3,9,4 -X\_3,9,9 0
- X\_3,9,5 -X\_3,9,6 0
- X\_3,9,5 -X\_3,9,7 0
- X\_3,9,5 -X\_3,9,8 0
- X\_3,9,5 -X\_3,9,9 0
- X\_3,9,6 -X\_3,9,7 0
- X\_3,9,6 -X\_3,9,8 0
- X\_3,9,6 -X\_3,9,9 0
- X\_3,9,7 -X\_3,9,8 0
- X\_3,9,7 -X\_3,9,9 0
- X\_3,9,8 -X\_3,9,9 0
- X\_4,1,1 -X\_4,1,2 0
- X\_4,1,1 -X\_4,1,3 0
- X\_4,1,1 -X\_4,1,4 0
- X\_4,1,1 -X\_4,1,5 0
- X\_4,1,1 -X\_4,1,6 0
- X\_4,1,1 -X\_4,1,7 0
- X\_4,1,1 -X\_4,1,8 0
- X\_4,1,1 -X\_4,1,9 0
- X\_4,1,2 -X\_4,1,3 0
- X\_4,1,2 -X\_4,1,4 0
- X\_4,1,2 -X\_4,1,5 0
- X\_4,1,2 -X\_4,1,6 0
- X\_4,1,2 -X\_4,1,7 0
- X\_4,1,2 -X\_4,1,8 0
- X\_4,1,2 -X\_4,1,9 0
- X\_4,1,3 -X\_4,1,4 0
- X\_4,1,3 -X\_4,1,5 0
- X\_4,1,3 -X\_4,1,6 0
- X\_4,1,3 -X\_4,1,7 0
- X\_4,1,3 -X\_4,1,8 0
- X\_4,1,3 -X\_4,1,9 0
- X\_4,1,4 -X\_4,1,5 0
- X\_4,1,4 -X\_4,1,6 0
- X\_4,1,4 -X\_4,1,7 0
- X\_4,1,4 -X\_4,1,8 0
- X\_4,1,4 -X\_4,1,9 0
- X\_4,1,5 -X\_4,1,6 0
- X\_4,1,5 -X\_4,1,7 0
- X\_4,1,5 -X\_4,1,8 0
- X\_4,1,5 -X\_4,1,9 0
- X\_4,1,6 -X\_4,1,7 0
- X\_4,1,6 -X\_4,1,8 0
- X\_4,1,6 -X\_4,1,9 0
- X\_4,1,7 -X\_4,1,8 0
- X\_4,1,7 -X\_4,1,9 0
- X\_4,1,8 -X\_4,1,9 0
- X\_4,2,1 -X\_4,2,2 0
- X\_4,2,1 -X\_4,2,3 0
- X\_4,2,1 -X\_4,2,4 0
- X\_4,2,1 -X\_4,2,5 0
- X\_4,2,1 -X\_4,2,6 0
- X\_4,2,1 -X\_4,2,7 0
- X\_4,2,1 -X\_4,2,8 0
- X\_4,2,1 -X\_4,2,9 0
- X\_4,2,2 -X\_4,2,3 0
- X\_4,2,2 -X\_4,2,4 0
- X\_4,2,2 -X\_4,2,5 0
- X\_4,2,2 -X\_4,2,6 0
- X\_4,2,2 -X\_4,2,7 0
- X\_4,2,2 -X\_4,2,8 0
- X\_4,2,2 -X\_4,2,9 0
- X\_4,2,3 -X\_4,2,4 0
- X\_4,2,3 -X\_4,2,5 0
- X\_4,2,3 -X\_4,2,6 0
- X\_4,2,3 -X\_4,2,7 0
- X\_4,2,3 -X\_4,2,8 0
- X\_4,2,3 -X\_4,2,9 0
- X\_4,2,4 -X\_4,2,5 0
- X\_4,2,4 -X\_4,2,6 0
- X\_4,2,4 -X\_4,2,7 0
- X\_4,2,4 -X\_4,2,8 0
- X\_4,2,4 -X\_4,2,9 0
- X\_4,2,5 -X\_4,2,6 0
- X\_4,2,5 -X\_4,2,7 0
- X\_4,2,5 -X\_4,2,8 0
- X\_4,2,5 -X\_4,2,9 0
- X\_4,2,6 -X\_4,2,7 0
- X\_4,2,6 -X\_4,2,8 0
- X\_4,2,6 -X\_4,2,9 0
- X\_4,2,7 -X\_4,2,8 0
- X\_4,2,7 -X\_4,2,9 0
- X\_4,2,8 -X\_4,2,9 0
- X\_4,3,1 -X\_4,3,2 0
- X\_4,3,1 -X\_4,3,3 0
- X\_4,3,1 -X\_4,3,4 0
- X\_4,3,1 -X\_4,3,5 0
- X\_4,3,1 -X\_4,3,6 0
- X\_4,3,1 -X\_4,3,7 0
- X\_4,3,1 -X\_4,3,8 0
- X\_4,3,1 -X\_4,3,9 0
- X\_4,3,2 -X\_4,3,3 0
- X\_4,3,2 -X\_4,3,4 0
- X\_4,3,2 -X\_4,3,5 0
- X\_4,3,2 -X\_4,3,6 0
- X\_4,3,2 -X\_4,3,7 0
- X\_4,3,2 -X\_4,3,8 0
- X\_4,3,2 -X\_4,3,9 0
- X\_4,3,3 -X\_4,3,4 0
- X\_4,3,3 -X\_4,3,5 0
- X\_4,3,3 -X\_4,3,6 0
- X\_4,3,3 -X\_4,3,7 0
- X\_4,3,3 -X\_4,3,8 0
- X\_4,3,3 -X\_4,3,9 0
- X\_4,3,4 -X\_4,3,5 0
- X\_4,3,4 -X\_4,3,6 0
- X\_4,3,4 -X\_4,3,7 0
- X\_4,3,4 -X\_4,3,8 0
- X\_4,3,4 -X\_4,3,9 0
- X\_4,3,5 -X\_4,3,6 0
- X\_4,3,5 -X\_4,3,7 0
- X\_4,3,5 -X\_4,3,8 0
- X\_4,3,5 -X\_4,3,9 0
- X\_4,3,6 -X\_4,3,7 0
- X\_4,3,6 -X\_4,3,8 0
- X\_4,3,6 -X\_4,3,9 0
- X\_4,3,7 -X\_4,3,8 0
- X\_4,3,7 -X\_4,3,9 0
- X\_4,3,8 -X\_4,3,9 0
- X\_4,4,1 -X\_4,4,2 0
- X\_4,4,1 -X\_4,4,3 0
- X\_4,4,1 -X\_4,4,4 0
- X\_4,4,1 -X\_4,4,5 0
- X\_4,4,1 -X\_4,4,6 0
- X\_4,4,1 -X\_4,4,7 0
- X\_4,4,1 -X\_4,4,8 0
- X\_4,4,1 -X\_4,4,9 0
- X\_4,4,2 -X\_4,4,3 0
- X\_4,4,2 -X\_4,4,4 0
- X\_4,4,2 -X\_4,4,5 0
- X\_4,4,2 -X\_4,4,6 0
- X\_4,4,2 -X\_4,4,7 0
- X\_4,4,2 -X\_4,4,8 0
- X\_4,4,2 -X\_4,4,9 0
- X\_4,4,3 -X\_4,4,4 0
- X\_4,4,3 -X\_4,4,5 0
- X\_4,4,3 -X\_4,4,6 0
- X\_4,4,3 -X\_4,4,7 0
- X\_4,4,3 -X\_4,4,8 0
- X\_4,4,3 -X\_4,4,9 0
- X\_4,4,4 -X\_4,4,5 0
- X\_4,4,4 -X\_4,4,6 0
- X\_4,4,4 -X\_4,4,7 0
- X\_4,4,4 -X\_4,4,8 0
- X\_4,4,4 -X\_4,4,9 0
- X\_4,4,5 -X\_4,4,6 0
- X\_4,4,5 -X\_4,4,7 0
- X\_4,4,5 -X\_4,4,8 0
- X\_4,4,5 -X\_4,4,9 0
- X\_4,4,6 -X\_4,4,7 0
- X\_4,4,6 -X\_4,4,8 0
- X\_4,4,6 -X\_4,4,9 0
- X\_4,4,7 -X\_4,4,8 0
- X\_4,4,7 -X\_4,4,9 0
- X\_4,4,8 -X\_4,4,9 0
- X\_4,5,1 -X\_4,5,2 0
- X\_4,5,1 -X\_4,5,3 0
- X\_4,5,1 -X\_4,5,4 0
- X\_4,5,1 -X\_4,5,5 0
- X\_4,5,1 -X\_4,5,6 0
- X\_4,5,1 -X\_4,5,7 0
- X\_4,5,1 -X\_4,5,8 0
- X\_4,5,1 -X\_4,5,9 0
- X\_4,5,2 -X\_4,5,3 0
- X\_4,5,2 -X\_4,5,4 0
- X\_4,5,2 -X\_4,5,5 0
- X\_4,5,2 -X\_4,5,6 0
- X\_4,5,2 -X\_4,5,7 0
- X\_4,5,2 -X\_4,5,8 0
- X\_4,5,2 -X\_4,5,9 0
- X\_4,5,3 -X\_4,5,4 0
- X\_4,5,3 -X\_4,5,5 0
- X\_4,5,3 -X\_4,5,6 0
- X\_4,5,3 -X\_4,5,7 0
- X\_4,5,3 -X\_4,5,8 0
- X\_4,5,3 -X\_4,5,9 0
- X\_4,5,4 -X\_4,5,5 0
- X\_4,5,4 -X\_4,5,6 0
- X\_4,5,4 -X\_4,5,7 0
- X\_4,5,4 -X\_4,5,8 0
- X\_4,5,4 -X\_4,5,9 0
- X\_4,5,5 -X\_4,5,6 0
- X\_4,5,5 -X\_4,5,7 0
- X\_4,5,5 -X\_4,5,8 0
- X\_4,5,5 -X\_4,5,9 0
- X\_4,5,6 -X\_4,5,7 0
- X\_4,5,6 -X\_4,5,8 0
- X\_4,5,6 -X\_4,5,9 0
- X\_4,5,7 -X\_4,5,8 0
- X\_4,5,7 -X\_4,5,9 0
- X\_4,5,8 -X\_4,5,9 0
- X\_4,6,1 -X\_4,6,2 0
- X\_4,6,1 -X\_4,6,3 0
- X\_4,6,1 -X\_4,6,4 0
- X\_4,6,1 -X\_4,6,5 0
- X\_4,6,1 -X\_4,6,6 0
- X\_4,6,1 -X\_4,6,7 0
- X\_4,6,1 -X\_4,6,8 0
- X\_4,6,1 -X\_4,6,9 0
- X\_4,6,2 -X\_4,6,3 0
- X\_4,6,2 -X\_4,6,4 0
- X\_4,6,2 -X\_4,6,5 0
- X\_4,6,2 -X\_4,6,6 0
- X\_4,6,2 -X\_4,6,7 0
- X\_4,6,2 -X\_4,6,8 0
- X\_4,6,2 -X\_4,6,9 0
- X\_4,6,3 -X\_4,6,4 0
- X\_4,6,3 -X\_4,6,5 0
- X\_4,6,3 -X\_4,6,6 0
- X\_4,6,3 -X\_4,6,7 0
- X\_4,6,3 -X\_4,6,8 0
- X\_4,6,3 -X\_4,6,9 0
- X\_4,6,4 -X\_4,6,5 0
- X\_4,6,4 -X\_4,6,6 0
- X\_4,6,4 -X\_4,6,7 0
- X\_4,6,4 -X\_4,6,8 0
- X\_4,6,4 -X\_4,6,9 0
- X\_4,6,5 -X\_4,6,6 0
- X\_4,6,5 -X\_4,6,7 0
- X\_4,6,5 -X\_4,6,8 0
- X\_4,6,5 -X\_4,6,9 0
- X\_4,6,6 -X\_4,6,7 0
- X\_4,6,6 -X\_4,6,8 0
- X\_4,6,6 -X\_4,6,9 0
- X\_4,6,7 -X\_4,6,8 0
- X\_4,6,7 -X\_4,6,9 0
- X\_4,6,8 -X\_4,6,9 0
- X\_4,7,1 -X\_4,7,2 0
- X\_4,7,1 -X\_4,7,3 0
- X\_4,7,1 -X\_4,7,4 0
- X\_4,7,1 -X\_4,7,5 0
- X\_4,7,1 -X\_4,7,6 0
- X\_4,7,1 -X\_4,7,7 0
- X\_4,7,1 -X\_4,7,8 0
- X\_4,7,1 -X\_4,7,9 0
- X\_4,7,2 -X\_4,7,3 0
- X\_4,7,2 -X\_4,7,4 0
- X\_4,7,2 -X\_4,7,5 0
- X\_4,7,2 -X\_4,7,6 0
- X\_4,7,2 -X\_4,7,7 0
- X\_4,7,2 -X\_4,7,8 0
- X\_4,7,2 -X\_4,7,9 0
- X\_4,7,3 -X\_4,7,4 0
- X\_4,7,3 -X\_4,7,5 0
- X\_4,7,3 -X\_4,7,6 0
- X\_4,7,3 -X\_4,7,7 0
- X\_4,7,3 -X\_4,7,8 0
- X\_4,7,3 -X\_4,7,9 0
- X\_4,7,4 -X\_4,7,5 0
- X\_4,7,4 -X\_4,7,6 0
- X\_4,7,4 -X\_4,7,7 0
- X\_4,7,4 -X\_4,7,8 0
- X\_4,7,4 -X\_4,7,9 0
- X\_4,7,5 -X\_4,7,6 0
- X\_4,7,5 -X\_4,7,7 0
- X\_4,7,5 -X\_4,7,8 0
- X\_4,7,5 -X\_4,7,9 0
- X\_4,7,6 -X\_4,7,7 0
- X\_4,7,6 -X\_4,7,8 0
- X\_4,7,6 -X\_4,7,9 0
- X\_4,7,7 -X\_4,7,8 0
- X\_4,7,7 -X\_4,7,9 0
- X\_4,7,8 -X\_4,7,9 0
- X\_4,8,1 -X\_4,8,2 0
- X\_4,8,1 -X\_4,8,3 0
- X\_4,8,1 -X\_4,8,4 0
- X\_4,8,1 -X\_4,8,5 0
- X\_4,8,1 -X\_4,8,6 0
- X\_4,8,1 -X\_4,8,7 0
- X\_4,8,1 -X\_4,8,8 0
- X\_4,8,1 -X\_4,8,9 0
- X\_4,8,2 -X\_4,8,3 0
- X\_4,8,2 -X\_4,8,4 0
- X\_4,8,2 -X\_4,8,5 0
- X\_4,8,2 -X\_4,8,6 0
- X\_4,8,2 -X\_4,8,7 0
- X\_4,8,2 -X\_4,8,8 0
- X\_4,8,2 -X\_4,8,9 0
- X\_4,8,3 -X\_4,8,4 0
- X\_4,8,3 -X\_4,8,5 0
- X\_4,8,3 -X\_4,8,6 0
- X\_4,8,3 -X\_4,8,7 0
- X\_4,8,3 -X\_4,8,8 0
- X\_4,8,3 -X\_4,8,9 0
- X\_4,8,4 -X\_4,8,5 0
- X\_4,8,4 -X\_4,8,6 0
- X\_4,8,4 -X\_4,8,7 0
- X\_4,8,4 -X\_4,8,8 0
- X\_4,8,4 -X\_4,8,9 0
- X\_4,8,5 -X\_4,8,6 0
- X\_4,8,5 -X\_4,8,7 0
- X\_4,8,5 -X\_4,8,8 0
- X\_4,8,5 -X\_4,8,9 0
- X\_4,8,6 -X\_4,8,7 0
- X\_4,8,6 -X\_4,8,8 0
- X\_4,8,6 -X\_4,8,9 0
- X\_4,8,7 -X\_4,8,8 0
- X\_4,8,7 -X\_4,8,9 0
- X\_4,8,8 -X\_4,8,9 0
- X\_4,9,1 -X\_4,9,2 0
- X\_4,9,1 -X\_4,9,3 0
- X\_4,9,1 -X\_4,9,4 0
- X\_4,9,1 -X\_4,9,5 0
- X\_4,9,1 -X\_4,9,6 0
- X\_4,9,1 -X\_4,9,7 0
- X\_4,9,1 -X\_4,9,8 0
- X\_4,9,1 -X\_4,9,9 0
- X\_4,9,2 -X\_4,9,3 0
- X\_4,9,2 -X\_4,9,4 0
- X\_4,9,2 -X\_4,9,5 0
- X\_4,9,2 -X\_4,9,6 0
- X\_4,9,2 -X\_4,9,7 0
- X\_4,9,2 -X\_4,9,8 0
- X\_4,9,2 -X\_4,9,9 0
- X\_4,9,3 -X\_4,9,4 0
- X\_4,9,3 -X\_4,9,5 0
- X\_4,9,3 -X\_4,9,6 0
- X\_4,9,3 -X\_4,9,7 0
- X\_4,9,3 -X\_4,9,8 0
- X\_4,9,3 -X\_4,9,9 0
- X\_4,9,4 -X\_4,9,5 0
- X\_4,9,4 -X\_4,9,6 0
- X\_4,9,4 -X\_4,9,7 0
- X\_4,9,4 -X\_4,9,8 0
- X\_4,9,4 -X\_4,9,9 0
- X\_4,9,5 -X\_4,9,6 0
- X\_4,9,5 -X\_4,9,7 0
- X\_4,9,5 -X\_4,9,8 0
- X\_4,9,5 -X\_4,9,9 0
- X\_4,9,6 -X\_4,9,7 0
- X\_4,9,6 -X\_4,9,8 0
- X\_4,9,6 -X\_4,9,9 0
- X\_4,9,7 -X\_4,9,8 0
- X\_4,9,7 -X\_4,9,9 0
- X\_4,9,8 -X\_4,9,9 0
- X\_5,1,1 -X\_5,1,2 0
- X\_5,1,1 -X\_5,1,3 0
- X\_5,1,1 -X\_5,1,4 0
- X\_5,1,1 -X\_5,1,5 0
- X\_5,1,1 -X\_5,1,6 0
- X\_5,1,1 -X\_5,1,7 0
- X\_5,1,1 -X\_5,1,8 0
- X\_5,1,1 -X\_5,1,9 0
- X\_5,1,2 -X\_5,1,3 0
- X\_5,1,2 -X\_5,1,4 0
- X\_5,1,2 -X\_5,1,5 0
- X\_5,1,2 -X\_5,1,6 0
- X\_5,1,2 -X\_5,1,7 0
- X\_5,1,2 -X\_5,1,8 0
- X\_5,1,2 -X\_5,1,9 0
- X\_5,1,3 -X\_5,1,4 0
- X\_5,1,3 -X\_5,1,5 0
- X\_5,1,3 -X\_5,1,6 0
- X\_5,1,3 -X\_5,1,7 0
- X\_5,1,3 -X\_5,1,8 0
- X\_5,1,3 -X\_5,1,9 0
- X\_5,1,4 -X\_5,1,5 0
- X\_5,1,4 -X\_5,1,6 0
- X\_5,1,4 -X\_5,1,7 0
- X\_5,1,4 -X\_5,1,8 0
- X\_5,1,4 -X\_5,1,9 0
- X\_5,1,5 -X\_5,1,6 0
- X\_5,1,5 -X\_5,1,7 0
- X\_5,1,5 -X\_5,1,8 0
- X\_5,1,5 -X\_5,1,9 0
- X\_5,1,6 -X\_5,1,7 0
- X\_5,1,6 -X\_5,1,8 0
- X\_5,1,6 -X\_5,1,9 0
- X\_5,1,7 -X\_5,1,8 0
- X\_5,1,7 -X\_5,1,9 0
- X\_5,1,8 -X\_5,1,9 0
- X\_5,2,1 -X\_5,2,2 0
- X\_5,2,1 -X\_5,2,3 0
- X\_5,2,1 -X\_5,2,4 0
- X\_5,2,1 -X\_5,2,5 0
- X\_5,2,1 -X\_5,2,6 0
- X\_5,2,1 -X\_5,2,7 0
- X\_5,2,1 -X\_5,2,8 0
- X\_5,2,1 -X\_5,2,9 0
- X\_5,2,2 -X\_5,2,3 0
- X\_5,2,2 -X\_5,2,4 0
- X\_5,2,2 -X\_5,2,5 0
- X\_5,2,2 -X\_5,2,6 0
- X\_5,2,2 -X\_5,2,7 0
- X\_5,2,2 -X\_5,2,8 0
- X\_5,2,2 -X\_5,2,9 0
- X\_5,2,3 -X\_5,2,4 0
- X\_5,2,3 -X\_5,2,5 0
- X\_5,2,3 -X\_5,2,6 0
- X\_5,2,3 -X\_5,2,7 0
- X\_5,2,3 -X\_5,2,8 0
- X\_5,2,3 -X\_5,2,9 0
- X\_5,2,4 -X\_5,2,5 0
- X\_5,2,4 -X\_5,2,6 0
- X\_5,2,4 -X\_5,2,7 0
- X\_5,2,4 -X\_5,2,8 0
- X\_5,2,4 -X\_5,2,9 0
- X\_5,2,5 -X\_5,2,6 0
- X\_5,2,5 -X\_5,2,7 0
- X\_5,2,5 -X\_5,2,8 0
- X\_5,2,5 -X\_5,2,9 0
- X\_5,2,6 -X\_5,2,7 0
- X\_5,2,6 -X\_5,2,8 0
- X\_5,2,6 -X\_5,2,9 0
- X\_5,2,7 -X\_5,2,8 0
- X\_5,2,7 -X\_5,2,9 0
- X\_5,2,8 -X\_5,2,9 0
- X\_5,3,1 -X\_5,3,2 0
- X\_5,3,1 -X\_5,3,3 0
- X\_5,3,1 -X\_5,3,4 0
- X\_5,3,1 -X\_5,3,5 0
- X\_5,3,1 -X\_5,3,6 0
- X\_5,3,1 -X\_5,3,7 0
- X\_5,3,1 -X\_5,3,8 0
- X\_5,3,1 -X\_5,3,9 0
- X\_5,3,2 -X\_5,3,3 0
- X\_5,3,2 -X\_5,3,4 0
- X\_5,3,2 -X\_5,3,5 0
- X\_5,3,2 -X\_5,3,6 0
- X\_5,3,2 -X\_5,3,7 0
- X\_5,3,2 -X\_5,3,8 0
- X\_5,3,2 -X\_5,3,9 0
- X\_5,3,3 -X\_5,3,4 0
- X\_5,3,3 -X\_5,3,5 0
- X\_5,3,3 -X\_5,3,6 0
- X\_5,3,3 -X\_5,3,7 0
- X\_5,3,3 -X\_5,3,8 0
- X\_5,3,3 -X\_5,3,9 0
- X\_5,3,4 -X\_5,3,5 0
- X\_5,3,4 -X\_5,3,6 0
- X\_5,3,4 -X\_5,3,7 0
- X\_5,3,4 -X\_5,3,8 0
- X\_5,3,4 -X\_5,3,9 0
- X\_5,3,5 -X\_5,3,6 0
- X\_5,3,5 -X\_5,3,7 0
- X\_5,3,5 -X\_5,3,8 0
- X\_5,3,5 -X\_5,3,9 0
- X\_5,3,6 -X\_5,3,7 0
- X\_5,3,6 -X\_5,3,8 0
- X\_5,3,6 -X\_5,3,9 0
- X\_5,3,7 -X\_5,3,8 0
- X\_5,3,7 -X\_5,3,9 0
- X\_5,3,8 -X\_5,3,9 0
- X\_5,4,1 -X\_5,4,2 0
- X\_5,4,1 -X\_5,4,3 0
- X\_5,4,1 -X\_5,4,4 0
- X\_5,4,1 -X\_5,4,5 0
- X\_5,4,1 -X\_5,4,6 0
- X\_5,4,1 -X\_5,4,7 0
- X\_5,4,1 -X\_5,4,8 0
- X\_5,4,1 -X\_5,4,9 0
- X\_5,4,2 -X\_5,4,3 0
- X\_5,4,2 -X\_5,4,4 0
- X\_5,4,2 -X\_5,4,5 0
- X\_5,4,2 -X\_5,4,6 0
- X\_5,4,2 -X\_5,4,7 0
- X\_5,4,2 -X\_5,4,8 0
- X\_5,4,2 -X\_5,4,9 0
- X\_5,4,3 -X\_5,4,4 0
- X\_5,4,3 -X\_5,4,5 0
- X\_5,4,3 -X\_5,4,6 0
- X\_5,4,3 -X\_5,4,7 0
- X\_5,4,3 -X\_5,4,8 0
- X\_5,4,3 -X\_5,4,9 0
- X\_5,4,4 -X\_5,4,5 0
- X\_5,4,4 -X\_5,4,6 0
- X\_5,4,4 -X\_5,4,7 0
- X\_5,4,4 -X\_5,4,8 0
- X\_5,4,4 -X\_5,4,9 0
- X\_5,4,5 -X\_5,4,6 0
- X\_5,4,5 -X\_5,4,7 0
- X\_5,4,5 -X\_5,4,8 0
- X\_5,4,5 -X\_5,4,9 0
- X\_5,4,6 -X\_5,4,7 0
- X\_5,4,6 -X\_5,4,8 0
- X\_5,4,6 -X\_5,4,9 0
- X\_5,4,7 -X\_5,4,8 0
- X\_5,4,7 -X\_5,4,9 0
- X\_5,4,8 -X\_5,4,9 0
- X\_5,5,1 -X\_5,5,2 0
- X\_5,5,1 -X\_5,5,3 0
- X\_5,5,1 -X\_5,5,4 0
- X\_5,5,1 -X\_5,5,5 0
- X\_5,5,1 -X\_5,5,6 0
- X\_5,5,1 -X\_5,5,7 0
- X\_5,5,1 -X\_5,5,8 0
- X\_5,5,1 -X\_5,5,9 0
- X\_5,5,2 -X\_5,5,3 0
- X\_5,5,2 -X\_5,5,4 0
- X\_5,5,2 -X\_5,5,5 0
- X\_5,5,2 -X\_5,5,6 0
- X\_5,5,2 -X\_5,5,7 0
- X\_5,5,2 -X\_5,5,8 0
- X\_5,5,2 -X\_5,5,9 0
- X\_5,5,3 -X\_5,5,4 0
- X\_5,5,3 -X\_5,5,5 0
- X\_5,5,3 -X\_5,5,6 0
- X\_5,5,3 -X\_5,5,7 0
- X\_5,5,3 -X\_5,5,8 0
- X\_5,5,3 -X\_5,5,9 0
- X\_5,5,4 -X\_5,5,5 0
- X\_5,5,4 -X\_5,5,6 0
- X\_5,5,4 -X\_5,5,7 0
- X\_5,5,4 -X\_5,5,8 0
- X\_5,5,4 -X\_5,5,9 0
- X\_5,5,5 -X\_5,5,6 0
- X\_5,5,5 -X\_5,5,7 0
- X\_5,5,5 -X\_5,5,8 0
- X\_5,5,5 -X\_5,5,9 0
- X\_5,5,6 -X\_5,5,7 0
- X\_5,5,6 -X\_5,5,8 0
- X\_5,5,6 -X\_5,5,9 0
- X\_5,5,7 -X\_5,5,8 0
- X\_5,5,7 -X\_5,5,9 0
- X\_5,5,8 -X\_5,5,9 0
- X\_5,6,1 -X\_5,6,2 0
- X\_5,6,1 -X\_5,6,3 0
- X\_5,6,1 -X\_5,6,4 0
- X\_5,6,1 -X\_5,6,5 0
- X\_5,6,1 -X\_5,6,6 0
- X\_5,6,1 -X\_5,6,7 0
- X\_5,6,1 -X\_5,6,8 0
- X\_5,6,1 -X\_5,6,9 0
- X\_5,6,2 -X\_5,6,3 0
- X\_5,6,2 -X\_5,6,4 0
- X\_5,6,2 -X\_5,6,5 0
- X\_5,6,2 -X\_5,6,6 0
- X\_5,6,2 -X\_5,6,7 0
- X\_5,6,2 -X\_5,6,8 0
- X\_5,6,2 -X\_5,6,9 0
- X\_5,6,3 -X\_5,6,4 0
- X\_5,6,3 -X\_5,6,5 0
- X\_5,6,3 -X\_5,6,6 0
- X\_5,6,3 -X\_5,6,7 0
- X\_5,6,3 -X\_5,6,8 0
- X\_5,6,3 -X\_5,6,9 0
- X\_5,6,4 -X\_5,6,5 0
- X\_5,6,4 -X\_5,6,6 0
- X\_5,6,4 -X\_5,6,7 0
- X\_5,6,4 -X\_5,6,8 0
- X\_5,6,4 -X\_5,6,9 0
- X\_5,6,5 -X\_5,6,6 0
- X\_5,6,5 -X\_5,6,7 0
- X\_5,6,5 -X\_5,6,8 0
- X\_5,6,5 -X\_5,6,9 0
- X\_5,6,6 -X\_5,6,7 0
- X\_5,6,6 -X\_5,6,8 0
- X\_5,6,6 -X\_5,6,9 0
- X\_5,6,7 -X\_5,6,8 0
- X\_5,6,7 -X\_5,6,9 0
- X\_5,6,8 -X\_5,6,9 0
- X\_5,7,1 -X\_5,7,2 0
- X\_5,7,1 -X\_5,7,3 0
- X\_5,7,1 -X\_5,7,4 0
- X\_5,7,1 -X\_5,7,5 0
- X\_5,7,1 -X\_5,7,6 0
- X\_5,7,1 -X\_5,7,7 0
- X\_5,7,1 -X\_5,7,8 0
- X\_5,7,1 -X\_5,7,9 0
- X\_5,7,2 -X\_5,7,3 0
- X\_5,7,2 -X\_5,7,4 0
- X\_5,7,2 -X\_5,7,5 0
- X\_5,7,2 -X\_5,7,6 0
- X\_5,7,2 -X\_5,7,7 0
- X\_5,7,2 -X\_5,7,8 0
- X\_5,7,2 -X\_5,7,9 0
- X\_5,7,3 -X\_5,7,4 0
- X\_5,7,3 -X\_5,7,5 0
- X\_5,7,3 -X\_5,7,6 0
- X\_5,7,3 -X\_5,7,7 0
- X\_5,7,3 -X\_5,7,8 0
- X\_5,7,3 -X\_5,7,9 0
- X\_5,7,4 -X\_5,7,5 0
- X\_5,7,4 -X\_5,7,6 0
- X\_5,7,4 -X\_5,7,7 0
- X\_5,7,4 -X\_5,7,8 0
- X\_5,7,4 -X\_5,7,9 0
- X\_5,7,5 -X\_5,7,6 0
- X\_5,7,5 -X\_5,7,7 0
- X\_5,7,5 -X\_5,7,8 0
- X\_5,7,5 -X\_5,7,9 0
- X\_5,7,6 -X\_5,7,7 0
- X\_5,7,6 -X\_5,7,8 0
- X\_5,7,6 -X\_5,7,9 0
- X\_5,7,7 -X\_5,7,8 0
- X\_5,7,7 -X\_5,7,9 0
- X\_5,7,8 -X\_5,7,9 0
- X\_5,8,1 -X\_5,8,2 0
- X\_5,8,1 -X\_5,8,3 0
- X\_5,8,1 -X\_5,8,4 0
- X\_5,8,1 -X\_5,8,5 0
- X\_5,8,1 -X\_5,8,6 0
- X\_5,8,1 -X\_5,8,7 0
- X\_5,8,1 -X\_5,8,8 0
- X\_5,8,1 -X\_5,8,9 0
- X\_5,8,2 -X\_5,8,3 0
- X\_5,8,2 -X\_5,8,4 0
- X\_5,8,2 -X\_5,8,5 0
- X\_5,8,2 -X\_5,8,6 0
- X\_5,8,2 -X\_5,8,7 0
- X\_5,8,2 -X\_5,8,8 0
- X\_5,8,2 -X\_5,8,9 0
- X\_5,8,3 -X\_5,8,4 0
- X\_5,8,3 -X\_5,8,5 0
- X\_5,8,3 -X\_5,8,6 0
- X\_5,8,3 -X\_5,8,7 0
- X\_5,8,3 -X\_5,8,8 0
- X\_5,8,3 -X\_5,8,9 0
- X\_5,8,4 -X\_5,8,5 0
- X\_5,8,4 -X\_5,8,6 0
- X\_5,8,4 -X\_5,8,7 0
- X\_5,8,4 -X\_5,8,8 0
- X\_5,8,4 -X\_5,8,9 0
- X\_5,8,5 -X\_5,8,6 0
- X\_5,8,5 -X\_5,8,7 0
- X\_5,8,5 -X\_5,8,8 0
- X\_5,8,5 -X\_5,8,9 0
- X\_5,8,6 -X\_5,8,7 0
- X\_5,8,6 -X\_5,8,8 0
- X\_5,8,6 -X\_5,8,9 0
- X\_5,8,7 -X\_5,8,8 0
- X\_5,8,7 -X\_5,8,9 0
- X\_5,8,8 -X\_5,8,9 0
- X\_5,9,1 -X\_5,9,2 0
- X\_5,9,1 -X\_5,9,3 0
- X\_5,9,1 -X\_5,9,4 0
- X\_5,9,1 -X\_5,9,5 0
- X\_5,9,1 -X\_5,9,6 0
- X\_5,9,1 -X\_5,9,7 0
- X\_5,9,1 -X\_5,9,8 0
- X\_5,9,1 -X\_5,9,9 0
- X\_5,9,2 -X\_5,9,3 0
- X\_5,9,2 -X\_5,9,4 0
- X\_5,9,2 -X\_5,9,5 0
- X\_5,9,2 -X\_5,9,6 0
- X\_5,9,2 -X\_5,9,7 0
- X\_5,9,2 -X\_5,9,8 0
- X\_5,9,2 -X\_5,9,9 0
- X\_5,9,3 -X\_5,9,4 0
- X\_5,9,3 -X\_5,9,5 0
- X\_5,9,3 -X\_5,9,6 0
- X\_5,9,3 -X\_5,9,7 0
- X\_5,9,3 -X\_5,9,8 0
- X\_5,9,3 -X\_5,9,9 0
- X\_5,9,4 -X\_5,9,5 0
- X\_5,9,4 -X\_5,9,6 0
- X\_5,9,4 -X\_5,9,7 0
- X\_5,9,4 -X\_5,9,8 0
- X\_5,9,4 -X\_5,9,9 0
- X\_5,9,5 -X\_5,9,6 0
- X\_5,9,5 -X\_5,9,7 0
- X\_5,9,5 -X\_5,9,8 0
- X\_5,9,5 -X\_5,9,9 0
- X\_5,9,6 -X\_5,9,7 0
- X\_5,9,6 -X\_5,9,8 0
- X\_5,9,6 -X\_5,9,9 0
- X\_5,9,7 -X\_5,9,8 0
- X\_5,9,7 -X\_5,9,9 0
- X\_5,9,8 -X\_5,9,9 0
- X\_6,1,1 -X\_6,1,2 0
- X\_6,1,1 -X\_6,1,3 0
- X\_6,1,1 -X\_6,1,4 0
- X\_6,1,1 -X\_6,1,5 0
- X\_6,1,1 -X\_6,1,6 0
- X\_6,1,1 -X\_6,1,7 0
- X\_6,1,1 -X\_6,1,8 0
- X\_6,1,1 -X\_6,1,9 0
- X\_6,1,2 -X\_6,1,3 0
- X\_6,1,2 -X\_6,1,4 0
- X\_6,1,2 -X\_6,1,5 0
- X\_6,1,2 -X\_6,1,6 0
- X\_6,1,2 -X\_6,1,7 0
- X\_6,1,2 -X\_6,1,8 0
- X\_6,1,2 -X\_6,1,9 0
- X\_6,1,3 -X\_6,1,4 0
- X\_6,1,3 -X\_6,1,5 0
- X\_6,1,3 -X\_6,1,6 0
- X\_6,1,3 -X\_6,1,7 0
- X\_6,1,3 -X\_6,1,8 0
- X\_6,1,3 -X\_6,1,9 0
- X\_6,1,4 -X\_6,1,5 0
- X\_6,1,4 -X\_6,1,6 0
- X\_6,1,4 -X\_6,1,7 0
- X\_6,1,4 -X\_6,1,8 0
- X\_6,1,4 -X\_6,1,9 0
- X\_6,1,5 -X\_6,1,6 0
- X\_6,1,5 -X\_6,1,7 0
- X\_6,1,5 -X\_6,1,8 0
- X\_6,1,5 -X\_6,1,9 0
- X\_6,1,6 -X\_6,1,7 0
- X\_6,1,6 -X\_6,1,8 0
- X\_6,1,6 -X\_6,1,9 0
- X\_6,1,7 -X\_6,1,8 0
- X\_6,1,7 -X\_6,1,9 0
- X\_6,1,8 -X\_6,1,9 0
- X\_6,2,1 -X\_6,2,2 0
- X\_6,2,1 -X\_6,2,3 0
- X\_6,2,1 -X\_6,2,4 0
- X\_6,2,1 -X\_6,2,5 0
- X\_6,2,1 -X\_6,2,6 0
- X\_6,2,1 -X\_6,2,7 0
- X\_6,2,1 -X\_6,2,8 0
- X\_6,2,1 -X\_6,2,9 0
- X\_6,2,2 -X\_6,2,3 0
- X\_6,2,2 -X\_6,2,4 0
- X\_6,2,2 -X\_6,2,5 0
- X\_6,2,2 -X\_6,2,6 0
- X\_6,2,2 -X\_6,2,7 0
- X\_6,2,2 -X\_6,2,8 0
- X\_6,2,2 -X\_6,2,9 0
- X\_6,2,3 -X\_6,2,4 0
- X\_6,2,3 -X\_6,2,5 0
- X\_6,2,3 -X\_6,2,6 0
- X\_6,2,3 -X\_6,2,7 0
- X\_6,2,3 -X\_6,2,8 0
- X\_6,2,3 -X\_6,2,9 0
- X\_6,2,4 -X\_6,2,5 0
- X\_6,2,4 -X\_6,2,6 0
- X\_6,2,4 -X\_6,2,7 0
- X\_6,2,4 -X\_6,2,8 0
- X\_6,2,4 -X\_6,2,9 0
- X\_6,2,5 -X\_6,2,6 0
- X\_6,2,5 -X\_6,2,7 0
- X\_6,2,5 -X\_6,2,8 0
- X\_6,2,5 -X\_6,2,9 0
- X\_6,2,6 -X\_6,2,7 0
- X\_6,2,6 -X\_6,2,8 0
- X\_6,2,6 -X\_6,2,9 0
- X\_6,2,7 -X\_6,2,8 0
- X\_6,2,7 -X\_6,2,9 0
- X\_6,2,8 -X\_6,2,9 0
- X\_6,3,1 -X\_6,3,2 0
- X\_6,3,1 -X\_6,3,3 0
- X\_6,3,1 -X\_6,3,4 0
- X\_6,3,1 -X\_6,3,5 0
- X\_6,3,1 -X\_6,3,6 0
- X\_6,3,1 -X\_6,3,7 0
- X\_6,3,1 -X\_6,3,8 0
- X\_6,3,1 -X\_6,3,9 0
- X\_6,3,2 -X\_6,3,3 0
- X\_6,3,2 -X\_6,3,4 0
- X\_6,3,2 -X\_6,3,5 0
- X\_6,3,2 -X\_6,3,6 0
- X\_6,3,2 -X\_6,3,7 0
- X\_6,3,2 -X\_6,3,8 0
- X\_6,3,2 -X\_6,3,9 0
- X\_6,3,3 -X\_6,3,4 0
- X\_6,3,3 -X\_6,3,5 0
- X\_6,3,3 -X\_6,3,6 0
- X\_6,3,3 -X\_6,3,7 0
- X\_6,3,3 -X\_6,3,8 0
- X\_6,3,3 -X\_6,3,9 0
- X\_6,3,4 -X\_6,3,5 0
- X\_6,3,4 -X\_6,3,6 0
- X\_6,3,4 -X\_6,3,7 0
- X\_6,3,4 -X\_6,3,8 0
- X\_6,3,4 -X\_6,3,9 0
- X\_6,3,5 -X\_6,3,6 0
- X\_6,3,5 -X\_6,3,7 0
- X\_6,3,5 -X\_6,3,8 0
- X\_6,3,5 -X\_6,3,9 0
- X\_6,3,6 -X\_6,3,7 0
- X\_6,3,6 -X\_6,3,8 0
- X\_6,3,6 -X\_6,3,9 0
- X\_6,3,7 -X\_6,3,8 0
- X\_6,3,7 -X\_6,3,9 0
- X\_6,3,8 -X\_6,3,9 0
- X\_6,4,1 -X\_6,4,2 0
- X\_6,4,1 -X\_6,4,3 0
- X\_6,4,1 -X\_6,4,4 0
- X\_6,4,1 -X\_6,4,5 0
- X\_6,4,1 -X\_6,4,6 0
- X\_6,4,1 -X\_6,4,7 0
- X\_6,4,1 -X\_6,4,8 0
- X\_6,4,1 -X\_6,4,9 0
- X\_6,4,2 -X\_6,4,3 0
- X\_6,4,2 -X\_6,4,4 0
- X\_6,4,2 -X\_6,4,5 0
- X\_6,4,2 -X\_6,4,6 0
- X\_6,4,2 -X\_6,4,7 0
- X\_6,4,2 -X\_6,4,8 0
- X\_6,4,2 -X\_6,4,9 0
- X\_6,4,3 -X\_6,4,4 0
- X\_6,4,3 -X\_6,4,5 0
- X\_6,4,3 -X\_6,4,6 0
- X\_6,4,3 -X\_6,4,7 0
- X\_6,4,3 -X\_6,4,8 0
- X\_6,4,3 -X\_6,4,9 0
- X\_6,4,4 -X\_6,4,5 0
- X\_6,4,4 -X\_6,4,6 0
- X\_6,4,4 -X\_6,4,7 0
- X\_6,4,4 -X\_6,4,8 0
- X\_6,4,4 -X\_6,4,9 0
- X\_6,4,5 -X\_6,4,6 0
- X\_6,4,5 -X\_6,4,7 0
- X\_6,4,5 -X\_6,4,8 0
- X\_6,4,5 -X\_6,4,9 0
- X\_6,4,6 -X\_6,4,7 0
- X\_6,4,6 -X\_6,4,8 0
- X\_6,4,6 -X\_6,4,9 0
- X\_6,4,7 -X\_6,4,8 0
- X\_6,4,7 -X\_6,4,9 0
- X\_6,4,8 -X\_6,4,9 0
- X\_6,5,1 -X\_6,5,2 0
- X\_6,5,1 -X\_6,5,3 0
- X\_6,5,1 -X\_6,5,4 0
- X\_6,5,1 -X\_6,5,5 0
- X\_6,5,1 -X\_6,5,6 0
- X\_6,5,1 -X\_6,5,7 0
- X\_6,5,1 -X\_6,5,8 0
- X\_6,5,1 -X\_6,5,9 0
- X\_6,5,2 -X\_6,5,3 0
- X\_6,5,2 -X\_6,5,4 0
- X\_6,5,2 -X\_6,5,5 0
- X\_6,5,2 -X\_6,5,6 0
- X\_6,5,2 -X\_6,5,7 0
- X\_6,5,2 -X\_6,5,8 0
- X\_6,5,2 -X\_6,5,9 0
- X\_6,5,3 -X\_6,5,4 0
- X\_6,5,3 -X\_6,5,5 0
- X\_6,5,3 -X\_6,5,6 0
- X\_6,5,3 -X\_6,5,7 0
- X\_6,5,3 -X\_6,5,8 0
- X\_6,5,3 -X\_6,5,9 0
- X\_6,5,4 -X\_6,5,5 0
- X\_6,5,4 -X\_6,5,6 0
- X\_6,5,4 -X\_6,5,7 0
- X\_6,5,4 -X\_6,5,8 0
- X\_6,5,4 -X\_6,5,9 0
- X\_6,5,5 -X\_6,5,6 0
- X\_6,5,5 -X\_6,5,7 0
- X\_6,5,5 -X\_6,5,8 0
- X\_6,5,5 -X\_6,5,9 0
- X\_6,5,6 -X\_6,5,7 0
- X\_6,5,6 -X\_6,5,8 0
- X\_6,5,6 -X\_6,5,9 0
- X\_6,5,7 -X\_6,5,8 0
- X\_6,5,7 -X\_6,5,9 0
- X\_6,5,8 -X\_6,5,9 0
- X\_6,6,1 -X\_6,6,2 0
- X\_6,6,1 -X\_6,6,3 0
- X\_6,6,1 -X\_6,6,4 0
- X\_6,6,1 -X\_6,6,5 0
- X\_6,6,1 -X\_6,6,6 0
- X\_6,6,1 -X\_6,6,7 0
- X\_6,6,1 -X\_6,6,8 0
- X\_6,6,1 -X\_6,6,9 0
- X\_6,6,2 -X\_6,6,3 0
- X\_6,6,2 -X\_6,6,4 0
- X\_6,6,2 -X\_6,6,5 0
- X\_6,6,2 -X\_6,6,6 0
- X\_6,6,2 -X\_6,6,7 0
- X\_6,6,2 -X\_6,6,8 0
- X\_6,6,2 -X\_6,6,9 0
- X\_6,6,3 -X\_6,6,4 0
- X\_6,6,3 -X\_6,6,5 0
- X\_6,6,3 -X\_6,6,6 0
- X\_6,6,3 -X\_6,6,7 0
- X\_6,6,3 -X\_6,6,8 0
- X\_6,6,3 -X\_6,6,9 0
- X\_6,6,4 -X\_6,6,5 0
- X\_6,6,4 -X\_6,6,6 0
- X\_6,6,4 -X\_6,6,7 0
- X\_6,6,4 -X\_6,6,8 0
- X\_6,6,4 -X\_6,6,9 0
- X\_6,6,5 -X\_6,6,6 0
- X\_6,6,5 -X\_6,6,7 0
- X\_6,6,5 -X\_6,6,8 0
- X\_6,6,5 -X\_6,6,9 0
- X\_6,6,6 -X\_6,6,7 0
- X\_6,6,6 -X\_6,6,8 0
- X\_6,6,6 -X\_6,6,9 0
- X\_6,6,7 -X\_6,6,8 0
- X\_6,6,7 -X\_6,6,9 0
- X\_6,6,8 -X\_6,6,9 0
- X\_6,7,1 -X\_6,7,2 0
- X\_6,7,1 -X\_6,7,3 0
- X\_6,7,1 -X\_6,7,4 0
- X\_6,7,1 -X\_6,7,5 0
- X\_6,7,1 -X\_6,7,6 0
- X\_6,7,1 -X\_6,7,7 0
- X\_6,7,1 -X\_6,7,8 0
- X\_6,7,1 -X\_6,7,9 0
- X\_6,7,2 -X\_6,7,3 0
- X\_6,7,2 -X\_6,7,4 0
- X\_6,7,2 -X\_6,7,5 0
- X\_6,7,2 -X\_6,7,6 0
- X\_6,7,2 -X\_6,7,7 0
- X\_6,7,2 -X\_6,7,8 0
- X\_6,7,2 -X\_6,7,9 0
- X\_6,7,3 -X\_6,7,4 0
- X\_6,7,3 -X\_6,7,5 0
- X\_6,7,3 -X\_6,7,6 0
- X\_6,7,3 -X\_6,7,7 0
- X\_6,7,3 -X\_6,7,8 0
- X\_6,7,3 -X\_6,7,9 0
- X\_6,7,4 -X\_6,7,5 0
- X\_6,7,4 -X\_6,7,6 0
- X\_6,7,4 -X\_6,7,7 0
- X\_6,7,4 -X\_6,7,8 0
- X\_6,7,4 -X\_6,7,9 0
- X\_6,7,5 -X\_6,7,6 0
- X\_6,7,5 -X\_6,7,7 0
- X\_6,7,5 -X\_6,7,8 0
- X\_6,7,5 -X\_6,7,9 0
- X\_6,7,6 -X\_6,7,7 0
- X\_6,7,6 -X\_6,7,8 0
- X\_6,7,6 -X\_6,7,9 0
- X\_6,7,7 -X\_6,7,8 0
- X\_6,7,7 -X\_6,7,9 0
- X\_6,7,8 -X\_6,7,9 0
- X\_6,8,1 -X\_6,8,2 0
- X\_6,8,1 -X\_6,8,3 0
- X\_6,8,1 -X\_6,8,4 0
- X\_6,8,1 -X\_6,8,5 0
- X\_6,8,1 -X\_6,8,6 0
- X\_6,8,1 -X\_6,8,7 0
- X\_6,8,1 -X\_6,8,8 0
- X\_6,8,1 -X\_6,8,9 0
- X\_6,8,2 -X\_6,8,3 0
- X\_6,8,2 -X\_6,8,4 0
- X\_6,8,2 -X\_6,8,5 0
- X\_6,8,2 -X\_6,8,6 0
- X\_6,8,2 -X\_6,8,7 0
- X\_6,8,2 -X\_6,8,8 0
- X\_6,8,2 -X\_6,8,9 0
- X\_6,8,3 -X\_6,8,4 0
- X\_6,8,3 -X\_6,8,5 0
- X\_6,8,3 -X\_6,8,6 0
- X\_6,8,3 -X\_6,8,7 0
- X\_6,8,3 -X\_6,8,8 0
- X\_6,8,3 -X\_6,8,9 0
- X\_6,8,4 -X\_6,8,5 0
- X\_6,8,4 -X\_6,8,6 0
- X\_6,8,4 -X\_6,8,7 0
- X\_6,8,4 -X\_6,8,8 0
- X\_6,8,4 -X\_6,8,9 0
- X\_6,8,5 -X\_6,8,6 0
- X\_6,8,5 -X\_6,8,7 0
- X\_6,8,5 -X\_6,8,8 0
- X\_6,8,5 -X\_6,8,9 0
- X\_6,8,6 -X\_6,8,7 0
- X\_6,8,6 -X\_6,8,8 0
- X\_6,8,6 -X\_6,8,9 0
- X\_6,8,7 -X\_6,8,8 0
- X\_6,8,7 -X\_6,8,9 0
- X\_6,8,8 -X\_6,8,9 0
- X\_6,9,1 -X\_6,9,2 0
- X\_6,9,1 -X\_6,9,3 0
- X\_6,9,1 -X\_6,9,4 0
- X\_6,9,1 -X\_6,9,5 0
- X\_6,9,1 -X\_6,9,6 0
- X\_6,9,1 -X\_6,9,7 0
- X\_6,9,1 -X\_6,9,8 0
- X\_6,9,1 -X\_6,9,9 0
- X\_6,9,2 -X\_6,9,3 0
- X\_6,9,2 -X\_6,9,4 0
- X\_6,9,2 -X\_6,9,5 0
- X\_6,9,2 -X\_6,9,6 0
- X\_6,9,2 -X\_6,9,7 0
- X\_6,9,2 -X\_6,9,8 0
- X\_6,9,2 -X\_6,9,9 0
- X\_6,9,3 -X\_6,9,4 0
- X\_6,9,3 -X\_6,9,5 0
- X\_6,9,3 -X\_6,9,6 0
- X\_6,9,3 -X\_6,9,7 0
- X\_6,9,3 -X\_6,9,8 0
- X\_6,9,3 -X\_6,9,9 0
- X\_6,9,4 -X\_6,9,5 0
- X\_6,9,4 -X\_6,9,6 0
- X\_6,9,4 -X\_6,9,7 0
- X\_6,9,4 -X\_6,9,8 0
- X\_6,9,4 -X\_6,9,9 0
- X\_6,9,5 -X\_6,9,6 0
- X\_6,9,5 -X\_6,9,7 0
- X\_6,9,5 -X\_6,9,8 0
- X\_6,9,5 -X\_6,9,9 0
- X\_6,9,6 -X\_6,9,7 0
- X\_6,9,6 -X\_6,9,8 0
- X\_6,9,6 -X\_6,9,9 0
- X\_6,9,7 -X\_6,9,8 0
- X\_6,9,7 -X\_6,9,9 0
- X\_6,9,8 -X\_6,9,9 0
- X\_7,1,1 -X\_7,1,2 0
- X\_7,1,1 -X\_7,1,3 0
- X\_7,1,1 -X\_7,1,4 0
- X\_7,1,1 -X\_7,1,5 0
- X\_7,1,1 -X\_7,1,6 0
- X\_7,1,1 -X\_7,1,7 0
- X\_7,1,1 -X\_7,1,8 0
- X\_7,1,1 -X\_7,1,9 0
- X\_7,1,2 -X\_7,1,3 0
- X\_7,1,2 -X\_7,1,4 0
- X\_7,1,2 -X\_7,1,5 0
- X\_7,1,2 -X\_7,1,6 0
- X\_7,1,2 -X\_7,1,7 0
- X\_7,1,2 -X\_7,1,8 0
- X\_7,1,2 -X\_7,1,9 0
- X\_7,1,3 -X\_7,1,4 0
- X\_7,1,3 -X\_7,1,5 0
- X\_7,1,3 -X\_7,1,6 0
- X\_7,1,3 -X\_7,1,7 0
- X\_7,1,3 -X\_7,1,8 0
- X\_7,1,3 -X\_7,1,9 0
- X\_7,1,4 -X\_7,1,5 0
- X\_7,1,4 -X\_7,1,6 0
- X\_7,1,4 -X\_7,1,7 0
- X\_7,1,4 -X\_7,1,8 0
- X\_7,1,4 -X\_7,1,9 0
- X\_7,1,5 -X\_7,1,6 0
- X\_7,1,5 -X\_7,1,7 0
- X\_7,1,5 -X\_7,1,8 0
- X\_7,1,5 -X\_7,1,9 0
- X\_7,1,6 -X\_7,1,7 0
- X\_7,1,6 -X\_7,1,8 0
- X\_7,1,6 -X\_7,1,9 0
- X\_7,1,7 -X\_7,1,8 0
- X\_7,1,7 -X\_7,1,9 0
- X\_7,1,8 -X\_7,1,9 0
- X\_7,2,1 -X\_7,2,2 0
- X\_7,2,1 -X\_7,2,3 0
- X\_7,2,1 -X\_7,2,4 0
- X\_7,2,1 -X\_7,2,5 0
- X\_7,2,1 -X\_7,2,6 0
- X\_7,2,1 -X\_7,2,7 0
- X\_7,2,1 -X\_7,2,8 0
- X\_7,2,1 -X\_7,2,9 0
- X\_7,2,2 -X\_7,2,3 0
- X\_7,2,2 -X\_7,2,4 0
- X\_7,2,2 -X\_7,2,5 0
- X\_7,2,2 -X\_7,2,6 0
- X\_7,2,2 -X\_7,2,7 0
- X\_7,2,2 -X\_7,2,8 0
- X\_7,2,2 -X\_7,2,9 0
- X\_7,2,3 -X\_7,2,4 0
- X\_7,2,3 -X\_7,2,5 0
- X\_7,2,3 -X\_7,2,6 0
- X\_7,2,3 -X\_7,2,7 0
- X\_7,2,3 -X\_7,2,8 0
- X\_7,2,3 -X\_7,2,9 0
- X\_7,2,4 -X\_7,2,5 0
- X\_7,2,4 -X\_7,2,6 0
- X\_7,2,4 -X\_7,2,7 0
- X\_7,2,4 -X\_7,2,8 0
- X\_7,2,4 -X\_7,2,9 0
- X\_7,2,5 -X\_7,2,6 0
- X\_7,2,5 -X\_7,2,7 0
- X\_7,2,5 -X\_7,2,8 0
- X\_7,2,5 -X\_7,2,9 0
- X\_7,2,6 -X\_7,2,7 0
- X\_7,2,6 -X\_7,2,8 0
- X\_7,2,6 -X\_7,2,9 0
- X\_7,2,7 -X\_7,2,8 0
- X\_7,2,7 -X\_7,2,9 0
- X\_7,2,8 -X\_7,2,9 0
- X\_7,3,1 -X\_7,3,2 0
- X\_7,3,1 -X\_7,3,3 0
- X\_7,3,1 -X\_7,3,4 0
- X\_7,3,1 -X\_7,3,5 0
- X\_7,3,1 -X\_7,3,6 0
- X\_7,3,1 -X\_7,3,7 0
- X\_7,3,1 -X\_7,3,8 0
- X\_7,3,1 -X\_7,3,9 0
- X\_7,3,2 -X\_7,3,3 0
- X\_7,3,2 -X\_7,3,4 0
- X\_7,3,2 -X\_7,3,5 0
- X\_7,3,2 -X\_7,3,6 0
- X\_7,3,2 -X\_7,3,7 0
- X\_7,3,2 -X\_7,3,8 0
- X\_7,3,2 -X\_7,3,9 0
- X\_7,3,3 -X\_7,3,4 0
- X\_7,3,3 -X\_7,3,5 0
- X\_7,3,3 -X\_7,3,6 0
- X\_7,3,3 -X\_7,3,7 0
- X\_7,3,3 -X\_7,3,8 0
- X\_7,3,3 -X\_7,3,9 0
- X\_7,3,4 -X\_7,3,5 0
- X\_7,3,4 -X\_7,3,6 0
- X\_7,3,4 -X\_7,3,7 0
- X\_7,3,4 -X\_7,3,8 0
- X\_7,3,4 -X\_7,3,9 0
- X\_7,3,5 -X\_7,3,6 0
- X\_7,3,5 -X\_7,3,7 0
- X\_7,3,5 -X\_7,3,8 0
- X\_7,3,5 -X\_7,3,9 0
- X\_7,3,6 -X\_7,3,7 0
- X\_7,3,6 -X\_7,3,8 0
- X\_7,3,6 -X\_7,3,9 0
- X\_7,3,7 -X\_7,3,8 0
- X\_7,3,7 -X\_7,3,9 0
- X\_7,3,8 -X\_7,3,9 0
- X\_7,4,1 -X\_7,4,2 0
- X\_7,4,1 -X\_7,4,3 0
- X\_7,4,1 -X\_7,4,4 0
- X\_7,4,1 -X\_7,4,5 0
- X\_7,4,1 -X\_7,4,6 0
- X\_7,4,1 -X\_7,4,7 0
- X\_7,4,1 -X\_7,4,8 0
- X\_7,4,1 -X\_7,4,9 0
- X\_7,4,2 -X\_7,4,3 0
- X\_7,4,2 -X\_7,4,4 0
- X\_7,4,2 -X\_7,4,5 0
- X\_7,4,2 -X\_7,4,6 0
- X\_7,4,2 -X\_7,4,7 0
- X\_7,4,2 -X\_7,4,8 0
- X\_7,4,2 -X\_7,4,9 0
- X\_7,4,3 -X\_7,4,4 0
- X\_7,4,3 -X\_7,4,5 0
- X\_7,4,3 -X\_7,4,6 0
- X\_7,4,3 -X\_7,4,7 0
- X\_7,4,3 -X\_7,4,8 0
- X\_7,4,3 -X\_7,4,9 0
- X\_7,4,4 -X\_7,4,5 0
- X\_7,4,4 -X\_7,4,6 0
- X\_7,4,4 -X\_7,4,7 0
- X\_7,4,4 -X\_7,4,8 0
- X\_7,4,4 -X\_7,4,9 0
- X\_7,4,5 -X\_7,4,6 0
- X\_7,4,5 -X\_7,4,7 0
- X\_7,4,5 -X\_7,4,8 0
- X\_7,4,5 -X\_7,4,9 0
- X\_7,4,6 -X\_7,4,7 0
- X\_7,4,6 -X\_7,4,8 0
- X\_7,4,6 -X\_7,4,9 0
- X\_7,4,7 -X\_7,4,8 0
- X\_7,4,7 -X\_7,4,9 0
- X\_7,4,8 -X\_7,4,9 0
- X\_7,5,1 -X\_7,5,2 0
- X\_7,5,1 -X\_7,5,3 0
- X\_7,5,1 -X\_7,5,4 0
- X\_7,5,1 -X\_7,5,5 0
- X\_7,5,1 -X\_7,5,6 0
- X\_7,5,1 -X\_7,5,7 0
- X\_7,5,1 -X\_7,5,8 0
- X\_7,5,1 -X\_7,5,9 0
- X\_7,5,2 -X\_7,5,3 0
- X\_7,5,2 -X\_7,5,4 0
- X\_7,5,2 -X\_7,5,5 0
- X\_7,5,2 -X\_7,5,6 0
- X\_7,5,2 -X\_7,5,7 0
- X\_7,5,2 -X\_7,5,8 0
- X\_7,5,2 -X\_7,5,9 0
- X\_7,5,3 -X\_7,5,4 0
- X\_7,5,3 -X\_7,5,5 0
- X\_7,5,3 -X\_7,5,6 0
- X\_7,5,3 -X\_7,5,7 0
- X\_7,5,3 -X\_7,5,8 0
- X\_7,5,3 -X\_7,5,9 0
- X\_7,5,4 -X\_7,5,5 0
- X\_7,5,4 -X\_7,5,6 0
- X\_7,5,4 -X\_7,5,7 0
- X\_7,5,4 -X\_7,5,8 0
- X\_7,5,4 -X\_7,5,9 0
- X\_7,5,5 -X\_7,5,6 0
- X\_7,5,5 -X\_7,5,7 0
- X\_7,5,5 -X\_7,5,8 0
- X\_7,5,5 -X\_7,5,9 0
- X\_7,5,6 -X\_7,5,7 0
- X\_7,5,6 -X\_7,5,8 0
- X\_7,5,6 -X\_7,5,9 0
- X\_7,5,7 -X\_7,5,8 0
- X\_7,5,7 -X\_7,5,9 0
- X\_7,5,8 -X\_7,5,9 0
- X\_7,6,1 -X\_7,6,2 0
- X\_7,6,1 -X\_7,6,3 0
- X\_7,6,1 -X\_7,6,4 0
- X\_7,6,1 -X\_7,6,5 0
- X\_7,6,1 -X\_7,6,6 0
- X\_7,6,1 -X\_7,6,7 0
- X\_7,6,1 -X\_7,6,8 0
- X\_7,6,1 -X\_7,6,9 0
- X\_7,6,2 -X\_7,6,3 0
- X\_7,6,2 -X\_7,6,4 0
- X\_7,6,2 -X\_7,6,5 0
- X\_7,6,2 -X\_7,6,6 0
- X\_7,6,2 -X\_7,6,7 0
- X\_7,6,2 -X\_7,6,8 0
- X\_7,6,2 -X\_7,6,9 0
- X\_7,6,3 -X\_7,6,4 0
- X\_7,6,3 -X\_7,6,5 0
- X\_7,6,3 -X\_7,6,6 0
- X\_7,6,3 -X\_7,6,7 0
- X\_7,6,3 -X\_7,6,8 0
- X\_7,6,3 -X\_7,6,9 0
- X\_7,6,4 -X\_7,6,5 0
- X\_7,6,4 -X\_7,6,6 0
- X\_7,6,4 -X\_7,6,7 0
- X\_7,6,4 -X\_7,6,8 0
- X\_7,6,4 -X\_7,6,9 0
- X\_7,6,5 -X\_7,6,6 0
- X\_7,6,5 -X\_7,6,7 0
- X\_7,6,5 -X\_7,6,8 0
- X\_7,6,5 -X\_7,6,9 0
- X\_7,6,6 -X\_7,6,7 0
- X\_7,6,6 -X\_7,6,8 0
- X\_7,6,6 -X\_7,6,9 0
- X\_7,6,7 -X\_7,6,8 0
- X\_7,6,7 -X\_7,6,9 0
- X\_7,6,8 -X\_7,6,9 0
- X\_7,7,1 -X\_7,7,2 0
- X\_7,7,1 -X\_7,7,3 0
- X\_7,7,1 -X\_7,7,4 0
- X\_7,7,1 -X\_7,7,5 0
- X\_7,7,1 -X\_7,7,6 0
- X\_7,7,1 -X\_7,7,7 0
- X\_7,7,1 -X\_7,7,8 0
- X\_7,7,1 -X\_7,7,9 0
- X\_7,7,2 -X\_7,7,3 0
- X\_7,7,2 -X\_7,7,4 0
- X\_7,7,2 -X\_7,7,5 0
- X\_7,7,2 -X\_7,7,6 0
- X\_7,7,2 -X\_7,7,7 0
- X\_7,7,2 -X\_7,7,8 0
- X\_7,7,2 -X\_7,7,9 0
- X\_7,7,3 -X\_7,7,4 0
- X\_7,7,3 -X\_7,7,5 0
- X\_7,7,3 -X\_7,7,6 0
- X\_7,7,3 -X\_7,7,7 0
- X\_7,7,3 -X\_7,7,8 0
- X\_7,7,3 -X\_7,7,9 0
- X\_7,7,4 -X\_7,7,5 0
- X\_7,7,4 -X\_7,7,6 0
- X\_7,7,4 -X\_7,7,7 0
- X\_7,7,4 -X\_7,7,8 0
- X\_7,7,4 -X\_7,7,9 0
- X\_7,7,5 -X\_7,7,6 0
- X\_7,7,5 -X\_7,7,7 0
- X\_7,7,5 -X\_7,7,8 0
- X\_7,7,5 -X\_7,7,9 0
- X\_7,7,6 -X\_7,7,7 0
- X\_7,7,6 -X\_7,7,8 0
- X\_7,7,6 -X\_7,7,9 0
- X\_7,7,7 -X\_7,7,8 0
- X\_7,7,7 -X\_7,7,9 0
- X\_7,7,8 -X\_7,7,9 0
- X\_7,8,1 -X\_7,8,2 0
- X\_7,8,1 -X\_7,8,3 0
- X\_7,8,1 -X\_7,8,4 0
- X\_7,8,1 -X\_7,8,5 0
- X\_7,8,1 -X\_7,8,6 0
- X\_7,8,1 -X\_7,8,7 0
- X\_7,8,1 -X\_7,8,8 0
- X\_7,8,1 -X\_7,8,9 0
- X\_7,8,2 -X\_7,8,3 0
- X\_7,8,2 -X\_7,8,4 0
- X\_7,8,2 -X\_7,8,5 0
- X\_7,8,2 -X\_7,8,6 0
- X\_7,8,2 -X\_7,8,7 0
- X\_7,8,2 -X\_7,8,8 0
- X\_7,8,2 -X\_7,8,9 0
- X\_7,8,3 -X\_7,8,4 0
- X\_7,8,3 -X\_7,8,5 0
- X\_7,8,3 -X\_7,8,6 0
- X\_7,8,3 -X\_7,8,7 0
- X\_7,8,3 -X\_7,8,8 0
- X\_7,8,3 -X\_7,8,9 0
- X\_7,8,4 -X\_7,8,5 0
- X\_7,8,4 -X\_7,8,6 0
- X\_7,8,4 -X\_7,8,7 0
- X\_7,8,4 -X\_7,8,8 0
- X\_7,8,4 -X\_7,8,9 0
- X\_7,8,5 -X\_7,8,6 0
- X\_7,8,5 -X\_7,8,7 0
- X\_7,8,5 -X\_7,8,8 0
- X\_7,8,5 -X\_7,8,9 0
- X\_7,8,6 -X\_7,8,7 0
- X\_7,8,6 -X\_7,8,8 0
- X\_7,8,6 -X\_7,8,9 0
- X\_7,8,7 -X\_7,8,8 0
- X\_7,8,7 -X\_7,8,9 0
- X\_7,8,8 -X\_7,8,9 0
- X\_7,9,1 -X\_7,9,2 0
- X\_7,9,1 -X\_7,9,3 0
- X\_7,9,1 -X\_7,9,4 0
- X\_7,9,1 -X\_7,9,5 0
- X\_7,9,1 -X\_7,9,6 0
- X\_7,9,1 -X\_7,9,7 0
- X\_7,9,1 -X\_7,9,8 0
- X\_7,9,1 -X\_7,9,9 0
- X\_7,9,2 -X\_7,9,3 0
- X\_7,9,2 -X\_7,9,4 0
- X\_7,9,2 -X\_7,9,5 0
- X\_7,9,2 -X\_7,9,6 0
- X\_7,9,2 -X\_7,9,7 0
- X\_7,9,2 -X\_7,9,8 0
- X\_7,9,2 -X\_7,9,9 0
- X\_7,9,3 -X\_7,9,4 0
- X\_7,9,3 -X\_7,9,5 0
- X\_7,9,3 -X\_7,9,6 0
- X\_7,9,3 -X\_7,9,7 0
- X\_7,9,3 -X\_7,9,8 0
- X\_7,9,3 -X\_7,9,9 0
- X\_7,9,4 -X\_7,9,5 0
- X\_7,9,4 -X\_7,9,6 0
- X\_7,9,4 -X\_7,9,7 0
- X\_7,9,4 -X\_7,9,8 0
- X\_7,9,4 -X\_7,9,9 0
- X\_7,9,5 -X\_7,9,6 0
- X\_7,9,5 -X\_7,9,7 0
- X\_7,9,5 -X\_7,9,8 0
- X\_7,9,5 -X\_7,9,9 0
- X\_7,9,6 -X\_7,9,7 0
- X\_7,9,6 -X\_7,9,8 0
- X\_7,9,6 -X\_7,9,9 0
- X\_7,9,7 -X\_7,9,8 0
- X\_7,9,7 -X\_7,9,9 0
- X\_7,9,8 -X\_7,9,9 0
- X\_8,1,1 -X\_8,1,2 0
- X\_8,1,1 -X\_8,1,3 0
- X\_8,1,1 -X\_8,1,4 0
- X\_8,1,1 -X\_8,1,5 0
- X\_8,1,1 -X\_8,1,6 0
- X\_8,1,1 -X\_8,1,7 0
- X\_8,1,1 -X\_8,1,8 0
- X\_8,1,1 -X\_8,1,9 0
- X\_8,1,2 -X\_8,1,3 0
- X\_8,1,2 -X\_8,1,4 0
- X\_8,1,2 -X\_8,1,5 0
- X\_8,1,2 -X\_8,1,6 0
- X\_8,1,2 -X\_8,1,7 0
- X\_8,1,2 -X\_8,1,8 0
- X\_8,1,2 -X\_8,1,9 0
- X\_8,1,3 -X\_8,1,4 0
- X\_8,1,3 -X\_8,1,5 0
- X\_8,1,3 -X\_8,1,6 0
- X\_8,1,3 -X\_8,1,7 0
- X\_8,1,3 -X\_8,1,8 0
- X\_8,1,3 -X\_8,1,9 0
- X\_8,1,4 -X\_8,1,5 0
- X\_8,1,4 -X\_8,1,6 0
- X\_8,1,4 -X\_8,1,7 0
- X\_8,1,4 -X\_8,1,8 0
- X\_8,1,4 -X\_8,1,9 0
- X\_8,1,5 -X\_8,1,6 0
- X\_8,1,5 -X\_8,1,7 0
- X\_8,1,5 -X\_8,1,8 0
- X\_8,1,5 -X\_8,1,9 0
- X\_8,1,6 -X\_8,1,7 0
- X\_8,1,6 -X\_8,1,8 0
- X\_8,1,6 -X\_8,1,9 0
- X\_8,1,7 -X\_8,1,8 0
- X\_8,1,7 -X\_8,1,9 0
- X\_8,1,8 -X\_8,1,9 0
- X\_8,2,1 -X\_8,2,2 0
- X\_8,2,1 -X\_8,2,3 0
- X\_8,2,1 -X\_8,2,4 0
- X\_8,2,1 -X\_8,2,5 0
- X\_8,2,1 -X\_8,2,6 0
- X\_8,2,1 -X\_8,2,7 0
- X\_8,2,1 -X\_8,2,8 0
- X\_8,2,1 -X\_8,2,9 0
- X\_8,2,2 -X\_8,2,3 0
- X\_8,2,2 -X\_8,2,4 0
- X\_8,2,2 -X\_8,2,5 0
- X\_8,2,2 -X\_8,2,6 0
- X\_8,2,2 -X\_8,2,7 0
- X\_8,2,2 -X\_8,2,8 0
- X\_8,2,2 -X\_8,2,9 0
- X\_8,2,3 -X\_8,2,4 0
- X\_8,2,3 -X\_8,2,5 0
- X\_8,2,3 -X\_8,2,6 0
- X\_8,2,3 -X\_8,2,7 0
- X\_8,2,3 -X\_8,2,8 0
- X\_8,2,3 -X\_8,2,9 0
- X\_8,2,4 -X\_8,2,5 0
- X\_8,2,4 -X\_8,2,6 0
- X\_8,2,4 -X\_8,2,7 0
- X\_8,2,4 -X\_8,2,8 0
- X\_8,2,4 -X\_8,2,9 0
- X\_8,2,5 -X\_8,2,6 0
- X\_8,2,5 -X\_8,2,7 0
- X\_8,2,5 -X\_8,2,8 0
- X\_8,2,5 -X\_8,2,9 0
- X\_8,2,6 -X\_8,2,7 0
- X\_8,2,6 -X\_8,2,8 0
- X\_8,2,6 -X\_8,2,9 0
- X\_8,2,7 -X\_8,2,8 0
- X\_8,2,7 -X\_8,2,9 0
- X\_8,2,8 -X\_8,2,9 0
- X\_8,3,1 -X\_8,3,2 0
- X\_8,3,1 -X\_8,3,3 0
- X\_8,3,1 -X\_8,3,4 0
- X\_8,3,1 -X\_8,3,5 0
- X\_8,3,1 -X\_8,3,6 0
- X\_8,3,1 -X\_8,3,7 0
- X\_8,3,1 -X\_8,3,8 0
- X\_8,3,1 -X\_8,3,9 0
- X\_8,3,2 -X\_8,3,3 0
- X\_8,3,2 -X\_8,3,4 0
- X\_8,3,2 -X\_8,3,5 0
- X\_8,3,2 -X\_8,3,6 0
- X\_8,3,2 -X\_8,3,7 0
- X\_8,3,2 -X\_8,3,8 0
- X\_8,3,2 -X\_8,3,9 0
- X\_8,3,3 -X\_8,3,4 0
- X\_8,3,3 -X\_8,3,5 0
- X\_8,3,3 -X\_8,3,6 0
- X\_8,3,3 -X\_8,3,7 0
- X\_8,3,3 -X\_8,3,8 0
- X\_8,3,3 -X\_8,3,9 0
- X\_8,3,4 -X\_8,3,5 0
- X\_8,3,4 -X\_8,3,6 0
- X\_8,3,4 -X\_8,3,7 0
- X\_8,3,4 -X\_8,3,8 0
- X\_8,3,4 -X\_8,3,9 0
- X\_8,3,5 -X\_8,3,6 0
- X\_8,3,5 -X\_8,3,7 0
- X\_8,3,5 -X\_8,3,8 0
- X\_8,3,5 -X\_8,3,9 0
- X\_8,3,6 -X\_8,3,7 0
- X\_8,3,6 -X\_8,3,8 0
- X\_8,3,6 -X\_8,3,9 0
- X\_8,3,7 -X\_8,3,8 0
- X\_8,3,7 -X\_8,3,9 0
- X\_8,3,8 -X\_8,3,9 0
- X\_8,4,1 -X\_8,4,2 0
- X\_8,4,1 -X\_8,4,3 0
- X\_8,4,1 -X\_8,4,4 0
- X\_8,4,1 -X\_8,4,5 0
- X\_8,4,1 -X\_8,4,6 0
- X\_8,4,1 -X\_8,4,7 0
- X\_8,4,1 -X\_8,4,8 0
- X\_8,4,1 -X\_8,4,9 0
- X\_8,4,2 -X\_8,4,3 0
- X\_8,4,2 -X\_8,4,4 0
- X\_8,4,2 -X\_8,4,5 0
- X\_8,4,2 -X\_8,4,6 0
- X\_8,4,2 -X\_8,4,7 0
- X\_8,4,2 -X\_8,4,8 0
- X\_8,4,2 -X\_8,4,9 0
- X\_8,4,3 -X\_8,4,4 0
- X\_8,4,3 -X\_8,4,5 0
- X\_8,4,3 -X\_8,4,6 0
- X\_8,4,3 -X\_8,4,7 0
- X\_8,4,3 -X\_8,4,8 0
- X\_8,4,3 -X\_8,4,9 0
- X\_8,4,4 -X\_8,4,5 0
- X\_8,4,4 -X\_8,4,6 0
- X\_8,4,4 -X\_8,4,7 0
- X\_8,4,4 -X\_8,4,8 0
- X\_8,4,4 -X\_8,4,9 0
- X\_8,4,5 -X\_8,4,6 0
- X\_8,4,5 -X\_8,4,7 0
- X\_8,4,5 -X\_8,4,8 0
- X\_8,4,5 -X\_8,4,9 0
- X\_8,4,6 -X\_8,4,7 0
- X\_8,4,6 -X\_8,4,8 0
- X\_8,4,6 -X\_8,4,9 0
- X\_8,4,7 -X\_8,4,8 0
- X\_8,4,7 -X\_8,4,9 0
- X\_8,4,8 -X\_8,4,9 0
- X\_8,5,1 -X\_8,5,2 0
- X\_8,5,1 -X\_8,5,3 0
- X\_8,5,1 -X\_8,5,4 0
- X\_8,5,1 -X\_8,5,5 0
- X\_8,5,1 -X\_8,5,6 0
- X\_8,5,1 -X\_8,5,7 0
- X\_8,5,1 -X\_8,5,8 0
- X\_8,5,1 -X\_8,5,9 0
- X\_8,5,2 -X\_8,5,3 0
- X\_8,5,2 -X\_8,5,4 0
- X\_8,5,2 -X\_8,5,5 0
- X\_8,5,2 -X\_8,5,6 0
- X\_8,5,2 -X\_8,5,7 0
- X\_8,5,2 -X\_8,5,8 0
- X\_8,5,2 -X\_8,5,9 0
- X\_8,5,3 -X\_8,5,4 0
- X\_8,5,3 -X\_8,5,5 0
- X\_8,5,3 -X\_8,5,6 0
- X\_8,5,3 -X\_8,5,7 0
- X\_8,5,3 -X\_8,5,8 0
- X\_8,5,3 -X\_8,5,9 0
- X\_8,5,4 -X\_8,5,5 0
- X\_8,5,4 -X\_8,5,6 0
- X\_8,5,4 -X\_8,5,7 0
- X\_8,5,4 -X\_8,5,8 0
- X\_8,5,4 -X\_8,5,9 0
- X\_8,5,5 -X\_8,5,6 0
- X\_8,5,5 -X\_8,5,7 0
- X\_8,5,5 -X\_8,5,8 0
- X\_8,5,5 -X\_8,5,9 0
- X\_8,5,6 -X\_8,5,7 0
- X\_8,5,6 -X\_8,5,8 0
- X\_8,5,6 -X\_8,5,9 0
- X\_8,5,7 -X\_8,5,8 0
- X\_8,5,7 -X\_8,5,9 0
- X\_8,5,8 -X\_8,5,9 0
- X\_8,6,1 -X\_8,6,2 0
- X\_8,6,1 -X\_8,6,3 0
- X\_8,6,1 -X\_8,6,4 0
- X\_8,6,1 -X\_8,6,5 0
- X\_8,6,1 -X\_8,6,6 0
- X\_8,6,1 -X\_8,6,7 0
- X\_8,6,1 -X\_8,6,8 0
- X\_8,6,1 -X\_8,6,9 0
- X\_8,6,2 -X\_8,6,3 0
- X\_8,6,2 -X\_8,6,4 0
- X\_8,6,2 -X\_8,6,5 0
- X\_8,6,2 -X\_8,6,6 0
- X\_8,6,2 -X\_8,6,7 0
- X\_8,6,2 -X\_8,6,8 0
- X\_8,6,2 -X\_8,6,9 0
- X\_8,6,3 -X\_8,6,4 0
- X\_8,6,3 -X\_8,6,5 0
- X\_8,6,3 -X\_8,6,6 0
- X\_8,6,3 -X\_8,6,7 0
- X\_8,6,3 -X\_8,6,8 0
- X\_8,6,3 -X\_8,6,9 0
- X\_8,6,4 -X\_8,6,5 0
- X\_8,6,4 -X\_8,6,6 0
- X\_8,6,4 -X\_8,6,7 0
- X\_8,6,4 -X\_8,6,8 0
- X\_8,6,4 -X\_8,6,9 0
- X\_8,6,5 -X\_8,6,6 0
- X\_8,6,5 -X\_8,6,7 0
- X\_8,6,5 -X\_8,6,8 0
- X\_8,6,5 -X\_8,6,9 0
- X\_8,6,6 -X\_8,6,7 0
- X\_8,6,6 -X\_8,6,8 0
- X\_8,6,6 -X\_8,6,9 0
- X\_8,6,7 -X\_8,6,8 0
- X\_8,6,7 -X\_8,6,9 0
- X\_8,6,8 -X\_8,6,9 0
- X\_8,7,1 -X\_8,7,2 0
- X\_8,7,1 -X\_8,7,3 0
- X\_8,7,1 -X\_8,7,4 0
- X\_8,7,1 -X\_8,7,5 0
- X\_8,7,1 -X\_8,7,6 0
- X\_8,7,1 -X\_8,7,7 0
- X\_8,7,1 -X\_8,7,8 0
- X\_8,7,1 -X\_8,7,9 0
- X\_8,7,2 -X\_8,7,3 0
- X\_8,7,2 -X\_8,7,4 0
- X\_8,7,2 -X\_8,7,5 0
- X\_8,7,2 -X\_8,7,6 0
- X\_8,7,2 -X\_8,7,7 0
- X\_8,7,2 -X\_8,7,8 0
- X\_8,7,2 -X\_8,7,9 0
- X\_8,7,3 -X\_8,7,4 0
- X\_8,7,3 -X\_8,7,5 0
- X\_8,7,3 -X\_8,7,6 0
- X\_8,7,3 -X\_8,7,7 0
- X\_8,7,3 -X\_8,7,8 0
- X\_8,7,3 -X\_8,7,9 0
- X\_8,7,4 -X\_8,7,5 0
- X\_8,7,4 -X\_8,7,6 0
- X\_8,7,4 -X\_8,7,7 0
- X\_8,7,4 -X\_8,7,8 0
- X\_8,7,4 -X\_8,7,9 0
- X\_8,7,5 -X\_8,7,6 0
- X\_8,7,5 -X\_8,7,7 0
- X\_8,7,5 -X\_8,7,8 0
- X\_8,7,5 -X\_8,7,9 0
- X\_8,7,6 -X\_8,7,7 0
- X\_8,7,6 -X\_8,7,8 0
- X\_8,7,6 -X\_8,7,9 0
- X\_8,7,7 -X\_8,7,8 0
- X\_8,7,7 -X\_8,7,9 0
- X\_8,7,8 -X\_8,7,9 0
- X\_8,8,1 -X\_8,8,2 0
- X\_8,8,1 -X\_8,8,3 0
- X\_8,8,1 -X\_8,8,4 0
- X\_8,8,1 -X\_8,8,5 0
- X\_8,8,1 -X\_8,8,6 0
- X\_8,8,1 -X\_8,8,7 0
- X\_8,8,1 -X\_8,8,8 0
- X\_8,8,1 -X\_8,8,9 0
- X\_8,8,2 -X\_8,8,3 0
- X\_8,8,2 -X\_8,8,4 0
- X\_8,8,2 -X\_8,8,5 0
- X\_8,8,2 -X\_8,8,6 0
- X\_8,8,2 -X\_8,8,7 0
- X\_8,8,2 -X\_8,8,8 0
- X\_8,8,2 -X\_8,8,9 0
- X\_8,8,3 -X\_8,8,4 0
- X\_8,8,3 -X\_8,8,5 0
- X\_8,8,3 -X\_8,8,6 0
- X\_8,8,3 -X\_8,8,7 0
- X\_8,8,3 -X\_8,8,8 0
- X\_8,8,3 -X\_8,8,9 0
- X\_8,8,4 -X\_8,8,5 0
- X\_8,8,4 -X\_8,8,6 0
- X\_8,8,4 -X\_8,8,7 0
- X\_8,8,4 -X\_8,8,8 0
- X\_8,8,4 -X\_8,8,9 0
- X\_8,8,5 -X\_8,8,6 0
- X\_8,8,5 -X\_8,8,7 0
- X\_8,8,5 -X\_8,8,8 0
- X\_8,8,5 -X\_8,8,9 0
- X\_8,8,6 -X\_8,8,7 0
- X\_8,8,6 -X\_8,8,8 0
- X\_8,8,6 -X\_8,8,9 0
- X\_8,8,7 -X\_8,8,8 0
- X\_8,8,7 -X\_8,8,9 0
- X\_8,8,8 -X\_8,8,9 0
- X\_8,9,1 -X\_8,9,2 0
- X\_8,9,1 -X\_8,9,3 0
- X\_8,9,1 -X\_8,9,4 0
- X\_8,9,1 -X\_8,9,5 0
- X\_8,9,1 -X\_8,9,6 0
- X\_8,9,1 -X\_8,9,7 0
- X\_8,9,1 -X\_8,9,8 0
- X\_8,9,1 -X\_8,9,9 0
- X\_8,9,2 -X\_8,9,3 0
- X\_8,9,2 -X\_8,9,4 0
- X\_8,9,2 -X\_8,9,5 0
- X\_8,9,2 -X\_8,9,6 0
- X\_8,9,2 -X\_8,9,7 0
- X\_8,9,2 -X\_8,9,8 0
- X\_8,9,2 -X\_8,9,9 0
- X\_8,9,3 -X\_8,9,4 0
- X\_8,9,3 -X\_8,9,5 0
- X\_8,9,3 -X\_8,9,6 0
- X\_8,9,3 -X\_8,9,7 0
- X\_8,9,3 -X\_8,9,8 0
- X\_8,9,3 -X\_8,9,9 0
- X\_8,9,4 -X\_8,9,5 0
- X\_8,9,4 -X\_8,9,6 0
- X\_8,9,4 -X\_8,9,7 0
- X\_8,9,4 -X\_8,9,8 0
- X\_8,9,4 -X\_8,9,9 0
- X\_8,9,5 -X\_8,9,6 0
- X\_8,9,5 -X\_8,9,7 0
- X\_8,9,5 -X\_8,9,8 0
- X\_8,9,5 -X\_8,9,9 0
- X\_8,9,6 -X\_8,9,7 0
- X\_8,9,6 -X\_8,9,8 0
- X\_8,9,6 -X\_8,9,9 0
- X\_8,9,7 -X\_8,9,8 0
- X\_8,9,7 -X\_8,9,9 0
- X\_8,9,8 -X\_8,9,9 0
- X\_9,1,1 -X\_9,1,2 0
- X\_9,1,1 -X\_9,1,3 0
- X\_9,1,1 -X\_9,1,4 0
- X\_9,1,1 -X\_9,1,5 0
- X\_9,1,1 -X\_9,1,6 0
- X\_9,1,1 -X\_9,1,7 0
- X\_9,1,1 -X\_9,1,8 0
- X\_9,1,1 -X\_9,1,9 0
- X\_9,1,2 -X\_9,1,3 0
- X\_9,1,2 -X\_9,1,4 0
- X\_9,1,2 -X\_9,1,5 0
- X\_9,1,2 -X\_9,1,6 0
- X\_9,1,2 -X\_9,1,7 0
- X\_9,1,2 -X\_9,1,8 0
- X\_9,1,2 -X\_9,1,9 0
- X\_9,1,3 -X\_9,1,4 0
- X\_9,1,3 -X\_9,1,5 0
- X\_9,1,3 -X\_9,1,6 0
- X\_9,1,3 -X\_9,1,7 0
- X\_9,1,3 -X\_9,1,8 0
- X\_9,1,3 -X\_9,1,9 0
- X\_9,1,4 -X\_9,1,5 0
- X\_9,1,4 -X\_9,1,6 0
- X\_9,1,4 -X\_9,1,7 0
- X\_9,1,4 -X\_9,1,8 0
- X\_9,1,4 -X\_9,1,9 0
- X\_9,1,5 -X\_9,1,6 0
- X\_9,1,5 -X\_9,1,7 0
- X\_9,1,5 -X\_9,1,8 0
- X\_9,1,5 -X\_9,1,9 0
- X\_9,1,6 -X\_9,1,7 0
- X\_9,1,6 -X\_9,1,8 0
- X\_9,1,6 -X\_9,1,9 0
- X\_9,1,7 -X\_9,1,8 0
- X\_9,1,7 -X\_9,1,9 0
- X\_9,1,8 -X\_9,1,9 0
- X\_9,2,1 -X\_9,2,2 0
- X\_9,2,1 -X\_9,2,3 0
- X\_9,2,1 -X\_9,2,4 0
- X\_9,2,1 -X\_9,2,5 0
- X\_9,2,1 -X\_9,2,6 0
- X\_9,2,1 -X\_9,2,7 0
- X\_9,2,1 -X\_9,2,8 0
- X\_9,2,1 -X\_9,2,9 0
- X\_9,2,2 -X\_9,2,3 0
- X\_9,2,2 -X\_9,2,4 0
- X\_9,2,2 -X\_9,2,5 0
- X\_9,2,2 -X\_9,2,6 0
- X\_9,2,2 -X\_9,2,7 0
- X\_9,2,2 -X\_9,2,8 0
- X\_9,2,2 -X\_9,2,9 0
- X\_9,2,3 -X\_9,2,4 0
- X\_9,2,3 -X\_9,2,5 0
- X\_9,2,3 -X\_9,2,6 0
- X\_9,2,3 -X\_9,2,7 0
- X\_9,2,3 -X\_9,2,8 0
- X\_9,2,3 -X\_9,2,9 0
- X\_9,2,4 -X\_9,2,5 0
- X\_9,2,4 -X\_9,2,6 0
- X\_9,2,4 -X\_9,2,7 0
- X\_9,2,4 -X\_9,2,8 0
- X\_9,2,4 -X\_9,2,9 0
- X\_9,2,5 -X\_9,2,6 0
- X\_9,2,5 -X\_9,2,7 0
- X\_9,2,5 -X\_9,2,8 0
- X\_9,2,5 -X\_9,2,9 0
- X\_9,2,6 -X\_9,2,7 0
- X\_9,2,6 -X\_9,2,8 0
- X\_9,2,6 -X\_9,2,9 0
- X\_9,2,7 -X\_9,2,8 0
- X\_9,2,7 -X\_9,2,9 0
- X\_9,2,8 -X\_9,2,9 0
- X\_9,3,1 -X\_9,3,2 0
- X\_9,3,1 -X\_9,3,3 0
- X\_9,3,1 -X\_9,3,4 0
- X\_9,3,1 -X\_9,3,5 0
- X\_9,3,1 -X\_9,3,6 0
- X\_9,3,1 -X\_9,3,7 0
- X\_9,3,1 -X\_9,3,8 0
- X\_9,3,1 -X\_9,3,9 0
- X\_9,3,2 -X\_9,3,3 0
- X\_9,3,2 -X\_9,3,4 0
- X\_9,3,2 -X\_9,3,5 0
- X\_9,3,2 -X\_9,3,6 0
- X\_9,3,2 -X\_9,3,7 0
- X\_9,3,2 -X\_9,3,8 0
- X\_9,3,2 -X\_9,3,9 0
- X\_9,3,3 -X\_9,3,4 0
- X\_9,3,3 -X\_9,3,5 0
- X\_9,3,3 -X\_9,3,6 0
- X\_9,3,3 -X\_9,3,7 0
- X\_9,3,3 -X\_9,3,8 0
- X\_9,3,3 -X\_9,3,9 0
- X\_9,3,4 -X\_9,3,5 0
- X\_9,3,4 -X\_9,3,6 0
- X\_9,3,4 -X\_9,3,7 0
- X\_9,3,4 -X\_9,3,8 0
- X\_9,3,4 -X\_9,3,9 0
- X\_9,3,5 -X\_9,3,6 0
- X\_9,3,5 -X\_9,3,7 0
- X\_9,3,5 -X\_9,3,8 0
- X\_9,3,5 -X\_9,3,9 0
- X\_9,3,6 -X\_9,3,7 0
- X\_9,3,6 -X\_9,3,8 0
- X\_9,3,6 -X\_9,3,9 0
- X\_9,3,7 -X\_9,3,8 0
- X\_9,3,7 -X\_9,3,9 0
- X\_9,3,8 -X\_9,3,9 0
- X\_9,4,1 -X\_9,4,2 0
- X\_9,4,1 -X\_9,4,3 0
- X\_9,4,1 -X\_9,4,4 0
- X\_9,4,1 -X\_9,4,5 0
- X\_9,4,1 -X\_9,4,6 0
- X\_9,4,1 -X\_9,4,7 0
- X\_9,4,1 -X\_9,4,8 0
- X\_9,4,1 -X\_9,4,9 0
- X\_9,4,2 -X\_9,4,3 0
- X\_9,4,2 -X\_9,4,4 0
- X\_9,4,2 -X\_9,4,5 0
- X\_9,4,2 -X\_9,4,6 0
- X\_9,4,2 -X\_9,4,7 0
- X\_9,4,2 -X\_9,4,8 0
- X\_9,4,2 -X\_9,4,9 0
- X\_9,4,3 -X\_9,4,4 0
- X\_9,4,3 -X\_9,4,5 0
- X\_9,4,3 -X\_9,4,6 0
- X\_9,4,3 -X\_9,4,7 0
- X\_9,4,3 -X\_9,4,8 0
- X\_9,4,3 -X\_9,4,9 0
- X\_9,4,4 -X\_9,4,5 0
- X\_9,4,4 -X\_9,4,6 0
- X\_9,4,4 -X\_9,4,7 0
- X\_9,4,4 -X\_9,4,8 0
- X\_9,4,4 -X\_9,4,9 0
- X\_9,4,5 -X\_9,4,6 0
- X\_9,4,5 -X\_9,4,7 0
- X\_9,4,5 -X\_9,4,8 0
- X\_9,4,5 -X\_9,4,9 0
- X\_9,4,6 -X\_9,4,7 0
- X\_9,4,6 -X\_9,4,8 0
- X\_9,4,6 -X\_9,4,9 0
- X\_9,4,7 -X\_9,4,8 0
- X\_9,4,7 -X\_9,4,9 0
- X\_9,4,8 -X\_9,4,9 0
- X\_9,5,1 -X\_9,5,2 0
- X\_9,5,1 -X\_9,5,3 0
- X\_9,5,1 -X\_9,5,4 0
- X\_9,5,1 -X\_9,5,5 0
- X\_9,5,1 -X\_9,5,6 0
- X\_9,5,1 -X\_9,5,7 0
- X\_9,5,1 -X\_9,5,8 0
- X\_9,5,1 -X\_9,5,9 0
- X\_9,5,2 -X\_9,5,3 0
- X\_9,5,2 -X\_9,5,4 0
- X\_9,5,2 -X\_9,5,5 0
- X\_9,5,2 -X\_9,5,6 0
- X\_9,5,2 -X\_9,5,7 0
- X\_9,5,2 -X\_9,5,8 0
- X\_9,5,2 -X\_9,5,9 0
- X\_9,5,3 -X\_9,5,4 0
- X\_9,5,3 -X\_9,5,5 0
- X\_9,5,3 -X\_9,5,6 0
- X\_9,5,3 -X\_9,5,7 0
- X\_9,5,3 -X\_9,5,8 0
- X\_9,5,3 -X\_9,5,9 0
- X\_9,5,4 -X\_9,5,5 0
- X\_9,5,4 -X\_9,5,6 0
- X\_9,5,4 -X\_9,5,7 0
- X\_9,5,4 -X\_9,5,8 0
- X\_9,5,4 -X\_9,5,9 0
- X\_9,5,5 -X\_9,5,6 0
- X\_9,5,5 -X\_9,5,7 0
- X\_9,5,5 -X\_9,5,8 0
- X\_9,5,5 -X\_9,5,9 0
- X\_9,5,6 -X\_9,5,7 0
- X\_9,5,6 -X\_9,5,8 0
- X\_9,5,6 -X\_9,5,9 0
- X\_9,5,7 -X\_9,5,8 0
- X\_9,5,7 -X\_9,5,9 0
- X\_9,5,8 -X\_9,5,9 0
- X\_9,6,1 -X\_9,6,2 0
- X\_9,6,1 -X\_9,6,3 0
- X\_9,6,1 -X\_9,6,4 0
- X\_9,6,1 -X\_9,6,5 0
- X\_9,6,1 -X\_9,6,6 0
- X\_9,6,1 -X\_9,6,7 0
- X\_9,6,1 -X\_9,6,8 0
- X\_9,6,1 -X\_9,6,9 0
- X\_9,6,2 -X\_9,6,3 0
- X\_9,6,2 -X\_9,6,4 0
- X\_9,6,2 -X\_9,6,5 0
- X\_9,6,2 -X\_9,6,6 0
- X\_9,6,2 -X\_9,6,7 0
- X\_9,6,2 -X\_9,6,8 0
- X\_9,6,2 -X\_9,6,9 0
- X\_9,6,3 -X\_9,6,4 0
- X\_9,6,3 -X\_9,6,5 0
- X\_9,6,3 -X\_9,6,6 0
- X\_9,6,3 -X\_9,6,7 0
- X\_9,6,3 -X\_9,6,8 0
- X\_9,6,3 -X\_9,6,9 0
- X\_9,6,4 -X\_9,6,5 0
- X\_9,6,4 -X\_9,6,6 0
- X\_9,6,4 -X\_9,6,7 0
- X\_9,6,4 -X\_9,6,8 0
- X\_9,6,4 -X\_9,6,9 0
- X\_9,6,5 -X\_9,6,6 0
- X\_9,6,5 -X\_9,6,7 0
- X\_9,6,5 -X\_9,6,8 0
- X\_9,6,5 -X\_9,6,9 0
- X\_9,6,6 -X\_9,6,7 0
- X\_9,6,6 -X\_9,6,8 0
- X\_9,6,6 -X\_9,6,9 0
- X\_9,6,7 -X\_9,6,8 0
- X\_9,6,7 -X\_9,6,9 0
- X\_9,6,8 -X\_9,6,9 0
- X\_9,7,1 -X\_9,7,2 0
- X\_9,7,1 -X\_9,7,3 0
- X\_9,7,1 -X\_9,7,4 0
- X\_9,7,1 -X\_9,7,5 0
- X\_9,7,1 -X\_9,7,6 0
- X\_9,7,1 -X\_9,7,7 0
- X\_9,7,1 -X\_9,7,8 0
- X\_9,7,1 -X\_9,7,9 0
- X\_9,7,2 -X\_9,7,3 0
- X\_9,7,2 -X\_9,7,4 0
- X\_9,7,2 -X\_9,7,5 0
- X\_9,7,2 -X\_9,7,6 0
- X\_9,7,2 -X\_9,7,7 0
- X\_9,7,2 -X\_9,7,8 0
- X\_9,7,2 -X\_9,7,9 0
- X\_9,7,3 -X\_9,7,4 0
- X\_9,7,3 -X\_9,7,5 0
- X\_9,7,3 -X\_9,7,6 0
- X\_9,7,3 -X\_9,7,7 0
- X\_9,7,3 -X\_9,7,8 0
- X\_9,7,3 -X\_9,7,9 0
- X\_9,7,4 -X\_9,7,5 0
- X\_9,7,4 -X\_9,7,6 0
- X\_9,7,4 -X\_9,7,7 0
- X\_9,7,4 -X\_9,7,8 0
- X\_9,7,4 -X\_9,7,9 0
- X\_9,7,5 -X\_9,7,6 0
- X\_9,7,5 -X\_9,7,7 0
- X\_9,7,5 -X\_9,7,8 0
- X\_9,7,5 -X\_9,7,9 0
- X\_9,7,6 -X\_9,7,7 0
- X\_9,7,6 -X\_9,7,8 0
- X\_9,7,6 -X\_9,7,9 0
- X\_9,7,7 -X\_9,7,8 0
- X\_9,7,7 -X\_9,7,9 0
- X\_9,7,8 -X\_9,7,9 0
- X\_9,8,1 -X\_9,8,2 0
- X\_9,8,1 -X\_9,8,3 0
- X\_9,8,1 -X\_9,8,4 0
- X\_9,8,1 -X\_9,8,5 0
- X\_9,8,1 -X\_9,8,6 0
- X\_9,8,1 -X\_9,8,7 0
- X\_9,8,1 -X\_9,8,8 0
- X\_9,8,1 -X\_9,8,9 0
- X\_9,8,2 -X\_9,8,3 0
- X\_9,8,2 -X\_9,8,4 0
- X\_9,8,2 -X\_9,8,5 0
- X\_9,8,2 -X\_9,8,6 0
- X\_9,8,2 -X\_9,8,7 0
- X\_9,8,2 -X\_9,8,8 0
- X\_9,8,2 -X\_9,8,9 0
- X\_9,8,3 -X\_9,8,4 0
- X\_9,8,3 -X\_9,8,5 0
- X\_9,8,3 -X\_9,8,6 0
- X\_9,8,3 -X\_9,8,7 0
- X\_9,8,3 -X\_9,8,8 0
- X\_9,8,3 -X\_9,8,9 0
- X\_9,8,4 -X\_9,8,5 0
- X\_9,8,4 -X\_9,8,6 0
- X\_9,8,4 -X\_9,8,7 0
- X\_9,8,4 -X\_9,8,8 0
- X\_9,8,4 -X\_9,8,9 0
- X\_9,8,5 -X\_9,8,6 0
- X\_9,8,5 -X\_9,8,7 0
- X\_9,8,5 -X\_9,8,8 0
- X\_9,8,5 -X\_9,8,9 0
- X\_9,8,6 -X\_9,8,7 0
- X\_9,8,6 -X\_9,8,8 0
- X\_9,8,6 -X\_9,8,9 0
- X\_9,8,7 -X\_9,8,8 0
- X\_9,8,7 -X\_9,8,9 0
- X\_9,8,8 -X\_9,8,9 0
- X\_9,9,1 -X\_9,9,2 0
- X\_9,9,1 -X\_9,9,3 0
- X\_9,9,1 -X\_9,9,4 0
- X\_9,9,1 -X\_9,9,5 0
- X\_9,9,1 -X\_9,9,6 0
- X\_9,9,1 -X\_9,9,7 0
- X\_9,9,1 -X\_9,9,8 0
- X\_9,9,1 -X\_9,9,9 0
- X\_9,9,2 -X\_9,9,3 0
- X\_9,9,2 -X\_9,9,4 0
- X\_9,9,2 -X\_9,9,5 0
- X\_9,9,2 -X\_9,9,6 0
- X\_9,9,2 -X\_9,9,7 0
- X\_9,9,2 -X\_9,9,8 0
- X\_9,9,2 -X\_9,9,9 0
- X\_9,9,3 -X\_9,9,4 0
- X\_9,9,3 -X\_9,9,5 0
- X\_9,9,3 -X\_9,9,6 0
- X\_9,9,3 -X\_9,9,7 0
- X\_9,9,3 -X\_9,9,8 0
- X\_9,9,3 -X\_9,9,9 0
- X\_9,9,4 -X\_9,9,5 0
- X\_9,9,4 -X\_9,9,6 0
- X\_9,9,4 -X\_9,9,7 0
- X\_9,9,4 -X\_9,9,8 0
- X\_9,9,4 -X\_9,9,9 0
- X\_9,9,5 -X\_9,9,6 0
- X\_9,9,5 -X\_9,9,7 0
- X\_9,9,5 -X\_9,9,8 0
- X\_9,9,5 -X\_9,9,9 0
- X\_9,9,6 -X\_9,9,7 0
- X\_9,9,6 -X\_9,9,8 0
- X\_9,9,6 -X\_9,9,9 0
- X\_9,9,7 -X\_9,9,8 0
- X\_9,9,7 -X\_9,9,9 0
- X\_9,9,8 -X\_9,9,9 0

X\_1,1,1 X\_1,2,1 X\_1,3,1 X\_1,4,1 X\_1,5,1 X\_1,6,1 X\_1,7,1 X\_1,8,1 X\_1,9,1 0

- X\_1,1,1 -X\_1,2,1 0
- X\_1,1,1 -X\_1,3,1 0
- X\_1,1,1 -X\_1,4,1 0
- X\_1,1,1 -X\_1,5,1 0
- X\_1,1,1 -X\_1,6,1 0
- X\_1,1,1 -X\_1,7,1 0
- X\_1,1,1 -X\_1,8,1 0
- X\_1,1,1 -X\_1,9,1 0
- X\_1,2,1 -X\_1,3,1 0
- X\_1,2,1 -X\_1,4,1 0
- X\_1,2,1 -X\_1,5,1 0
- X\_1,2,1 -X\_1,6,1 0
- X\_1,2,1 -X\_1,7,1 0
- X\_1,2,1 -X\_1,8,1 0
- X\_1,2,1 -X\_1,9,1 0
- X\_1,3,1 -X\_1,4,1 0
- X\_1,3,1 -X\_1,5,1 0
- X\_1,3,1 -X\_1,6,1 0
- X\_1,3,1 -X\_1,7,1 0
- X\_1,3,1 -X\_1,8,1 0
- X\_1,3,1 -X\_1,9,1 0
- X\_1,4,1 -X\_1,5,1 0
- X\_1,4,1 -X\_1,6,1 0
- X\_1,4,1 -X\_1,7,1 0
- X\_1,4,1 -X\_1,8,1 0
- X\_1,4,1 -X\_1,9,1 0
- X\_1,5,1 -X\_1,6,1 0
- X\_1,5,1 -X\_1,7,1 0
- X\_1,5,1 -X\_1,8,1 0
- X\_1,5,1 -X\_1,9,1 0
- X\_1,6,1 -X\_1,7,1 0
- X\_1,6,1 -X\_1,8,1 0
- X\_1,6,1 -X\_1,9,1 0
- X\_1,7,1 -X\_1,8,1 0
- X\_1,7,1 -X\_1,9,1 0
- X\_1,8,1 -X\_1,9,1 0

X\_1,1,2 X\_1,2,2 X\_1,3,2 X\_1,4,2 X\_1,5,2 X\_1,6,2 X\_1,7,2 X\_1,8,2 X\_1,9,2 0

- X\_1,1,2 -X\_1,2,2 0
- X\_1,1,2 -X\_1,3,2 0
- X\_1,1,2 -X\_1,4,2 0
- X\_1,1,2 -X\_1,5,2 0
- X\_1,1,2 -X\_1,6,2 0
- X\_1,1,2 -X\_1,7,2 0
- X\_1,1,2 -X\_1,8,2 0
- X\_1,1,2 -X\_1,9,2 0
- X\_1,2,2 -X\_1,3,2 0
- X\_1,2,2 -X\_1,4,2 0
- X\_1,2,2 -X\_1,5,2 0
- X\_1,2,2 -X\_1,6,2 0
- X\_1,2,2 -X\_1,7,2 0
- X\_1,2,2 -X\_1,8,2 0
- X\_1,2,2 -X\_1,9,2 0
- X\_1,3,2 -X\_1,4,2 0
- X\_1,3,2 -X\_1,5,2 0
- X\_1,3,2 -X\_1,6,2 0
- X\_1,3,2 -X\_1,7,2 0
- X\_1,3,2 -X\_1,8,2 0
- X\_1,3,2 -X\_1,9,2 0
- X\_1,4,2 -X\_1,5,2 0
- X\_1,4,2 -X\_1,6,2 0
- X\_1,4,2 -X\_1,7,2 0
- X\_1,4,2 -X\_1,8,2 0
- X\_1,4,2 -X\_1,9,2 0
- X\_1,5,2 -X\_1,6,2 0
- X\_1,5,2 -X\_1,7,2 0
- X\_1,5,2 -X\_1,8,2 0
- X\_1,5,2 -X\_1,9,2 0
- X\_1,6,2 -X\_1,7,2 0
- X\_1,6,2 -X\_1,8,2 0
- X\_1,6,2 -X\_1,9,2 0
- X\_1,7,2 -X\_1,8,2 0
- X\_1,7,2 -X\_1,9,2 0
- X\_1,8,2 -X\_1,9,2 0

X\_1,1,3 X\_1,2,3 X\_1,3,3 X\_1,4,3 X\_1,5,3 X\_1,6,3 X\_1,7,3 X\_1,8,3 X\_1,9,3 0

- X\_1,1,3 -X\_1,2,3 0
- X\_1,1,3 -X\_1,3,3 0
- X\_1,1,3 -X\_1,4,3 0
- X\_1,1,3 -X\_1,5,3 0
- X\_1,1,3 -X\_1,6,3 0
- X\_1,1,3 -X\_1,7,3 0
- X\_1,1,3 -X\_1,8,3 0
- X\_1,1,3 -X\_1,9,3 0
- X\_1,2,3 -X\_1,3,3 0
- X\_1,2,3 -X\_1,4,3 0
- X\_1,2,3 -X\_1,5,3 0
- X\_1,2,3 -X\_1,6,3 0
- X\_1,2,3 -X\_1,7,3 0
- X\_1,2,3 -X\_1,8,3 0
- X\_1,2,3 -X\_1,9,3 0
- X\_1,3,3 -X\_1,4,3 0
- X\_1,3,3 -X\_1,5,3 0
- X\_1,3,3 -X\_1,6,3 0
- X\_1,3,3 -X\_1,7,3 0
- X\_1,3,3 -X\_1,8,3 0
- X\_1,3,3 -X\_1,9,3 0
- X\_1,4,3 -X\_1,5,3 0
- X\_1,4,3 -X\_1,6,3 0
- X\_1,4,3 -X\_1,7,3 0
- X\_1,4,3 -X\_1,8,3 0
- X\_1,4,3 -X\_1,9,3 0
- X\_1,5,3 -X\_1,6,3 0
- X\_1,5,3 -X\_1,7,3 0
- X\_1,5,3 -X\_1,8,3 0
- X\_1,5,3 -X\_1,9,3 0
- X\_1,6,3 -X\_1,7,3 0
- X\_1,6,3 -X\_1,8,3 0
- X\_1,6,3 -X\_1,9,3 0
- X\_1,7,3 -X\_1,8,3 0
- X\_1,7,3 -X\_1,9,3 0
- X\_1,8,3 -X\_1,9,3 0

X\_1,1,4 X\_1,2,4 X\_1,3,4 X\_1,4,4 X\_1,5,4 X\_1,6,4 X\_1,7,4 X\_1,8,4 X\_1,9,4 0

- X\_1,1,4 -X\_1,2,4 0
- X\_1,1,4 -X\_1,3,4 0
- X\_1,1,4 -X\_1,4,4 0
- X\_1,1,4 -X\_1,5,4 0
- X\_1,1,4 -X\_1,6,4 0
- X\_1,1,4 -X\_1,7,4 0
- X\_1,1,4 -X\_1,8,4 0
- X\_1,1,4 -X\_1,9,4 0
- X\_1,2,4 -X\_1,3,4 0
- X\_1,2,4 -X\_1,4,4 0
- X\_1,2,4 -X\_1,5,4 0
- X\_1,2,4 -X\_1,6,4 0
- X\_1,2,4 -X\_1,7,4 0
- X\_1,2,4 -X\_1,8,4 0
- X\_1,2,4 -X\_1,9,4 0
- X\_1,3,4 -X\_1,4,4 0
- X\_1,3,4 -X\_1,5,4 0
- X\_1,3,4 -X\_1,6,4 0
- X\_1,3,4 -X\_1,7,4 0
- X\_1,3,4 -X\_1,8,4 0
- X\_1,3,4 -X\_1,9,4 0
- X\_1,4,4 -X\_1,5,4 0
- X\_1,4,4 -X\_1,6,4 0
- X\_1,4,4 -X\_1,7,4 0
- X\_1,4,4 -X\_1,8,4 0
- X\_1,4,4 -X\_1,9,4 0
- X\_1,5,4 -X\_1,6,4 0
- X\_1,5,4 -X\_1,7,4 0
- X\_1,5,4 -X\_1,8,4 0
- X\_1,5,4 -X\_1,9,4 0
- X\_1,6,4 -X\_1,7,4 0
- X\_1,6,4 -X\_1,8,4 0
- X\_1,6,4 -X\_1,9,4 0
- X\_1,7,4 -X\_1,8,4 0
- X\_1,7,4 -X\_1,9,4 0
- X\_1,8,4 -X\_1,9,4 0

X\_1,1,5 X\_1,2,5 X\_1,3,5 X\_1,4,5 X\_1,5,5 X\_1,6,5 X\_1,7,5 X\_1,8,5 X\_1,9,5 0

- X\_1,1,5 -X\_1,2,5 0
- X\_1,1,5 -X\_1,3,5 0
- X\_1,1,5 -X\_1,4,5 0
- X\_1,1,5 -X\_1,5,5 0
- X\_1,1,5 -X\_1,6,5 0
- X\_1,1,5 -X\_1,7,5 0
- X\_1,1,5 -X\_1,8,5 0
- X\_1,1,5 -X\_1,9,5 0
- X\_1,2,5 -X\_1,3,5 0
- X\_1,2,5 -X\_1,4,5 0
- X\_1,2,5 -X\_1,5,5 0
- X\_1,2,5 -X\_1,6,5 0
- X\_1,2,5 -X\_1,7,5 0
- X\_1,2,5 -X\_1,8,5 0
- X\_1,2,5 -X\_1,9,5 0
- X\_1,3,5 -X\_1,4,5 0
- X\_1,3,5 -X\_1,5,5 0
- X\_1,3,5 -X\_1,6,5 0
- X\_1,3,5 -X\_1,7,5 0
- X\_1,3,5 -X\_1,8,5 0
- X\_1,3,5 -X\_1,9,5 0
- X\_1,4,5 -X\_1,5,5 0
- X\_1,4,5 -X\_1,6,5 0
- X\_1,4,5 -X\_1,7,5 0
- X\_1,4,5 -X\_1,8,5 0
- X\_1,4,5 -X\_1,9,5 0
- X\_1,5,5 -X\_1,6,5 0
- X\_1,5,5 -X\_1,7,5 0
- X\_1,5,5 -X\_1,8,5 0
- X\_1,5,5 -X\_1,9,5 0
- X\_1,6,5 -X\_1,7,5 0
- X\_1,6,5 -X\_1,8,5 0
- X\_1,6,5 -X\_1,9,5 0
- X\_1,7,5 -X\_1,8,5 0
- X\_1,7,5 -X\_1,9,5 0
- X\_1,8,5 -X\_1,9,5 0

X\_1,1,6 X\_1,2,6 X\_1,3,6 X\_1,4,6 X\_1,5,6 X\_1,6,6 X\_1,7,6 X\_1,8,6 X\_1,9,6 0

- X\_1,1,6 -X\_1,2,6 0
- X\_1,1,6 -X\_1,3,6 0
- X\_1,1,6 -X\_1,4,6 0
- X\_1,1,6 -X\_1,5,6 0
- X\_1,1,6 -X\_1,6,6 0
- X\_1,1,6 -X\_1,7,6 0
- X\_1,1,6 -X\_1,8,6 0
- X\_1,1,6 -X\_1,9,6 0
- X\_1,2,6 -X\_1,3,6 0
- X\_1,2,6 -X\_1,4,6 0
- X\_1,2,6 -X\_1,5,6 0
- X\_1,2,6 -X\_1,6,6 0
- X\_1,2,6 -X\_1,7,6 0
- X\_1,2,6 -X\_1,8,6 0
- X\_1,2,6 -X\_1,9,6 0
- X\_1,3,6 -X\_1,4,6 0
- X\_1,3,6 -X\_1,5,6 0
- X\_1,3,6 -X\_1,6,6 0
- X\_1,3,6 -X\_1,7,6 0
- X\_1,3,6 -X\_1,8,6 0
- X\_1,3,6 -X\_1,9,6 0
- X\_1,4,6 -X\_1,5,6 0
- X\_1,4,6 -X\_1,6,6 0
- X\_1,4,6 -X\_1,7,6 0
- X\_1,4,6 -X\_1,8,6 0
- X\_1,4,6 -X\_1,9,6 0
- X\_1,5,6 -X\_1,6,6 0
- X\_1,5,6 -X\_1,7,6 0
- X\_1,5,6 -X\_1,8,6 0
- X\_1,5,6 -X\_1,9,6 0
- X\_1,6,6 -X\_1,7,6 0
- X\_1,6,6 -X\_1,8,6 0
- X\_1,6,6 -X\_1,9,6 0
- X\_1,7,6 -X\_1,8,6 0
- X\_1,7,6 -X\_1,9,6 0
- X\_1,8,6 -X\_1,9,6 0

X\_1,1,7 X\_1,2,7 X\_1,3,7 X\_1,4,7 X\_1,5,7 X\_1,6,7 X\_1,7,7 X\_1,8,7 X\_1,9,7 0

- X\_1,1,7 -X\_1,2,7 0
- X\_1,1,7 -X\_1,3,7 0
- X\_1,1,7 -X\_1,4,7 0
- X\_1,1,7 -X\_1,5,7 0
- X\_1,1,7 -X\_1,6,7 0
- X\_1,1,7 -X\_1,7,7 0
- X\_1,1,7 -X\_1,8,7 0
- X\_1,1,7 -X\_1,9,7 0
- X\_1,2,7 -X\_1,3,7 0
- X\_1,2,7 -X\_1,4,7 0
- X\_1,2,7 -X\_1,5,7 0
- X\_1,2,7 -X\_1,6,7 0
- X\_1,2,7 -X\_1,7,7 0
- X\_1,2,7 -X\_1,8,7 0
- X\_1,2,7 -X\_1,9,7 0
- X\_1,3,7 -X\_1,4,7 0
- X\_1,3,7 -X\_1,5,7 0
- X\_1,3,7 -X\_1,6,7 0
- X\_1,3,7 -X\_1,7,7 0
- X\_1,3,7 -X\_1,8,7 0
- X\_1,3,7 -X\_1,9,7 0
- X\_1,4,7 -X\_1,5,7 0
- X\_1,4,7 -X\_1,6,7 0
- X\_1,4,7 -X\_1,7,7 0
- X\_1,4,7 -X\_1,8,7 0
- X\_1,4,7 -X\_1,9,7 0
- X\_1,5,7 -X\_1,6,7 0
- X\_1,5,7 -X\_1,7,7 0
- X\_1,5,7 -X\_1,8,7 0
- X\_1,5,7 -X\_1,9,7 0
- X\_1,6,7 -X\_1,7,7 0
- X\_1,6,7 -X\_1,8,7 0
- X\_1,6,7 -X\_1,9,7 0
- X\_1,7,7 -X\_1,8,7 0
- X\_1,7,7 -X\_1,9,7 0
- X\_1,8,7 -X\_1,9,7 0

X\_1,1,8 X\_1,2,8 X\_1,3,8 X\_1,4,8 X\_1,5,8 X\_1,6,8 X\_1,7,8 X\_1,8,8 X\_1,9,8 0

- X\_1,1,8 -X\_1,2,8 0
- X\_1,1,8 -X\_1,3,8 0
- X\_1,1,8 -X\_1,4,8 0
- X\_1,1,8 -X\_1,5,8 0
- X\_1,1,8 -X\_1,6,8 0
- X\_1,1,8 -X\_1,7,8 0
- X\_1,1,8 -X\_1,8,8 0
- X\_1,1,8 -X\_1,9,8 0
- X\_1,2,8 -X\_1,3,8 0
- X\_1,2,8 -X\_1,4,8 0
- X\_1,2,8 -X\_1,5,8 0
- X\_1,2,8 -X\_1,6,8 0
- X\_1,2,8 -X\_1,7,8 0
- X\_1,2,8 -X\_1,8,8 0
- X\_1,2,8 -X\_1,9,8 0
- X\_1,3,8 -X\_1,4,8 0
- X\_1,3,8 -X\_1,5,8 0
- X\_1,3,8 -X\_1,6,8 0
- X\_1,3,8 -X\_1,7,8 0
- X\_1,3,8 -X\_1,8,8 0
- X\_1,3,8 -X\_1,9,8 0
- X\_1,4,8 -X\_1,5,8 0
- X\_1,4,8 -X\_1,6,8 0
- X\_1,4,8 -X\_1,7,8 0
- X\_1,4,8 -X\_1,8,8 0
- X\_1,4,8 -X\_1,9,8 0
- X\_1,5,8 -X\_1,6,8 0
- X\_1,5,8 -X\_1,7,8 0
- X\_1,5,8 -X\_1,8,8 0
- X\_1,5,8 -X\_1,9,8 0
- X\_1,6,8 -X\_1,7,8 0
- X\_1,6,8 -X\_1,8,8 0
- X\_1,6,8 -X\_1,9,8 0
- X\_1,7,8 -X\_1,8,8 0
- X\_1,7,8 -X\_1,9,8 0
- X\_1,8,8 -X\_1,9,8 0

X\_1,1,9 X\_1,2,9 X\_1,3,9 X\_1,4,9 X\_1,5,9 X\_1,6,9 X\_1,7,9 X\_1,8,9 X\_1,9,9 0

- X\_1,1,9 -X\_1,2,9 0
- X\_1,1,9 -X\_1,3,9 0
- X\_1,1,9 -X\_1,4,9 0
- X\_1,1,9 -X\_1,5,9 0
- X\_1,1,9 -X\_1,6,9 0
- X\_1,1,9 -X\_1,7,9 0
- X\_1,1,9 -X\_1,8,9 0
- X\_1,1,9 -X\_1,9,9 0
- X\_1,2,9 -X\_1,3,9 0
- X\_1,2,9 -X\_1,4,9 0
- X\_1,2,9 -X\_1,5,9 0
- X\_1,2,9 -X\_1,6,9 0
- X\_1,2,9 -X\_1,7,9 0
- X\_1,2,9 -X\_1,8,9 0
- X\_1,2,9 -X\_1,9,9 0
- X\_1,3,9 -X\_1,4,9 0
- X\_1,3,9 -X\_1,5,9 0
- X\_1,3,9 -X\_1,6,9 0
- X\_1,3,9 -X\_1,7,9 0
- X\_1,3,9 -X\_1,8,9 0
- X\_1,3,9 -X\_1,9,9 0
- X\_1,4,9 -X\_1,5,9 0
- X\_1,4,9 -X\_1,6,9 0
- X\_1,4,9 -X\_1,7,9 0
- X\_1,4,9 -X\_1,8,9 0
- X\_1,4,9 -X\_1,9,9 0
- X\_1,5,9 -X\_1,6,9 0
- X\_1,5,9 -X\_1,7,9 0
- X\_1,5,9 -X\_1,8,9 0
- X\_1,5,9 -X\_1,9,9 0
- X\_1,6,9 -X\_1,7,9 0
- X\_1,6,9 -X\_1,8,9 0
- X\_1,6,9 -X\_1,9,9 0
- X\_1,7,9 -X\_1,8,9 0
- X\_1,7,9 -X\_1,9,9 0
- X\_1,8,9 -X\_1,9,9 0

X\_2,1,1 X\_2,2,1 X\_2,3,1 X\_2,4,1 X\_2,5,1 X\_2,6,1 X\_2,7,1 X\_2,8,1 X\_2,9,1 0

- X\_2,1,1 -X\_2,2,1 0
- X\_2,1,1 -X\_2,3,1 0
- X\_2,1,1 -X\_2,4,1 0
- X\_2,1,1 -X\_2,5,1 0
- X\_2,1,1 -X\_2,6,1 0
- X\_2,1,1 -X\_2,7,1 0
- X\_2,1,1 -X\_2,8,1 0
- X\_2,1,1 -X\_2,9,1 0
- X\_2,2,1 -X\_2,3,1 0
- X\_2,2,1 -X\_2,4,1 0
- X\_2,2,1 -X\_2,5,1 0
- X\_2,2,1 -X\_2,6,1 0
- X\_2,2,1 -X\_2,7,1 0
- X\_2,2,1 -X\_2,8,1 0
- X\_2,2,1 -X\_2,9,1 0
- X\_2,3,1 -X\_2,4,1 0
- X\_2,3,1 -X\_2,5,1 0
- X\_2,3,1 -X\_2,6,1 0
- X\_2,3,1 -X\_2,7,1 0
- X\_2,3,1 -X\_2,8,1 0
- X\_2,3,1 -X\_2,9,1 0
- X\_2,4,1 -X\_2,5,1 0
- X\_2,4,1 -X\_2,6,1 0
- X\_2,4,1 -X\_2,7,1 0
- X\_2,4,1 -X\_2,8,1 0
- X\_2,4,1 -X\_2,9,1 0
- X\_2,5,1 -X\_2,6,1 0
- X\_2,5,1 -X\_2,7,1 0
- X\_2,5,1 -X\_2,8,1 0
- X\_2,5,1 -X\_2,9,1 0
- X\_2,6,1 -X\_2,7,1 0
- X\_2,6,1 -X\_2,8,1 0
- X\_2,6,1 -X\_2,9,1 0
- X\_2,7,1 -X\_2,8,1 0
- X\_2,7,1 -X\_2,9,1 0
- X\_2,8,1 -X\_2,9,1 0

X\_2,1,2 X\_2,2,2 X\_2,3,2 X\_2,4,2 X\_2,5,2 X\_2,6,2 X\_2,7,2 X\_2,8,2 X\_2,9,2 0

- X\_2,1,2 -X\_2,2,2 0
- X\_2,1,2 -X\_2,3,2 0
- X\_2,1,2 -X\_2,4,2 0
- X\_2,1,2 -X\_2,5,2 0
- X\_2,1,2 -X\_2,6,2 0
- X\_2,1,2 -X\_2,7,2 0
- X\_2,1,2 -X\_2,8,2 0
- X\_2,1,2 -X\_2,9,2 0
- X\_2,2,2 -X\_2,3,2 0
- X\_2,2,2 -X\_2,4,2 0
- X\_2,2,2 -X\_2,5,2 0
- X\_2,2,2 -X\_2,6,2 0
- X\_2,2,2 -X\_2,7,2 0
- X\_2,2,2 -X\_2,8,2 0
- X\_2,2,2 -X\_2,9,2 0
- X\_2,3,2 -X\_2,4,2 0
- X\_2,3,2 -X\_2,5,2 0
- X\_2,3,2 -X\_2,6,2 0
- X\_2,3,2 -X\_2,7,2 0
- X\_2,3,2 -X\_2,8,2 0
- X\_2,3,2 -X\_2,9,2 0
- X\_2,4,2 -X\_2,5,2 0
- X\_2,4,2 -X\_2,6,2 0
- X\_2,4,2 -X\_2,7,2 0
- X\_2,4,2 -X\_2,8,2 0
- X\_2,4,2 -X\_2,9,2 0
- X\_2,5,2 -X\_2,6,2 0
- X\_2,5,2 -X\_2,7,2 0
- X\_2,5,2 -X\_2,8,2 0
- X\_2,5,2 -X\_2,9,2 0
- X\_2,6,2 -X\_2,7,2 0
- X\_2,6,2 -X\_2,8,2 0
- X\_2,6,2 -X\_2,9,2 0
- X\_2,7,2 -X\_2,8,2 0
- X\_2,7,2 -X\_2,9,2 0
- X\_2,8,2 -X\_2,9,2 0

X\_2,1,3 X\_2,2,3 X\_2,3,3 X\_2,4,3 X\_2,5,3 X\_2,6,3 X\_2,7,3 X\_2,8,3 X\_2,9,3 0

- X\_2,1,3 -X\_2,2,3 0
- X\_2,1,3 -X\_2,3,3 0
- X\_2,1,3 -X\_2,4,3 0
- X\_2,1,3 -X\_2,5,3 0
- X\_2,1,3 -X\_2,6,3 0
- X\_2,1,3 -X\_2,7,3 0
- X\_2,1,3 -X\_2,8,3 0
- X\_2,1,3 -X\_2,9,3 0
- X\_2,2,3 -X\_2,3,3 0
- X\_2,2,3 -X\_2,4,3 0
- X\_2,2,3 -X\_2,5,3 0
- X\_2,2,3 -X\_2,6,3 0
- X\_2,2,3 -X\_2,7,3 0
- X\_2,2,3 -X\_2,8,3 0
- X\_2,2,3 -X\_2,9,3 0
- X\_2,3,3 -X\_2,4,3 0
- X\_2,3,3 -X\_2,5,3 0
- X\_2,3,3 -X\_2,6,3 0
- X\_2,3,3 -X\_2,7,3 0
- X\_2,3,3 -X\_2,8,3 0
- X\_2,3,3 -X\_2,9,3 0
- X\_2,4,3 -X\_2,5,3 0
- X\_2,4,3 -X\_2,6,3 0
- X\_2,4,3 -X\_2,7,3 0
- X\_2,4,3 -X\_2,8,3 0
- X\_2,4,3 -X\_2,9,3 0
- X\_2,5,3 -X\_2,6,3 0
- X\_2,5,3 -X\_2,7,3 0
- X\_2,5,3 -X\_2,8,3 0
- X\_2,5,3 -X\_2,9,3 0
- X\_2,6,3 -X\_2,7,3 0
- X\_2,6,3 -X\_2,8,3 0
- X\_2,6,3 -X\_2,9,3 0
- X\_2,7,3 -X\_2,8,3 0
- X\_2,7,3 -X\_2,9,3 0
- X\_2,8,3 -X\_2,9,3 0

X\_2,1,4 X\_2,2,4 X\_2,3,4 X\_2,4,4 X\_2,5,4 X\_2,6,4 X\_2,7,4 X\_2,8,4 X\_2,9,4 0

- X\_2,1,4 -X\_2,2,4 0
- X\_2,1,4 -X\_2,3,4 0
- X\_2,1,4 -X\_2,4,4 0
- X\_2,1,4 -X\_2,5,4 0
- X\_2,1,4 -X\_2,6,4 0
- X\_2,1,4 -X\_2,7,4 0
- X\_2,1,4 -X\_2,8,4 0
- X\_2,1,4 -X\_2,9,4 0
- X\_2,2,4 -X\_2,3,4 0
- X\_2,2,4 -X\_2,4,4 0
- X\_2,2,4 -X\_2,5,4 0
- X\_2,2,4 -X\_2,6,4 0
- X\_2,2,4 -X\_2,7,4 0
- X\_2,2,4 -X\_2,8,4 0
- X\_2,2,4 -X\_2,9,4 0
- X\_2,3,4 -X\_2,4,4 0
- X\_2,3,4 -X\_2,5,4 0
- X\_2,3,4 -X\_2,6,4 0
- X\_2,3,4 -X\_2,7,4 0
- X\_2,3,4 -X\_2,8,4 0
- X\_2,3,4 -X\_2,9,4 0
- X\_2,4,4 -X\_2,5,4 0
- X\_2,4,4 -X\_2,6,4 0
- X\_2,4,4 -X\_2,7,4 0
- X\_2,4,4 -X\_2,8,4 0
- X\_2,4,4 -X\_2,9,4 0
- X\_2,5,4 -X\_2,6,4 0
- X\_2,5,4 -X\_2,7,4 0
- X\_2,5,4 -X\_2,8,4 0
- X\_2,5,4 -X\_2,9,4 0
- X\_2,6,4 -X\_2,7,4 0
- X\_2,6,4 -X\_2,8,4 0
- X\_2,6,4 -X\_2,9,4 0
- X\_2,7,4 -X\_2,8,4 0
- X\_2,7,4 -X\_2,9,4 0
- X\_2,8,4 -X\_2,9,4 0

X\_2,1,5 X\_2,2,5 X\_2,3,5 X\_2,4,5 X\_2,5,5 X\_2,6,5 X\_2,7,5 X\_2,8,5 X\_2,9,5 0

- X\_2,1,5 -X\_2,2,5 0
- X\_2,1,5 -X\_2,3,5 0
- X\_2,1,5 -X\_2,4,5 0
- X\_2,1,5 -X\_2,5,5 0
- X\_2,1,5 -X\_2,6,5 0
- X\_2,1,5 -X\_2,7,5 0
- X\_2,1,5 -X\_2,8,5 0
- X\_2,1,5 -X\_2,9,5 0
- X\_2,2,5 -X\_2,3,5 0
- X\_2,2,5 -X\_2,4,5 0
- X\_2,2,5 -X\_2,5,5 0
- X\_2,2,5 -X\_2,6,5 0
- X\_2,2,5 -X\_2,7,5 0
- X\_2,2,5 -X\_2,8,5 0
- X\_2,2,5 -X\_2,9,5 0
- X\_2,3,5 -X\_2,4,5 0
- X\_2,3,5 -X\_2,5,5 0
- X\_2,3,5 -X\_2,6,5 0
- X\_2,3,5 -X\_2,7,5 0
- X\_2,3,5 -X\_2,8,5 0
- X\_2,3,5 -X\_2,9,5 0
- X\_2,4,5 -X\_2,5,5 0
- X\_2,4,5 -X\_2,6,5 0
- X\_2,4,5 -X\_2,7,5 0
- X\_2,4,5 -X\_2,8,5 0
- X\_2,4,5 -X\_2,9,5 0
- X\_2,5,5 -X\_2,6,5 0
- X\_2,5,5 -X\_2,7,5 0
- X\_2,5,5 -X\_2,8,5 0
- X\_2,5,5 -X\_2,9,5 0
- X\_2,6,5 -X\_2,7,5 0
- X\_2,6,5 -X\_2,8,5 0
- X\_2,6,5 -X\_2,9,5 0
- X\_2,7,5 -X\_2,8,5 0
- X\_2,7,5 -X\_2,9,5 0
- X\_2,8,5 -X\_2,9,5 0

X\_2,1,6 X\_2,2,6 X\_2,3,6 X\_2,4,6 X\_2,5,6 X\_2,6,6 X\_2,7,6 X\_2,8,6 X\_2,9,6 0

- X\_2,1,6 -X\_2,2,6 0
- X\_2,1,6 -X\_2,3,6 0
- X\_2,1,6 -X\_2,4,6 0
- X\_2,1,6 -X\_2,5,6 0
- X\_2,1,6 -X\_2,6,6 0
- X\_2,1,6 -X\_2,7,6 0
- X\_2,1,6 -X\_2,8,6 0
- X\_2,1,6 -X\_2,9,6 0
- X\_2,2,6 -X\_2,3,6 0
- X\_2,2,6 -X\_2,4,6 0
- X\_2,2,6 -X\_2,5,6 0
- X\_2,2,6 -X\_2,6,6 0
- X\_2,2,6 -X\_2,7,6 0
- X\_2,2,6 -X\_2,8,6 0
- X\_2,2,6 -X\_2,9,6 0
- X\_2,3,6 -X\_2,4,6 0
- X\_2,3,6 -X\_2,5,6 0
- X\_2,3,6 -X\_2,6,6 0
- X\_2,3,6 -X\_2,7,6 0
- X\_2,3,6 -X\_2,8,6 0
- X\_2,3,6 -X\_2,9,6 0
- X\_2,4,6 -X\_2,5,6 0
- X\_2,4,6 -X\_2,6,6 0
- X\_2,4,6 -X\_2,7,6 0
- X\_2,4,6 -X\_2,8,6 0
- X\_2,4,6 -X\_2,9,6 0
- X\_2,5,6 -X\_2,6,6 0
- X\_2,5,6 -X\_2,7,6 0
- X\_2,5,6 -X\_2,8,6 0
- X\_2,5,6 -X\_2,9,6 0
- X\_2,6,6 -X\_2,7,6 0
- X\_2,6,6 -X\_2,8,6 0
- X\_2,6,6 -X\_2,9,6 0
- X\_2,7,6 -X\_2,8,6 0
- X\_2,7,6 -X\_2,9,6 0
- X\_2,8,6 -X\_2,9,6 0

X\_2,1,7 X\_2,2,7 X\_2,3,7 X\_2,4,7 X\_2,5,7 X\_2,6,7 X\_2,7,7 X\_2,8,7 X\_2,9,7 0

- X\_2,1,7 -X\_2,2,7 0
- X\_2,1,7 -X\_2,3,7 0
- X\_2,1,7 -X\_2,4,7 0
- X\_2,1,7 -X\_2,5,7 0
- X\_2,1,7 -X\_2,6,7 0
- X\_2,1,7 -X\_2,7,7 0
- X\_2,1,7 -X\_2,8,7 0
- X\_2,1,7 -X\_2,9,7 0
- X\_2,2,7 -X\_2,3,7 0
- X\_2,2,7 -X\_2,4,7 0
- X\_2,2,7 -X\_2,5,7 0
- X\_2,2,7 -X\_2,6,7 0
- X\_2,2,7 -X\_2,7,7 0
- X\_2,2,7 -X\_2,8,7 0
- X\_2,2,7 -X\_2,9,7 0
- X\_2,3,7 -X\_2,4,7 0
- X\_2,3,7 -X\_2,5,7 0
- X\_2,3,7 -X\_2,6,7 0
- X\_2,3,7 -X\_2,7,7 0
- X\_2,3,7 -X\_2,8,7 0
- X\_2,3,7 -X\_2,9,7 0
- X\_2,4,7 -X\_2,5,7 0
- X\_2,4,7 -X\_2,6,7 0
- X\_2,4,7 -X\_2,7,7 0
- X\_2,4,7 -X\_2,8,7 0
- X\_2,4,7 -X\_2,9,7 0
- X\_2,5,7 -X\_2,6,7 0
- X\_2,5,7 -X\_2,7,7 0
- X\_2,5,7 -X\_2,8,7 0
- X\_2,5,7 -X\_2,9,7 0
- X\_2,6,7 -X\_2,7,7 0
- X\_2,6,7 -X\_2,8,7 0
- X\_2,6,7 -X\_2,9,7 0
- X\_2,7,7 -X\_2,8,7 0
- X\_2,7,7 -X\_2,9,7 0
- X\_2,8,7 -X\_2,9,7 0

X\_2,1,8 X\_2,2,8 X\_2,3,8 X\_2,4,8 X\_2,5,8 X\_2,6,8 X\_2,7,8 X\_2,8,8 X\_2,9,8 0

- X\_2,1,8 -X\_2,2,8 0
- X\_2,1,8 -X\_2,3,8 0
- X\_2,1,8 -X\_2,4,8 0
- X\_2,1,8 -X\_2,5,8 0
- X\_2,1,8 -X\_2,6,8 0
- X\_2,1,8 -X\_2,7,8 0
- X\_2,1,8 -X\_2,8,8 0
- X\_2,1,8 -X\_2,9,8 0
- X\_2,2,8 -X\_2,3,8 0
- X\_2,2,8 -X\_2,4,8 0
- X\_2,2,8 -X\_2,5,8 0
- X\_2,2,8 -X\_2,6,8 0
- X\_2,2,8 -X\_2,7,8 0
- X\_2,2,8 -X\_2,8,8 0
- X\_2,2,8 -X\_2,9,8 0
- X\_2,3,8 -X\_2,4,8 0
- X\_2,3,8 -X\_2,5,8 0
- X\_2,3,8 -X\_2,6,8 0
- X\_2,3,8 -X\_2,7,8 0
- X\_2,3,8 -X\_2,8,8 0
- X\_2,3,8 -X\_2,9,8 0
- X\_2,4,8 -X\_2,5,8 0
- X\_2,4,8 -X\_2,6,8 0
- X\_2,4,8 -X\_2,7,8 0
- X\_2,4,8 -X\_2,8,8 0
- X\_2,4,8 -X\_2,9,8 0
- X\_2,5,8 -X\_2,6,8 0
- X\_2,5,8 -X\_2,7,8 0
- X\_2,5,8 -X\_2,8,8 0
- X\_2,5,8 -X\_2,9,8 0
- X\_2,6,8 -X\_2,7,8 0
- X\_2,6,8 -X\_2,8,8 0
- X\_2,6,8 -X\_2,9,8 0
- X\_2,7,8 -X\_2,8,8 0
- X\_2,7,8 -X\_2,9,8 0
- X\_2,8,8 -X\_2,9,8 0

X\_2,1,9 X\_2,2,9 X\_2,3,9 X\_2,4,9 X\_2,5,9 X\_2,6,9 X\_2,7,9 X\_2,8,9 X\_2,9,9 0

- X\_2,1,9 -X\_2,2,9 0
- X\_2,1,9 -X\_2,3,9 0
- X\_2,1,9 -X\_2,4,9 0
- X\_2,1,9 -X\_2,5,9 0
- X\_2,1,9 -X\_2,6,9 0
- X\_2,1,9 -X\_2,7,9 0
- X\_2,1,9 -X\_2,8,9 0
- X\_2,1,9 -X\_2,9,9 0
- X\_2,2,9 -X\_2,3,9 0
- X\_2,2,9 -X\_2,4,9 0
- X\_2,2,9 -X\_2,5,9 0
- X\_2,2,9 -X\_2,6,9 0
- X\_2,2,9 -X\_2,7,9 0
- X\_2,2,9 -X\_2,8,9 0
- X\_2,2,9 -X\_2,9,9 0
- X\_2,3,9 -X\_2,4,9 0
- X\_2,3,9 -X\_2,5,9 0
- X\_2,3,9 -X\_2,6,9 0
- X\_2,3,9 -X\_2,7,9 0
- X\_2,3,9 -X\_2,8,9 0
- X\_2,3,9 -X\_2,9,9 0
- X\_2,4,9 -X\_2,5,9 0
- X\_2,4,9 -X\_2,6,9 0
- X\_2,4,9 -X\_2,7,9 0
- X\_2,4,9 -X\_2,8,9 0
- X\_2,4,9 -X\_2,9,9 0
- X\_2,5,9 -X\_2,6,9 0
- X\_2,5,9 -X\_2,7,9 0
- X\_2,5,9 -X\_2,8,9 0
- X\_2,5,9 -X\_2,9,9 0
- X\_2,6,9 -X\_2,7,9 0
- X\_2,6,9 -X\_2,8,9 0
- X\_2,6,9 -X\_2,9,9 0
- X\_2,7,9 -X\_2,8,9 0
- X\_2,7,9 -X\_2,9,9 0
- X\_2,8,9 -X\_2,9,9 0

X\_3,1,1 X\_3,2,1 X\_3,3,1 X\_3,4,1 X\_3,5,1 X\_3,6,1 X\_3,7,1 X\_3,8,1 X\_3,9,1 0

- X\_3,1,1 -X\_3,2,1 0
- X\_3,1,1 -X\_3,3,1 0
- X\_3,1,1 -X\_3,4,1 0
- X\_3,1,1 -X\_3,5,1 0
- X\_3,1,1 -X\_3,6,1 0
- X\_3,1,1 -X\_3,7,1 0
- X\_3,1,1 -X\_3,8,1 0
- X\_3,1,1 -X\_3,9,1 0
- X\_3,2,1 -X\_3,3,1 0
- X\_3,2,1 -X\_3,4,1 0
- X\_3,2,1 -X\_3,5,1 0
- X\_3,2,1 -X\_3,6,1 0
- X\_3,2,1 -X\_3,7,1 0
- X\_3,2,1 -X\_3,8,1 0
- X\_3,2,1 -X\_3,9,1 0
- X\_3,3,1 -X\_3,4,1 0
- X\_3,3,1 -X\_3,5,1 0
- X\_3,3,1 -X\_3,6,1 0
- X\_3,3,1 -X\_3,7,1 0
- X\_3,3,1 -X\_3,8,1 0
- X\_3,3,1 -X\_3,9,1 0
- X\_3,4,1 -X\_3,5,1 0
- X\_3,4,1 -X\_3,6,1 0
- X\_3,4,1 -X\_3,7,1 0
- X\_3,4,1 -X\_3,8,1 0
- X\_3,4,1 -X\_3,9,1 0
- X\_3,5,1 -X\_3,6,1 0
- X\_3,5,1 -X\_3,7,1 0
- X\_3,5,1 -X\_3,8,1 0
- X\_3,5,1 -X\_3,9,1 0
- X\_3,6,1 -X\_3,7,1 0
- X\_3,6,1 -X\_3,8,1 0
- X\_3,6,1 -X\_3,9,1 0
- X\_3,7,1 -X\_3,8,1 0
- X\_3,7,1 -X\_3,9,1 0
- X\_3,8,1 -X\_3,9,1 0

X\_3,1,2 X\_3,2,2 X\_3,3,2 X\_3,4,2 X\_3,5,2 X\_3,6,2 X\_3,7,2 X\_3,8,2 X\_3,9,2 0

- X\_3,1,2 -X\_3,2,2 0
- X\_3,1,2 -X\_3,3,2 0
- X\_3,1,2 -X\_3,4,2 0
- X\_3,1,2 -X\_3,5,2 0
- X\_3,1,2 -X\_3,6,2 0
- X\_3,1,2 -X\_3,7,2 0
- X\_3,1,2 -X\_3,8,2 0
- X\_3,1,2 -X\_3,9,2 0
- X\_3,2,2 -X\_3,3,2 0
- X\_3,2,2 -X\_3,4,2 0
- X\_3,2,2 -X\_3,5,2 0
- X\_3,2,2 -X\_3,6,2 0
- X\_3,2,2 -X\_3,7,2 0
- X\_3,2,2 -X\_3,8,2 0
- X\_3,2,2 -X\_3,9,2 0
- X\_3,3,2 -X\_3,4,2 0
- X\_3,3,2 -X\_3,5,2 0
- X\_3,3,2 -X\_3,6,2 0
- X\_3,3,2 -X\_3,7,2 0
- X\_3,3,2 -X\_3,8,2 0
- X\_3,3,2 -X\_3,9,2 0
- X\_3,4,2 -X\_3,5,2 0
- X\_3,4,2 -X\_3,6,2 0
- X\_3,4,2 -X\_3,7,2 0
- X\_3,4,2 -X\_3,8,2 0
- X\_3,4,2 -X\_3,9,2 0
- X\_3,5,2 -X\_3,6,2 0
- X\_3,5,2 -X\_3,7,2 0
- X\_3,5,2 -X\_3,8,2 0
- X\_3,5,2 -X\_3,9,2 0
- X\_3,6,2 -X\_3,7,2 0
- X\_3,6,2 -X\_3,8,2 0
- X\_3,6,2 -X\_3,9,2 0
- X\_3,7,2 -X\_3,8,2 0
- X\_3,7,2 -X\_3,9,2 0
- X\_3,8,2 -X\_3,9,2 0

X\_3,1,3 X\_3,2,3 X\_3,3,3 X\_3,4,3 X\_3,5,3 X\_3,6,3 X\_3,7,3 X\_3,8,3 X\_3,9,3 0

- X\_3,1,3 -X\_3,2,3 0
- X\_3,1,3 -X\_3,3,3 0
- X\_3,1,3 -X\_3,4,3 0
- X\_3,1,3 -X\_3,5,3 0
- X\_3,1,3 -X\_3,6,3 0
- X\_3,1,3 -X\_3,7,3 0
- X\_3,1,3 -X\_3,8,3 0
- X\_3,1,3 -X\_3,9,3 0
- X\_3,2,3 -X\_3,3,3 0
- X\_3,2,3 -X\_3,4,3 0
- X\_3,2,3 -X\_3,5,3 0
- X\_3,2,3 -X\_3,6,3 0
- X\_3,2,3 -X\_3,7,3 0
- X\_3,2,3 -X\_3,8,3 0
- X\_3,2,3 -X\_3,9,3 0
- X\_3,3,3 -X\_3,4,3 0
- X\_3,3,3 -X\_3,5,3 0
- X\_3,3,3 -X\_3,6,3 0
- X\_3,3,3 -X\_3,7,3 0
- X\_3,3,3 -X\_3,8,3 0
- X\_3,3,3 -X\_3,9,3 0
- X\_3,4,3 -X\_3,5,3 0
- X\_3,4,3 -X\_3,6,3 0
- X\_3,4,3 -X\_3,7,3 0
- X\_3,4,3 -X\_3,8,3 0
- X\_3,4,3 -X\_3,9,3 0
- X\_3,5,3 -X\_3,6,3 0
- X\_3,5,3 -X\_3,7,3 0
- X\_3,5,3 -X\_3,8,3 0
- X\_3,5,3 -X\_3,9,3 0
- X\_3,6,3 -X\_3,7,3 0
- X\_3,6,3 -X\_3,8,3 0
- X\_3,6,3 -X\_3,9,3 0
- X\_3,7,3 -X\_3,8,3 0
- X\_3,7,3 -X\_3,9,3 0
- X\_3,8,3 -X\_3,9,3 0

X\_3,1,4 X\_3,2,4 X\_3,3,4 X\_3,4,4 X\_3,5,4 X\_3,6,4 X\_3,7,4 X\_3,8,4 X\_3,9,4 0

- X\_3,1,4 -X\_3,2,4 0
- X\_3,1,4 -X\_3,3,4 0
- X\_3,1,4 -X\_3,4,4 0
- X\_3,1,4 -X\_3,5,4 0
- X\_3,1,4 -X\_3,6,4 0
- X\_3,1,4 -X\_3,7,4 0
- X\_3,1,4 -X\_3,8,4 0
- X\_3,1,4 -X\_3,9,4 0
- X\_3,2,4 -X\_3,3,4 0
- X\_3,2,4 -X\_3,4,4 0
- X\_3,2,4 -X\_3,5,4 0
- X\_3,2,4 -X\_3,6,4 0
- X\_3,2,4 -X\_3,7,4 0
- X\_3,2,4 -X\_3,8,4 0
- X\_3,2,4 -X\_3,9,4 0
- X\_3,3,4 -X\_3,4,4 0
- X\_3,3,4 -X\_3,5,4 0
- X\_3,3,4 -X\_3,6,4 0
- X\_3,3,4 -X\_3,7,4 0
- X\_3,3,4 -X\_3,8,4 0
- X\_3,3,4 -X\_3,9,4 0
- X\_3,4,4 -X\_3,5,4 0
- X\_3,4,4 -X\_3,6,4 0
- X\_3,4,4 -X\_3,7,4 0
- X\_3,4,4 -X\_3,8,4 0
- X\_3,4,4 -X\_3,9,4 0
- X\_3,5,4 -X\_3,6,4 0
- X\_3,5,4 -X\_3,7,4 0
- X\_3,5,4 -X\_3,8,4 0
- X\_3,5,4 -X\_3,9,4 0
- X\_3,6,4 -X\_3,7,4 0
- X\_3,6,4 -X\_3,8,4 0
- X\_3,6,4 -X\_3,9,4 0
- X\_3,7,4 -X\_3,8,4 0
- X\_3,7,4 -X\_3,9,4 0
- X\_3,8,4 -X\_3,9,4 0

X\_3,1,5 X\_3,2,5 X\_3,3,5 X\_3,4,5 X\_3,5,5 X\_3,6,5 X\_3,7,5 X\_3,8,5 X\_3,9,5 0

- X\_3,1,5 -X\_3,2,5 0
- X\_3,1,5 -X\_3,3,5 0
- X\_3,1,5 -X\_3,4,5 0
- X\_3,1,5 -X\_3,5,5 0
- X\_3,1,5 -X\_3,6,5 0
- X\_3,1,5 -X\_3,7,5 0
- X\_3,1,5 -X\_3,8,5 0
- X\_3,1,5 -X\_3,9,5 0
- X\_3,2,5 -X\_3,3,5 0
- X\_3,2,5 -X\_3,4,5 0
- X\_3,2,5 -X\_3,5,5 0
- X\_3,2,5 -X\_3,6,5 0
- X\_3,2,5 -X\_3,7,5 0
- X\_3,2,5 -X\_3,8,5 0
- X\_3,2,5 -X\_3,9,5 0
- X\_3,3,5 -X\_3,4,5 0
- X\_3,3,5 -X\_3,5,5 0
- X\_3,3,5 -X\_3,6,5 0
- X\_3,3,5 -X\_3,7,5 0
- X\_3,3,5 -X\_3,8,5 0
- X\_3,3,5 -X\_3,9,5 0
- X\_3,4,5 -X\_3,5,5 0
- X\_3,4,5 -X\_3,6,5 0
- X\_3,4,5 -X\_3,7,5 0
- X\_3,4,5 -X\_3,8,5 0
- X\_3,4,5 -X\_3,9,5 0
- X\_3,5,5 -X\_3,6,5 0
- X\_3,5,5 -X\_3,7,5 0
- X\_3,5,5 -X\_3,8,5 0
- X\_3,5,5 -X\_3,9,5 0
- X\_3,6,5 -X\_3,7,5 0
- X\_3,6,5 -X\_3,8,5 0
- X\_3,6,5 -X\_3,9,5 0
- X\_3,7,5 -X\_3,8,5 0
- X\_3,7,5 -X\_3,9,5 0
- X\_3,8,5 -X\_3,9,5 0

X\_3,1,6 X\_3,2,6 X\_3,3,6 X\_3,4,6 X\_3,5,6 X\_3,6,6 X\_3,7,6 X\_3,8,6 X\_3,9,6 0

- X\_3,1,6 -X\_3,2,6 0
- X\_3,1,6 -X\_3,3,6 0
- X\_3,1,6 -X\_3,4,6 0
- X\_3,1,6 -X\_3,5,6 0
- X\_3,1,6 -X\_3,6,6 0
- X\_3,1,6 -X\_3,7,6 0
- X\_3,1,6 -X\_3,8,6 0
- X\_3,1,6 -X\_3,9,6 0
- X\_3,2,6 -X\_3,3,6 0
- X\_3,2,6 -X\_3,4,6 0
- X\_3,2,6 -X\_3,5,6 0
- X\_3,2,6 -X\_3,6,6 0
- X\_3,2,6 -X\_3,7,6 0
- X\_3,2,6 -X\_3,8,6 0
- X\_3,2,6 -X\_3,9,6 0
- X\_3,3,6 -X\_3,4,6 0
- X\_3,3,6 -X\_3,5,6 0
- X\_3,3,6 -X\_3,6,6 0
- X\_3,3,6 -X\_3,7,6 0
- X\_3,3,6 -X\_3,8,6 0
- X\_3,3,6 -X\_3,9,6 0
- X\_3,4,6 -X\_3,5,6 0
- X\_3,4,6 -X\_3,6,6 0
- X\_3,4,6 -X\_3,7,6 0
- X\_3,4,6 -X\_3,8,6 0
- X\_3,4,6 -X\_3,9,6 0
- X\_3,5,6 -X\_3,6,6 0
- X\_3,5,6 -X\_3,7,6 0
- X\_3,5,6 -X\_3,8,6 0
- X\_3,5,6 -X\_3,9,6 0
- X\_3,6,6 -X\_3,7,6 0
- X\_3,6,6 -X\_3,8,6 0
- X\_3,6,6 -X\_3,9,6 0
- X\_3,7,6 -X\_3,8,6 0
- X\_3,7,6 -X\_3,9,6 0
- X\_3,8,6 -X\_3,9,6 0

X\_3,1,7 X\_3,2,7 X\_3,3,7 X\_3,4,7 X\_3,5,7 X\_3,6,7 X\_3,7,7 X\_3,8,7 X\_3,9,7 0

- X\_3,1,7 -X\_3,2,7 0
- X\_3,1,7 -X\_3,3,7 0
- X\_3,1,7 -X\_3,4,7 0
- X\_3,1,7 -X\_3,5,7 0
- X\_3,1,7 -X\_3,6,7 0
- X\_3,1,7 -X\_3,7,7 0
- X\_3,1,7 -X\_3,8,7 0
- X\_3,1,7 -X\_3,9,7 0
- X\_3,2,7 -X\_3,3,7 0
- X\_3,2,7 -X\_3,4,7 0
- X\_3,2,7 -X\_3,5,7 0
- X\_3,2,7 -X\_3,6,7 0
- X\_3,2,7 -X\_3,7,7 0
- X\_3,2,7 -X\_3,8,7 0
- X\_3,2,7 -X\_3,9,7 0
- X\_3,3,7 -X\_3,4,7 0
- X\_3,3,7 -X\_3,5,7 0
- X\_3,3,7 -X\_3,6,7 0
- X\_3,3,7 -X\_3,7,7 0
- X\_3,3,7 -X\_3,8,7 0
- X\_3,3,7 -X\_3,9,7 0
- X\_3,4,7 -X\_3,5,7 0
- X\_3,4,7 -X\_3,6,7 0
- X\_3,4,7 -X\_3,7,7 0
- X\_3,4,7 -X\_3,8,7 0
- X\_3,4,7 -X\_3,9,7 0
- X\_3,5,7 -X\_3,6,7 0
- X\_3,5,7 -X\_3,7,7 0
- X\_3,5,7 -X\_3,8,7 0
- X\_3,5,7 -X\_3,9,7 0
- X\_3,6,7 -X\_3,7,7 0
- X\_3,6,7 -X\_3,8,7 0
- X\_3,6,7 -X\_3,9,7 0
- X\_3,7,7 -X\_3,8,7 0
- X\_3,7,7 -X\_3,9,7 0
- X\_3,8,7 -X\_3,9,7 0

X\_3,1,8 X\_3,2,8 X\_3,3,8 X\_3,4,8 X\_3,5,8 X\_3,6,8 X\_3,7,8 X\_3,8,8 X\_3,9,8 0

- X\_3,1,8 -X\_3,2,8 0
- X\_3,1,8 -X\_3,3,8 0
- X\_3,1,8 -X\_3,4,8 0
- X\_3,1,8 -X\_3,5,8 0
- X\_3,1,8 -X\_3,6,8 0
- X\_3,1,8 -X\_3,7,8 0
- X\_3,1,8 -X\_3,8,8 0
- X\_3,1,8 -X\_3,9,8 0
- X\_3,2,8 -X\_3,3,8 0
- X\_3,2,8 -X\_3,4,8 0
- X\_3,2,8 -X\_3,5,8 0
- X\_3,2,8 -X\_3,6,8 0
- X\_3,2,8 -X\_3,7,8 0
- X\_3,2,8 -X\_3,8,8 0
- X\_3,2,8 -X\_3,9,8 0
- X\_3,3,8 -X\_3,4,8 0
- X\_3,3,8 -X\_3,5,8 0
- X\_3,3,8 -X\_3,6,8 0
- X\_3,3,8 -X\_3,7,8 0
- X\_3,3,8 -X\_3,8,8 0
- X\_3,3,8 -X\_3,9,8 0
- X\_3,4,8 -X\_3,5,8 0
- X\_3,4,8 -X\_3,6,8 0
- X\_3,4,8 -X\_3,7,8 0
- X\_3,4,8 -X\_3,8,8 0
- X\_3,4,8 -X\_3,9,8 0
- X\_3,5,8 -X\_3,6,8 0
- X\_3,5,8 -X\_3,7,8 0
- X\_3,5,8 -X\_3,8,8 0
- X\_3,5,8 -X\_3,9,8 0
- X\_3,6,8 -X\_3,7,8 0
- X\_3,6,8 -X\_3,8,8 0
- X\_3,6,8 -X\_3,9,8 0
- X\_3,7,8 -X\_3,8,8 0
- X\_3,7,8 -X\_3,9,8 0
- X\_3,8,8 -X\_3,9,8 0

X\_3,1,9 X\_3,2,9 X\_3,3,9 X\_3,4,9 X\_3,5,9 X\_3,6,9 X\_3,7,9 X\_3,8,9 X\_3,9,9 0

- X\_3,1,9 -X\_3,2,9 0
- X\_3,1,9 -X\_3,3,9 0
- X\_3,1,9 -X\_3,4,9 0
- X\_3,1,9 -X\_3,5,9 0
- X\_3,1,9 -X\_3,6,9 0
- X\_3,1,9 -X\_3,7,9 0
- X\_3,1,9 -X\_3,8,9 0
- X\_3,1,9 -X\_3,9,9 0
- X\_3,2,9 -X\_3,3,9 0
- X\_3,2,9 -X\_3,4,9 0
- X\_3,2,9 -X\_3,5,9 0
- X\_3,2,9 -X\_3,6,9 0
- X\_3,2,9 -X\_3,7,9 0
- X\_3,2,9 -X\_3,8,9 0
- X\_3,2,9 -X\_3,9,9 0
- X\_3,3,9 -X\_3,4,9 0
- X\_3,3,9 -X\_3,5,9 0
- X\_3,3,9 -X\_3,6,9 0
- X\_3,3,9 -X\_3,7,9 0
- X\_3,3,9 -X\_3,8,9 0
- X\_3,3,9 -X\_3,9,9 0
- X\_3,4,9 -X\_3,5,9 0
- X\_3,4,9 -X\_3,6,9 0
- X\_3,4,9 -X\_3,7,9 0
- X\_3,4,9 -X\_3,8,9 0
- X\_3,4,9 -X\_3,9,9 0
- X\_3,5,9 -X\_3,6,9 0
- X\_3,5,9 -X\_3,7,9 0
- X\_3,5,9 -X\_3,8,9 0
- X\_3,5,9 -X\_3,9,9 0
- X\_3,6,9 -X\_3,7,9 0
- X\_3,6,9 -X\_3,8,9 0
- X\_3,6,9 -X\_3,9,9 0
- X\_3,7,9 -X\_3,8,9 0
- X\_3,7,9 -X\_3,9,9 0
- X\_3,8,9 -X\_3,9,9 0

X\_4,1,1 X\_4,2,1 X\_4,3,1 X\_4,4,1 X\_4,5,1 X\_4,6,1 X\_4,7,1 X\_4,8,1 X\_4,9,1 0

- X\_4,1,1 -X\_4,2,1 0
- X\_4,1,1 -X\_4,3,1 0
- X\_4,1,1 -X\_4,4,1 0
- X\_4,1,1 -X\_4,5,1 0
- X\_4,1,1 -X\_4,6,1 0
- X\_4,1,1 -X\_4,7,1 0
- X\_4,1,1 -X\_4,8,1 0
- X\_4,1,1 -X\_4,9,1 0
- X\_4,2,1 -X\_4,3,1 0
- X\_4,2,1 -X\_4,4,1 0
- X\_4,2,1 -X\_4,5,1 0
- X\_4,2,1 -X\_4,6,1 0
- X\_4,2,1 -X\_4,7,1 0
- X\_4,2,1 -X\_4,8,1 0
- X\_4,2,1 -X\_4,9,1 0
- X\_4,3,1 -X\_4,4,1 0
- X\_4,3,1 -X\_4,5,1 0
- X\_4,3,1 -X\_4,6,1 0
- X\_4,3,1 -X\_4,7,1 0
- X\_4,3,1 -X\_4,8,1 0
- X\_4,3,1 -X\_4,9,1 0
- X\_4,4,1 -X\_4,5,1 0
- X\_4,4,1 -X\_4,6,1 0
- X\_4,4,1 -X\_4,7,1 0
- X\_4,4,1 -X\_4,8,1 0
- X\_4,4,1 -X\_4,9,1 0
- X\_4,5,1 -X\_4,6,1 0
- X\_4,5,1 -X\_4,7,1 0
- X\_4,5,1 -X\_4,8,1 0
- X\_4,5,1 -X\_4,9,1 0
- X\_4,6,1 -X\_4,7,1 0
- X\_4,6,1 -X\_4,8,1 0
- X\_4,6,1 -X\_4,9,1 0
- X\_4,7,1 -X\_4,8,1 0
- X\_4,7,1 -X\_4,9,1 0
- X\_4,8,1 -X\_4,9,1 0

X\_4,1,2 X\_4,2,2 X\_4,3,2 X\_4,4,2 X\_4,5,2 X\_4,6,2 X\_4,7,2 X\_4,8,2 X\_4,9,2 0

- X\_4,1,2 -X\_4,2,2 0
- X\_4,1,2 -X\_4,3,2 0
- X\_4,1,2 -X\_4,4,2 0
- X\_4,1,2 -X\_4,5,2 0
- X\_4,1,2 -X\_4,6,2 0
- X\_4,1,2 -X\_4,7,2 0
- X\_4,1,2 -X\_4,8,2 0
- X\_4,1,2 -X\_4,9,2 0
- X\_4,2,2 -X\_4,3,2 0
- X\_4,2,2 -X\_4,4,2 0
- X\_4,2,2 -X\_4,5,2 0
- X\_4,2,2 -X\_4,6,2 0
- X\_4,2,2 -X\_4,7,2 0
- X\_4,2,2 -X\_4,8,2 0
- X\_4,2,2 -X\_4,9,2 0
- X\_4,3,2 -X\_4,4,2 0
- X\_4,3,2 -X\_4,5,2 0
- X\_4,3,2 -X\_4,6,2 0
- X\_4,3,2 -X\_4,7,2 0
- X\_4,3,2 -X\_4,8,2 0
- X\_4,3,2 -X\_4,9,2 0
- X\_4,4,2 -X\_4,5,2 0
- X\_4,4,2 -X\_4,6,2 0
- X\_4,4,2 -X\_4,7,2 0
- X\_4,4,2 -X\_4,8,2 0
- X\_4,4,2 -X\_4,9,2 0
- X\_4,5,2 -X\_4,6,2 0
- X\_4,5,2 -X\_4,7,2 0
- X\_4,5,2 -X\_4,8,2 0
- X\_4,5,2 -X\_4,9,2 0
- X\_4,6,2 -X\_4,7,2 0
- X\_4,6,2 -X\_4,8,2 0
- X\_4,6,2 -X\_4,9,2 0
- X\_4,7,2 -X\_4,8,2 0
- X\_4,7,2 -X\_4,9,2 0
- X\_4,8,2 -X\_4,9,2 0

X\_4,1,3 X\_4,2,3 X\_4,3,3 X\_4,4,3 X\_4,5,3 X\_4,6,3 X\_4,7,3 X\_4,8,3 X\_4,9,3 0

- X\_4,1,3 -X\_4,2,3 0
- X\_4,1,3 -X\_4,3,3 0
- X\_4,1,3 -X\_4,4,3 0
- X\_4,1,3 -X\_4,5,3 0
- X\_4,1,3 -X\_4,6,3 0
- X\_4,1,3 -X\_4,7,3 0
- X\_4,1,3 -X\_4,8,3 0
- X\_4,1,3 -X\_4,9,3 0
- X\_4,2,3 -X\_4,3,3 0
- X\_4,2,3 -X\_4,4,3 0
- X\_4,2,3 -X\_4,5,3 0
- X\_4,2,3 -X\_4,6,3 0
- X\_4,2,3 -X\_4,7,3 0
- X\_4,2,3 -X\_4,8,3 0
- X\_4,2,3 -X\_4,9,3 0
- X\_4,3,3 -X\_4,4,3 0
- X\_4,3,3 -X\_4,5,3 0
- X\_4,3,3 -X\_4,6,3 0
- X\_4,3,3 -X\_4,7,3 0
- X\_4,3,3 -X\_4,8,3 0
- X\_4,3,3 -X\_4,9,3 0
- X\_4,4,3 -X\_4,5,3 0
- X\_4,4,3 -X\_4,6,3 0
- X\_4,4,3 -X\_4,7,3 0
- X\_4,4,3 -X\_4,8,3 0
- X\_4,4,3 -X\_4,9,3 0
- X\_4,5,3 -X\_4,6,3 0
- X\_4,5,3 -X\_4,7,3 0
- X\_4,5,3 -X\_4,8,3 0
- X\_4,5,3 -X\_4,9,3 0
- X\_4,6,3 -X\_4,7,3 0
- X\_4,6,3 -X\_4,8,3 0
- X\_4,6,3 -X\_4,9,3 0
- X\_4,7,3 -X\_4,8,3 0
- X\_4,7,3 -X\_4,9,3 0
- X\_4,8,3 -X\_4,9,3 0

X\_4,1,4 X\_4,2,4 X\_4,3,4 X\_4,4,4 X\_4,5,4 X\_4,6,4 X\_4,7,4 X\_4,8,4 X\_4,9,4 0

- X\_4,1,4 -X\_4,2,4 0
- X\_4,1,4 -X\_4,3,4 0
- X\_4,1,4 -X\_4,4,4 0
- X\_4,1,4 -X\_4,5,4 0
- X\_4,1,4 -X\_4,6,4 0
- X\_4,1,4 -X\_4,7,4 0
- X\_4,1,4 -X\_4,8,4 0
- X\_4,1,4 -X\_4,9,4 0
- X\_4,2,4 -X\_4,3,4 0
- X\_4,2,4 -X\_4,4,4 0
- X\_4,2,4 -X\_4,5,4 0
- X\_4,2,4 -X\_4,6,4 0
- X\_4,2,4 -X\_4,7,4 0
- X\_4,2,4 -X\_4,8,4 0
- X\_4,2,4 -X\_4,9,4 0
- X\_4,3,4 -X\_4,4,4 0
- X\_4,3,4 -X\_4,5,4 0
- X\_4,3,4 -X\_4,6,4 0
- X\_4,3,4 -X\_4,7,4 0
- X\_4,3,4 -X\_4,8,4 0
- X\_4,3,4 -X\_4,9,4 0
- X\_4,4,4 -X\_4,5,4 0
- X\_4,4,4 -X\_4,6,4 0
- X\_4,4,4 -X\_4,7,4 0
- X\_4,4,4 -X\_4,8,4 0
- X\_4,4,4 -X\_4,9,4 0
- X\_4,5,4 -X\_4,6,4 0
- X\_4,5,4 -X\_4,7,4 0
- X\_4,5,4 -X\_4,8,4 0
- X\_4,5,4 -X\_4,9,4 0
- X\_4,6,4 -X\_4,7,4 0
- X\_4,6,4 -X\_4,8,4 0
- X\_4,6,4 -X\_4,9,4 0
- X\_4,7,4 -X\_4,8,4 0
- X\_4,7,4 -X\_4,9,4 0
- X\_4,8,4 -X\_4,9,4 0

X\_4,1,5 X\_4,2,5 X\_4,3,5 X\_4,4,5 X\_4,5,5 X\_4,6,5 X\_4,7,5 X\_4,8,5 X\_4,9,5 0

- X\_4,1,5 -X\_4,2,5 0
- X\_4,1,5 -X\_4,3,5 0
- X\_4,1,5 -X\_4,4,5 0
- X\_4,1,5 -X\_4,5,5 0
- X\_4,1,5 -X\_4,6,5 0
- X\_4,1,5 -X\_4,7,5 0
- X\_4,1,5 -X\_4,8,5 0
- X\_4,1,5 -X\_4,9,5 0
- X\_4,2,5 -X\_4,3,5 0
- X\_4,2,5 -X\_4,4,5 0
- X\_4,2,5 -X\_4,5,5 0
- X\_4,2,5 -X\_4,6,5 0
- X\_4,2,5 -X\_4,7,5 0
- X\_4,2,5 -X\_4,8,5 0
- X\_4,2,5 -X\_4,9,5 0
- X\_4,3,5 -X\_4,4,5 0
- X\_4,3,5 -X\_4,5,5 0
- X\_4,3,5 -X\_4,6,5 0
- X\_4,3,5 -X\_4,7,5 0
- X\_4,3,5 -X\_4,8,5 0
- X\_4,3,5 -X\_4,9,5 0
- X\_4,4,5 -X\_4,5,5 0
- X\_4,4,5 -X\_4,6,5 0
- X\_4,4,5 -X\_4,7,5 0
- X\_4,4,5 -X\_4,8,5 0
- X\_4,4,5 -X\_4,9,5 0
- X\_4,5,5 -X\_4,6,5 0
- X\_4,5,5 -X\_4,7,5 0
- X\_4,5,5 -X\_4,8,5 0
- X\_4,5,5 -X\_4,9,5 0
- X\_4,6,5 -X\_4,7,5 0
- X\_4,6,5 -X\_4,8,5 0
- X\_4,6,5 -X\_4,9,5 0
- X\_4,7,5 -X\_4,8,5 0
- X\_4,7,5 -X\_4,9,5 0
- X\_4,8,5 -X\_4,9,5 0

X\_4,1,6 X\_4,2,6 X\_4,3,6 X\_4,4,6 X\_4,5,6 X\_4,6,6 X\_4,7,6 X\_4,8,6 X\_4,9,6 0

- X\_4,1,6 -X\_4,2,6 0
- X\_4,1,6 -X\_4,3,6 0
- X\_4,1,6 -X\_4,4,6 0
- X\_4,1,6 -X\_4,5,6 0
- X\_4,1,6 -X\_4,6,6 0
- X\_4,1,6 -X\_4,7,6 0
- X\_4,1,6 -X\_4,8,6 0
- X\_4,1,6 -X\_4,9,6 0
- X\_4,2,6 -X\_4,3,6 0
- X\_4,2,6 -X\_4,4,6 0
- X\_4,2,6 -X\_4,5,6 0
- X\_4,2,6 -X\_4,6,6 0
- X\_4,2,6 -X\_4,7,6 0
- X\_4,2,6 -X\_4,8,6 0
- X\_4,2,6 -X\_4,9,6 0
- X\_4,3,6 -X\_4,4,6 0
- X\_4,3,6 -X\_4,5,6 0
- X\_4,3,6 -X\_4,6,6 0
- X\_4,3,6 -X\_4,7,6 0
- X\_4,3,6 -X\_4,8,6 0
- X\_4,3,6 -X\_4,9,6 0
- X\_4,4,6 -X\_4,5,6 0
- X\_4,4,6 -X\_4,6,6 0
- X\_4,4,6 -X\_4,7,6 0
- X\_4,4,6 -X\_4,8,6 0
- X\_4,4,6 -X\_4,9,6 0
- X\_4,5,6 -X\_4,6,6 0
- X\_4,5,6 -X\_4,7,6 0
- X\_4,5,6 -X\_4,8,6 0
- X\_4,5,6 -X\_4,9,6 0
- X\_4,6,6 -X\_4,7,6 0
- X\_4,6,6 -X\_4,8,6 0
- X\_4,6,6 -X\_4,9,6 0
- X\_4,7,6 -X\_4,8,6 0
- X\_4,7,6 -X\_4,9,6 0
- X\_4,8,6 -X\_4,9,6 0

X\_4,1,7 X\_4,2,7 X\_4,3,7 X\_4,4,7 X\_4,5,7 X\_4,6,7 X\_4,7,7 X\_4,8,7 X\_4,9,7 0

- X\_4,1,7 -X\_4,2,7 0
- X\_4,1,7 -X\_4,3,7 0
- X\_4,1,7 -X\_4,4,7 0
- X\_4,1,7 -X\_4,5,7 0
- X\_4,1,7 -X\_4,6,7 0
- X\_4,1,7 -X\_4,7,7 0
- X\_4,1,7 -X\_4,8,7 0
- X\_4,1,7 -X\_4,9,7 0
- X\_4,2,7 -X\_4,3,7 0
- X\_4,2,7 -X\_4,4,7 0
- X\_4,2,7 -X\_4,5,7 0
- X\_4,2,7 -X\_4,6,7 0
- X\_4,2,7 -X\_4,7,7 0
- X\_4,2,7 -X\_4,8,7 0
- X\_4,2,7 -X\_4,9,7 0
- X\_4,3,7 -X\_4,4,7 0
- X\_4,3,7 -X\_4,5,7 0
- X\_4,3,7 -X\_4,6,7 0
- X\_4,3,7 -X\_4,7,7 0
- X\_4,3,7 -X\_4,8,7 0
- X\_4,3,7 -X\_4,9,7 0
- X\_4,4,7 -X\_4,5,7 0
- X\_4,4,7 -X\_4,6,7 0
- X\_4,4,7 -X\_4,7,7 0
- X\_4,4,7 -X\_4,8,7 0
- X\_4,4,7 -X\_4,9,7 0
- X\_4,5,7 -X\_4,6,7 0
- X\_4,5,7 -X\_4,7,7 0
- X\_4,5,7 -X\_4,8,7 0
- X\_4,5,7 -X\_4,9,7 0
- X\_4,6,7 -X\_4,7,7 0
- X\_4,6,7 -X\_4,8,7 0
- X\_4,6,7 -X\_4,9,7 0
- X\_4,7,7 -X\_4,8,7 0
- X\_4,7,7 -X\_4,9,7 0
- X\_4,8,7 -X\_4,9,7 0

X\_4,1,8 X\_4,2,8 X\_4,3,8 X\_4,4,8 X\_4,5,8 X\_4,6,8 X\_4,7,8 X\_4,8,8 X\_4,9,8 0

- X\_4,1,8 -X\_4,2,8 0
- X\_4,1,8 -X\_4,3,8 0
- X\_4,1,8 -X\_4,4,8 0
- X\_4,1,8 -X\_4,5,8 0
- X\_4,1,8 -X\_4,6,8 0
- X\_4,1,8 -X\_4,7,8 0
- X\_4,1,8 -X\_4,8,8 0
- X\_4,1,8 -X\_4,9,8 0
- X\_4,2,8 -X\_4,3,8 0
- X\_4,2,8 -X\_4,4,8 0
- X\_4,2,8 -X\_4,5,8 0
- X\_4,2,8 -X\_4,6,8 0
- X\_4,2,8 -X\_4,7,8 0
- X\_4,2,8 -X\_4,8,8 0
- X\_4,2,8 -X\_4,9,8 0
- X\_4,3,8 -X\_4,4,8 0
- X\_4,3,8 -X\_4,5,8 0
- X\_4,3,8 -X\_4,6,8 0
- X\_4,3,8 -X\_4,7,8 0
- X\_4,3,8 -X\_4,8,8 0
- X\_4,3,8 -X\_4,9,8 0
- X\_4,4,8 -X\_4,5,8 0
- X\_4,4,8 -X\_4,6,8 0
- X\_4,4,8 -X\_4,7,8 0
- X\_4,4,8 -X\_4,8,8 0
- X\_4,4,8 -X\_4,9,8 0
- X\_4,5,8 -X\_4,6,8 0
- X\_4,5,8 -X\_4,7,8 0
- X\_4,5,8 -X\_4,8,8 0
- X\_4,5,8 -X\_4,9,8 0
- X\_4,6,8 -X\_4,7,8 0
- X\_4,6,8 -X\_4,8,8 0
- X\_4,6,8 -X\_4,9,8 0
- X\_4,7,8 -X\_4,8,8 0
- X\_4,7,8 -X\_4,9,8 0
- X\_4,8,8 -X\_4,9,8 0

X\_4,1,9 X\_4,2,9 X\_4,3,9 X\_4,4,9 X\_4,5,9 X\_4,6,9 X\_4,7,9 X\_4,8,9 X\_4,9,9 0

- X\_4,1,9 -X\_4,2,9 0
- X\_4,1,9 -X\_4,3,9 0
- X\_4,1,9 -X\_4,4,9 0
- X\_4,1,9 -X\_4,5,9 0
- X\_4,1,9 -X\_4,6,9 0
- X\_4,1,9 -X\_4,7,9 0
- X\_4,1,9 -X\_4,8,9 0
- X\_4,1,9 -X\_4,9,9 0
- X\_4,2,9 -X\_4,3,9 0
- X\_4,2,9 -X\_4,4,9 0
- X\_4,2,9 -X\_4,5,9 0
- X\_4,2,9 -X\_4,6,9 0
- X\_4,2,9 -X\_4,7,9 0
- X\_4,2,9 -X\_4,8,9 0
- X\_4,2,9 -X\_4,9,9 0
- X\_4,3,9 -X\_4,4,9 0
- X\_4,3,9 -X\_4,5,9 0
- X\_4,3,9 -X\_4,6,9 0
- X\_4,3,9 -X\_4,7,9 0
- X\_4,3,9 -X\_4,8,9 0
- X\_4,3,9 -X\_4,9,9 0
- X\_4,4,9 -X\_4,5,9 0
- X\_4,4,9 -X\_4,6,9 0
- X\_4,4,9 -X\_4,7,9 0
- X\_4,4,9 -X\_4,8,9 0
- X\_4,4,9 -X\_4,9,9 0
- X\_4,5,9 -X\_4,6,9 0
- X\_4,5,9 -X\_4,7,9 0
- X\_4,5,9 -X\_4,8,9 0
- X\_4,5,9 -X\_4,9,9 0
- X\_4,6,9 -X\_4,7,9 0
- X\_4,6,9 -X\_4,8,9 0
- X\_4,6,9 -X\_4,9,9 0
- X\_4,7,9 -X\_4,8,9 0
- X\_4,7,9 -X\_4,9,9 0
- X\_4,8,9 -X\_4,9,9 0

X\_5,1,1 X\_5,2,1 X\_5,3,1 X\_5,4,1 X\_5,5,1 X\_5,6,1 X\_5,7,1 X\_5,8,1 X\_5,9,1 0

- X\_5,1,1 -X\_5,2,1 0
- X\_5,1,1 -X\_5,3,1 0
- X\_5,1,1 -X\_5,4,1 0
- X\_5,1,1 -X\_5,5,1 0
- X\_5,1,1 -X\_5,6,1 0
- X\_5,1,1 -X\_5,7,1 0
- X\_5,1,1 -X\_5,8,1 0
- X\_5,1,1 -X\_5,9,1 0
- X\_5,2,1 -X\_5,3,1 0
- X\_5,2,1 -X\_5,4,1 0
- X\_5,2,1 -X\_5,5,1 0
- X\_5,2,1 -X\_5,6,1 0
- X\_5,2,1 -X\_5,7,1 0
- X\_5,2,1 -X\_5,8,1 0
- X\_5,2,1 -X\_5,9,1 0
- X\_5,3,1 -X\_5,4,1 0
- X\_5,3,1 -X\_5,5,1 0
- X\_5,3,1 -X\_5,6,1 0
- X\_5,3,1 -X\_5,7,1 0
- X\_5,3,1 -X\_5,8,1 0
- X\_5,3,1 -X\_5,9,1 0
- X\_5,4,1 -X\_5,5,1 0
- X\_5,4,1 -X\_5,6,1 0
- X\_5,4,1 -X\_5,7,1 0
- X\_5,4,1 -X\_5,8,1 0
- X\_5,4,1 -X\_5,9,1 0
- X\_5,5,1 -X\_5,6,1 0
- X\_5,5,1 -X\_5,7,1 0
- X\_5,5,1 -X\_5,8,1 0
- X\_5,5,1 -X\_5,9,1 0
- X\_5,6,1 -X\_5,7,1 0
- X\_5,6,1 -X\_5,8,1 0
- X\_5,6,1 -X\_5,9,1 0
- X\_5,7,1 -X\_5,8,1 0
- X\_5,7,1 -X\_5,9,1 0
- X\_5,8,1 -X\_5,9,1 0

X\_5,1,2 X\_5,2,2 X\_5,3,2 X\_5,4,2 X\_5,5,2 X\_5,6,2 X\_5,7,2 X\_5,8,2 X\_5,9,2 0

- X\_5,1,2 -X\_5,2,2 0
- X\_5,1,2 -X\_5,3,2 0
- X\_5,1,2 -X\_5,4,2 0
- X\_5,1,2 -X\_5,5,2 0
- X\_5,1,2 -X\_5,6,2 0
- X\_5,1,2 -X\_5,7,2 0
- X\_5,1,2 -X\_5,8,2 0
- X\_5,1,2 -X\_5,9,2 0
- X\_5,2,2 -X\_5,3,2 0
- X\_5,2,2 -X\_5,4,2 0
- X\_5,2,2 -X\_5,5,2 0
- X\_5,2,2 -X\_5,6,2 0
- X\_5,2,2 -X\_5,7,2 0
- X\_5,2,2 -X\_5,8,2 0
- X\_5,2,2 -X\_5,9,2 0
- X\_5,3,2 -X\_5,4,2 0
- X\_5,3,2 -X\_5,5,2 0
- X\_5,3,2 -X\_5,6,2 0
- X\_5,3,2 -X\_5,7,2 0
- X\_5,3,2 -X\_5,8,2 0
- X\_5,3,2 -X\_5,9,2 0
- X\_5,4,2 -X\_5,5,2 0
- X\_5,4,2 -X\_5,6,2 0
- X\_5,4,2 -X\_5,7,2 0
- X\_5,4,2 -X\_5,8,2 0
- X\_5,4,2 -X\_5,9,2 0
- X\_5,5,2 -X\_5,6,2 0
- X\_5,5,2 -X\_5,7,2 0
- X\_5,5,2 -X\_5,8,2 0
- X\_5,5,2 -X\_5,9,2 0
- X\_5,6,2 -X\_5,7,2 0
- X\_5,6,2 -X\_5,8,2 0
- X\_5,6,2 -X\_5,9,2 0
- X\_5,7,2 -X\_5,8,2 0
- X\_5,7,2 -X\_5,9,2 0
- X\_5,8,2 -X\_5,9,2 0

X\_5,1,3 X\_5,2,3 X\_5,3,3 X\_5,4,3 X\_5,5,3 X\_5,6,3 X\_5,7,3 X\_5,8,3 X\_5,9,3 0

- X\_5,1,3 -X\_5,2,3 0
- X\_5,1,3 -X\_5,3,3 0
- X\_5,1,3 -X\_5,4,3 0
- X\_5,1,3 -X\_5,5,3 0
- X\_5,1,3 -X\_5,6,3 0
- X\_5,1,3 -X\_5,7,3 0
- X\_5,1,3 -X\_5,8,3 0
- X\_5,1,3 -X\_5,9,3 0
- X\_5,2,3 -X\_5,3,3 0
- X\_5,2,3 -X\_5,4,3 0
- X\_5,2,3 -X\_5,5,3 0
- X\_5,2,3 -X\_5,6,3 0
- X\_5,2,3 -X\_5,7,3 0
- X\_5,2,3 -X\_5,8,3 0
- X\_5,2,3 -X\_5,9,3 0
- X\_5,3,3 -X\_5,4,3 0
- X\_5,3,3 -X\_5,5,3 0
- X\_5,3,3 -X\_5,6,3 0
- X\_5,3,3 -X\_5,7,3 0
- X\_5,3,3 -X\_5,8,3 0
- X\_5,3,3 -X\_5,9,3 0
- X\_5,4,3 -X\_5,5,3 0
- X\_5,4,3 -X\_5,6,3 0
- X\_5,4,3 -X\_5,7,3 0
- X\_5,4,3 -X\_5,8,3 0
- X\_5,4,3 -X\_5,9,3 0
- X\_5,5,3 -X\_5,6,3 0
- X\_5,5,3 -X\_5,7,3 0
- X\_5,5,3 -X\_5,8,3 0
- X\_5,5,3 -X\_5,9,3 0
- X\_5,6,3 -X\_5,7,3 0
- X\_5,6,3 -X\_5,8,3 0
- X\_5,6,3 -X\_5,9,3 0
- X\_5,7,3 -X\_5,8,3 0
- X\_5,7,3 -X\_5,9,3 0
- X\_5,8,3 -X\_5,9,3 0

X\_5,1,4 X\_5,2,4 X\_5,3,4 X\_5,4,4 X\_5,5,4 X\_5,6,4 X\_5,7,4 X\_5,8,4 X\_5,9,4 0

- X\_5,1,4 -X\_5,2,4 0
- X\_5,1,4 -X\_5,3,4 0
- X\_5,1,4 -X\_5,4,4 0
- X\_5,1,4 -X\_5,5,4 0
- X\_5,1,4 -X\_5,6,4 0
- X\_5,1,4 -X\_5,7,4 0
- X\_5,1,4 -X\_5,8,4 0
- X\_5,1,4 -X\_5,9,4 0
- X\_5,2,4 -X\_5,3,4 0
- X\_5,2,4 -X\_5,4,4 0
- X\_5,2,4 -X\_5,5,4 0
- X\_5,2,4 -X\_5,6,4 0
- X\_5,2,4 -X\_5,7,4 0
- X\_5,2,4 -X\_5,8,4 0
- X\_5,2,4 -X\_5,9,4 0
- X\_5,3,4 -X\_5,4,4 0
- X\_5,3,4 -X\_5,5,4 0
- X\_5,3,4 -X\_5,6,4 0
- X\_5,3,4 -X\_5,7,4 0
- X\_5,3,4 -X\_5,8,4 0
- X\_5,3,4 -X\_5,9,4 0
- X\_5,4,4 -X\_5,5,4 0
- X\_5,4,4 -X\_5,6,4 0
- X\_5,4,4 -X\_5,7,4 0
- X\_5,4,4 -X\_5,8,4 0
- X\_5,4,4 -X\_5,9,4 0
- X\_5,5,4 -X\_5,6,4 0
- X\_5,5,4 -X\_5,7,4 0
- X\_5,5,4 -X\_5,8,4 0
- X\_5,5,4 -X\_5,9,4 0
- X\_5,6,4 -X\_5,7,4 0
- X\_5,6,4 -X\_5,8,4 0
- X\_5,6,4 -X\_5,9,4 0
- X\_5,7,4 -X\_5,8,4 0
- X\_5,7,4 -X\_5,9,4 0
- X\_5,8,4 -X\_5,9,4 0

X\_5,1,5 X\_5,2,5 X\_5,3,5 X\_5,4,5 X\_5,5,5 X\_5,6,5 X\_5,7,5 X\_5,8,5 X\_5,9,5 0

- X\_5,1,5 -X\_5,2,5 0
- X\_5,1,5 -X\_5,3,5 0
- X\_5,1,5 -X\_5,4,5 0
- X\_5,1,5 -X\_5,5,5 0
- X\_5,1,5 -X\_5,6,5 0
- X\_5,1,5 -X\_5,7,5 0
- X\_5,1,5 -X\_5,8,5 0
- X\_5,1,5 -X\_5,9,5 0
- X\_5,2,5 -X\_5,3,5 0
- X\_5,2,5 -X\_5,4,5 0
- X\_5,2,5 -X\_5,5,5 0
- X\_5,2,5 -X\_5,6,5 0
- X\_5,2,5 -X\_5,7,5 0
- X\_5,2,5 -X\_5,8,5 0
- X\_5,2,5 -X\_5,9,5 0
- X\_5,3,5 -X\_5,4,5 0
- X\_5,3,5 -X\_5,5,5 0
- X\_5,3,5 -X\_5,6,5 0
- X\_5,3,5 -X\_5,7,5 0
- X\_5,3,5 -X\_5,8,5 0
- X\_5,3,5 -X\_5,9,5 0
- X\_5,4,5 -X\_5,5,5 0
- X\_5,4,5 -X\_5,6,5 0
- X\_5,4,5 -X\_5,7,5 0
- X\_5,4,5 -X\_5,8,5 0
- X\_5,4,5 -X\_5,9,5 0
- X\_5,5,5 -X\_5,6,5 0
- X\_5,5,5 -X\_5,7,5 0
- X\_5,5,5 -X\_5,8,5 0
- X\_5,5,5 -X\_5,9,5 0
- X\_5,6,5 -X\_5,7,5 0
- X\_5,6,5 -X\_5,8,5 0
- X\_5,6,5 -X\_5,9,5 0
- X\_5,7,5 -X\_5,8,5 0
- X\_5,7,5 -X\_5,9,5 0
- X\_5,8,5 -X\_5,9,5 0

X\_5,1,6 X\_5,2,6 X\_5,3,6 X\_5,4,6 X\_5,5,6 X\_5,6,6 X\_5,7,6 X\_5,8,6 X\_5,9,6 0

- X\_5,1,6 -X\_5,2,6 0
- X\_5,1,6 -X\_5,3,6 0
- X\_5,1,6 -X\_5,4,6 0
- X\_5,1,6 -X\_5,5,6 0
- X\_5,1,6 -X\_5,6,6 0
- X\_5,1,6 -X\_5,7,6 0
- X\_5,1,6 -X\_5,8,6 0
- X\_5,1,6 -X\_5,9,6 0
- X\_5,2,6 -X\_5,3,6 0
- X\_5,2,6 -X\_5,4,6 0
- X\_5,2,6 -X\_5,5,6 0
- X\_5,2,6 -X\_5,6,6 0
- X\_5,2,6 -X\_5,7,6 0
- X\_5,2,6 -X\_5,8,6 0
- X\_5,2,6 -X\_5,9,6 0
- X\_5,3,6 -X\_5,4,6 0
- X\_5,3,6 -X\_5,5,6 0
- X\_5,3,6 -X\_5,6,6 0
- X\_5,3,6 -X\_5,7,6 0
- X\_5,3,6 -X\_5,8,6 0
- X\_5,3,6 -X\_5,9,6 0
- X\_5,4,6 -X\_5,5,6 0
- X\_5,4,6 -X\_5,6,6 0
- X\_5,4,6 -X\_5,7,6 0
- X\_5,4,6 -X\_5,8,6 0
- X\_5,4,6 -X\_5,9,6 0
- X\_5,5,6 -X\_5,6,6 0
- X\_5,5,6 -X\_5,7,6 0
- X\_5,5,6 -X\_5,8,6 0
- X\_5,5,6 -X\_5,9,6 0
- X\_5,6,6 -X\_5,7,6 0
- X\_5,6,6 -X\_5,8,6 0
- X\_5,6,6 -X\_5,9,6 0
- X\_5,7,6 -X\_5,8,6 0
- X\_5,7,6 -X\_5,9,6 0
- X\_5,8,6 -X\_5,9,6 0

X\_5,1,7 X\_5,2,7 X\_5,3,7 X\_5,4,7 X\_5,5,7 X\_5,6,7 X\_5,7,7 X\_5,8,7 X\_5,9,7 0

- X\_5,1,7 -X\_5,2,7 0
- X\_5,1,7 -X\_5,3,7 0
- X\_5,1,7 -X\_5,4,7 0
- X\_5,1,7 -X\_5,5,7 0
- X\_5,1,7 -X\_5,6,7 0
- X\_5,1,7 -X\_5,7,7 0
- X\_5,1,7 -X\_5,8,7 0
- X\_5,1,7 -X\_5,9,7 0
- X\_5,2,7 -X\_5,3,7 0
- X\_5,2,7 -X\_5,4,7 0
- X\_5,2,7 -X\_5,5,7 0
- X\_5,2,7 -X\_5,6,7 0
- X\_5,2,7 -X\_5,7,7 0
- X\_5,2,7 -X\_5,8,7 0
- X\_5,2,7 -X\_5,9,7 0
- X\_5,3,7 -X\_5,4,7 0
- X\_5,3,7 -X\_5,5,7 0
- X\_5,3,7 -X\_5,6,7 0
- X\_5,3,7 -X\_5,7,7 0
- X\_5,3,7 -X\_5,8,7 0
- X\_5,3,7 -X\_5,9,7 0
- X\_5,4,7 -X\_5,5,7 0
- X\_5,4,7 -X\_5,6,7 0
- X\_5,4,7 -X\_5,7,7 0
- X\_5,4,7 -X\_5,8,7 0
- X\_5,4,7 -X\_5,9,7 0
- X\_5,5,7 -X\_5,6,7 0
- X\_5,5,7 -X\_5,7,7 0
- X\_5,5,7 -X\_5,8,7 0
- X\_5,5,7 -X\_5,9,7 0
- X\_5,6,7 -X\_5,7,7 0
- X\_5,6,7 -X\_5,8,7 0
- X\_5,6,7 -X\_5,9,7 0
- X\_5,7,7 -X\_5,8,7 0
- X\_5,7,7 -X\_5,9,7 0
- X\_5,8,7 -X\_5,9,7 0

X\_5,1,8 X\_5,2,8 X\_5,3,8 X\_5,4,8 X\_5,5,8 X\_5,6,8 X\_5,7,8 X\_5,8,8 X\_5,9,8 0

- X\_5,1,8 -X\_5,2,8 0
- X\_5,1,8 -X\_5,3,8 0
- X\_5,1,8 -X\_5,4,8 0
- X\_5,1,8 -X\_5,5,8 0
- X\_5,1,8 -X\_5,6,8 0
- X\_5,1,8 -X\_5,7,8 0
- X\_5,1,8 -X\_5,8,8 0
- X\_5,1,8 -X\_5,9,8 0
- X\_5,2,8 -X\_5,3,8 0
- X\_5,2,8 -X\_5,4,8 0
- X\_5,2,8 -X\_5,5,8 0
- X\_5,2,8 -X\_5,6,8 0
- X\_5,2,8 -X\_5,7,8 0
- X\_5,2,8 -X\_5,8,8 0
- X\_5,2,8 -X\_5,9,8 0
- X\_5,3,8 -X\_5,4,8 0
- X\_5,3,8 -X\_5,5,8 0
- X\_5,3,8 -X\_5,6,8 0
- X\_5,3,8 -X\_5,7,8 0
- X\_5,3,8 -X\_5,8,8 0
- X\_5,3,8 -X\_5,9,8 0
- X\_5,4,8 -X\_5,5,8 0
- X\_5,4,8 -X\_5,6,8 0
- X\_5,4,8 -X\_5,7,8 0
- X\_5,4,8 -X\_5,8,8 0
- X\_5,4,8 -X\_5,9,8 0
- X\_5,5,8 -X\_5,6,8 0
- X\_5,5,8 -X\_5,7,8 0
- X\_5,5,8 -X\_5,8,8 0
- X\_5,5,8 -X\_5,9,8 0
- X\_5,6,8 -X\_5,7,8 0
- X\_5,6,8 -X\_5,8,8 0
- X\_5,6,8 -X\_5,9,8 0
- X\_5,7,8 -X\_5,8,8 0
- X\_5,7,8 -X\_5,9,8 0
- X\_5,8,8 -X\_5,9,8 0

X\_5,1,9 X\_5,2,9 X\_5,3,9 X\_5,4,9 X\_5,5,9 X\_5,6,9 X\_5,7,9 X\_5,8,9 X\_5,9,9 0

- X\_5,1,9 -X\_5,2,9 0
- X\_5,1,9 -X\_5,3,9 0
- X\_5,1,9 -X\_5,4,9 0
- X\_5,1,9 -X\_5,5,9 0
- X\_5,1,9 -X\_5,6,9 0
- X\_5,1,9 -X\_5,7,9 0
- X\_5,1,9 -X\_5,8,9 0
- X\_5,1,9 -X\_5,9,9 0
- X\_5,2,9 -X\_5,3,9 0
- X\_5,2,9 -X\_5,4,9 0
- X\_5,2,9 -X\_5,5,9 0
- X\_5,2,9 -X\_5,6,9 0
- X\_5,2,9 -X\_5,7,9 0
- X\_5,2,9 -X\_5,8,9 0
- X\_5,2,9 -X\_5,9,9 0
- X\_5,3,9 -X\_5,4,9 0
- X\_5,3,9 -X\_5,5,9 0
- X\_5,3,9 -X\_5,6,9 0
- X\_5,3,9 -X\_5,7,9 0
- X\_5,3,9 -X\_5,8,9 0
- X\_5,3,9 -X\_5,9,9 0
- X\_5,4,9 -X\_5,5,9 0
- X\_5,4,9 -X\_5,6,9 0
- X\_5,4,9 -X\_5,7,9 0
- X\_5,4,9 -X\_5,8,9 0
- X\_5,4,9 -X\_5,9,9 0
- X\_5,5,9 -X\_5,6,9 0
- X\_5,5,9 -X\_5,7,9 0
- X\_5,5,9 -X\_5,8,9 0
- X\_5,5,9 -X\_5,9,9 0
- X\_5,6,9 -X\_5,7,9 0
- X\_5,6,9 -X\_5,8,9 0
- X\_5,6,9 -X\_5,9,9 0
- X\_5,7,9 -X\_5,8,9 0
- X\_5,7,9 -X\_5,9,9 0
- X\_5,8,9 -X\_5,9,9 0

X\_6,1,1 X\_6,2,1 X\_6,3,1 X\_6,4,1 X\_6,5,1 X\_6,6,1 X\_6,7,1 X\_6,8,1 X\_6,9,1 0

- X\_6,1,1 -X\_6,2,1 0
- X\_6,1,1 -X\_6,3,1 0
- X\_6,1,1 -X\_6,4,1 0
- X\_6,1,1 -X\_6,5,1 0
- X\_6,1,1 -X\_6,6,1 0
- X\_6,1,1 -X\_6,7,1 0
- X\_6,1,1 -X\_6,8,1 0
- X\_6,1,1 -X\_6,9,1 0
- X\_6,2,1 -X\_6,3,1 0
- X\_6,2,1 -X\_6,4,1 0
- X\_6,2,1 -X\_6,5,1 0
- X\_6,2,1 -X\_6,6,1 0
- X\_6,2,1 -X\_6,7,1 0
- X\_6,2,1 -X\_6,8,1 0
- X\_6,2,1 -X\_6,9,1 0
- X\_6,3,1 -X\_6,4,1 0
- X\_6,3,1 -X\_6,5,1 0
- X\_6,3,1 -X\_6,6,1 0
- X\_6,3,1 -X\_6,7,1 0
- X\_6,3,1 -X\_6,8,1 0
- X\_6,3,1 -X\_6,9,1 0
- X\_6,4,1 -X\_6,5,1 0
- X\_6,4,1 -X\_6,6,1 0
- X\_6,4,1 -X\_6,7,1 0
- X\_6,4,1 -X\_6,8,1 0
- X\_6,4,1 -X\_6,9,1 0
- X\_6,5,1 -X\_6,6,1 0
- X\_6,5,1 -X\_6,7,1 0
- X\_6,5,1 -X\_6,8,1 0
- X\_6,5,1 -X\_6,9,1 0
- X\_6,6,1 -X\_6,7,1 0
- X\_6,6,1 -X\_6,8,1 0
- X\_6,6,1 -X\_6,9,1 0
- X\_6,7,1 -X\_6,8,1 0
- X\_6,7,1 -X\_6,9,1 0
- X\_6,8,1 -X\_6,9,1 0

X\_6,1,2 X\_6,2,2 X\_6,3,2 X\_6,4,2 X\_6,5,2 X\_6,6,2 X\_6,7,2 X\_6,8,2 X\_6,9,2 0

- X\_6,1,2 -X\_6,2,2 0
- X\_6,1,2 -X\_6,3,2 0
- X\_6,1,2 -X\_6,4,2 0
- X\_6,1,2 -X\_6,5,2 0
- X\_6,1,2 -X\_6,6,2 0
- X\_6,1,2 -X\_6,7,2 0
- X\_6,1,2 -X\_6,8,2 0
- X\_6,1,2 -X\_6,9,2 0
- X\_6,2,2 -X\_6,3,2 0
- X\_6,2,2 -X\_6,4,2 0
- X\_6,2,2 -X\_6,5,2 0
- X\_6,2,2 -X\_6,6,2 0
- X\_6,2,2 -X\_6,7,2 0
- X\_6,2,2 -X\_6,8,2 0
- X\_6,2,2 -X\_6,9,2 0
- X\_6,3,2 -X\_6,4,2 0
- X\_6,3,2 -X\_6,5,2 0
- X\_6,3,2 -X\_6,6,2 0
- X\_6,3,2 -X\_6,7,2 0
- X\_6,3,2 -X\_6,8,2 0
- X\_6,3,2 -X\_6,9,2 0
- X\_6,4,2 -X\_6,5,2 0
- X\_6,4,2 -X\_6,6,2 0
- X\_6,4,2 -X\_6,7,2 0
- X\_6,4,2 -X\_6,8,2 0
- X\_6,4,2 -X\_6,9,2 0
- X\_6,5,2 -X\_6,6,2 0
- X\_6,5,2 -X\_6,7,2 0
- X\_6,5,2 -X\_6,8,2 0
- X\_6,5,2 -X\_6,9,2 0
- X\_6,6,2 -X\_6,7,2 0
- X\_6,6,2 -X\_6,8,2 0
- X\_6,6,2 -X\_6,9,2 0
- X\_6,7,2 -X\_6,8,2 0
- X\_6,7,2 -X\_6,9,2 0
- X\_6,8,2 -X\_6,9,2 0

X\_6,1,3 X\_6,2,3 X\_6,3,3 X\_6,4,3 X\_6,5,3 X\_6,6,3 X\_6,7,3 X\_6,8,3 X\_6,9,3 0

- X\_6,1,3 -X\_6,2,3 0
- X\_6,1,3 -X\_6,3,3 0
- X\_6,1,3 -X\_6,4,3 0
- X\_6,1,3 -X\_6,5,3 0
- X\_6,1,3 -X\_6,6,3 0
- X\_6,1,3 -X\_6,7,3 0
- X\_6,1,3 -X\_6,8,3 0
- X\_6,1,3 -X\_6,9,3 0
- X\_6,2,3 -X\_6,3,3 0
- X\_6,2,3 -X\_6,4,3 0
- X\_6,2,3 -X\_6,5,3 0
- X\_6,2,3 -X\_6,6,3 0
- X\_6,2,3 -X\_6,7,3 0
- X\_6,2,3 -X\_6,8,3 0
- X\_6,2,3 -X\_6,9,3 0
- X\_6,3,3 -X\_6,4,3 0
- X\_6,3,3 -X\_6,5,3 0
- X\_6,3,3 -X\_6,6,3 0
- X\_6,3,3 -X\_6,7,3 0
- X\_6,3,3 -X\_6,8,3 0
- X\_6,3,3 -X\_6,9,3 0
- X\_6,4,3 -X\_6,5,3 0
- X\_6,4,3 -X\_6,6,3 0
- X\_6,4,3 -X\_6,7,3 0
- X\_6,4,3 -X\_6,8,3 0
- X\_6,4,3 -X\_6,9,3 0
- X\_6,5,3 -X\_6,6,3 0
- X\_6,5,3 -X\_6,7,3 0
- X\_6,5,3 -X\_6,8,3 0
- X\_6,5,3 -X\_6,9,3 0
- X\_6,6,3 -X\_6,7,3 0
- X\_6,6,3 -X\_6,8,3 0
- X\_6,6,3 -X\_6,9,3 0
- X\_6,7,3 -X\_6,8,3 0
- X\_6,7,3 -X\_6,9,3 0
- X\_6,8,3 -X\_6,9,3 0

X\_6,1,4 X\_6,2,4 X\_6,3,4 X\_6,4,4 X\_6,5,4 X\_6,6,4 X\_6,7,4 X\_6,8,4 X\_6,9,4 0

- X\_6,1,4 -X\_6,2,4 0
- X\_6,1,4 -X\_6,3,4 0
- X\_6,1,4 -X\_6,4,4 0
- X\_6,1,4 -X\_6,5,4 0
- X\_6,1,4 -X\_6,6,4 0
- X\_6,1,4 -X\_6,7,4 0
- X\_6,1,4 -X\_6,8,4 0
- X\_6,1,4 -X\_6,9,4 0
- X\_6,2,4 -X\_6,3,4 0
- X\_6,2,4 -X\_6,4,4 0
- X\_6,2,4 -X\_6,5,4 0
- X\_6,2,4 -X\_6,6,4 0
- X\_6,2,4 -X\_6,7,4 0
- X\_6,2,4 -X\_6,8,4 0
- X\_6,2,4 -X\_6,9,4 0
- X\_6,3,4 -X\_6,4,4 0
- X\_6,3,4 -X\_6,5,4 0
- X\_6,3,4 -X\_6,6,4 0
- X\_6,3,4 -X\_6,7,4 0
- X\_6,3,4 -X\_6,8,4 0
- X\_6,3,4 -X\_6,9,4 0
- X\_6,4,4 -X\_6,5,4 0
- X\_6,4,4 -X\_6,6,4 0
- X\_6,4,4 -X\_6,7,4 0
- X\_6,4,4 -X\_6,8,4 0
- X\_6,4,4 -X\_6,9,4 0
- X\_6,5,4 -X\_6,6,4 0
- X\_6,5,4 -X\_6,7,4 0
- X\_6,5,4 -X\_6,8,4 0
- X\_6,5,4 -X\_6,9,4 0
- X\_6,6,4 -X\_6,7,4 0
- X\_6,6,4 -X\_6,8,4 0
- X\_6,6,4 -X\_6,9,4 0
- X\_6,7,4 -X\_6,8,4 0
- X\_6,7,4 -X\_6,9,4 0
- X\_6,8,4 -X\_6,9,4 0

X\_6,1,5 X\_6,2,5 X\_6,3,5 X\_6,4,5 X\_6,5,5 X\_6,6,5 X\_6,7,5 X\_6,8,5 X\_6,9,5 0

- X\_6,1,5 -X\_6,2,5 0
- X\_6,1,5 -X\_6,3,5 0
- X\_6,1,5 -X\_6,4,5 0
- X\_6,1,5 -X\_6,5,5 0
- X\_6,1,5 -X\_6,6,5 0
- X\_6,1,5 -X\_6,7,5 0
- X\_6,1,5 -X\_6,8,5 0
- X\_6,1,5 -X\_6,9,5 0
- X\_6,2,5 -X\_6,3,5 0
- X\_6,2,5 -X\_6,4,5 0
- X\_6,2,5 -X\_6,5,5 0
- X\_6,2,5 -X\_6,6,5 0
- X\_6,2,5 -X\_6,7,5 0
- X\_6,2,5 -X\_6,8,5 0
- X\_6,2,5 -X\_6,9,5 0
- X\_6,3,5 -X\_6,4,5 0
- X\_6,3,5 -X\_6,5,5 0
- X\_6,3,5 -X\_6,6,5 0
- X\_6,3,5 -X\_6,7,5 0
- X\_6,3,5 -X\_6,8,5 0
- X\_6,3,5 -X\_6,9,5 0
- X\_6,4,5 -X\_6,5,5 0
- X\_6,4,5 -X\_6,6,5 0
- X\_6,4,5 -X\_6,7,5 0
- X\_6,4,5 -X\_6,8,5 0
- X\_6,4,5 -X\_6,9,5 0
- X\_6,5,5 -X\_6,6,5 0
- X\_6,5,5 -X\_6,7,5 0
- X\_6,5,5 -X\_6,8,5 0
- X\_6,5,5 -X\_6,9,5 0
- X\_6,6,5 -X\_6,7,5 0
- X\_6,6,5 -X\_6,8,5 0
- X\_6,6,5 -X\_6,9,5 0
- X\_6,7,5 -X\_6,8,5 0
- X\_6,7,5 -X\_6,9,5 0
- X\_6,8,5 -X\_6,9,5 0

X\_6,1,6 X\_6,2,6 X\_6,3,6 X\_6,4,6 X\_6,5,6 X\_6,6,6 X\_6,7,6 X\_6,8,6 X\_6,9,6 0

- X\_6,1,6 -X\_6,2,6 0
- X\_6,1,6 -X\_6,3,6 0
- X\_6,1,6 -X\_6,4,6 0
- X\_6,1,6 -X\_6,5,6 0
- X\_6,1,6 -X\_6,6,6 0
- X\_6,1,6 -X\_6,7,6 0
- X\_6,1,6 -X\_6,8,6 0
- X\_6,1,6 -X\_6,9,6 0
- X\_6,2,6 -X\_6,3,6 0
- X\_6,2,6 -X\_6,4,6 0
- X\_6,2,6 -X\_6,5,6 0
- X\_6,2,6 -X\_6,6,6 0
- X\_6,2,6 -X\_6,7,6 0
- X\_6,2,6 -X\_6,8,6 0
- X\_6,2,6 -X\_6,9,6 0
- X\_6,3,6 -X\_6,4,6 0
- X\_6,3,6 -X\_6,5,6 0
- X\_6,3,6 -X\_6,6,6 0
- X\_6,3,6 -X\_6,7,6 0
- X\_6,3,6 -X\_6,8,6 0
- X\_6,3,6 -X\_6,9,6 0
- X\_6,4,6 -X\_6,5,6 0
- X\_6,4,6 -X\_6,6,6 0
- X\_6,4,6 -X\_6,7,6 0
- X\_6,4,6 -X\_6,8,6 0
- X\_6,4,6 -X\_6,9,6 0
- X\_6,5,6 -X\_6,6,6 0
- X\_6,5,6 -X\_6,7,6 0
- X\_6,5,6 -X\_6,8,6 0
- X\_6,5,6 -X\_6,9,6 0
- X\_6,6,6 -X\_6,7,6 0
- X\_6,6,6 -X\_6,8,6 0
- X\_6,6,6 -X\_6,9,6 0
- X\_6,7,6 -X\_6,8,6 0
- X\_6,7,6 -X\_6,9,6 0
- X\_6,8,6 -X\_6,9,6 0

X\_6,1,7 X\_6,2,7 X\_6,3,7 X\_6,4,7 X\_6,5,7 X\_6,6,7 X\_6,7,7 X\_6,8,7 X\_6,9,7 0

- X\_6,1,7 -X\_6,2,7 0
- X\_6,1,7 -X\_6,3,7 0
- X\_6,1,7 -X\_6,4,7 0
- X\_6,1,7 -X\_6,5,7 0
- X\_6,1,7 -X\_6,6,7 0
- X\_6,1,7 -X\_6,7,7 0
- X\_6,1,7 -X\_6,8,7 0
- X\_6,1,7 -X\_6,9,7 0
- X\_6,2,7 -X\_6,3,7 0
- X\_6,2,7 -X\_6,4,7 0
- X\_6,2,7 -X\_6,5,7 0
- X\_6,2,7 -X\_6,6,7 0
- X\_6,2,7 -X\_6,7,7 0
- X\_6,2,7 -X\_6,8,7 0
- X\_6,2,7 -X\_6,9,7 0
- X\_6,3,7 -X\_6,4,7 0
- X\_6,3,7 -X\_6,5,7 0
- X\_6,3,7 -X\_6,6,7 0
- X\_6,3,7 -X\_6,7,7 0
- X\_6,3,7 -X\_6,8,7 0
- X\_6,3,7 -X\_6,9,7 0
- X\_6,4,7 -X\_6,5,7 0
- X\_6,4,7 -X\_6,6,7 0
- X\_6,4,7 -X\_6,7,7 0
- X\_6,4,7 -X\_6,8,7 0
- X\_6,4,7 -X\_6,9,7 0
- X\_6,5,7 -X\_6,6,7 0
- X\_6,5,7 -X\_6,7,7 0
- X\_6,5,7 -X\_6,8,7 0
- X\_6,5,7 -X\_6,9,7 0
- X\_6,6,7 -X\_6,7,7 0
- X\_6,6,7 -X\_6,8,7 0
- X\_6,6,7 -X\_6,9,7 0
- X\_6,7,7 -X\_6,8,7 0
- X\_6,7,7 -X\_6,9,7 0
- X\_6,8,7 -X\_6,9,7 0

X\_6,1,8 X\_6,2,8 X\_6,3,8 X\_6,4,8 X\_6,5,8 X\_6,6,8 X\_6,7,8 X\_6,8,8 X\_6,9,8 0

- X\_6,1,8 -X\_6,2,8 0
- X\_6,1,8 -X\_6,3,8 0
- X\_6,1,8 -X\_6,4,8 0
- X\_6,1,8 -X\_6,5,8 0
- X\_6,1,8 -X\_6,6,8 0
- X\_6,1,8 -X\_6,7,8 0
- X\_6,1,8 -X\_6,8,8 0
- X\_6,1,8 -X\_6,9,8 0
- X\_6,2,8 -X\_6,3,8 0
- X\_6,2,8 -X\_6,4,8 0
- X\_6,2,8 -X\_6,5,8 0
- X\_6,2,8 -X\_6,6,8 0
- X\_6,2,8 -X\_6,7,8 0
- X\_6,2,8 -X\_6,8,8 0
- X\_6,2,8 -X\_6,9,8 0
- X\_6,3,8 -X\_6,4,8 0
- X\_6,3,8 -X\_6,5,8 0
- X\_6,3,8 -X\_6,6,8 0
- X\_6,3,8 -X\_6,7,8 0
- X\_6,3,8 -X\_6,8,8 0
- X\_6,3,8 -X\_6,9,8 0
- X\_6,4,8 -X\_6,5,8 0
- X\_6,4,8 -X\_6,6,8 0
- X\_6,4,8 -X\_6,7,8 0
- X\_6,4,8 -X\_6,8,8 0
- X\_6,4,8 -X\_6,9,8 0
- X\_6,5,8 -X\_6,6,8 0
- X\_6,5,8 -X\_6,7,8 0
- X\_6,5,8 -X\_6,8,8 0
- X\_6,5,8 -X\_6,9,8 0
- X\_6,6,8 -X\_6,7,8 0
- X\_6,6,8 -X\_6,8,8 0
- X\_6,6,8 -X\_6,9,8 0
- X\_6,7,8 -X\_6,8,8 0
- X\_6,7,8 -X\_6,9,8 0
- X\_6,8,8 -X\_6,9,8 0

X\_6,1,9 X\_6,2,9 X\_6,3,9 X\_6,4,9 X\_6,5,9 X\_6,6,9 X\_6,7,9 X\_6,8,9 X\_6,9,9 0

- X\_6,1,9 -X\_6,2,9 0
- X\_6,1,9 -X\_6,3,9 0
- X\_6,1,9 -X\_6,4,9 0
- X\_6,1,9 -X\_6,5,9 0
- X\_6,1,9 -X\_6,6,9 0
- X\_6,1,9 -X\_6,7,9 0
- X\_6,1,9 -X\_6,8,9 0
- X\_6,1,9 -X\_6,9,9 0
- X\_6,2,9 -X\_6,3,9 0
- X\_6,2,9 -X\_6,4,9 0
- X\_6,2,9 -X\_6,5,9 0
- X\_6,2,9 -X\_6,6,9 0
- X\_6,2,9 -X\_6,7,9 0
- X\_6,2,9 -X\_6,8,9 0
- X\_6,2,9 -X\_6,9,9 0
- X\_6,3,9 -X\_6,4,9 0
- X\_6,3,9 -X\_6,5,9 0
- X\_6,3,9 -X\_6,6,9 0
- X\_6,3,9 -X\_6,7,9 0
- X\_6,3,9 -X\_6,8,9 0
- X\_6,3,9 -X\_6,9,9 0
- X\_6,4,9 -X\_6,5,9 0
- X\_6,4,9 -X\_6,6,9 0
- X\_6,4,9 -X\_6,7,9 0
- X\_6,4,9 -X\_6,8,9 0
- X\_6,4,9 -X\_6,9,9 0
- X\_6,5,9 -X\_6,6,9 0
- X\_6,5,9 -X\_6,7,9 0
- X\_6,5,9 -X\_6,8,9 0
- X\_6,5,9 -X\_6,9,9 0
- X\_6,6,9 -X\_6,7,9 0
- X\_6,6,9 -X\_6,8,9 0
- X\_6,6,9 -X\_6,9,9 0
- X\_6,7,9 -X\_6,8,9 0
- X\_6,7,9 -X\_6,9,9 0
- X\_6,8,9 -X\_6,9,9 0

X\_7,1,1 X\_7,2,1 X\_7,3,1 X\_7,4,1 X\_7,5,1 X\_7,6,1 X\_7,7,1 X\_7,8,1 X\_7,9,1 0

- X\_7,1,1 -X\_7,2,1 0
- X\_7,1,1 -X\_7,3,1 0
- X\_7,1,1 -X\_7,4,1 0
- X\_7,1,1 -X\_7,5,1 0
- X\_7,1,1 -X\_7,6,1 0
- X\_7,1,1 -X\_7,7,1 0
- X\_7,1,1 -X\_7,8,1 0
- X\_7,1,1 -X\_7,9,1 0
- X\_7,2,1 -X\_7,3,1 0
- X\_7,2,1 -X\_7,4,1 0
- X\_7,2,1 -X\_7,5,1 0
- X\_7,2,1 -X\_7,6,1 0
- X\_7,2,1 -X\_7,7,1 0
- X\_7,2,1 -X\_7,8,1 0
- X\_7,2,1 -X\_7,9,1 0
- X\_7,3,1 -X\_7,4,1 0
- X\_7,3,1 -X\_7,5,1 0
- X\_7,3,1 -X\_7,6,1 0
- X\_7,3,1 -X\_7,7,1 0
- X\_7,3,1 -X\_7,8,1 0
- X\_7,3,1 -X\_7,9,1 0
- X\_7,4,1 -X\_7,5,1 0
- X\_7,4,1 -X\_7,6,1 0
- X\_7,4,1 -X\_7,7,1 0
- X\_7,4,1 -X\_7,8,1 0
- X\_7,4,1 -X\_7,9,1 0
- X\_7,5,1 -X\_7,6,1 0
- X\_7,5,1 -X\_7,7,1 0
- X\_7,5,1 -X\_7,8,1 0
- X\_7,5,1 -X\_7,9,1 0
- X\_7,6,1 -X\_7,7,1 0
- X\_7,6,1 -X\_7,8,1 0
- X\_7,6,1 -X\_7,9,1 0
- X\_7,7,1 -X\_7,8,1 0
- X\_7,7,1 -X\_7,9,1 0
- X\_7,8,1 -X\_7,9,1 0

X\_7,1,2 X\_7,2,2 X\_7,3,2 X\_7,4,2 X\_7,5,2 X\_7,6,2 X\_7,7,2 X\_7,8,2 X\_7,9,2 0

- X\_7,1,2 -X\_7,2,2 0
- X\_7,1,2 -X\_7,3,2 0
- X\_7,1,2 -X\_7,4,2 0
- X\_7,1,2 -X\_7,5,2 0
- X\_7,1,2 -X\_7,6,2 0
- X\_7,1,2 -X\_7,7,2 0
- X\_7,1,2 -X\_7,8,2 0
- X\_7,1,2 -X\_7,9,2 0
- X\_7,2,2 -X\_7,3,2 0
- X\_7,2,2 -X\_7,4,2 0
- X\_7,2,2 -X\_7,5,2 0
- X\_7,2,2 -X\_7,6,2 0
- X\_7,2,2 -X\_7,7,2 0
- X\_7,2,2 -X\_7,8,2 0
- X\_7,2,2 -X\_7,9,2 0
- X\_7,3,2 -X\_7,4,2 0
- X\_7,3,2 -X\_7,5,2 0
- X\_7,3,2 -X\_7,6,2 0
- X\_7,3,2 -X\_7,7,2 0
- X\_7,3,2 -X\_7,8,2 0
- X\_7,3,2 -X\_7,9,2 0
- X\_7,4,2 -X\_7,5,2 0
- X\_7,4,2 -X\_7,6,2 0
- X\_7,4,2 -X\_7,7,2 0
- X\_7,4,2 -X\_7,8,2 0
- X\_7,4,2 -X\_7,9,2 0
- X\_7,5,2 -X\_7,6,2 0
- X\_7,5,2 -X\_7,7,2 0
- X\_7,5,2 -X\_7,8,2 0
- X\_7,5,2 -X\_7,9,2 0
- X\_7,6,2 -X\_7,7,2 0
- X\_7,6,2 -X\_7,8,2 0
- X\_7,6,2 -X\_7,9,2 0
- X\_7,7,2 -X\_7,8,2 0
- X\_7,7,2 -X\_7,9,2 0
- X\_7,8,2 -X\_7,9,2 0

X\_7,1,3 X\_7,2,3 X\_7,3,3 X\_7,4,3 X\_7,5,3 X\_7,6,3 X\_7,7,3 X\_7,8,3 X\_7,9,3 0

- X\_7,1,3 -X\_7,2,3 0
- X\_7,1,3 -X\_7,3,3 0
- X\_7,1,3 -X\_7,4,3 0
- X\_7,1,3 -X\_7,5,3 0
- X\_7,1,3 -X\_7,6,3 0
- X\_7,1,3 -X\_7,7,3 0
- X\_7,1,3 -X\_7,8,3 0
- X\_7,1,3 -X\_7,9,3 0
- X\_7,2,3 -X\_7,3,3 0
- X\_7,2,3 -X\_7,4,3 0
- X\_7,2,3 -X\_7,5,3 0
- X\_7,2,3 -X\_7,6,3 0
- X\_7,2,3 -X\_7,7,3 0
- X\_7,2,3 -X\_7,8,3 0
- X\_7,2,3 -X\_7,9,3 0
- X\_7,3,3 -X\_7,4,3 0
- X\_7,3,3 -X\_7,5,3 0
- X\_7,3,3 -X\_7,6,3 0
- X\_7,3,3 -X\_7,7,3 0
- X\_7,3,3 -X\_7,8,3 0
- X\_7,3,3 -X\_7,9,3 0
- X\_7,4,3 -X\_7,5,3 0
- X\_7,4,3 -X\_7,6,3 0
- X\_7,4,3 -X\_7,7,3 0
- X\_7,4,3 -X\_7,8,3 0
- X\_7,4,3 -X\_7,9,3 0
- X\_7,5,3 -X\_7,6,3 0
- X\_7,5,3 -X\_7,7,3 0
- X\_7,5,3 -X\_7,8,3 0
- X\_7,5,3 -X\_7,9,3 0
- X\_7,6,3 -X\_7,7,3 0
- X\_7,6,3 -X\_7,8,3 0
- X\_7,6,3 -X\_7,9,3 0
- X\_7,7,3 -X\_7,8,3 0
- X\_7,7,3 -X\_7,9,3 0
- X\_7,8,3 -X\_7,9,3 0

X\_7,1,4 X\_7,2,4 X\_7,3,4 X\_7,4,4 X\_7,5,4 X\_7,6,4 X\_7,7,4 X\_7,8,4 X\_7,9,4 0

- X\_7,1,4 -X\_7,2,4 0
- X\_7,1,4 -X\_7,3,4 0
- X\_7,1,4 -X\_7,4,4 0
- X\_7,1,4 -X\_7,5,4 0
- X\_7,1,4 -X\_7,6,4 0
- X\_7,1,4 -X\_7,7,4 0
- X\_7,1,4 -X\_7,8,4 0
- X\_7,1,4 -X\_7,9,4 0
- X\_7,2,4 -X\_7,3,4 0
- X\_7,2,4 -X\_7,4,4 0
- X\_7,2,4 -X\_7,5,4 0
- X\_7,2,4 -X\_7,6,4 0
- X\_7,2,4 -X\_7,7,4 0
- X\_7,2,4 -X\_7,8,4 0
- X\_7,2,4 -X\_7,9,4 0
- X\_7,3,4 -X\_7,4,4 0
- X\_7,3,4 -X\_7,5,4 0
- X\_7,3,4 -X\_7,6,4 0
- X\_7,3,4 -X\_7,7,4 0
- X\_7,3,4 -X\_7,8,4 0
- X\_7,3,4 -X\_7,9,4 0
- X\_7,4,4 -X\_7,5,4 0
- X\_7,4,4 -X\_7,6,4 0
- X\_7,4,4 -X\_7,7,4 0
- X\_7,4,4 -X\_7,8,4 0
- X\_7,4,4 -X\_7,9,4 0
- X\_7,5,4 -X\_7,6,4 0
- X\_7,5,4 -X\_7,7,4 0
- X\_7,5,4 -X\_7,8,4 0
- X\_7,5,4 -X\_7,9,4 0
- X\_7,6,4 -X\_7,7,4 0
- X\_7,6,4 -X\_7,8,4 0
- X\_7,6,4 -X\_7,9,4 0
- X\_7,7,4 -X\_7,8,4 0
- X\_7,7,4 -X\_7,9,4 0
- X\_7,8,4 -X\_7,9,4 0

X\_7,1,5 X\_7,2,5 X\_7,3,5 X\_7,4,5 X\_7,5,5 X\_7,6,5 X\_7,7,5 X\_7,8,5 X\_7,9,5 0

- X\_7,1,5 -X\_7,2,5 0
- X\_7,1,5 -X\_7,3,5 0
- X\_7,1,5 -X\_7,4,5 0
- X\_7,1,5 -X\_7,5,5 0
- X\_7,1,5 -X\_7,6,5 0
- X\_7,1,5 -X\_7,7,5 0
- X\_7,1,5 -X\_7,8,5 0
- X\_7,1,5 -X\_7,9,5 0
- X\_7,2,5 -X\_7,3,5 0
- X\_7,2,5 -X\_7,4,5 0
- X\_7,2,5 -X\_7,5,5 0
- X\_7,2,5 -X\_7,6,5 0
- X\_7,2,5 -X\_7,7,5 0
- X\_7,2,5 -X\_7,8,5 0
- X\_7,2,5 -X\_7,9,5 0
- X\_7,3,5 -X\_7,4,5 0
- X\_7,3,5 -X\_7,5,5 0
- X\_7,3,5 -X\_7,6,5 0
- X\_7,3,5 -X\_7,7,5 0
- X\_7,3,5 -X\_7,8,5 0
- X\_7,3,5 -X\_7,9,5 0
- X\_7,4,5 -X\_7,5,5 0
- X\_7,4,5 -X\_7,6,5 0
- X\_7,4,5 -X\_7,7,5 0
- X\_7,4,5 -X\_7,8,5 0
- X\_7,4,5 -X\_7,9,5 0
- X\_7,5,5 -X\_7,6,5 0
- X\_7,5,5 -X\_7,7,5 0
- X\_7,5,5 -X\_7,8,5 0
- X\_7,5,5 -X\_7,9,5 0
- X\_7,6,5 -X\_7,7,5 0
- X\_7,6,5 -X\_7,8,5 0
- X\_7,6,5 -X\_7,9,5 0
- X\_7,7,5 -X\_7,8,5 0
- X\_7,7,5 -X\_7,9,5 0
- X\_7,8,5 -X\_7,9,5 0

X\_7,1,6 X\_7,2,6 X\_7,3,6 X\_7,4,6 X\_7,5,6 X\_7,6,6 X\_7,7,6 X\_7,8,6 X\_7,9,6 0

- X\_7,1,6 -X\_7,2,6 0
- X\_7,1,6 -X\_7,3,6 0
- X\_7,1,6 -X\_7,4,6 0
- X\_7,1,6 -X\_7,5,6 0
- X\_7,1,6 -X\_7,6,6 0
- X\_7,1,6 -X\_7,7,6 0
- X\_7,1,6 -X\_7,8,6 0
- X\_7,1,6 -X\_7,9,6 0
- X\_7,2,6 -X\_7,3,6 0
- X\_7,2,6 -X\_7,4,6 0
- X\_7,2,6 -X\_7,5,6 0
- X\_7,2,6 -X\_7,6,6 0
- X\_7,2,6 -X\_7,7,6 0
- X\_7,2,6 -X\_7,8,6 0
- X\_7,2,6 -X\_7,9,6 0
- X\_7,3,6 -X\_7,4,6 0
- X\_7,3,6 -X\_7,5,6 0
- X\_7,3,6 -X\_7,6,6 0
- X\_7,3,6 -X\_7,7,6 0
- X\_7,3,6 -X\_7,8,6 0
- X\_7,3,6 -X\_7,9,6 0
- X\_7,4,6 -X\_7,5,6 0
- X\_7,4,6 -X\_7,6,6 0
- X\_7,4,6 -X\_7,7,6 0
- X\_7,4,6 -X\_7,8,6 0
- X\_7,4,6 -X\_7,9,6 0
- X\_7,5,6 -X\_7,6,6 0
- X\_7,5,6 -X\_7,7,6 0
- X\_7,5,6 -X\_7,8,6 0
- X\_7,5,6 -X\_7,9,6 0
- X\_7,6,6 -X\_7,7,6 0
- X\_7,6,6 -X\_7,8,6 0
- X\_7,6,6 -X\_7,9,6 0
- X\_7,7,6 -X\_7,8,6 0
- X\_7,7,6 -X\_7,9,6 0
- X\_7,8,6 -X\_7,9,6 0

X\_7,1,7 X\_7,2,7 X\_7,3,7 X\_7,4,7 X\_7,5,7 X\_7,6,7 X\_7,7,7 X\_7,8,7 X\_7,9,7 0

- X\_7,1,7 -X\_7,2,7 0
- X\_7,1,7 -X\_7,3,7 0
- X\_7,1,7 -X\_7,4,7 0
- X\_7,1,7 -X\_7,5,7 0
- X\_7,1,7 -X\_7,6,7 0
- X\_7,1,7 -X\_7,7,7 0
- X\_7,1,7 -X\_7,8,7 0
- X\_7,1,7 -X\_7,9,7 0
- X\_7,2,7 -X\_7,3,7 0
- X\_7,2,7 -X\_7,4,7 0
- X\_7,2,7 -X\_7,5,7 0
- X\_7,2,7 -X\_7,6,7 0
- X\_7,2,7 -X\_7,7,7 0
- X\_7,2,7 -X\_7,8,7 0
- X\_7,2,7 -X\_7,9,7 0
- X\_7,3,7 -X\_7,4,7 0
- X\_7,3,7 -X\_7,5,7 0
- X\_7,3,7 -X\_7,6,7 0
- X\_7,3,7 -X\_7,7,7 0
- X\_7,3,7 -X\_7,8,7 0
- X\_7,3,7 -X\_7,9,7 0
- X\_7,4,7 -X\_7,5,7 0
- X\_7,4,7 -X\_7,6,7 0
- X\_7,4,7 -X\_7,7,7 0
- X\_7,4,7 -X\_7,8,7 0
- X\_7,4,7 -X\_7,9,7 0
- X\_7,5,7 -X\_7,6,7 0
- X\_7,5,7 -X\_7,7,7 0
- X\_7,5,7 -X\_7,8,7 0
- X\_7,5,7 -X\_7,9,7 0
- X\_7,6,7 -X\_7,7,7 0
- X\_7,6,7 -X\_7,8,7 0
- X\_7,6,7 -X\_7,9,7 0
- X\_7,7,7 -X\_7,8,7 0
- X\_7,7,7 -X\_7,9,7 0
- X\_7,8,7 -X\_7,9,7 0

X\_7,1,8 X\_7,2,8 X\_7,3,8 X\_7,4,8 X\_7,5,8 X\_7,6,8 X\_7,7,8 X\_7,8,8 X\_7,9,8 0

- X\_7,1,8 -X\_7,2,8 0
- X\_7,1,8 -X\_7,3,8 0
- X\_7,1,8 -X\_7,4,8 0
- X\_7,1,8 -X\_7,5,8 0
- X\_7,1,8 -X\_7,6,8 0
- X\_7,1,8 -X\_7,7,8 0
- X\_7,1,8 -X\_7,8,8 0
- X\_7,1,8 -X\_7,9,8 0
- X\_7,2,8 -X\_7,3,8 0
- X\_7,2,8 -X\_7,4,8 0
- X\_7,2,8 -X\_7,5,8 0
- X\_7,2,8 -X\_7,6,8 0
- X\_7,2,8 -X\_7,7,8 0
- X\_7,2,8 -X\_7,8,8 0
- X\_7,2,8 -X\_7,9,8 0
- X\_7,3,8 -X\_7,4,8 0
- X\_7,3,8 -X\_7,5,8 0
- X\_7,3,8 -X\_7,6,8 0
- X\_7,3,8 -X\_7,7,8 0
- X\_7,3,8 -X\_7,8,8 0
- X\_7,3,8 -X\_7,9,8 0
- X\_7,4,8 -X\_7,5,8 0
- X\_7,4,8 -X\_7,6,8 0
- X\_7,4,8 -X\_7,7,8 0
- X\_7,4,8 -X\_7,8,8 0
- X\_7,4,8 -X\_7,9,8 0
- X\_7,5,8 -X\_7,6,8 0
- X\_7,5,8 -X\_7,7,8 0
- X\_7,5,8 -X\_7,8,8 0
- X\_7,5,8 -X\_7,9,8 0
- X\_7,6,8 -X\_7,7,8 0
- X\_7,6,8 -X\_7,8,8 0
- X\_7,6,8 -X\_7,9,8 0
- X\_7,7,8 -X\_7,8,8 0
- X\_7,7,8 -X\_7,9,8 0
- X\_7,8,8 -X\_7,9,8 0

X\_7,1,9 X\_7,2,9 X\_7,3,9 X\_7,4,9 X\_7,5,9 X\_7,6,9 X\_7,7,9 X\_7,8,9 X\_7,9,9 0

- X\_7,1,9 -X\_7,2,9 0
- X\_7,1,9 -X\_7,3,9 0
- X\_7,1,9 -X\_7,4,9 0
- X\_7,1,9 -X\_7,5,9 0
- X\_7,1,9 -X\_7,6,9 0
- X\_7,1,9 -X\_7,7,9 0
- X\_7,1,9 -X\_7,8,9 0
- X\_7,1,9 -X\_7,9,9 0
- X\_7,2,9 -X\_7,3,9 0
- X\_7,2,9 -X\_7,4,9 0
- X\_7,2,9 -X\_7,5,9 0
- X\_7,2,9 -X\_7,6,9 0
- X\_7,2,9 -X\_7,7,9 0
- X\_7,2,9 -X\_7,8,9 0
- X\_7,2,9 -X\_7,9,9 0
- X\_7,3,9 -X\_7,4,9 0
- X\_7,3,9 -X\_7,5,9 0
- X\_7,3,9 -X\_7,6,9 0
- X\_7,3,9 -X\_7,7,9 0
- X\_7,3,9 -X\_7,8,9 0
- X\_7,3,9 -X\_7,9,9 0
- X\_7,4,9 -X\_7,5,9 0
- X\_7,4,9 -X\_7,6,9 0
- X\_7,4,9 -X\_7,7,9 0
- X\_7,4,9 -X\_7,8,9 0
- X\_7,4,9 -X\_7,9,9 0
- X\_7,5,9 -X\_7,6,9 0
- X\_7,5,9 -X\_7,7,9 0
- X\_7,5,9 -X\_7,8,9 0
- X\_7,5,9 -X\_7,9,9 0
- X\_7,6,9 -X\_7,7,9 0
- X\_7,6,9 -X\_7,8,9 0
- X\_7,6,9 -X\_7,9,9 0
- X\_7,7,9 -X\_7,8,9 0
- X\_7,7,9 -X\_7,9,9 0
- X\_7,8,9 -X\_7,9,9 0

X\_8,1,1 X\_8,2,1 X\_8,3,1 X\_8,4,1 X\_8,5,1 X\_8,6,1 X\_8,7,1 X\_8,8,1 X\_8,9,1 0

- X\_8,1,1 -X\_8,2,1 0
- X\_8,1,1 -X\_8,3,1 0
- X\_8,1,1 -X\_8,4,1 0
- X\_8,1,1 -X\_8,5,1 0
- X\_8,1,1 -X\_8,6,1 0
- X\_8,1,1 -X\_8,7,1 0
- X\_8,1,1 -X\_8,8,1 0
- X\_8,1,1 -X\_8,9,1 0
- X\_8,2,1 -X\_8,3,1 0
- X\_8,2,1 -X\_8,4,1 0
- X\_8,2,1 -X\_8,5,1 0
- X\_8,2,1 -X\_8,6,1 0
- X\_8,2,1 -X\_8,7,1 0
- X\_8,2,1 -X\_8,8,1 0
- X\_8,2,1 -X\_8,9,1 0
- X\_8,3,1 -X\_8,4,1 0
- X\_8,3,1 -X\_8,5,1 0
- X\_8,3,1 -X\_8,6,1 0
- X\_8,3,1 -X\_8,7,1 0
- X\_8,3,1 -X\_8,8,1 0
- X\_8,3,1 -X\_8,9,1 0
- X\_8,4,1 -X\_8,5,1 0
- X\_8,4,1 -X\_8,6,1 0
- X\_8,4,1 -X\_8,7,1 0
- X\_8,4,1 -X\_8,8,1 0
- X\_8,4,1 -X\_8,9,1 0
- X\_8,5,1 -X\_8,6,1 0
- X\_8,5,1 -X\_8,7,1 0
- X\_8,5,1 -X\_8,8,1 0
- X\_8,5,1 -X\_8,9,1 0
- X\_8,6,1 -X\_8,7,1 0
- X\_8,6,1 -X\_8,8,1 0
- X\_8,6,1 -X\_8,9,1 0
- X\_8,7,1 -X\_8,8,1 0
- X\_8,7,1 -X\_8,9,1 0
- X\_8,8,1 -X\_8,9,1 0

X\_8,1,2 X\_8,2,2 X\_8,3,2 X\_8,4,2 X\_8,5,2 X\_8,6,2 X\_8,7,2 X\_8,8,2 X\_8,9,2 0

- X\_8,1,2 -X\_8,2,2 0
- X\_8,1,2 -X\_8,3,2 0
- X\_8,1,2 -X\_8,4,2 0
- X\_8,1,2 -X\_8,5,2 0
- X\_8,1,2 -X\_8,6,2 0
- X\_8,1,2 -X\_8,7,2 0
- X\_8,1,2 -X\_8,8,2 0
- X\_8,1,2 -X\_8,9,2 0
- X\_8,2,2 -X\_8,3,2 0
- X\_8,2,2 -X\_8,4,2 0
- X\_8,2,2 -X\_8,5,2 0
- X\_8,2,2 -X\_8,6,2 0
- X\_8,2,2 -X\_8,7,2 0
- X\_8,2,2 -X\_8,8,2 0
- X\_8,2,2 -X\_8,9,2 0
- X\_8,3,2 -X\_8,4,2 0
- X\_8,3,2 -X\_8,5,2 0
- X\_8,3,2 -X\_8,6,2 0
- X\_8,3,2 -X\_8,7,2 0
- X\_8,3,2 -X\_8,8,2 0
- X\_8,3,2 -X\_8,9,2 0
- X\_8,4,2 -X\_8,5,2 0
- X\_8,4,2 -X\_8,6,2 0
- X\_8,4,2 -X\_8,7,2 0
- X\_8,4,2 -X\_8,8,2 0
- X\_8,4,2 -X\_8,9,2 0
- X\_8,5,2 -X\_8,6,2 0
- X\_8,5,2 -X\_8,7,2 0
- X\_8,5,2 -X\_8,8,2 0
- X\_8,5,2 -X\_8,9,2 0
- X\_8,6,2 -X\_8,7,2 0
- X\_8,6,2 -X\_8,8,2 0
- X\_8,6,2 -X\_8,9,2 0
- X\_8,7,2 -X\_8,8,2 0
- X\_8,7,2 -X\_8,9,2 0
- X\_8,8,2 -X\_8,9,2 0

X\_8,1,3 X\_8,2,3 X\_8,3,3 X\_8,4,3 X\_8,5,3 X\_8,6,3 X\_8,7,3 X\_8,8,3 X\_8,9,3 0

- X\_8,1,3 -X\_8,2,3 0
- X\_8,1,3 -X\_8,3,3 0
- X\_8,1,3 -X\_8,4,3 0
- X\_8,1,3 -X\_8,5,3 0
- X\_8,1,3 -X\_8,6,3 0
- X\_8,1,3 -X\_8,7,3 0
- X\_8,1,3 -X\_8,8,3 0
- X\_8,1,3 -X\_8,9,3 0
- X\_8,2,3 -X\_8,3,3 0
- X\_8,2,3 -X\_8,4,3 0
- X\_8,2,3 -X\_8,5,3 0
- X\_8,2,3 -X\_8,6,3 0
- X\_8,2,3 -X\_8,7,3 0
- X\_8,2,3 -X\_8,8,3 0
- X\_8,2,3 -X\_8,9,3 0
- X\_8,3,3 -X\_8,4,3 0
- X\_8,3,3 -X\_8,5,3 0
- X\_8,3,3 -X\_8,6,3 0
- X\_8,3,3 -X\_8,7,3 0
- X\_8,3,3 -X\_8,8,3 0
- X\_8,3,3 -X\_8,9,3 0
- X\_8,4,3 -X\_8,5,3 0
- X\_8,4,3 -X\_8,6,3 0
- X\_8,4,3 -X\_8,7,3 0
- X\_8,4,3 -X\_8,8,3 0
- X\_8,4,3 -X\_8,9,3 0
- X\_8,5,3 -X\_8,6,3 0
- X\_8,5,3 -X\_8,7,3 0
- X\_8,5,3 -X\_8,8,3 0
- X\_8,5,3 -X\_8,9,3 0
- X\_8,6,3 -X\_8,7,3 0
- X\_8,6,3 -X\_8,8,3 0
- X\_8,6,3 -X\_8,9,3 0
- X\_8,7,3 -X\_8,8,3 0
- X\_8,7,3 -X\_8,9,3 0
- X\_8,8,3 -X\_8,9,3 0

X\_8,1,4 X\_8,2,4 X\_8,3,4 X\_8,4,4 X\_8,5,4 X\_8,6,4 X\_8,7,4 X\_8,8,4 X\_8,9,4 0

- X\_8,1,4 -X\_8,2,4 0
- X\_8,1,4 -X\_8,3,4 0
- X\_8,1,4 -X\_8,4,4 0
- X\_8,1,4 -X\_8,5,4 0
- X\_8,1,4 -X\_8,6,4 0
- X\_8,1,4 -X\_8,7,4 0
- X\_8,1,4 -X\_8,8,4 0
- X\_8,1,4 -X\_8,9,4 0
- X\_8,2,4 -X\_8,3,4 0
- X\_8,2,4 -X\_8,4,4 0
- X\_8,2,4 -X\_8,5,4 0
- X\_8,2,4 -X\_8,6,4 0
- X\_8,2,4 -X\_8,7,4 0
- X\_8,2,4 -X\_8,8,4 0
- X\_8,2,4 -X\_8,9,4 0
- X\_8,3,4 -X\_8,4,4 0
- X\_8,3,4 -X\_8,5,4 0
- X\_8,3,4 -X\_8,6,4 0
- X\_8,3,4 -X\_8,7,4 0
- X\_8,3,4 -X\_8,8,4 0
- X\_8,3,4 -X\_8,9,4 0
- X\_8,4,4 -X\_8,5,4 0
- X\_8,4,4 -X\_8,6,4 0
- X\_8,4,4 -X\_8,7,4 0
- X\_8,4,4 -X\_8,8,4 0
- X\_8,4,4 -X\_8,9,4 0
- X\_8,5,4 -X\_8,6,4 0
- X\_8,5,4 -X\_8,7,4 0
- X\_8,5,4 -X\_8,8,4 0
- X\_8,5,4 -X\_8,9,4 0
- X\_8,6,4 -X\_8,7,4 0
- X\_8,6,4 -X\_8,8,4 0
- X\_8,6,4 -X\_8,9,4 0
- X\_8,7,4 -X\_8,8,4 0
- X\_8,7,4 -X\_8,9,4 0
- X\_8,8,4 -X\_8,9,4 0

X\_8,1,5 X\_8,2,5 X\_8,3,5 X\_8,4,5 X\_8,5,5 X\_8,6,5 X\_8,7,5 X\_8,8,5 X\_8,9,5 0

- X\_8,1,5 -X\_8,2,5 0
- X\_8,1,5 -X\_8,3,5 0
- X\_8,1,5 -X\_8,4,5 0
- X\_8,1,5 -X\_8,5,5 0
- X\_8,1,5 -X\_8,6,5 0
- X\_8,1,5 -X\_8,7,5 0
- X\_8,1,5 -X\_8,8,5 0
- X\_8,1,5 -X\_8,9,5 0
- X\_8,2,5 -X\_8,3,5 0
- X\_8,2,5 -X\_8,4,5 0
- X\_8,2,5 -X\_8,5,5 0
- X\_8,2,5 -X\_8,6,5 0
- X\_8,2,5 -X\_8,7,5 0
- X\_8,2,5 -X\_8,8,5 0
- X\_8,2,5 -X\_8,9,5 0
- X\_8,3,5 -X\_8,4,5 0
- X\_8,3,5 -X\_8,5,5 0
- X\_8,3,5 -X\_8,6,5 0
- X\_8,3,5 -X\_8,7,5 0
- X\_8,3,5 -X\_8,8,5 0
- X\_8,3,5 -X\_8,9,5 0
- X\_8,4,5 -X\_8,5,5 0
- X\_8,4,5 -X\_8,6,5 0
- X\_8,4,5 -X\_8,7,5 0
- X\_8,4,5 -X\_8,8,5 0
- X\_8,4,5 -X\_8,9,5 0
- X\_8,5,5 -X\_8,6,5 0
- X\_8,5,5 -X\_8,7,5 0
- X\_8,5,5 -X\_8,8,5 0
- X\_8,5,5 -X\_8,9,5 0
- X\_8,6,5 -X\_8,7,5 0
- X\_8,6,5 -X\_8,8,5 0
- X\_8,6,5 -X\_8,9,5 0
- X\_8,7,5 -X\_8,8,5 0
- X\_8,7,5 -X\_8,9,5 0
- X\_8,8,5 -X\_8,9,5 0

X\_8,1,6 X\_8,2,6 X\_8,3,6 X\_8,4,6 X\_8,5,6 X\_8,6,6 X\_8,7,6 X\_8,8,6 X\_8,9,6 0

- X\_8,1,6 -X\_8,2,6 0
- X\_8,1,6 -X\_8,3,6 0
- X\_8,1,6 -X\_8,4,6 0
- X\_8,1,6 -X\_8,5,6 0
- X\_8,1,6 -X\_8,6,6 0
- X\_8,1,6 -X\_8,7,6 0
- X\_8,1,6 -X\_8,8,6 0
- X\_8,1,6 -X\_8,9,6 0
- X\_8,2,6 -X\_8,3,6 0
- X\_8,2,6 -X\_8,4,6 0
- X\_8,2,6 -X\_8,5,6 0
- X\_8,2,6 -X\_8,6,6 0
- X\_8,2,6 -X\_8,7,6 0
- X\_8,2,6 -X\_8,8,6 0
- X\_8,2,6 -X\_8,9,6 0
- X\_8,3,6 -X\_8,4,6 0
- X\_8,3,6 -X\_8,5,6 0
- X\_8,3,6 -X\_8,6,6 0
- X\_8,3,6 -X\_8,7,6 0
- X\_8,3,6 -X\_8,8,6 0
- X\_8,3,6 -X\_8,9,6 0
- X\_8,4,6 -X\_8,5,6 0
- X\_8,4,6 -X\_8,6,6 0
- X\_8,4,6 -X\_8,7,6 0
- X\_8,4,6 -X\_8,8,6 0
- X\_8,4,6 -X\_8,9,6 0
- X\_8,5,6 -X\_8,6,6 0
- X\_8,5,6 -X\_8,7,6 0
- X\_8,5,6 -X\_8,8,6 0
- X\_8,5,6 -X\_8,9,6 0
- X\_8,6,6 -X\_8,7,6 0
- X\_8,6,6 -X\_8,8,6 0
- X\_8,6,6 -X\_8,9,6 0
- X\_8,7,6 -X\_8,8,6 0
- X\_8,7,6 -X\_8,9,6 0
- X\_8,8,6 -X\_8,9,6 0

X\_8,1,7 X\_8,2,7 X\_8,3,7 X\_8,4,7 X\_8,5,7 X\_8,6,7 X\_8,7,7 X\_8,8,7 X\_8,9,7 0

- X\_8,1,7 -X\_8,2,7 0
- X\_8,1,7 -X\_8,3,7 0
- X\_8,1,7 -X\_8,4,7 0
- X\_8,1,7 -X\_8,5,7 0
- X\_8,1,7 -X\_8,6,7 0
- X\_8,1,7 -X\_8,7,7 0
- X\_8,1,7 -X\_8,8,7 0
- X\_8,1,7 -X\_8,9,7 0
- X\_8,2,7 -X\_8,3,7 0
- X\_8,2,7 -X\_8,4,7 0
- X\_8,2,7 -X\_8,5,7 0
- X\_8,2,7 -X\_8,6,7 0
- X\_8,2,7 -X\_8,7,7 0
- X\_8,2,7 -X\_8,8,7 0
- X\_8,2,7 -X\_8,9,7 0
- X\_8,3,7 -X\_8,4,7 0
- X\_8,3,7 -X\_8,5,7 0
- X\_8,3,7 -X\_8,6,7 0
- X\_8,3,7 -X\_8,7,7 0
- X\_8,3,7 -X\_8,8,7 0
- X\_8,3,7 -X\_8,9,7 0
- X\_8,4,7 -X\_8,5,7 0
- X\_8,4,7 -X\_8,6,7 0
- X\_8,4,7 -X\_8,7,7 0
- X\_8,4,7 -X\_8,8,7 0
- X\_8,4,7 -X\_8,9,7 0
- X\_8,5,7 -X\_8,6,7 0
- X\_8,5,7 -X\_8,7,7 0
- X\_8,5,7 -X\_8,8,7 0
- X\_8,5,7 -X\_8,9,7 0
- X\_8,6,7 -X\_8,7,7 0
- X\_8,6,7 -X\_8,8,7 0
- X\_8,6,7 -X\_8,9,7 0
- X\_8,7,7 -X\_8,8,7 0
- X\_8,7,7 -X\_8,9,7 0
- X\_8,8,7 -X\_8,9,7 0

X\_8,1,8 X\_8,2,8 X\_8,3,8 X\_8,4,8 X\_8,5,8 X\_8,6,8 X\_8,7,8 X\_8,8,8 X\_8,9,8 0

- X\_8,1,8 -X\_8,2,8 0
- X\_8,1,8 -X\_8,3,8 0
- X\_8,1,8 -X\_8,4,8 0
- X\_8,1,8 -X\_8,5,8 0
- X\_8,1,8 -X\_8,6,8 0
- X\_8,1,8 -X\_8,7,8 0
- X\_8,1,8 -X\_8,8,8 0
- X\_8,1,8 -X\_8,9,8 0
- X\_8,2,8 -X\_8,3,8 0
- X\_8,2,8 -X\_8,4,8 0
- X\_8,2,8 -X\_8,5,8 0
- X\_8,2,8 -X\_8,6,8 0
- X\_8,2,8 -X\_8,7,8 0
- X\_8,2,8 -X\_8,8,8 0
- X\_8,2,8 -X\_8,9,8 0
- X\_8,3,8 -X\_8,4,8 0
- X\_8,3,8 -X\_8,5,8 0
- X\_8,3,8 -X\_8,6,8 0
- X\_8,3,8 -X\_8,7,8 0
- X\_8,3,8 -X\_8,8,8 0
- X\_8,3,8 -X\_8,9,8 0
- X\_8,4,8 -X\_8,5,8 0
- X\_8,4,8 -X\_8,6,8 0
- X\_8,4,8 -X\_8,7,8 0
- X\_8,4,8 -X\_8,8,8 0
- X\_8,4,8 -X\_8,9,8 0
- X\_8,5,8 -X\_8,6,8 0
- X\_8,5,8 -X\_8,7,8 0
- X\_8,5,8 -X\_8,8,8 0
- X\_8,5,8 -X\_8,9,8 0
- X\_8,6,8 -X\_8,7,8 0
- X\_8,6,8 -X\_8,8,8 0
- X\_8,6,8 -X\_8,9,8 0
- X\_8,7,8 -X\_8,8,8 0
- X\_8,7,8 -X\_8,9,8 0
- X\_8,8,8 -X\_8,9,8 0

X\_8,1,9 X\_8,2,9 X\_8,3,9 X\_8,4,9 X\_8,5,9 X\_8,6,9 X\_8,7,9 X\_8,8,9 X\_8,9,9 0

- X\_8,1,9 -X\_8,2,9 0
- X\_8,1,9 -X\_8,3,9 0
- X\_8,1,9 -X\_8,4,9 0
- X\_8,1,9 -X\_8,5,9 0
- X\_8,1,9 -X\_8,6,9 0
- X\_8,1,9 -X\_8,7,9 0
- X\_8,1,9 -X\_8,8,9 0
- X\_8,1,9 -X\_8,9,9 0
- X\_8,2,9 -X\_8,3,9 0
- X\_8,2,9 -X\_8,4,9 0
- X\_8,2,9 -X\_8,5,9 0
- X\_8,2,9 -X\_8,6,9 0
- X\_8,2,9 -X\_8,7,9 0
- X\_8,2,9 -X\_8,8,9 0
- X\_8,2,9 -X\_8,9,9 0
- X\_8,3,9 -X\_8,4,9 0
- X\_8,3,9 -X\_8,5,9 0
- X\_8,3,9 -X\_8,6,9 0
- X\_8,3,9 -X\_8,7,9 0
- X\_8,3,9 -X\_8,8,9 0
- X\_8,3,9 -X\_8,9,9 0
- X\_8,4,9 -X\_8,5,9 0
- X\_8,4,9 -X\_8,6,9 0
- X\_8,4,9 -X\_8,7,9 0
- X\_8,4,9 -X\_8,8,9 0
- X\_8,4,9 -X\_8,9,9 0
- X\_8,5,9 -X\_8,6,9 0
- X\_8,5,9 -X\_8,7,9 0
- X\_8,5,9 -X\_8,8,9 0
- X\_8,5,9 -X\_8,9,9 0
- X\_8,6,9 -X\_8,7,9 0
- X\_8,6,9 -X\_8,8,9 0
- X\_8,6,9 -X\_8,9,9 0
- X\_8,7,9 -X\_8,8,9 0
- X\_8,7,9 -X\_8,9,9 0
- X\_8,8,9 -X\_8,9,9 0

X\_9,1,1 X\_9,2,1 X\_9,3,1 X\_9,4,1 X\_9,5,1 X\_9,6,1 X\_9,7,1 X\_9,8,1 X\_9,9,1 0

- X\_9,1,1 -X\_9,2,1 0
- X\_9,1,1 -X\_9,3,1 0
- X\_9,1,1 -X\_9,4,1 0
- X\_9,1,1 -X\_9,5,1 0
- X\_9,1,1 -X\_9,6,1 0
- X\_9,1,1 -X\_9,7,1 0
- X\_9,1,1 -X\_9,8,1 0
- X\_9,1,1 -X\_9,9,1 0
- X\_9,2,1 -X\_9,3,1 0
- X\_9,2,1 -X\_9,4,1 0
- X\_9,2,1 -X\_9,5,1 0
- X\_9,2,1 -X\_9,6,1 0
- X\_9,2,1 -X\_9,7,1 0
- X\_9,2,1 -X\_9,8,1 0
- X\_9,2,1 -X\_9,9,1 0
- X\_9,3,1 -X\_9,4,1 0
- X\_9,3,1 -X\_9,5,1 0
- X\_9,3,1 -X\_9,6,1 0
- X\_9,3,1 -X\_9,7,1 0
- X\_9,3,1 -X\_9,8,1 0
- X\_9,3,1 -X\_9,9,1 0
- X\_9,4,1 -X\_9,5,1 0
- X\_9,4,1 -X\_9,6,1 0
- X\_9,4,1 -X\_9,7,1 0
- X\_9,4,1 -X\_9,8,1 0
- X\_9,4,1 -X\_9,9,1 0
- X\_9,5,1 -X\_9,6,1 0
- X\_9,5,1 -X\_9,7,1 0
- X\_9,5,1 -X\_9,8,1 0
- X\_9,5,1 -X\_9,9,1 0
- X\_9,6,1 -X\_9,7,1 0
- X\_9,6,1 -X\_9,8,1 0
- X\_9,6,1 -X\_9,9,1 0
- X\_9,7,1 -X\_9,8,1 0
- X\_9,7,1 -X\_9,9,1 0
- X\_9,8,1 -X\_9,9,1 0

X\_9,1,2 X\_9,2,2 X\_9,3,2 X\_9,4,2 X\_9,5,2 X\_9,6,2 X\_9,7,2 X\_9,8,2 X\_9,9,2 0

- X\_9,1,2 -X\_9,2,2 0
- X\_9,1,2 -X\_9,3,2 0
- X\_9,1,2 -X\_9,4,2 0
- X\_9,1,2 -X\_9,5,2 0
- X\_9,1,2 -X\_9,6,2 0
- X\_9,1,2 -X\_9,7,2 0
- X\_9,1,2 -X\_9,8,2 0
- X\_9,1,2 -X\_9,9,2 0
- X\_9,2,2 -X\_9,3,2 0
- X\_9,2,2 -X\_9,4,2 0
- X\_9,2,2 -X\_9,5,2 0
- X\_9,2,2 -X\_9,6,2 0
- X\_9,2,2 -X\_9,7,2 0
- X\_9,2,2 -X\_9,8,2 0
- X\_9,2,2 -X\_9,9,2 0
- X\_9,3,2 -X\_9,4,2 0
- X\_9,3,2 -X\_9,5,2 0
- X\_9,3,2 -X\_9,6,2 0
- X\_9,3,2 -X\_9,7,2 0
- X\_9,3,2 -X\_9,8,2 0
- X\_9,3,2 -X\_9,9,2 0
- X\_9,4,2 -X\_9,5,2 0
- X\_9,4,2 -X\_9,6,2 0
- X\_9,4,2 -X\_9,7,2 0
- X\_9,4,2 -X\_9,8,2 0
- X\_9,4,2 -X\_9,9,2 0
- X\_9,5,2 -X\_9,6,2 0
- X\_9,5,2 -X\_9,7,2 0
- X\_9,5,2 -X\_9,8,2 0
- X\_9,5,2 -X\_9,9,2 0
- X\_9,6,2 -X\_9,7,2 0
- X\_9,6,2 -X\_9,8,2 0
- X\_9,6,2 -X\_9,9,2 0
- X\_9,7,2 -X\_9,8,2 0
- X\_9,7,2 -X\_9,9,2 0
- X\_9,8,2 -X\_9,9,2 0

X\_9,1,3 X\_9,2,3 X\_9,3,3 X\_9,4,3 X\_9,5,3 X\_9,6,3 X\_9,7,3 X\_9,8,3 X\_9,9,3 0

- X\_9,1,3 -X\_9,2,3 0
- X\_9,1,3 -X\_9,3,3 0
- X\_9,1,3 -X\_9,4,3 0
- X\_9,1,3 -X\_9,5,3 0
- X\_9,1,3 -X\_9,6,3 0
- X\_9,1,3 -X\_9,7,3 0
- X\_9,1,3 -X\_9,8,3 0
- X\_9,1,3 -X\_9,9,3 0
- X\_9,2,3 -X\_9,3,3 0
- X\_9,2,3 -X\_9,4,3 0
- X\_9,2,3 -X\_9,5,3 0
- X\_9,2,3 -X\_9,6,3 0
- X\_9,2,3 -X\_9,7,3 0
- X\_9,2,3 -X\_9,8,3 0
- X\_9,2,3 -X\_9,9,3 0
- X\_9,3,3 -X\_9,4,3 0
- X\_9,3,3 -X\_9,5,3 0
- X\_9,3,3 -X\_9,6,3 0
- X\_9,3,3 -X\_9,7,3 0
- X\_9,3,3 -X\_9,8,3 0
- X\_9,3,3 -X\_9,9,3 0
- X\_9,4,3 -X\_9,5,3 0
- X\_9,4,3 -X\_9,6,3 0
- X\_9,4,3 -X\_9,7,3 0
- X\_9,4,3 -X\_9,8,3 0
- X\_9,4,3 -X\_9,9,3 0
- X\_9,5,3 -X\_9,6,3 0
- X\_9,5,3 -X\_9,7,3 0
- X\_9,5,3 -X\_9,8,3 0
- X\_9,5,3 -X\_9,9,3 0
- X\_9,6,3 -X\_9,7,3 0
- X\_9,6,3 -X\_9,8,3 0
- X\_9,6,3 -X\_9,9,3 0
- X\_9,7,3 -X\_9,8,3 0
- X\_9,7,3 -X\_9,9,3 0
- X\_9,8,3 -X\_9,9,3 0

X\_9,1,4 X\_9,2,4 X\_9,3,4 X\_9,4,4 X\_9,5,4 X\_9,6,4 X\_9,7,4 X\_9,8,4 X\_9,9,4 0

- X\_9,1,4 -X\_9,2,4 0
- X\_9,1,4 -X\_9,3,4 0
- X\_9,1,4 -X\_9,4,4 0
- X\_9,1,4 -X\_9,5,4 0
- X\_9,1,4 -X\_9,6,4 0
- X\_9,1,4 -X\_9,7,4 0
- X\_9,1,4 -X\_9,8,4 0
- X\_9,1,4 -X\_9,9,4 0
- X\_9,2,4 -X\_9,3,4 0
- X\_9,2,4 -X\_9,4,4 0
- X\_9,2,4 -X\_9,5,4 0
- X\_9,2,4 -X\_9,6,4 0
- X\_9,2,4 -X\_9,7,4 0
- X\_9,2,4 -X\_9,8,4 0
- X\_9,2,4 -X\_9,9,4 0
- X\_9,3,4 -X\_9,4,4 0
- X\_9,3,4 -X\_9,5,4 0
- X\_9,3,4 -X\_9,6,4 0
- X\_9,3,4 -X\_9,7,4 0
- X\_9,3,4 -X\_9,8,4 0
- X\_9,3,4 -X\_9,9,4 0
- X\_9,4,4 -X\_9,5,4 0
- X\_9,4,4 -X\_9,6,4 0
- X\_9,4,4 -X\_9,7,4 0
- X\_9,4,4 -X\_9,8,4 0
- X\_9,4,4 -X\_9,9,4 0
- X\_9,5,4 -X\_9,6,4 0
- X\_9,5,4 -X\_9,7,4 0
- X\_9,5,4 -X\_9,8,4 0
- X\_9,5,4 -X\_9,9,4 0
- X\_9,6,4 -X\_9,7,4 0
- X\_9,6,4 -X\_9,8,4 0
- X\_9,6,4 -X\_9,9,4 0
- X\_9,7,4 -X\_9,8,4 0
- X\_9,7,4 -X\_9,9,4 0
- X\_9,8,4 -X\_9,9,4 0

X\_9,1,5 X\_9,2,5 X\_9,3,5 X\_9,4,5 X\_9,5,5 X\_9,6,5 X\_9,7,5 X\_9,8,5 X\_9,9,5 0

- X\_9,1,5 -X\_9,2,5 0
- X\_9,1,5 -X\_9,3,5 0
- X\_9,1,5 -X\_9,4,5 0
- X\_9,1,5 -X\_9,5,5 0
- X\_9,1,5 -X\_9,6,5 0
- X\_9,1,5 -X\_9,7,5 0
- X\_9,1,5 -X\_9,8,5 0
- X\_9,1,5 -X\_9,9,5 0
- X\_9,2,5 -X\_9,3,5 0
- X\_9,2,5 -X\_9,4,5 0
- X\_9,2,5 -X\_9,5,5 0
- X\_9,2,5 -X\_9,6,5 0
- X\_9,2,5 -X\_9,7,5 0
- X\_9,2,5 -X\_9,8,5 0
- X\_9,2,5 -X\_9,9,5 0
- X\_9,3,5 -X\_9,4,5 0
- X\_9,3,5 -X\_9,5,5 0
- X\_9,3,5 -X\_9,6,5 0
- X\_9,3,5 -X\_9,7,5 0
- X\_9,3,5 -X\_9,8,5 0
- X\_9,3,5 -X\_9,9,5 0
- X\_9,4,5 -X\_9,5,5 0
- X\_9,4,5 -X\_9,6,5 0
- X\_9,4,5 -X\_9,7,5 0
- X\_9,4,5 -X\_9,8,5 0
- X\_9,4,5 -X\_9,9,5 0
- X\_9,5,5 -X\_9,6,5 0
- X\_9,5,5 -X\_9,7,5 0
- X\_9,5,5 -X\_9,8,5 0
- X\_9,5,5 -X\_9,9,5 0
- X\_9,6,5 -X\_9,7,5 0
- X\_9,6,5 -X\_9,8,5 0
- X\_9,6,5 -X\_9,9,5 0
- X\_9,7,5 -X\_9,8,5 0
- X\_9,7,5 -X\_9,9,5 0
- X\_9,8,5 -X\_9,9,5 0

X\_9,1,6 X\_9,2,6 X\_9,3,6 X\_9,4,6 X\_9,5,6 X\_9,6,6 X\_9,7,6 X\_9,8,6 X\_9,9,6 0

- X\_9,1,6 -X\_9,2,6 0
- X\_9,1,6 -X\_9,3,6 0
- X\_9,1,6 -X\_9,4,6 0
- X\_9,1,6 -X\_9,5,6 0
- X\_9,1,6 -X\_9,6,6 0
- X\_9,1,6 -X\_9,7,6 0
- X\_9,1,6 -X\_9,8,6 0
- X\_9,1,6 -X\_9,9,6 0
- X\_9,2,6 -X\_9,3,6 0
- X\_9,2,6 -X\_9,4,6 0
- X\_9,2,6 -X\_9,5,6 0
- X\_9,2,6 -X\_9,6,6 0
- X\_9,2,6 -X\_9,7,6 0
- X\_9,2,6 -X\_9,8,6 0
- X\_9,2,6 -X\_9,9,6 0
- X\_9,3,6 -X\_9,4,6 0
- X\_9,3,6 -X\_9,5,6 0
- X\_9,3,6 -X\_9,6,6 0
- X\_9,3,6 -X\_9,7,6 0
- X\_9,3,6 -X\_9,8,6 0
- X\_9,3,6 -X\_9,9,6 0
- X\_9,4,6 -X\_9,5,6 0
- X\_9,4,6 -X\_9,6,6 0
- X\_9,4,6 -X\_9,7,6 0
- X\_9,4,6 -X\_9,8,6 0
- X\_9,4,6 -X\_9,9,6 0
- X\_9,5,6 -X\_9,6,6 0
- X\_9,5,6 -X\_9,7,6 0
- X\_9,5,6 -X\_9,8,6 0
- X\_9,5,6 -X\_9,9,6 0
- X\_9,6,6 -X\_9,7,6 0
- X\_9,6,6 -X\_9,8,6 0
- X\_9,6,6 -X\_9,9,6 0
- X\_9,7,6 -X\_9,8,6 0
- X\_9,7,6 -X\_9,9,6 0
- X\_9,8,6 -X\_9,9,6 0

X\_9,1,7 X\_9,2,7 X\_9,3,7 X\_9,4,7 X\_9,5,7 X\_9,6,7 X\_9,7,7 X\_9,8,7 X\_9,9,7 0

- X\_9,1,7 -X\_9,2,7 0
- X\_9,1,7 -X\_9,3,7 0
- X\_9,1,7 -X\_9,4,7 0
- X\_9,1,7 -X\_9,5,7 0
- X\_9,1,7 -X\_9,6,7 0
- X\_9,1,7 -X\_9,7,7 0
- X\_9,1,7 -X\_9,8,7 0
- X\_9,1,7 -X\_9,9,7 0
- X\_9,2,7 -X\_9,3,7 0
- X\_9,2,7 -X\_9,4,7 0
- X\_9,2,7 -X\_9,5,7 0
- X\_9,2,7 -X\_9,6,7 0
- X\_9,2,7 -X\_9,7,7 0
- X\_9,2,7 -X\_9,8,7 0
- X\_9,2,7 -X\_9,9,7 0
- X\_9,3,7 -X\_9,4,7 0
- X\_9,3,7 -X\_9,5,7 0
- X\_9,3,7 -X\_9,6,7 0
- X\_9,3,7 -X\_9,7,7 0
- X\_9,3,7 -X\_9,8,7 0
- X\_9,3,7 -X\_9,9,7 0
- X\_9,4,7 -X\_9,5,7 0
- X\_9,4,7 -X\_9,6,7 0
- X\_9,4,7 -X\_9,7,7 0
- X\_9,4,7 -X\_9,8,7 0
- X\_9,4,7 -X\_9,9,7 0
- X\_9,5,7 -X\_9,6,7 0
- X\_9,5,7 -X\_9,7,7 0
- X\_9,5,7 -X\_9,8,7 0
- X\_9,5,7 -X\_9,9,7 0
- X\_9,6,7 -X\_9,7,7 0
- X\_9,6,7 -X\_9,8,7 0
- X\_9,6,7 -X\_9,9,7 0
- X\_9,7,7 -X\_9,8,7 0
- X\_9,7,7 -X\_9,9,7 0
- X\_9,8,7 -X\_9,9,7 0

X\_9,1,8 X\_9,2,8 X\_9,3,8 X\_9,4,8 X\_9,5,8 X\_9,6,8 X\_9,7,8 X\_9,8,8 X\_9,9,8 0

- X\_9,1,8 -X\_9,2,8 0
- X\_9,1,8 -X\_9,3,8 0
- X\_9,1,8 -X\_9,4,8 0
- X\_9,1,8 -X\_9,5,8 0
- X\_9,1,8 -X\_9,6,8 0
- X\_9,1,8 -X\_9,7,8 0
- X\_9,1,8 -X\_9,8,8 0
- X\_9,1,8 -X\_9,9,8 0
- X\_9,2,8 -X\_9,3,8 0
- X\_9,2,8 -X\_9,4,8 0
- X\_9,2,8 -X\_9,5,8 0
- X\_9,2,8 -X\_9,6,8 0
- X\_9,2,8 -X\_9,7,8 0
- X\_9,2,8 -X\_9,8,8 0
- X\_9,2,8 -X\_9,9,8 0
- X\_9,3,8 -X\_9,4,8 0
- X\_9,3,8 -X\_9,5,8 0
- X\_9,3,8 -X\_9,6,8 0
- X\_9,3,8 -X\_9,7,8 0
- X\_9,3,8 -X\_9,8,8 0
- X\_9,3,8 -X\_9,9,8 0
- X\_9,4,8 -X\_9,5,8 0
- X\_9,4,8 -X\_9,6,8 0
- X\_9,4,8 -X\_9,7,8 0
- X\_9,4,8 -X\_9,8,8 0
- X\_9,4,8 -X\_9,9,8 0
- X\_9,5,8 -X\_9,6,8 0
- X\_9,5,8 -X\_9,7,8 0
- X\_9,5,8 -X\_9,8,8 0
- X\_9,5,8 -X\_9,9,8 0
- X\_9,6,8 -X\_9,7,8 0
- X\_9,6,8 -X\_9,8,8 0
- X\_9,6,8 -X\_9,9,8 0
- X\_9,7,8 -X\_9,8,8 0
- X\_9,7,8 -X\_9,9,8 0
- X\_9,8,8 -X\_9,9,8 0

X\_9,1,9 X\_9,2,9 X\_9,3,9 X\_9,4,9 X\_9,5,9 X\_9,6,9 X\_9,7,9 X\_9,8,9 X\_9,9,9 0

- X\_9,1,9 -X\_9,2,9 0
- X\_9,1,9 -X\_9,3,9 0
- X\_9,1,9 -X\_9,4,9 0
- X\_9,1,9 -X\_9,5,9 0
- X\_9,1,9 -X\_9,6,9 0
- X\_9,1,9 -X\_9,7,9 0
- X\_9,1,9 -X\_9,8,9 0
- X\_9,1,9 -X\_9,9,9 0
- X\_9,2,9 -X\_9,3,9 0
- X\_9,2,9 -X\_9,4,9 0
- X\_9,2,9 -X\_9,5,9 0
- X\_9,2,9 -X\_9,6,9 0
- X\_9,2,9 -X\_9,7,9 0
- X\_9,2,9 -X\_9,8,9 0
- X\_9,2,9 -X\_9,9,9 0
- X\_9,3,9 -X\_9,4,9 0
- X\_9,3,9 -X\_9,5,9 0
- X\_9,3,9 -X\_9,6,9 0
- X\_9,3,9 -X\_9,7,9 0
- X\_9,3,9 -X\_9,8,9 0
- X\_9,3,9 -X\_9,9,9 0
- X\_9,4,9 -X\_9,5,9 0
- X\_9,4,9 -X\_9,6,9 0
- X\_9,4,9 -X\_9,7,9 0
- X\_9,4,9 -X\_9,8,9 0
- X\_9,4,9 -X\_9,9,9 0
- X\_9,5,9 -X\_9,6,9 0
- X\_9,5,9 -X\_9,7,9 0
- X\_9,5,9 -X\_9,8,9 0
- X\_9,5,9 -X\_9,9,9 0
- X\_9,6,9 -X\_9,7,9 0
- X\_9,6,9 -X\_9,8,9 0
- X\_9,6,9 -X\_9,9,9 0
- X\_9,7,9 -X\_9,8,9 0
- X\_9,7,9 -X\_9,9,9 0
- X\_9,8,9 -X\_9,9,9 0

X\_1,1,1 X\_2,1,1 X\_3,1,1 X\_4,1,1 X\_5,1,1 X\_6,1,1 X\_7,1,1 X\_8,1,1 X\_9,1,1 0

- X\_1,1,1 -X\_2,1,1 0
- X\_1,1,1 -X\_3,1,1 0
- X\_1,1,1 -X\_4,1,1 0
- X\_1,1,1 -X\_5,1,1 0
- X\_1,1,1 -X\_6,1,1 0
- X\_1,1,1 -X\_7,1,1 0
- X\_1,1,1 -X\_8,1,1 0
- X\_1,1,1 -X\_9,1,1 0
- X\_2,1,1 -X\_3,1,1 0
- X\_2,1,1 -X\_4,1,1 0
- X\_2,1,1 -X\_5,1,1 0
- X\_2,1,1 -X\_6,1,1 0
- X\_2,1,1 -X\_7,1,1 0
- X\_2,1,1 -X\_8,1,1 0
- X\_2,1,1 -X\_9,1,1 0
- X\_3,1,1 -X\_4,1,1 0
- X\_3,1,1 -X\_5,1,1 0
- X\_3,1,1 -X\_6,1,1 0
- X\_3,1,1 -X\_7,1,1 0
- X\_3,1,1 -X\_8,1,1 0
- X\_3,1,1 -X\_9,1,1 0
- X\_4,1,1 -X\_5,1,1 0
- X\_4,1,1 -X\_6,1,1 0
- X\_4,1,1 -X\_7,1,1 0
- X\_4,1,1 -X\_8,1,1 0
- X\_4,1,1 -X\_9,1,1 0
- X\_5,1,1 -X\_6,1,1 0
- X\_5,1,1 -X\_7,1,1 0
- X\_5,1,1 -X\_8,1,1 0
- X\_5,1,1 -X\_9,1,1 0
- X\_6,1,1 -X\_7,1,1 0
- X\_6,1,1 -X\_8,1,1 0
- X\_6,1,1 -X\_9,1,1 0
- X\_7,1,1 -X\_8,1,1 0
- X\_7,1,1 -X\_9,1,1 0
- X\_8,1,1 -X\_9,1,1 0

X\_1,1,2 X\_2,1,2 X\_3,1,2 X\_4,1,2 X\_5,1,2 X\_6,1,2 X\_7,1,2 X\_8,1,2 X\_9,1,2 0

- X\_1,1,2 -X\_2,1,2 0
- X\_1,1,2 -X\_3,1,2 0
- X\_1,1,2 -X\_4,1,2 0
- X\_1,1,2 -X\_5,1,2 0
- X\_1,1,2 -X\_6,1,2 0
- X\_1,1,2 -X\_7,1,2 0
- X\_1,1,2 -X\_8,1,2 0
- X\_1,1,2 -X\_9,1,2 0
- X\_2,1,2 -X\_3,1,2 0
- X\_2,1,2 -X\_4,1,2 0
- X\_2,1,2 -X\_5,1,2 0
- X\_2,1,2 -X\_6,1,2 0
- X\_2,1,2 -X\_7,1,2 0
- X\_2,1,2 -X\_8,1,2 0
- X\_2,1,2 -X\_9,1,2 0
- X\_3,1,2 -X\_4,1,2 0
- X\_3,1,2 -X\_5,1,2 0
- X\_3,1,2 -X\_6,1,2 0
- X\_3,1,2 -X\_7,1,2 0
- X\_3,1,2 -X\_8,1,2 0
- X\_3,1,2 -X\_9,1,2 0
- X\_4,1,2 -X\_5,1,2 0
- X\_4,1,2 -X\_6,1,2 0
- X\_4,1,2 -X\_7,1,2 0
- X\_4,1,2 -X\_8,1,2 0
- X\_4,1,2 -X\_9,1,2 0
- X\_5,1,2 -X\_6,1,2 0
- X\_5,1,2 -X\_7,1,2 0
- X\_5,1,2 -X\_8,1,2 0
- X\_5,1,2 -X\_9,1,2 0
- X\_6,1,2 -X\_7,1,2 0
- X\_6,1,2 -X\_8,1,2 0
- X\_6,1,2 -X\_9,1,2 0
- X\_7,1,2 -X\_8,1,2 0
- X\_7,1,2 -X\_9,1,2 0
- X\_8,1,2 -X\_9,1,2 0

X\_1,1,3 X\_2,1,3 X\_3,1,3 X\_4,1,3 X\_5,1,3 X\_6,1,3 X\_7,1,3 X\_8,1,3 X\_9,1,3 0

- X\_1,1,3 -X\_2,1,3 0
- X\_1,1,3 -X\_3,1,3 0
- X\_1,1,3 -X\_4,1,3 0
- X\_1,1,3 -X\_5,1,3 0
- X\_1,1,3 -X\_6,1,3 0
- X\_1,1,3 -X\_7,1,3 0
- X\_1,1,3 -X\_8,1,3 0
- X\_1,1,3 -X\_9,1,3 0
- X\_2,1,3 -X\_3,1,3 0
- X\_2,1,3 -X\_4,1,3 0
- X\_2,1,3 -X\_5,1,3 0
- X\_2,1,3 -X\_6,1,3 0
- X\_2,1,3 -X\_7,1,3 0
- X\_2,1,3 -X\_8,1,3 0
- X\_2,1,3 -X\_9,1,3 0
- X\_3,1,3 -X\_4,1,3 0
- X\_3,1,3 -X\_5,1,3 0
- X\_3,1,3 -X\_6,1,3 0
- X\_3,1,3 -X\_7,1,3 0
- X\_3,1,3 -X\_8,1,3 0
- X\_3,1,3 -X\_9,1,3 0
- X\_4,1,3 -X\_5,1,3 0
- X\_4,1,3 -X\_6,1,3 0
- X\_4,1,3 -X\_7,1,3 0
- X\_4,1,3 -X\_8,1,3 0
- X\_4,1,3 -X\_9,1,3 0
- X\_5,1,3 -X\_6,1,3 0
- X\_5,1,3 -X\_7,1,3 0
- X\_5,1,3 -X\_8,1,3 0
- X\_5,1,3 -X\_9,1,3 0
- X\_6,1,3 -X\_7,1,3 0
- X\_6,1,3 -X\_8,1,3 0
- X\_6,1,3 -X\_9,1,3 0
- X\_7,1,3 -X\_8,1,3 0
- X\_7,1,3 -X\_9,1,3 0
- X\_8,1,3 -X\_9,1,3 0

X\_1,1,4 X\_2,1,4 X\_3,1,4 X\_4,1,4 X\_5,1,4 X\_6,1,4 X\_7,1,4 X\_8,1,4 X\_9,1,4 0

- X\_1,1,4 -X\_2,1,4 0
- X\_1,1,4 -X\_3,1,4 0
- X\_1,1,4 -X\_4,1,4 0
- X\_1,1,4 -X\_5,1,4 0
- X\_1,1,4 -X\_6,1,4 0
- X\_1,1,4 -X\_7,1,4 0
- X\_1,1,4 -X\_8,1,4 0
- X\_1,1,4 -X\_9,1,4 0
- X\_2,1,4 -X\_3,1,4 0
- X\_2,1,4 -X\_4,1,4 0
- X\_2,1,4 -X\_5,1,4 0
- X\_2,1,4 -X\_6,1,4 0
- X\_2,1,4 -X\_7,1,4 0
- X\_2,1,4 -X\_8,1,4 0
- X\_2,1,4 -X\_9,1,4 0
- X\_3,1,4 -X\_4,1,4 0
- X\_3,1,4 -X\_5,1,4 0
- X\_3,1,4 -X\_6,1,4 0
- X\_3,1,4 -X\_7,1,4 0
- X\_3,1,4 -X\_8,1,4 0
- X\_3,1,4 -X\_9,1,4 0
- X\_4,1,4 -X\_5,1,4 0
- X\_4,1,4 -X\_6,1,4 0
- X\_4,1,4 -X\_7,1,4 0
- X\_4,1,4 -X\_8,1,4 0
- X\_4,1,4 -X\_9,1,4 0
- X\_5,1,4 -X\_6,1,4 0
- X\_5,1,4 -X\_7,1,4 0
- X\_5,1,4 -X\_8,1,4 0
- X\_5,1,4 -X\_9,1,4 0
- X\_6,1,4 -X\_7,1,4 0
- X\_6,1,4 -X\_8,1,4 0
- X\_6,1,4 -X\_9,1,4 0
- X\_7,1,4 -X\_8,1,4 0
- X\_7,1,4 -X\_9,1,4 0
- X\_8,1,4 -X\_9,1,4 0

X\_1,1,5 X\_2,1,5 X\_3,1,5 X\_4,1,5 X\_5,1,5 X\_6,1,5 X\_7,1,5 X\_8,1,5 X\_9,1,5 0

- X\_1,1,5 -X\_2,1,5 0
- X\_1,1,5 -X\_3,1,5 0
- X\_1,1,5 -X\_4,1,5 0
- X\_1,1,5 -X\_5,1,5 0
- X\_1,1,5 -X\_6,1,5 0
- X\_1,1,5 -X\_7,1,5 0
- X\_1,1,5 -X\_8,1,5 0
- X\_1,1,5 -X\_9,1,5 0
- X\_2,1,5 -X\_3,1,5 0
- X\_2,1,5 -X\_4,1,5 0
- X\_2,1,5 -X\_5,1,5 0
- X\_2,1,5 -X\_6,1,5 0
- X\_2,1,5 -X\_7,1,5 0
- X\_2,1,5 -X\_8,1,5 0
- X\_2,1,5 -X\_9,1,5 0
- X\_3,1,5 -X\_4,1,5 0
- X\_3,1,5 -X\_5,1,5 0
- X\_3,1,5 -X\_6,1,5 0
- X\_3,1,5 -X\_7,1,5 0
- X\_3,1,5 -X\_8,1,5 0
- X\_3,1,5 -X\_9,1,5 0
- X\_4,1,5 -X\_5,1,5 0
- X\_4,1,5 -X\_6,1,5 0
- X\_4,1,5 -X\_7,1,5 0
- X\_4,1,5 -X\_8,1,5 0
- X\_4,1,5 -X\_9,1,5 0
- X\_5,1,5 -X\_6,1,5 0
- X\_5,1,5 -X\_7,1,5 0
- X\_5,1,5 -X\_8,1,5 0
- X\_5,1,5 -X\_9,1,5 0
- X\_6,1,5 -X\_7,1,5 0
- X\_6,1,5 -X\_8,1,5 0
- X\_6,1,5 -X\_9,1,5 0
- X\_7,1,5 -X\_8,1,5 0
- X\_7,1,5 -X\_9,1,5 0
- X\_8,1,5 -X\_9,1,5 0

X\_1,1,6 X\_2,1,6 X\_3,1,6 X\_4,1,6 X\_5,1,6 X\_6,1,6 X\_7,1,6 X\_8,1,6 X\_9,1,6 0

- X\_1,1,6 -X\_2,1,6 0
- X\_1,1,6 -X\_3,1,6 0
- X\_1,1,6 -X\_4,1,6 0
- X\_1,1,6 -X\_5,1,6 0
- X\_1,1,6 -X\_6,1,6 0
- X\_1,1,6 -X\_7,1,6 0
- X\_1,1,6 -X\_8,1,6 0
- X\_1,1,6 -X\_9,1,6 0
- X\_2,1,6 -X\_3,1,6 0
- X\_2,1,6 -X\_4,1,6 0
- X\_2,1,6 -X\_5,1,6 0
- X\_2,1,6 -X\_6,1,6 0
- X\_2,1,6 -X\_7,1,6 0
- X\_2,1,6 -X\_8,1,6 0
- X\_2,1,6 -X\_9,1,6 0
- X\_3,1,6 -X\_4,1,6 0
- X\_3,1,6 -X\_5,1,6 0
- X\_3,1,6 -X\_6,1,6 0
- X\_3,1,6 -X\_7,1,6 0
- X\_3,1,6 -X\_8,1,6 0
- X\_3,1,6 -X\_9,1,6 0
- X\_4,1,6 -X\_5,1,6 0
- X\_4,1,6 -X\_6,1,6 0
- X\_4,1,6 -X\_7,1,6 0
- X\_4,1,6 -X\_8,1,6 0
- X\_4,1,6 -X\_9,1,6 0
- X\_5,1,6 -X\_6,1,6 0
- X\_5,1,6 -X\_7,1,6 0
- X\_5,1,6 -X\_8,1,6 0
- X\_5,1,6 -X\_9,1,6 0
- X\_6,1,6 -X\_7,1,6 0
- X\_6,1,6 -X\_8,1,6 0
- X\_6,1,6 -X\_9,1,6 0
- X\_7,1,6 -X\_8,1,6 0
- X\_7,1,6 -X\_9,1,6 0
- X\_8,1,6 -X\_9,1,6 0

X\_1,1,7 X\_2,1,7 X\_3,1,7 X\_4,1,7 X\_5,1,7 X\_6,1,7 X\_7,1,7 X\_8,1,7 X\_9,1,7 0

- X\_1,1,7 -X\_2,1,7 0
- X\_1,1,7 -X\_3,1,7 0
- X\_1,1,7 -X\_4,1,7 0
- X\_1,1,7 -X\_5,1,7 0
- X\_1,1,7 -X\_6,1,7 0
- X\_1,1,7 -X\_7,1,7 0
- X\_1,1,7 -X\_8,1,7 0
- X\_1,1,7 -X\_9,1,7 0
- X\_2,1,7 -X\_3,1,7 0
- X\_2,1,7 -X\_4,1,7 0
- X\_2,1,7 -X\_5,1,7 0
- X\_2,1,7 -X\_6,1,7 0
- X\_2,1,7 -X\_7,1,7 0
- X\_2,1,7 -X\_8,1,7 0
- X\_2,1,7 -X\_9,1,7 0
- X\_3,1,7 -X\_4,1,7 0
- X\_3,1,7 -X\_5,1,7 0
- X\_3,1,7 -X\_6,1,7 0
- X\_3,1,7 -X\_7,1,7 0
- X\_3,1,7 -X\_8,1,7 0
- X\_3,1,7 -X\_9,1,7 0
- X\_4,1,7 -X\_5,1,7 0
- X\_4,1,7 -X\_6,1,7 0
- X\_4,1,7 -X\_7,1,7 0
- X\_4,1,7 -X\_8,1,7 0
- X\_4,1,7 -X\_9,1,7 0
- X\_5,1,7 -X\_6,1,7 0
- X\_5,1,7 -X\_7,1,7 0
- X\_5,1,7 -X\_8,1,7 0
- X\_5,1,7 -X\_9,1,7 0
- X\_6,1,7 -X\_7,1,7 0
- X\_6,1,7 -X\_8,1,7 0
- X\_6,1,7 -X\_9,1,7 0
- X\_7,1,7 -X\_8,1,7 0
- X\_7,1,7 -X\_9,1,7 0
- X\_8,1,7 -X\_9,1,7 0

X\_1,1,8 X\_2,1,8 X\_3,1,8 X\_4,1,8 X\_5,1,8 X\_6,1,8 X\_7,1,8 X\_8,1,8 X\_9,1,8 0

- X\_1,1,8 -X\_2,1,8 0
- X\_1,1,8 -X\_3,1,8 0
- X\_1,1,8 -X\_4,1,8 0
- X\_1,1,8 -X\_5,1,8 0
- X\_1,1,8 -X\_6,1,8 0
- X\_1,1,8 -X\_7,1,8 0
- X\_1,1,8 -X\_8,1,8 0
- X\_1,1,8 -X\_9,1,8 0
- X\_2,1,8 -X\_3,1,8 0
- X\_2,1,8 -X\_4,1,8 0
- X\_2,1,8 -X\_5,1,8 0
- X\_2,1,8 -X\_6,1,8 0
- X\_2,1,8 -X\_7,1,8 0
- X\_2,1,8 -X\_8,1,8 0
- X\_2,1,8 -X\_9,1,8 0
- X\_3,1,8 -X\_4,1,8 0
- X\_3,1,8 -X\_5,1,8 0
- X\_3,1,8 -X\_6,1,8 0
- X\_3,1,8 -X\_7,1,8 0
- X\_3,1,8 -X\_8,1,8 0
- X\_3,1,8 -X\_9,1,8 0
- X\_4,1,8 -X\_5,1,8 0
- X\_4,1,8 -X\_6,1,8 0
- X\_4,1,8 -X\_7,1,8 0
- X\_4,1,8 -X\_8,1,8 0
- X\_4,1,8 -X\_9,1,8 0
- X\_5,1,8 -X\_6,1,8 0
- X\_5,1,8 -X\_7,1,8 0
- X\_5,1,8 -X\_8,1,8 0
- X\_5,1,8 -X\_9,1,8 0
- X\_6,1,8 -X\_7,1,8 0
- X\_6,1,8 -X\_8,1,8 0
- X\_6,1,8 -X\_9,1,8 0
- X\_7,1,8 -X\_8,1,8 0
- X\_7,1,8 -X\_9,1,8 0
- X\_8,1,8 -X\_9,1,8 0

X\_1,1,9 X\_2,1,9 X\_3,1,9 X\_4,1,9 X\_5,1,9 X\_6,1,9 X\_7,1,9 X\_8,1,9 X\_9,1,9 0

- X\_1,1,9 -X\_2,1,9 0
- X\_1,1,9 -X\_3,1,9 0
- X\_1,1,9 -X\_4,1,9 0
- X\_1,1,9 -X\_5,1,9 0
- X\_1,1,9 -X\_6,1,9 0
- X\_1,1,9 -X\_7,1,9 0
- X\_1,1,9 -X\_8,1,9 0
- X\_1,1,9 -X\_9,1,9 0
- X\_2,1,9 -X\_3,1,9 0
- X\_2,1,9 -X\_4,1,9 0
- X\_2,1,9 -X\_5,1,9 0
- X\_2,1,9 -X\_6,1,9 0
- X\_2,1,9 -X\_7,1,9 0
- X\_2,1,9 -X\_8,1,9 0
- X\_2,1,9 -X\_9,1,9 0
- X\_3,1,9 -X\_4,1,9 0
- X\_3,1,9 -X\_5,1,9 0
- X\_3,1,9 -X\_6,1,9 0
- X\_3,1,9 -X\_7,1,9 0
- X\_3,1,9 -X\_8,1,9 0
- X\_3,1,9 -X\_9,1,9 0
- X\_4,1,9 -X\_5,1,9 0
- X\_4,1,9 -X\_6,1,9 0
- X\_4,1,9 -X\_7,1,9 0
- X\_4,1,9 -X\_8,1,9 0
- X\_4,1,9 -X\_9,1,9 0
- X\_5,1,9 -X\_6,1,9 0
- X\_5,1,9 -X\_7,1,9 0
- X\_5,1,9 -X\_8,1,9 0
- X\_5,1,9 -X\_9,1,9 0
- X\_6,1,9 -X\_7,1,9 0
- X\_6,1,9 -X\_8,1,9 0
- X\_6,1,9 -X\_9,1,9 0
- X\_7,1,9 -X\_8,1,9 0
- X\_7,1,9 -X\_9,1,9 0
- X\_8,1,9 -X\_9,1,9 0

X\_1,2,1 X\_2,2,1 X\_3,2,1 X\_4,2,1 X\_5,2,1 X\_6,2,1 X\_7,2,1 X\_8,2,1 X\_9,2,1 0

- X\_1,2,1 -X\_2,2,1 0
- X\_1,2,1 -X\_3,2,1 0
- X\_1,2,1 -X\_4,2,1 0
- X\_1,2,1 -X\_5,2,1 0
- X\_1,2,1 -X\_6,2,1 0
- X\_1,2,1 -X\_7,2,1 0
- X\_1,2,1 -X\_8,2,1 0
- X\_1,2,1 -X\_9,2,1 0
- X\_2,2,1 -X\_3,2,1 0
- X\_2,2,1 -X\_4,2,1 0
- X\_2,2,1 -X\_5,2,1 0
- X\_2,2,1 -X\_6,2,1 0
- X\_2,2,1 -X\_7,2,1 0
- X\_2,2,1 -X\_8,2,1 0
- X\_2,2,1 -X\_9,2,1 0
- X\_3,2,1 -X\_4,2,1 0
- X\_3,2,1 -X\_5,2,1 0
- X\_3,2,1 -X\_6,2,1 0
- X\_3,2,1 -X\_7,2,1 0
- X\_3,2,1 -X\_8,2,1 0
- X\_3,2,1 -X\_9,2,1 0
- X\_4,2,1 -X\_5,2,1 0
- X\_4,2,1 -X\_6,2,1 0
- X\_4,2,1 -X\_7,2,1 0
- X\_4,2,1 -X\_8,2,1 0
- X\_4,2,1 -X\_9,2,1 0
- X\_5,2,1 -X\_6,2,1 0
- X\_5,2,1 -X\_7,2,1 0
- X\_5,2,1 -X\_8,2,1 0
- X\_5,2,1 -X\_9,2,1 0
- X\_6,2,1 -X\_7,2,1 0
- X\_6,2,1 -X\_8,2,1 0
- X\_6,2,1 -X\_9,2,1 0
- X\_7,2,1 -X\_8,2,1 0
- X\_7,2,1 -X\_9,2,1 0
- X\_8,2,1 -X\_9,2,1 0

X\_1,2,2 X\_2,2,2 X\_3,2,2 X\_4,2,2 X\_5,2,2 X\_6,2,2 X\_7,2,2 X\_8,2,2 X\_9,2,2 0

- X\_1,2,2 -X\_2,2,2 0
- X\_1,2,2 -X\_3,2,2 0
- X\_1,2,2 -X\_4,2,2 0
- X\_1,2,2 -X\_5,2,2 0
- X\_1,2,2 -X\_6,2,2 0
- X\_1,2,2 -X\_7,2,2 0
- X\_1,2,2 -X\_8,2,2 0
- X\_1,2,2 -X\_9,2,2 0
- X\_2,2,2 -X\_3,2,2 0
- X\_2,2,2 -X\_4,2,2 0
- X\_2,2,2 -X\_5,2,2 0
- X\_2,2,2 -X\_6,2,2 0
- X\_2,2,2 -X\_7,2,2 0
- X\_2,2,2 -X\_8,2,2 0
- X\_2,2,2 -X\_9,2,2 0
- X\_3,2,2 -X\_4,2,2 0
- X\_3,2,2 -X\_5,2,2 0
- X\_3,2,2 -X\_6,2,2 0
- X\_3,2,2 -X\_7,2,2 0
- X\_3,2,2 -X\_8,2,2 0
- X\_3,2,2 -X\_9,2,2 0
- X\_4,2,2 -X\_5,2,2 0
- X\_4,2,2 -X\_6,2,2 0
- X\_4,2,2 -X\_7,2,2 0
- X\_4,2,2 -X\_8,2,2 0
- X\_4,2,2 -X\_9,2,2 0
- X\_5,2,2 -X\_6,2,2 0
- X\_5,2,2 -X\_7,2,2 0
- X\_5,2,2 -X\_8,2,2 0
- X\_5,2,2 -X\_9,2,2 0
- X\_6,2,2 -X\_7,2,2 0
- X\_6,2,2 -X\_8,2,2 0
- X\_6,2,2 -X\_9,2,2 0
- X\_7,2,2 -X\_8,2,2 0
- X\_7,2,2 -X\_9,2,2 0
- X\_8,2,2 -X\_9,2,2 0

X\_1,2,3 X\_2,2,3 X\_3,2,3 X\_4,2,3 X\_5,2,3 X\_6,2,3 X\_7,2,3 X\_8,2,3 X\_9,2,3 0

- X\_1,2,3 -X\_2,2,3 0
- X\_1,2,3 -X\_3,2,3 0
- X\_1,2,3 -X\_4,2,3 0
- X\_1,2,3 -X\_5,2,3 0
- X\_1,2,3 -X\_6,2,3 0
- X\_1,2,3 -X\_7,2,3 0
- X\_1,2,3 -X\_8,2,3 0
- X\_1,2,3 -X\_9,2,3 0
- X\_2,2,3 -X\_3,2,3 0
- X\_2,2,3 -X\_4,2,3 0
- X\_2,2,3 -X\_5,2,3 0
- X\_2,2,3 -X\_6,2,3 0
- X\_2,2,3 -X\_7,2,3 0
- X\_2,2,3 -X\_8,2,3 0
- X\_2,2,3 -X\_9,2,3 0
- X\_3,2,3 -X\_4,2,3 0
- X\_3,2,3 -X\_5,2,3 0
- X\_3,2,3 -X\_6,2,3 0
- X\_3,2,3 -X\_7,2,3 0
- X\_3,2,3 -X\_8,2,3 0
- X\_3,2,3 -X\_9,2,3 0
- X\_4,2,3 -X\_5,2,3 0
- X\_4,2,3 -X\_6,2,3 0
- X\_4,2,3 -X\_7,2,3 0
- X\_4,2,3 -X\_8,2,3 0
- X\_4,2,3 -X\_9,2,3 0
- X\_5,2,3 -X\_6,2,3 0
- X\_5,2,3 -X\_7,2,3 0
- X\_5,2,3 -X\_8,2,3 0
- X\_5,2,3 -X\_9,2,3 0
- X\_6,2,3 -X\_7,2,3 0
- X\_6,2,3 -X\_8,2,3 0
- X\_6,2,3 -X\_9,2,3 0
- X\_7,2,3 -X\_8,2,3 0
- X\_7,2,3 -X\_9,2,3 0
- X\_8,2,3 -X\_9,2,3 0

X\_1,2,4 X\_2,2,4 X\_3,2,4 X\_4,2,4 X\_5,2,4 X\_6,2,4 X\_7,2,4 X\_8,2,4 X\_9,2,4 0

- X\_1,2,4 -X\_2,2,4 0
- X\_1,2,4 -X\_3,2,4 0
- X\_1,2,4 -X\_4,2,4 0
- X\_1,2,4 -X\_5,2,4 0
- X\_1,2,4 -X\_6,2,4 0
- X\_1,2,4 -X\_7,2,4 0
- X\_1,2,4 -X\_8,2,4 0
- X\_1,2,4 -X\_9,2,4 0
- X\_2,2,4 -X\_3,2,4 0
- X\_2,2,4 -X\_4,2,4 0
- X\_2,2,4 -X\_5,2,4 0
- X\_2,2,4 -X\_6,2,4 0
- X\_2,2,4 -X\_7,2,4 0
- X\_2,2,4 -X\_8,2,4 0
- X\_2,2,4 -X\_9,2,4 0
- X\_3,2,4 -X\_4,2,4 0
- X\_3,2,4 -X\_5,2,4 0
- X\_3,2,4 -X\_6,2,4 0
- X\_3,2,4 -X\_7,2,4 0
- X\_3,2,4 -X\_8,2,4 0
- X\_3,2,4 -X\_9,2,4 0
- X\_4,2,4 -X\_5,2,4 0
- X\_4,2,4 -X\_6,2,4 0
- X\_4,2,4 -X\_7,2,4 0
- X\_4,2,4 -X\_8,2,4 0
- X\_4,2,4 -X\_9,2,4 0
- X\_5,2,4 -X\_6,2,4 0
- X\_5,2,4 -X\_7,2,4 0
- X\_5,2,4 -X\_8,2,4 0
- X\_5,2,4 -X\_9,2,4 0
- X\_6,2,4 -X\_7,2,4 0
- X\_6,2,4 -X\_8,2,4 0
- X\_6,2,4 -X\_9,2,4 0
- X\_7,2,4 -X\_8,2,4 0
- X\_7,2,4 -X\_9,2,4 0
- X\_8,2,4 -X\_9,2,4 0

X\_1,2,5 X\_2,2,5 X\_3,2,5 X\_4,2,5 X\_5,2,5 X\_6,2,5 X\_7,2,5 X\_8,2,5 X\_9,2,5 0

- X\_1,2,5 -X\_2,2,5 0
- X\_1,2,5 -X\_3,2,5 0
- X\_1,2,5 -X\_4,2,5 0
- X\_1,2,5 -X\_5,2,5 0
- X\_1,2,5 -X\_6,2,5 0
- X\_1,2,5 -X\_7,2,5 0
- X\_1,2,5 -X\_8,2,5 0
- X\_1,2,5 -X\_9,2,5 0
- X\_2,2,5 -X\_3,2,5 0
- X\_2,2,5 -X\_4,2,5 0
- X\_2,2,5 -X\_5,2,5 0
- X\_2,2,5 -X\_6,2,5 0
- X\_2,2,5 -X\_7,2,5 0
- X\_2,2,5 -X\_8,2,5 0
- X\_2,2,5 -X\_9,2,5 0
- X\_3,2,5 -X\_4,2,5 0
- X\_3,2,5 -X\_5,2,5 0
- X\_3,2,5 -X\_6,2,5 0
- X\_3,2,5 -X\_7,2,5 0
- X\_3,2,5 -X\_8,2,5 0
- X\_3,2,5 -X\_9,2,5 0
- X\_4,2,5 -X\_5,2,5 0
- X\_4,2,5 -X\_6,2,5 0
- X\_4,2,5 -X\_7,2,5 0
- X\_4,2,5 -X\_8,2,5 0
- X\_4,2,5 -X\_9,2,5 0
- X\_5,2,5 -X\_6,2,5 0
- X\_5,2,5 -X\_7,2,5 0
- X\_5,2,5 -X\_8,2,5 0
- X\_5,2,5 -X\_9,2,5 0
- X\_6,2,5 -X\_7,2,5 0
- X\_6,2,5 -X\_8,2,5 0
- X\_6,2,5 -X\_9,2,5 0
- X\_7,2,5 -X\_8,2,5 0
- X\_7,2,5 -X\_9,2,5 0
- X\_8,2,5 -X\_9,2,5 0

X\_1,2,6 X\_2,2,6 X\_3,2,6 X\_4,2,6 X\_5,2,6 X\_6,2,6 X\_7,2,6 X\_8,2,6 X\_9,2,6 0

- X\_1,2,6 -X\_2,2,6 0
- X\_1,2,6 -X\_3,2,6 0
- X\_1,2,6 -X\_4,2,6 0
- X\_1,2,6 -X\_5,2,6 0
- X\_1,2,6 -X\_6,2,6 0
- X\_1,2,6 -X\_7,2,6 0
- X\_1,2,6 -X\_8,2,6 0
- X\_1,2,6 -X\_9,2,6 0
- X\_2,2,6 -X\_3,2,6 0
- X\_2,2,6 -X\_4,2,6 0
- X\_2,2,6 -X\_5,2,6 0
- X\_2,2,6 -X\_6,2,6 0
- X\_2,2,6 -X\_7,2,6 0
- X\_2,2,6 -X\_8,2,6 0
- X\_2,2,6 -X\_9,2,6 0
- X\_3,2,6 -X\_4,2,6 0
- X\_3,2,6 -X\_5,2,6 0
- X\_3,2,6 -X\_6,2,6 0
- X\_3,2,6 -X\_7,2,6 0
- X\_3,2,6 -X\_8,2,6 0
- X\_3,2,6 -X\_9,2,6 0
- X\_4,2,6 -X\_5,2,6 0
- X\_4,2,6 -X\_6,2,6 0
- X\_4,2,6 -X\_7,2,6 0
- X\_4,2,6 -X\_8,2,6 0
- X\_4,2,6 -X\_9,2,6 0
- X\_5,2,6 -X\_6,2,6 0
- X\_5,2,6 -X\_7,2,6 0
- X\_5,2,6 -X\_8,2,6 0
- X\_5,2,6 -X\_9,2,6 0
- X\_6,2,6 -X\_7,2,6 0
- X\_6,2,6 -X\_8,2,6 0
- X\_6,2,6 -X\_9,2,6 0
- X\_7,2,6 -X\_8,2,6 0
- X\_7,2,6 -X\_9,2,6 0
- X\_8,2,6 -X\_9,2,6 0

X\_1,2,7 X\_2,2,7 X\_3,2,7 X\_4,2,7 X\_5,2,7 X\_6,2,7 X\_7,2,7 X\_8,2,7 X\_9,2,7 0

- X\_1,2,7 -X\_2,2,7 0
- X\_1,2,7 -X\_3,2,7 0
- X\_1,2,7 -X\_4,2,7 0
- X\_1,2,7 -X\_5,2,7 0
- X\_1,2,7 -X\_6,2,7 0
- X\_1,2,7 -X\_7,2,7 0
- X\_1,2,7 -X\_8,2,7 0
- X\_1,2,7 -X\_9,2,7 0
- X\_2,2,7 -X\_3,2,7 0
- X\_2,2,7 -X\_4,2,7 0
- X\_2,2,7 -X\_5,2,7 0
- X\_2,2,7 -X\_6,2,7 0
- X\_2,2,7 -X\_7,2,7 0
- X\_2,2,7 -X\_8,2,7 0
- X\_2,2,7 -X\_9,2,7 0
- X\_3,2,7 -X\_4,2,7 0
- X\_3,2,7 -X\_5,2,7 0
- X\_3,2,7 -X\_6,2,7 0
- X\_3,2,7 -X\_7,2,7 0
- X\_3,2,7 -X\_8,2,7 0
- X\_3,2,7 -X\_9,2,7 0
- X\_4,2,7 -X\_5,2,7 0
- X\_4,2,7 -X\_6,2,7 0
- X\_4,2,7 -X\_7,2,7 0
- X\_4,2,7 -X\_8,2,7 0
- X\_4,2,7 -X\_9,2,7 0
- X\_5,2,7 -X\_6,2,7 0
- X\_5,2,7 -X\_7,2,7 0
- X\_5,2,7 -X\_8,2,7 0
- X\_5,2,7 -X\_9,2,7 0
- X\_6,2,7 -X\_7,2,7 0
- X\_6,2,7 -X\_8,2,7 0
- X\_6,2,7 -X\_9,2,7 0
- X\_7,2,7 -X\_8,2,7 0
- X\_7,2,7 -X\_9,2,7 0
- X\_8,2,7 -X\_9,2,7 0

X\_1,2,8 X\_2,2,8 X\_3,2,8 X\_4,2,8 X\_5,2,8 X\_6,2,8 X\_7,2,8 X\_8,2,8 X\_9,2,8 0

- X\_1,2,8 -X\_2,2,8 0
- X\_1,2,8 -X\_3,2,8 0
- X\_1,2,8 -X\_4,2,8 0
- X\_1,2,8 -X\_5,2,8 0
- X\_1,2,8 -X\_6,2,8 0
- X\_1,2,8 -X\_7,2,8 0
- X\_1,2,8 -X\_8,2,8 0
- X\_1,2,8 -X\_9,2,8 0
- X\_2,2,8 -X\_3,2,8 0
- X\_2,2,8 -X\_4,2,8 0
- X\_2,2,8 -X\_5,2,8 0
- X\_2,2,8 -X\_6,2,8 0
- X\_2,2,8 -X\_7,2,8 0
- X\_2,2,8 -X\_8,2,8 0
- X\_2,2,8 -X\_9,2,8 0
- X\_3,2,8 -X\_4,2,8 0
- X\_3,2,8 -X\_5,2,8 0
- X\_3,2,8 -X\_6,2,8 0
- X\_3,2,8 -X\_7,2,8 0
- X\_3,2,8 -X\_8,2,8 0
- X\_3,2,8 -X\_9,2,8 0
- X\_4,2,8 -X\_5,2,8 0
- X\_4,2,8 -X\_6,2,8 0
- X\_4,2,8 -X\_7,2,8 0
- X\_4,2,8 -X\_8,2,8 0
- X\_4,2,8 -X\_9,2,8 0
- X\_5,2,8 -X\_6,2,8 0
- X\_5,2,8 -X\_7,2,8 0
- X\_5,2,8 -X\_8,2,8 0
- X\_5,2,8 -X\_9,2,8 0
- X\_6,2,8 -X\_7,2,8 0
- X\_6,2,8 -X\_8,2,8 0
- X\_6,2,8 -X\_9,2,8 0
- X\_7,2,8 -X\_8,2,8 0
- X\_7,2,8 -X\_9,2,8 0
- X\_8,2,8 -X\_9,2,8 0

X\_1,2,9 X\_2,2,9 X\_3,2,9 X\_4,2,9 X\_5,2,9 X\_6,2,9 X\_7,2,9 X\_8,2,9 X\_9,2,9 0

- X\_1,2,9 -X\_2,2,9 0
- X\_1,2,9 -X\_3,2,9 0
- X\_1,2,9 -X\_4,2,9 0
- X\_1,2,9 -X\_5,2,9 0
- X\_1,2,9 -X\_6,2,9 0
- X\_1,2,9 -X\_7,2,9 0
- X\_1,2,9 -X\_8,2,9 0
- X\_1,2,9 -X\_9,2,9 0
- X\_2,2,9 -X\_3,2,9 0
- X\_2,2,9 -X\_4,2,9 0
- X\_2,2,9 -X\_5,2,9 0
- X\_2,2,9 -X\_6,2,9 0
- X\_2,2,9 -X\_7,2,9 0
- X\_2,2,9 -X\_8,2,9 0
- X\_2,2,9 -X\_9,2,9 0
- X\_3,2,9 -X\_4,2,9 0
- X\_3,2,9 -X\_5,2,9 0
- X\_3,2,9 -X\_6,2,9 0
- X\_3,2,9 -X\_7,2,9 0
- X\_3,2,9 -X\_8,2,9 0
- X\_3,2,9 -X\_9,2,9 0
- X\_4,2,9 -X\_5,2,9 0
- X\_4,2,9 -X\_6,2,9 0
- X\_4,2,9 -X\_7,2,9 0
- X\_4,2,9 -X\_8,2,9 0
- X\_4,2,9 -X\_9,2,9 0
- X\_5,2,9 -X\_6,2,9 0
- X\_5,2,9 -X\_7,2,9 0
- X\_5,2,9 -X\_8,2,9 0
- X\_5,2,9 -X\_9,2,9 0
- X\_6,2,9 -X\_7,2,9 0
- X\_6,2,9 -X\_8,2,9 0
- X\_6,2,9 -X\_9,2,9 0
- X\_7,2,9 -X\_8,2,9 0
- X\_7,2,9 -X\_9,2,9 0
- X\_8,2,9 -X\_9,2,9 0

X\_1,3,1 X\_2,3,1 X\_3,3,1 X\_4,3,1 X\_5,3,1 X\_6,3,1 X\_7,3,1 X\_8,3,1 X\_9,3,1 0

- X\_1,3,1 -X\_2,3,1 0
- X\_1,3,1 -X\_3,3,1 0
- X\_1,3,1 -X\_4,3,1 0
- X\_1,3,1 -X\_5,3,1 0
- X\_1,3,1 -X\_6,3,1 0
- X\_1,3,1 -X\_7,3,1 0
- X\_1,3,1 -X\_8,3,1 0
- X\_1,3,1 -X\_9,3,1 0
- X\_2,3,1 -X\_3,3,1 0
- X\_2,3,1 -X\_4,3,1 0
- X\_2,3,1 -X\_5,3,1 0
- X\_2,3,1 -X\_6,3,1 0
- X\_2,3,1 -X\_7,3,1 0
- X\_2,3,1 -X\_8,3,1 0
- X\_2,3,1 -X\_9,3,1 0
- X\_3,3,1 -X\_4,3,1 0
- X\_3,3,1 -X\_5,3,1 0
- X\_3,3,1 -X\_6,3,1 0
- X\_3,3,1 -X\_7,3,1 0
- X\_3,3,1 -X\_8,3,1 0
- X\_3,3,1 -X\_9,3,1 0
- X\_4,3,1 -X\_5,3,1 0
- X\_4,3,1 -X\_6,3,1 0
- X\_4,3,1 -X\_7,3,1 0
- X\_4,3,1 -X\_8,3,1 0
- X\_4,3,1 -X\_9,3,1 0
- X\_5,3,1 -X\_6,3,1 0
- X\_5,3,1 -X\_7,3,1 0
- X\_5,3,1 -X\_8,3,1 0
- X\_5,3,1 -X\_9,3,1 0
- X\_6,3,1 -X\_7,3,1 0
- X\_6,3,1 -X\_8,3,1 0
- X\_6,3,1 -X\_9,3,1 0
- X\_7,3,1 -X\_8,3,1 0
- X\_7,3,1 -X\_9,3,1 0
- X\_8,3,1 -X\_9,3,1 0

X\_1,3,2 X\_2,3,2 X\_3,3,2 X\_4,3,2 X\_5,3,2 X\_6,3,2 X\_7,3,2 X\_8,3,2 X\_9,3,2 0

- X\_1,3,2 -X\_2,3,2 0
- X\_1,3,2 -X\_3,3,2 0
- X\_1,3,2 -X\_4,3,2 0
- X\_1,3,2 -X\_5,3,2 0
- X\_1,3,2 -X\_6,3,2 0
- X\_1,3,2 -X\_7,3,2 0
- X\_1,3,2 -X\_8,3,2 0
- X\_1,3,2 -X\_9,3,2 0
- X\_2,3,2 -X\_3,3,2 0
- X\_2,3,2 -X\_4,3,2 0
- X\_2,3,2 -X\_5,3,2 0
- X\_2,3,2 -X\_6,3,2 0
- X\_2,3,2 -X\_7,3,2 0
- X\_2,3,2 -X\_8,3,2 0
- X\_2,3,2 -X\_9,3,2 0
- X\_3,3,2 -X\_4,3,2 0
- X\_3,3,2 -X\_5,3,2 0
- X\_3,3,2 -X\_6,3,2 0
- X\_3,3,2 -X\_7,3,2 0
- X\_3,3,2 -X\_8,3,2 0
- X\_3,3,2 -X\_9,3,2 0
- X\_4,3,2 -X\_5,3,2 0
- X\_4,3,2 -X\_6,3,2 0
- X\_4,3,2 -X\_7,3,2 0
- X\_4,3,2 -X\_8,3,2 0
- X\_4,3,2 -X\_9,3,2 0
- X\_5,3,2 -X\_6,3,2 0
- X\_5,3,2 -X\_7,3,2 0
- X\_5,3,2 -X\_8,3,2 0
- X\_5,3,2 -X\_9,3,2 0
- X\_6,3,2 -X\_7,3,2 0
- X\_6,3,2 -X\_8,3,2 0
- X\_6,3,2 -X\_9,3,2 0
- X\_7,3,2 -X\_8,3,2 0
- X\_7,3,2 -X\_9,3,2 0
- X\_8,3,2 -X\_9,3,2 0

X\_1,3,3 X\_2,3,3 X\_3,3,3 X\_4,3,3 X\_5,3,3 X\_6,3,3 X\_7,3,3 X\_8,3,3 X\_9,3,3 0

- X\_1,3,3 -X\_2,3,3 0
- X\_1,3,3 -X\_3,3,3 0
- X\_1,3,3 -X\_4,3,3 0
- X\_1,3,3 -X\_5,3,3 0
- X\_1,3,3 -X\_6,3,3 0
- X\_1,3,3 -X\_7,3,3 0
- X\_1,3,3 -X\_8,3,3 0
- X\_1,3,3 -X\_9,3,3 0
- X\_2,3,3 -X\_3,3,3 0
- X\_2,3,3 -X\_4,3,3 0
- X\_2,3,3 -X\_5,3,3 0
- X\_2,3,3 -X\_6,3,3 0
- X\_2,3,3 -X\_7,3,3 0
- X\_2,3,3 -X\_8,3,3 0
- X\_2,3,3 -X\_9,3,3 0
- X\_3,3,3 -X\_4,3,3 0
- X\_3,3,3 -X\_5,3,3 0
- X\_3,3,3 -X\_6,3,3 0
- X\_3,3,3 -X\_7,3,3 0
- X\_3,3,3 -X\_8,3,3 0
- X\_3,3,3 -X\_9,3,3 0
- X\_4,3,3 -X\_5,3,3 0
- X\_4,3,3 -X\_6,3,3 0
- X\_4,3,3 -X\_7,3,3 0
- X\_4,3,3 -X\_8,3,3 0
- X\_4,3,3 -X\_9,3,3 0
- X\_5,3,3 -X\_6,3,3 0
- X\_5,3,3 -X\_7,3,3 0
- X\_5,3,3 -X\_8,3,3 0
- X\_5,3,3 -X\_9,3,3 0
- X\_6,3,3 -X\_7,3,3 0
- X\_6,3,3 -X\_8,3,3 0
- X\_6,3,3 -X\_9,3,3 0
- X\_7,3,3 -X\_8,3,3 0
- X\_7,3,3 -X\_9,3,3 0
- X\_8,3,3 -X\_9,3,3 0

X\_1,3,4 X\_2,3,4 X\_3,3,4 X\_4,3,4 X\_5,3,4 X\_6,3,4 X\_7,3,4 X\_8,3,4 X\_9,3,4 0

- X\_1,3,4 -X\_2,3,4 0
- X\_1,3,4 -X\_3,3,4 0
- X\_1,3,4 -X\_4,3,4 0
- X\_1,3,4 -X\_5,3,4 0
- X\_1,3,4 -X\_6,3,4 0
- X\_1,3,4 -X\_7,3,4 0
- X\_1,3,4 -X\_8,3,4 0
- X\_1,3,4 -X\_9,3,4 0
- X\_2,3,4 -X\_3,3,4 0
- X\_2,3,4 -X\_4,3,4 0
- X\_2,3,4 -X\_5,3,4 0
- X\_2,3,4 -X\_6,3,4 0
- X\_2,3,4 -X\_7,3,4 0
- X\_2,3,4 -X\_8,3,4 0
- X\_2,3,4 -X\_9,3,4 0
- X\_3,3,4 -X\_4,3,4 0
- X\_3,3,4 -X\_5,3,4 0
- X\_3,3,4 -X\_6,3,4 0
- X\_3,3,4 -X\_7,3,4 0
- X\_3,3,4 -X\_8,3,4 0
- X\_3,3,4 -X\_9,3,4 0
- X\_4,3,4 -X\_5,3,4 0
- X\_4,3,4 -X\_6,3,4 0
- X\_4,3,4 -X\_7,3,4 0
- X\_4,3,4 -X\_8,3,4 0
- X\_4,3,4 -X\_9,3,4 0
- X\_5,3,4 -X\_6,3,4 0
- X\_5,3,4 -X\_7,3,4 0
- X\_5,3,4 -X\_8,3,4 0
- X\_5,3,4 -X\_9,3,4 0
- X\_6,3,4 -X\_7,3,4 0
- X\_6,3,4 -X\_8,3,4 0
- X\_6,3,4 -X\_9,3,4 0
- X\_7,3,4 -X\_8,3,4 0
- X\_7,3,4 -X\_9,3,4 0
- X\_8,3,4 -X\_9,3,4 0

X\_1,3,5 X\_2,3,5 X\_3,3,5 X\_4,3,5 X\_5,3,5 X\_6,3,5 X\_7,3,5 X\_8,3,5 X\_9,3,5 0

- X\_1,3,5 -X\_2,3,5 0
- X\_1,3,5 -X\_3,3,5 0
- X\_1,3,5 -X\_4,3,5 0
- X\_1,3,5 -X\_5,3,5 0
- X\_1,3,5 -X\_6,3,5 0
- X\_1,3,5 -X\_7,3,5 0
- X\_1,3,5 -X\_8,3,5 0
- X\_1,3,5 -X\_9,3,5 0
- X\_2,3,5 -X\_3,3,5 0
- X\_2,3,5 -X\_4,3,5 0
- X\_2,3,5 -X\_5,3,5 0
- X\_2,3,5 -X\_6,3,5 0
- X\_2,3,5 -X\_7,3,5 0
- X\_2,3,5 -X\_8,3,5 0
- X\_2,3,5 -X\_9,3,5 0
- X\_3,3,5 -X\_4,3,5 0
- X\_3,3,5 -X\_5,3,5 0
- X\_3,3,5 -X\_6,3,5 0
- X\_3,3,5 -X\_7,3,5 0
- X\_3,3,5 -X\_8,3,5 0
- X\_3,3,5 -X\_9,3,5 0
- X\_4,3,5 -X\_5,3,5 0
- X\_4,3,5 -X\_6,3,5 0
- X\_4,3,5 -X\_7,3,5 0
- X\_4,3,5 -X\_8,3,5 0
- X\_4,3,5 -X\_9,3,5 0
- X\_5,3,5 -X\_6,3,5 0
- X\_5,3,5 -X\_7,3,5 0
- X\_5,3,5 -X\_8,3,5 0
- X\_5,3,5 -X\_9,3,5 0
- X\_6,3,5 -X\_7,3,5 0
- X\_6,3,5 -X\_8,3,5 0
- X\_6,3,5 -X\_9,3,5 0
- X\_7,3,5 -X\_8,3,5 0
- X\_7,3,5 -X\_9,3,5 0
- X\_8,3,5 -X\_9,3,5 0

X\_1,3,6 X\_2,3,6 X\_3,3,6 X\_4,3,6 X\_5,3,6 X\_6,3,6 X\_7,3,6 X\_8,3,6 X\_9,3,6 0

- X\_1,3,6 -X\_2,3,6 0
- X\_1,3,6 -X\_3,3,6 0
- X\_1,3,6 -X\_4,3,6 0
- X\_1,3,6 -X\_5,3,6 0
- X\_1,3,6 -X\_6,3,6 0
- X\_1,3,6 -X\_7,3,6 0
- X\_1,3,6 -X\_8,3,6 0
- X\_1,3,6 -X\_9,3,6 0
- X\_2,3,6 -X\_3,3,6 0
- X\_2,3,6 -X\_4,3,6 0
- X\_2,3,6 -X\_5,3,6 0
- X\_2,3,6 -X\_6,3,6 0
- X\_2,3,6 -X\_7,3,6 0
- X\_2,3,6 -X\_8,3,6 0
- X\_2,3,6 -X\_9,3,6 0
- X\_3,3,6 -X\_4,3,6 0
- X\_3,3,6 -X\_5,3,6 0
- X\_3,3,6 -X\_6,3,6 0
- X\_3,3,6 -X\_7,3,6 0
- X\_3,3,6 -X\_8,3,6 0
- X\_3,3,6 -X\_9,3,6 0
- X\_4,3,6 -X\_5,3,6 0
- X\_4,3,6 -X\_6,3,6 0
- X\_4,3,6 -X\_7,3,6 0
- X\_4,3,6 -X\_8,3,6 0
- X\_4,3,6 -X\_9,3,6 0
- X\_5,3,6 -X\_6,3,6 0
- X\_5,3,6 -X\_7,3,6 0
- X\_5,3,6 -X\_8,3,6 0
- X\_5,3,6 -X\_9,3,6 0
- X\_6,3,6 -X\_7,3,6 0
- X\_6,3,6 -X\_8,3,6 0
- X\_6,3,6 -X\_9,3,6 0
- X\_7,3,6 -X\_8,3,6 0
- X\_7,3,6 -X\_9,3,6 0
- X\_8,3,6 -X\_9,3,6 0

X\_1,3,7 X\_2,3,7 X\_3,3,7 X\_4,3,7 X\_5,3,7 X\_6,3,7 X\_7,3,7 X\_8,3,7 X\_9,3,7 0

- X\_1,3,7 -X\_2,3,7 0
- X\_1,3,7 -X\_3,3,7 0
- X\_1,3,7 -X\_4,3,7 0
- X\_1,3,7 -X\_5,3,7 0
- X\_1,3,7 -X\_6,3,7 0
- X\_1,3,7 -X\_7,3,7 0
- X\_1,3,7 -X\_8,3,7 0
- X\_1,3,7 -X\_9,3,7 0
- X\_2,3,7 -X\_3,3,7 0
- X\_2,3,7 -X\_4,3,7 0
- X\_2,3,7 -X\_5,3,7 0
- X\_2,3,7 -X\_6,3,7 0
- X\_2,3,7 -X\_7,3,7 0
- X\_2,3,7 -X\_8,3,7 0
- X\_2,3,7 -X\_9,3,7 0
- X\_3,3,7 -X\_4,3,7 0
- X\_3,3,7 -X\_5,3,7 0
- X\_3,3,7 -X\_6,3,7 0
- X\_3,3,7 -X\_7,3,7 0
- X\_3,3,7 -X\_8,3,7 0
- X\_3,3,7 -X\_9,3,7 0
- X\_4,3,7 -X\_5,3,7 0
- X\_4,3,7 -X\_6,3,7 0
- X\_4,3,7 -X\_7,3,7 0
- X\_4,3,7 -X\_8,3,7 0
- X\_4,3,7 -X\_9,3,7 0
- X\_5,3,7 -X\_6,3,7 0
- X\_5,3,7 -X\_7,3,7 0
- X\_5,3,7 -X\_8,3,7 0
- X\_5,3,7 -X\_9,3,7 0
- X\_6,3,7 -X\_7,3,7 0
- X\_6,3,7 -X\_8,3,7 0
- X\_6,3,7 -X\_9,3,7 0
- X\_7,3,7 -X\_8,3,7 0
- X\_7,3,7 -X\_9,3,7 0
- X\_8,3,7 -X\_9,3,7 0

X\_1,3,8 X\_2,3,8 X\_3,3,8 X\_4,3,8 X\_5,3,8 X\_6,3,8 X\_7,3,8 X\_8,3,8 X\_9,3,8 0

- X\_1,3,8 -X\_2,3,8 0
- X\_1,3,8 -X\_3,3,8 0
- X\_1,3,8 -X\_4,3,8 0
- X\_1,3,8 -X\_5,3,8 0
- X\_1,3,8 -X\_6,3,8 0
- X\_1,3,8 -X\_7,3,8 0
- X\_1,3,8 -X\_8,3,8 0
- X\_1,3,8 -X\_9,3,8 0
- X\_2,3,8 -X\_3,3,8 0
- X\_2,3,8 -X\_4,3,8 0
- X\_2,3,8 -X\_5,3,8 0
- X\_2,3,8 -X\_6,3,8 0
- X\_2,3,8 -X\_7,3,8 0
- X\_2,3,8 -X\_8,3,8 0
- X\_2,3,8 -X\_9,3,8 0
- X\_3,3,8 -X\_4,3,8 0
- X\_3,3,8 -X\_5,3,8 0
- X\_3,3,8 -X\_6,3,8 0
- X\_3,3,8 -X\_7,3,8 0
- X\_3,3,8 -X\_8,3,8 0
- X\_3,3,8 -X\_9,3,8 0
- X\_4,3,8 -X\_5,3,8 0
- X\_4,3,8 -X\_6,3,8 0
- X\_4,3,8 -X\_7,3,8 0
- X\_4,3,8 -X\_8,3,8 0
- X\_4,3,8 -X\_9,3,8 0
- X\_5,3,8 -X\_6,3,8 0
- X\_5,3,8 -X\_7,3,8 0
- X\_5,3,8 -X\_8,3,8 0
- X\_5,3,8 -X\_9,3,8 0
- X\_6,3,8 -X\_7,3,8 0
- X\_6,3,8 -X\_8,3,8 0
- X\_6,3,8 -X\_9,3,8 0
- X\_7,3,8 -X\_8,3,8 0
- X\_7,3,8 -X\_9,3,8 0
- X\_8,3,8 -X\_9,3,8 0

X\_1,3,9 X\_2,3,9 X\_3,3,9 X\_4,3,9 X\_5,3,9 X\_6,3,9 X\_7,3,9 X\_8,3,9 X\_9,3,9 0

- X\_1,3,9 -X\_2,3,9 0
- X\_1,3,9 -X\_3,3,9 0
- X\_1,3,9 -X\_4,3,9 0
- X\_1,3,9 -X\_5,3,9 0
- X\_1,3,9 -X\_6,3,9 0
- X\_1,3,9 -X\_7,3,9 0
- X\_1,3,9 -X\_8,3,9 0
- X\_1,3,9 -X\_9,3,9 0
- X\_2,3,9 -X\_3,3,9 0
- X\_2,3,9 -X\_4,3,9 0
- X\_2,3,9 -X\_5,3,9 0
- X\_2,3,9 -X\_6,3,9 0
- X\_2,3,9 -X\_7,3,9 0
- X\_2,3,9 -X\_8,3,9 0
- X\_2,3,9 -X\_9,3,9 0
- X\_3,3,9 -X\_4,3,9 0
- X\_3,3,9 -X\_5,3,9 0
- X\_3,3,9 -X\_6,3,9 0
- X\_3,3,9 -X\_7,3,9 0
- X\_3,3,9 -X\_8,3,9 0
- X\_3,3,9 -X\_9,3,9 0
- X\_4,3,9 -X\_5,3,9 0
- X\_4,3,9 -X\_6,3,9 0
- X\_4,3,9 -X\_7,3,9 0
- X\_4,3,9 -X\_8,3,9 0
- X\_4,3,9 -X\_9,3,9 0
- X\_5,3,9 -X\_6,3,9 0
- X\_5,3,9 -X\_7,3,9 0
- X\_5,3,9 -X\_8,3,9 0
- X\_5,3,9 -X\_9,3,9 0
- X\_6,3,9 -X\_7,3,9 0
- X\_6,3,9 -X\_8,3,9 0
- X\_6,3,9 -X\_9,3,9 0
- X\_7,3,9 -X\_8,3,9 0
- X\_7,3,9 -X\_9,3,9 0
- X\_8,3,9 -X\_9,3,9 0

X\_1,4,1 X\_2,4,1 X\_3,4,1 X\_4,4,1 X\_5,4,1 X\_6,4,1 X\_7,4,1 X\_8,4,1 X\_9,4,1 0

- X\_1,4,1 -X\_2,4,1 0
- X\_1,4,1 -X\_3,4,1 0
- X\_1,4,1 -X\_4,4,1 0
- X\_1,4,1 -X\_5,4,1 0
- X\_1,4,1 -X\_6,4,1 0
- X\_1,4,1 -X\_7,4,1 0
- X\_1,4,1 -X\_8,4,1 0
- X\_1,4,1 -X\_9,4,1 0
- X\_2,4,1 -X\_3,4,1 0
- X\_2,4,1 -X\_4,4,1 0
- X\_2,4,1 -X\_5,4,1 0
- X\_2,4,1 -X\_6,4,1 0
- X\_2,4,1 -X\_7,4,1 0
- X\_2,4,1 -X\_8,4,1 0
- X\_2,4,1 -X\_9,4,1 0
- X\_3,4,1 -X\_4,4,1 0
- X\_3,4,1 -X\_5,4,1 0
- X\_3,4,1 -X\_6,4,1 0
- X\_3,4,1 -X\_7,4,1 0
- X\_3,4,1 -X\_8,4,1 0
- X\_3,4,1 -X\_9,4,1 0
- X\_4,4,1 -X\_5,4,1 0
- X\_4,4,1 -X\_6,4,1 0
- X\_4,4,1 -X\_7,4,1 0
- X\_4,4,1 -X\_8,4,1 0
- X\_4,4,1 -X\_9,4,1 0
- X\_5,4,1 -X\_6,4,1 0
- X\_5,4,1 -X\_7,4,1 0
- X\_5,4,1 -X\_8,4,1 0
- X\_5,4,1 -X\_9,4,1 0
- X\_6,4,1 -X\_7,4,1 0
- X\_6,4,1 -X\_8,4,1 0
- X\_6,4,1 -X\_9,4,1 0
- X\_7,4,1 -X\_8,4,1 0
- X\_7,4,1 -X\_9,4,1 0
- X\_8,4,1 -X\_9,4,1 0

X\_1,4,2 X\_2,4,2 X\_3,4,2 X\_4,4,2 X\_5,4,2 X\_6,4,2 X\_7,4,2 X\_8,4,2 X\_9,4,2 0

- X\_1,4,2 -X\_2,4,2 0
- X\_1,4,2 -X\_3,4,2 0
- X\_1,4,2 -X\_4,4,2 0
- X\_1,4,2 -X\_5,4,2 0
- X\_1,4,2 -X\_6,4,2 0
- X\_1,4,2 -X\_7,4,2 0
- X\_1,4,2 -X\_8,4,2 0
- X\_1,4,2 -X\_9,4,2 0
- X\_2,4,2 -X\_3,4,2 0
- X\_2,4,2 -X\_4,4,2 0
- X\_2,4,2 -X\_5,4,2 0
- X\_2,4,2 -X\_6,4,2 0
- X\_2,4,2 -X\_7,4,2 0
- X\_2,4,2 -X\_8,4,2 0
- X\_2,4,2 -X\_9,4,2 0
- X\_3,4,2 -X\_4,4,2 0
- X\_3,4,2 -X\_5,4,2 0
- X\_3,4,2 -X\_6,4,2 0
- X\_3,4,2 -X\_7,4,2 0
- X\_3,4,2 -X\_8,4,2 0
- X\_3,4,2 -X\_9,4,2 0
- X\_4,4,2 -X\_5,4,2 0
- X\_4,4,2 -X\_6,4,2 0
- X\_4,4,2 -X\_7,4,2 0
- X\_4,4,2 -X\_8,4,2 0
- X\_4,4,2 -X\_9,4,2 0
- X\_5,4,2 -X\_6,4,2 0
- X\_5,4,2 -X\_7,4,2 0
- X\_5,4,2 -X\_8,4,2 0
- X\_5,4,2 -X\_9,4,2 0
- X\_6,4,2 -X\_7,4,2 0
- X\_6,4,2 -X\_8,4,2 0
- X\_6,4,2 -X\_9,4,2 0
- X\_7,4,2 -X\_8,4,2 0
- X\_7,4,2 -X\_9,4,2 0
- X\_8,4,2 -X\_9,4,2 0

X\_1,4,3 X\_2,4,3 X\_3,4,3 X\_4,4,3 X\_5,4,3 X\_6,4,3 X\_7,4,3 X\_8,4,3 X\_9,4,3 0

- X\_1,4,3 -X\_2,4,3 0
- X\_1,4,3 -X\_3,4,3 0
- X\_1,4,3 -X\_4,4,3 0
- X\_1,4,3 -X\_5,4,3 0
- X\_1,4,3 -X\_6,4,3 0
- X\_1,4,3 -X\_7,4,3 0
- X\_1,4,3 -X\_8,4,3 0
- X\_1,4,3 -X\_9,4,3 0
- X\_2,4,3 -X\_3,4,3 0
- X\_2,4,3 -X\_4,4,3 0
- X\_2,4,3 -X\_5,4,3 0
- X\_2,4,3 -X\_6,4,3 0
- X\_2,4,3 -X\_7,4,3 0
- X\_2,4,3 -X\_8,4,3 0
- X\_2,4,3 -X\_9,4,3 0
- X\_3,4,3 -X\_4,4,3 0
- X\_3,4,3 -X\_5,4,3 0
- X\_3,4,3 -X\_6,4,3 0
- X\_3,4,3 -X\_7,4,3 0
- X\_3,4,3 -X\_8,4,3 0
- X\_3,4,3 -X\_9,4,3 0
- X\_4,4,3 -X\_5,4,3 0
- X\_4,4,3 -X\_6,4,3 0
- X\_4,4,3 -X\_7,4,3 0
- X\_4,4,3 -X\_8,4,3 0
- X\_4,4,3 -X\_9,4,3 0
- X\_5,4,3 -X\_6,4,3 0
- X\_5,4,3 -X\_7,4,3 0
- X\_5,4,3 -X\_8,4,3 0
- X\_5,4,3 -X\_9,4,3 0
- X\_6,4,3 -X\_7,4,3 0
- X\_6,4,3 -X\_8,4,3 0
- X\_6,4,3 -X\_9,4,3 0
- X\_7,4,3 -X\_8,4,3 0
- X\_7,4,3 -X\_9,4,3 0
- X\_8,4,3 -X\_9,4,3 0

X\_1,4,4 X\_2,4,4 X\_3,4,4 X\_4,4,4 X\_5,4,4 X\_6,4,4 X\_7,4,4 X\_8,4,4 X\_9,4,4 0

- X\_1,4,4 -X\_2,4,4 0
- X\_1,4,4 -X\_3,4,4 0
- X\_1,4,4 -X\_4,4,4 0
- X\_1,4,4 -X\_5,4,4 0
- X\_1,4,4 -X\_6,4,4 0
- X\_1,4,4 -X\_7,4,4 0
- X\_1,4,4 -X\_8,4,4 0
- X\_1,4,4 -X\_9,4,4 0
- X\_2,4,4 -X\_3,4,4 0
- X\_2,4,4 -X\_4,4,4 0
- X\_2,4,4 -X\_5,4,4 0
- X\_2,4,4 -X\_6,4,4 0
- X\_2,4,4 -X\_7,4,4 0
- X\_2,4,4 -X\_8,4,4 0
- X\_2,4,4 -X\_9,4,4 0
- X\_3,4,4 -X\_4,4,4 0
- X\_3,4,4 -X\_5,4,4 0
- X\_3,4,4 -X\_6,4,4 0
- X\_3,4,4 -X\_7,4,4 0
- X\_3,4,4 -X\_8,4,4 0
- X\_3,4,4 -X\_9,4,4 0
- X\_4,4,4 -X\_5,4,4 0
- X\_4,4,4 -X\_6,4,4 0
- X\_4,4,4 -X\_7,4,4 0
- X\_4,4,4 -X\_8,4,4 0
- X\_4,4,4 -X\_9,4,4 0
- X\_5,4,4 -X\_6,4,4 0
- X\_5,4,4 -X\_7,4,4 0
- X\_5,4,4 -X\_8,4,4 0
- X\_5,4,4 -X\_9,4,4 0
- X\_6,4,4 -X\_7,4,4 0
- X\_6,4,4 -X\_8,4,4 0
- X\_6,4,4 -X\_9,4,4 0
- X\_7,4,4 -X\_8,4,4 0
- X\_7,4,4 -X\_9,4,4 0
- X\_8,4,4 -X\_9,4,4 0

X\_1,4,5 X\_2,4,5 X\_3,4,5 X\_4,4,5 X\_5,4,5 X\_6,4,5 X\_7,4,5 X\_8,4,5 X\_9,4,5 0

- X\_1,4,5 -X\_2,4,5 0
- X\_1,4,5 -X\_3,4,5 0
- X\_1,4,5 -X\_4,4,5 0
- X\_1,4,5 -X\_5,4,5 0
- X\_1,4,5 -X\_6,4,5 0
- X\_1,4,5 -X\_7,4,5 0
- X\_1,4,5 -X\_8,4,5 0
- X\_1,4,5 -X\_9,4,5 0
- X\_2,4,5 -X\_3,4,5 0
- X\_2,4,5 -X\_4,4,5 0
- X\_2,4,5 -X\_5,4,5 0
- X\_2,4,5 -X\_6,4,5 0
- X\_2,4,5 -X\_7,4,5 0
- X\_2,4,5 -X\_8,4,5 0
- X\_2,4,5 -X\_9,4,5 0
- X\_3,4,5 -X\_4,4,5 0
- X\_3,4,5 -X\_5,4,5 0
- X\_3,4,5 -X\_6,4,5 0
- X\_3,4,5 -X\_7,4,5 0
- X\_3,4,5 -X\_8,4,5 0
- X\_3,4,5 -X\_9,4,5 0
- X\_4,4,5 -X\_5,4,5 0
- X\_4,4,5 -X\_6,4,5 0
- X\_4,4,5 -X\_7,4,5 0
- X\_4,4,5 -X\_8,4,5 0
- X\_4,4,5 -X\_9,4,5 0
- X\_5,4,5 -X\_6,4,5 0
- X\_5,4,5 -X\_7,4,5 0
- X\_5,4,5 -X\_8,4,5 0
- X\_5,4,5 -X\_9,4,5 0
- X\_6,4,5 -X\_7,4,5 0
- X\_6,4,5 -X\_8,4,5 0
- X\_6,4,5 -X\_9,4,5 0
- X\_7,4,5 -X\_8,4,5 0
- X\_7,4,5 -X\_9,4,5 0
- X\_8,4,5 -X\_9,4,5 0

X\_1,4,6 X\_2,4,6 X\_3,4,6 X\_4,4,6 X\_5,4,6 X\_6,4,6 X\_7,4,6 X\_8,4,6 X\_9,4,6 0

- X\_1,4,6 -X\_2,4,6 0
- X\_1,4,6 -X\_3,4,6 0
- X\_1,4,6 -X\_4,4,6 0
- X\_1,4,6 -X\_5,4,6 0
- X\_1,4,6 -X\_6,4,6 0
- X\_1,4,6 -X\_7,4,6 0
- X\_1,4,6 -X\_8,4,6 0
- X\_1,4,6 -X\_9,4,6 0
- X\_2,4,6 -X\_3,4,6 0
- X\_2,4,6 -X\_4,4,6 0
- X\_2,4,6 -X\_5,4,6 0
- X\_2,4,6 -X\_6,4,6 0
- X\_2,4,6 -X\_7,4,6 0
- X\_2,4,6 -X\_8,4,6 0
- X\_2,4,6 -X\_9,4,6 0
- X\_3,4,6 -X\_4,4,6 0
- X\_3,4,6 -X\_5,4,6 0
- X\_3,4,6 -X\_6,4,6 0
- X\_3,4,6 -X\_7,4,6 0
- X\_3,4,6 -X\_8,4,6 0
- X\_3,4,6 -X\_9,4,6 0
- X\_4,4,6 -X\_5,4,6 0
- X\_4,4,6 -X\_6,4,6 0
- X\_4,4,6 -X\_7,4,6 0
- X\_4,4,6 -X\_8,4,6 0
- X\_4,4,6 -X\_9,4,6 0
- X\_5,4,6 -X\_6,4,6 0
- X\_5,4,6 -X\_7,4,6 0
- X\_5,4,6 -X\_8,4,6 0
- X\_5,4,6 -X\_9,4,6 0
- X\_6,4,6 -X\_7,4,6 0
- X\_6,4,6 -X\_8,4,6 0
- X\_6,4,6 -X\_9,4,6 0
- X\_7,4,6 -X\_8,4,6 0
- X\_7,4,6 -X\_9,4,6 0
- X\_8,4,6 -X\_9,4,6 0

X\_1,4,7 X\_2,4,7 X\_3,4,7 X\_4,4,7 X\_5,4,7 X\_6,4,7 X\_7,4,7 X\_8,4,7 X\_9,4,7 0

- X\_1,4,7 -X\_2,4,7 0
- X\_1,4,7 -X\_3,4,7 0
- X\_1,4,7 -X\_4,4,7 0
- X\_1,4,7 -X\_5,4,7 0
- X\_1,4,7 -X\_6,4,7 0
- X\_1,4,7 -X\_7,4,7 0
- X\_1,4,7 -X\_8,4,7 0
- X\_1,4,7 -X\_9,4,7 0
- X\_2,4,7 -X\_3,4,7 0
- X\_2,4,7 -X\_4,4,7 0
- X\_2,4,7 -X\_5,4,7 0
- X\_2,4,7 -X\_6,4,7 0
- X\_2,4,7 -X\_7,4,7 0
- X\_2,4,7 -X\_8,4,7 0
- X\_2,4,7 -X\_9,4,7 0
- X\_3,4,7 -X\_4,4,7 0
- X\_3,4,7 -X\_5,4,7 0
- X\_3,4,7 -X\_6,4,7 0
- X\_3,4,7 -X\_7,4,7 0
- X\_3,4,7 -X\_8,4,7 0
- X\_3,4,7 -X\_9,4,7 0
- X\_4,4,7 -X\_5,4,7 0
- X\_4,4,7 -X\_6,4,7 0
- X\_4,4,7 -X\_7,4,7 0
- X\_4,4,7 -X\_8,4,7 0
- X\_4,4,7 -X\_9,4,7 0
- X\_5,4,7 -X\_6,4,7 0
- X\_5,4,7 -X\_7,4,7 0
- X\_5,4,7 -X\_8,4,7 0
- X\_5,4,7 -X\_9,4,7 0
- X\_6,4,7 -X\_7,4,7 0
- X\_6,4,7 -X\_8,4,7 0
- X\_6,4,7 -X\_9,4,7 0
- X\_7,4,7 -X\_8,4,7 0
- X\_7,4,7 -X\_9,4,7 0
- X\_8,4,7 -X\_9,4,7 0

X\_1,4,8 X\_2,4,8 X\_3,4,8 X\_4,4,8 X\_5,4,8 X\_6,4,8 X\_7,4,8 X\_8,4,8 X\_9,4,8 0

- X\_1,4,8 -X\_2,4,8 0
- X\_1,4,8 -X\_3,4,8 0
- X\_1,4,8 -X\_4,4,8 0
- X\_1,4,8 -X\_5,4,8 0
- X\_1,4,8 -X\_6,4,8 0
- X\_1,4,8 -X\_7,4,8 0
- X\_1,4,8 -X\_8,4,8 0
- X\_1,4,8 -X\_9,4,8 0
- X\_2,4,8 -X\_3,4,8 0
- X\_2,4,8 -X\_4,4,8 0
- X\_2,4,8 -X\_5,4,8 0
- X\_2,4,8 -X\_6,4,8 0
- X\_2,4,8 -X\_7,4,8 0
- X\_2,4,8 -X\_8,4,8 0
- X\_2,4,8 -X\_9,4,8 0
- X\_3,4,8 -X\_4,4,8 0
- X\_3,4,8 -X\_5,4,8 0
- X\_3,4,8 -X\_6,4,8 0
- X\_3,4,8 -X\_7,4,8 0
- X\_3,4,8 -X\_8,4,8 0
- X\_3,4,8 -X\_9,4,8 0
- X\_4,4,8 -X\_5,4,8 0
- X\_4,4,8 -X\_6,4,8 0
- X\_4,4,8 -X\_7,4,8 0
- X\_4,4,8 -X\_8,4,8 0
- X\_4,4,8 -X\_9,4,8 0
- X\_5,4,8 -X\_6,4,8 0
- X\_5,4,8 -X\_7,4,8 0
- X\_5,4,8 -X\_8,4,8 0
- X\_5,4,8 -X\_9,4,8 0
- X\_6,4,8 -X\_7,4,8 0
- X\_6,4,8 -X\_8,4,8 0
- X\_6,4,8 -X\_9,4,8 0
- X\_7,4,8 -X\_8,4,8 0
- X\_7,4,8 -X\_9,4,8 0
- X\_8,4,8 -X\_9,4,8 0

X\_1,4,9 X\_2,4,9 X\_3,4,9 X\_4,4,9 X\_5,4,9 X\_6,4,9 X\_7,4,9 X\_8,4,9 X\_9,4,9 0

- X\_1,4,9 -X\_2,4,9 0
- X\_1,4,9 -X\_3,4,9 0
- X\_1,4,9 -X\_4,4,9 0
- X\_1,4,9 -X\_5,4,9 0
- X\_1,4,9 -X\_6,4,9 0
- X\_1,4,9 -X\_7,4,9 0
- X\_1,4,9 -X\_8,4,9 0
- X\_1,4,9 -X\_9,4,9 0
- X\_2,4,9 -X\_3,4,9 0
- X\_2,4,9 -X\_4,4,9 0
- X\_2,4,9 -X\_5,4,9 0
- X\_2,4,9 -X\_6,4,9 0
- X\_2,4,9 -X\_7,4,9 0
- X\_2,4,9 -X\_8,4,9 0
- X\_2,4,9 -X\_9,4,9 0
- X\_3,4,9 -X\_4,4,9 0
- X\_3,4,9 -X\_5,4,9 0
- X\_3,4,9 -X\_6,4,9 0
- X\_3,4,9 -X\_7,4,9 0
- X\_3,4,9 -X\_8,4,9 0
- X\_3,4,9 -X\_9,4,9 0
- X\_4,4,9 -X\_5,4,9 0
- X\_4,4,9 -X\_6,4,9 0
- X\_4,4,9 -X\_7,4,9 0
- X\_4,4,9 -X\_8,4,9 0
- X\_4,4,9 -X\_9,4,9 0
- X\_5,4,9 -X\_6,4,9 0
- X\_5,4,9 -X\_7,4,9 0
- X\_5,4,9 -X\_8,4,9 0
- X\_5,4,9 -X\_9,4,9 0
- X\_6,4,9 -X\_7,4,9 0
- X\_6,4,9 -X\_8,4,9 0
- X\_6,4,9 -X\_9,4,9 0
- X\_7,4,9 -X\_8,4,9 0
- X\_7,4,9 -X\_9,4,9 0
- X\_8,4,9 -X\_9,4,9 0

X\_1,5,1 X\_2,5,1 X\_3,5,1 X\_4,5,1 X\_5,5,1 X\_6,5,1 X\_7,5,1 X\_8,5,1 X\_9,5,1 0

- X\_1,5,1 -X\_2,5,1 0
- X\_1,5,1 -X\_3,5,1 0
- X\_1,5,1 -X\_4,5,1 0
- X\_1,5,1 -X\_5,5,1 0
- X\_1,5,1 -X\_6,5,1 0
- X\_1,5,1 -X\_7,5,1 0
- X\_1,5,1 -X\_8,5,1 0
- X\_1,5,1 -X\_9,5,1 0
- X\_2,5,1 -X\_3,5,1 0
- X\_2,5,1 -X\_4,5,1 0
- X\_2,5,1 -X\_5,5,1 0
- X\_2,5,1 -X\_6,5,1 0
- X\_2,5,1 -X\_7,5,1 0
- X\_2,5,1 -X\_8,5,1 0
- X\_2,5,1 -X\_9,5,1 0
- X\_3,5,1 -X\_4,5,1 0
- X\_3,5,1 -X\_5,5,1 0
- X\_3,5,1 -X\_6,5,1 0
- X\_3,5,1 -X\_7,5,1 0
- X\_3,5,1 -X\_8,5,1 0
- X\_3,5,1 -X\_9,5,1 0
- X\_4,5,1 -X\_5,5,1 0
- X\_4,5,1 -X\_6,5,1 0
- X\_4,5,1 -X\_7,5,1 0
- X\_4,5,1 -X\_8,5,1 0
- X\_4,5,1 -X\_9,5,1 0
- X\_5,5,1 -X\_6,5,1 0
- X\_5,5,1 -X\_7,5,1 0
- X\_5,5,1 -X\_8,5,1 0
- X\_5,5,1 -X\_9,5,1 0
- X\_6,5,1 -X\_7,5,1 0
- X\_6,5,1 -X\_8,5,1 0
- X\_6,5,1 -X\_9,5,1 0
- X\_7,5,1 -X\_8,5,1 0
- X\_7,5,1 -X\_9,5,1 0
- X\_8,5,1 -X\_9,5,1 0

X\_1,5,2 X\_2,5,2 X\_3,5,2 X\_4,5,2 X\_5,5,2 X\_6,5,2 X\_7,5,2 X\_8,5,2 X\_9,5,2 0

- X\_1,5,2 -X\_2,5,2 0
- X\_1,5,2 -X\_3,5,2 0
- X\_1,5,2 -X\_4,5,2 0
- X\_1,5,2 -X\_5,5,2 0
- X\_1,5,2 -X\_6,5,2 0
- X\_1,5,2 -X\_7,5,2 0
- X\_1,5,2 -X\_8,5,2 0
- X\_1,5,2 -X\_9,5,2 0
- X\_2,5,2 -X\_3,5,2 0
- X\_2,5,2 -X\_4,5,2 0
- X\_2,5,2 -X\_5,5,2 0
- X\_2,5,2 -X\_6,5,2 0
- X\_2,5,2 -X\_7,5,2 0
- X\_2,5,2 -X\_8,5,2 0
- X\_2,5,2 -X\_9,5,2 0
- X\_3,5,2 -X\_4,5,2 0
- X\_3,5,2 -X\_5,5,2 0
- X\_3,5,2 -X\_6,5,2 0
- X\_3,5,2 -X\_7,5,2 0
- X\_3,5,2 -X\_8,5,2 0
- X\_3,5,2 -X\_9,5,2 0
- X\_4,5,2 -X\_5,5,2 0
- X\_4,5,2 -X\_6,5,2 0
- X\_4,5,2 -X\_7,5,2 0
- X\_4,5,2 -X\_8,5,2 0
- X\_4,5,2 -X\_9,5,2 0
- X\_5,5,2 -X\_6,5,2 0
- X\_5,5,2 -X\_7,5,2 0
- X\_5,5,2 -X\_8,5,2 0
- X\_5,5,2 -X\_9,5,2 0
- X\_6,5,2 -X\_7,5,2 0
- X\_6,5,2 -X\_8,5,2 0
- X\_6,5,2 -X\_9,5,2 0
- X\_7,5,2 -X\_8,5,2 0
- X\_7,5,2 -X\_9,5,2 0
- X\_8,5,2 -X\_9,5,2 0

X\_1,5,3 X\_2,5,3 X\_3,5,3 X\_4,5,3 X\_5,5,3 X\_6,5,3 X\_7,5,3 X\_8,5,3 X\_9,5,3 0

- X\_1,5,3 -X\_2,5,3 0
- X\_1,5,3 -X\_3,5,3 0
- X\_1,5,3 -X\_4,5,3 0
- X\_1,5,3 -X\_5,5,3 0
- X\_1,5,3 -X\_6,5,3 0
- X\_1,5,3 -X\_7,5,3 0
- X\_1,5,3 -X\_8,5,3 0
- X\_1,5,3 -X\_9,5,3 0
- X\_2,5,3 -X\_3,5,3 0
- X\_2,5,3 -X\_4,5,3 0
- X\_2,5,3 -X\_5,5,3 0
- X\_2,5,3 -X\_6,5,3 0
- X\_2,5,3 -X\_7,5,3 0
- X\_2,5,3 -X\_8,5,3 0
- X\_2,5,3 -X\_9,5,3 0
- X\_3,5,3 -X\_4,5,3 0
- X\_3,5,3 -X\_5,5,3 0
- X\_3,5,3 -X\_6,5,3 0
- X\_3,5,3 -X\_7,5,3 0
- X\_3,5,3 -X\_8,5,3 0
- X\_3,5,3 -X\_9,5,3 0
- X\_4,5,3 -X\_5,5,3 0
- X\_4,5,3 -X\_6,5,3 0
- X\_4,5,3 -X\_7,5,3 0
- X\_4,5,3 -X\_8,5,3 0
- X\_4,5,3 -X\_9,5,3 0
- X\_5,5,3 -X\_6,5,3 0
- X\_5,5,3 -X\_7,5,3 0
- X\_5,5,3 -X\_8,5,3 0
- X\_5,5,3 -X\_9,5,3 0
- X\_6,5,3 -X\_7,5,3 0
- X\_6,5,3 -X\_8,5,3 0
- X\_6,5,3 -X\_9,5,3 0
- X\_7,5,3 -X\_8,5,3 0
- X\_7,5,3 -X\_9,5,3 0
- X\_8,5,3 -X\_9,5,3 0

X\_1,5,4 X\_2,5,4 X\_3,5,4 X\_4,5,4 X\_5,5,4 X\_6,5,4 X\_7,5,4 X\_8,5,4 X\_9,5,4 0

- X\_1,5,4 -X\_2,5,4 0
- X\_1,5,4 -X\_3,5,4 0
- X\_1,5,4 -X\_4,5,4 0
- X\_1,5,4 -X\_5,5,4 0
- X\_1,5,4 -X\_6,5,4 0
- X\_1,5,4 -X\_7,5,4 0
- X\_1,5,4 -X\_8,5,4 0
- X\_1,5,4 -X\_9,5,4 0
- X\_2,5,4 -X\_3,5,4 0
- X\_2,5,4 -X\_4,5,4 0
- X\_2,5,4 -X\_5,5,4 0
- X\_2,5,4 -X\_6,5,4 0
- X\_2,5,4 -X\_7,5,4 0
- X\_2,5,4 -X\_8,5,4 0
- X\_2,5,4 -X\_9,5,4 0
- X\_3,5,4 -X\_4,5,4 0
- X\_3,5,4 -X\_5,5,4 0
- X\_3,5,4 -X\_6,5,4 0
- X\_3,5,4 -X\_7,5,4 0
- X\_3,5,4 -X\_8,5,4 0
- X\_3,5,4 -X\_9,5,4 0
- X\_4,5,4 -X\_5,5,4 0
- X\_4,5,4 -X\_6,5,4 0
- X\_4,5,4 -X\_7,5,4 0
- X\_4,5,4 -X\_8,5,4 0
- X\_4,5,4 -X\_9,5,4 0
- X\_5,5,4 -X\_6,5,4 0
- X\_5,5,4 -X\_7,5,4 0
- X\_5,5,4 -X\_8,5,4 0
- X\_5,5,4 -X\_9,5,4 0
- X\_6,5,4 -X\_7,5,4 0
- X\_6,5,4 -X\_8,5,4 0
- X\_6,5,4 -X\_9,5,4 0
- X\_7,5,4 -X\_8,5,4 0
- X\_7,5,4 -X\_9,5,4 0
- X\_8,5,4 -X\_9,5,4 0

X\_1,5,5 X\_2,5,5 X\_3,5,5 X\_4,5,5 X\_5,5,5 X\_6,5,5 X\_7,5,5 X\_8,5,5 X\_9,5,5 0

- X\_1,5,5 -X\_2,5,5 0
- X\_1,5,5 -X\_3,5,5 0
- X\_1,5,5 -X\_4,5,5 0
- X\_1,5,5 -X\_5,5,5 0
- X\_1,5,5 -X\_6,5,5 0
- X\_1,5,5 -X\_7,5,5 0
- X\_1,5,5 -X\_8,5,5 0
- X\_1,5,5 -X\_9,5,5 0
- X\_2,5,5 -X\_3,5,5 0
- X\_2,5,5 -X\_4,5,5 0
- X\_2,5,5 -X\_5,5,5 0
- X\_2,5,5 -X\_6,5,5 0
- X\_2,5,5 -X\_7,5,5 0
- X\_2,5,5 -X\_8,5,5 0
- X\_2,5,5 -X\_9,5,5 0
- X\_3,5,5 -X\_4,5,5 0
- X\_3,5,5 -X\_5,5,5 0
- X\_3,5,5 -X\_6,5,5 0
- X\_3,5,5 -X\_7,5,5 0
- X\_3,5,5 -X\_8,5,5 0
- X\_3,5,5 -X\_9,5,5 0
- X\_4,5,5 -X\_5,5,5 0
- X\_4,5,5 -X\_6,5,5 0
- X\_4,5,5 -X\_7,5,5 0
- X\_4,5,5 -X\_8,5,5 0
- X\_4,5,5 -X\_9,5,5 0
- X\_5,5,5 -X\_6,5,5 0
- X\_5,5,5 -X\_7,5,5 0
- X\_5,5,5 -X\_8,5,5 0
- X\_5,5,5 -X\_9,5,5 0
- X\_6,5,5 -X\_7,5,5 0
- X\_6,5,5 -X\_8,5,5 0
- X\_6,5,5 -X\_9,5,5 0
- X\_7,5,5 -X\_8,5,5 0
- X\_7,5,5 -X\_9,5,5 0
- X\_8,5,5 -X\_9,5,5 0

X\_1,5,6 X\_2,5,6 X\_3,5,6 X\_4,5,6 X\_5,5,6 X\_6,5,6 X\_7,5,6 X\_8,5,6 X\_9,5,6 0

- X\_1,5,6 -X\_2,5,6 0
- X\_1,5,6 -X\_3,5,6 0
- X\_1,5,6 -X\_4,5,6 0
- X\_1,5,6 -X\_5,5,6 0
- X\_1,5,6 -X\_6,5,6 0
- X\_1,5,6 -X\_7,5,6 0
- X\_1,5,6 -X\_8,5,6 0
- X\_1,5,6 -X\_9,5,6 0
- X\_2,5,6 -X\_3,5,6 0
- X\_2,5,6 -X\_4,5,6 0
- X\_2,5,6 -X\_5,5,6 0
- X\_2,5,6 -X\_6,5,6 0
- X\_2,5,6 -X\_7,5,6 0
- X\_2,5,6 -X\_8,5,6 0
- X\_2,5,6 -X\_9,5,6 0
- X\_3,5,6 -X\_4,5,6 0
- X\_3,5,6 -X\_5,5,6 0
- X\_3,5,6 -X\_6,5,6 0
- X\_3,5,6 -X\_7,5,6 0
- X\_3,5,6 -X\_8,5,6 0
- X\_3,5,6 -X\_9,5,6 0
- X\_4,5,6 -X\_5,5,6 0
- X\_4,5,6 -X\_6,5,6 0
- X\_4,5,6 -X\_7,5,6 0
- X\_4,5,6 -X\_8,5,6 0
- X\_4,5,6 -X\_9,5,6 0
- X\_5,5,6 -X\_6,5,6 0
- X\_5,5,6 -X\_7,5,6 0
- X\_5,5,6 -X\_8,5,6 0
- X\_5,5,6 -X\_9,5,6 0
- X\_6,5,6 -X\_7,5,6 0
- X\_6,5,6 -X\_8,5,6 0
- X\_6,5,6 -X\_9,5,6 0
- X\_7,5,6 -X\_8,5,6 0
- X\_7,5,6 -X\_9,5,6 0
- X\_8,5,6 -X\_9,5,6 0

X\_1,5,7 X\_2,5,7 X\_3,5,7 X\_4,5,7 X\_5,5,7 X\_6,5,7 X\_7,5,7 X\_8,5,7 X\_9,5,7 0

- X\_1,5,7 -X\_2,5,7 0
- X\_1,5,7 -X\_3,5,7 0
- X\_1,5,7 -X\_4,5,7 0
- X\_1,5,7 -X\_5,5,7 0
- X\_1,5,7 -X\_6,5,7 0
- X\_1,5,7 -X\_7,5,7 0
- X\_1,5,7 -X\_8,5,7 0
- X\_1,5,7 -X\_9,5,7 0
- X\_2,5,7 -X\_3,5,7 0
- X\_2,5,7 -X\_4,5,7 0
- X\_2,5,7 -X\_5,5,7 0
- X\_2,5,7 -X\_6,5,7 0
- X\_2,5,7 -X\_7,5,7 0
- X\_2,5,7 -X\_8,5,7 0
- X\_2,5,7 -X\_9,5,7 0
- X\_3,5,7 -X\_4,5,7 0
- X\_3,5,7 -X\_5,5,7 0
- X\_3,5,7 -X\_6,5,7 0
- X\_3,5,7 -X\_7,5,7 0
- X\_3,5,7 -X\_8,5,7 0
- X\_3,5,7 -X\_9,5,7 0
- X\_4,5,7 -X\_5,5,7 0
- X\_4,5,7 -X\_6,5,7 0
- X\_4,5,7 -X\_7,5,7 0
- X\_4,5,7 -X\_8,5,7 0
- X\_4,5,7 -X\_9,5,7 0
- X\_5,5,7 -X\_6,5,7 0
- X\_5,5,7 -X\_7,5,7 0
- X\_5,5,7 -X\_8,5,7 0
- X\_5,5,7 -X\_9,5,7 0
- X\_6,5,7 -X\_7,5,7 0
- X\_6,5,7 -X\_8,5,7 0
- X\_6,5,7 -X\_9,5,7 0
- X\_7,5,7 -X\_8,5,7 0
- X\_7,5,7 -X\_9,5,7 0
- X\_8,5,7 -X\_9,5,7 0

X\_1,5,8 X\_2,5,8 X\_3,5,8 X\_4,5,8 X\_5,5,8 X\_6,5,8 X\_7,5,8 X\_8,5,8 X\_9,5,8 0

- X\_1,5,8 -X\_2,5,8 0
- X\_1,5,8 -X\_3,5,8 0
- X\_1,5,8 -X\_4,5,8 0
- X\_1,5,8 -X\_5,5,8 0
- X\_1,5,8 -X\_6,5,8 0
- X\_1,5,8 -X\_7,5,8 0
- X\_1,5,8 -X\_8,5,8 0
- X\_1,5,8 -X\_9,5,8 0
- X\_2,5,8 -X\_3,5,8 0
- X\_2,5,8 -X\_4,5,8 0
- X\_2,5,8 -X\_5,5,8 0
- X\_2,5,8 -X\_6,5,8 0
- X\_2,5,8 -X\_7,5,8 0
- X\_2,5,8 -X\_8,5,8 0
- X\_2,5,8 -X\_9,5,8 0
- X\_3,5,8 -X\_4,5,8 0
- X\_3,5,8 -X\_5,5,8 0
- X\_3,5,8 -X\_6,5,8 0
- X\_3,5,8 -X\_7,5,8 0
- X\_3,5,8 -X\_8,5,8 0
- X\_3,5,8 -X\_9,5,8 0
- X\_4,5,8 -X\_5,5,8 0
- X\_4,5,8 -X\_6,5,8 0
- X\_4,5,8 -X\_7,5,8 0
- X\_4,5,8 -X\_8,5,8 0
- X\_4,5,8 -X\_9,5,8 0
- X\_5,5,8 -X\_6,5,8 0
- X\_5,5,8 -X\_7,5,8 0
- X\_5,5,8 -X\_8,5,8 0
- X\_5,5,8 -X\_9,5,8 0
- X\_6,5,8 -X\_7,5,8 0
- X\_6,5,8 -X\_8,5,8 0
- X\_6,5,8 -X\_9,5,8 0
- X\_7,5,8 -X\_8,5,8 0
- X\_7,5,8 -X\_9,5,8 0
- X\_8,5,8 -X\_9,5,8 0

X\_1,5,9 X\_2,5,9 X\_3,5,9 X\_4,5,9 X\_5,5,9 X\_6,5,9 X\_7,5,9 X\_8,5,9 X\_9,5,9 0

- X\_1,5,9 -X\_2,5,9 0
- X\_1,5,9 -X\_3,5,9 0
- X\_1,5,9 -X\_4,5,9 0
- X\_1,5,9 -X\_5,5,9 0
- X\_1,5,9 -X\_6,5,9 0
- X\_1,5,9 -X\_7,5,9 0
- X\_1,5,9 -X\_8,5,9 0
- X\_1,5,9 -X\_9,5,9 0
- X\_2,5,9 -X\_3,5,9 0
- X\_2,5,9 -X\_4,5,9 0
- X\_2,5,9 -X\_5,5,9 0
- X\_2,5,9 -X\_6,5,9 0
- X\_2,5,9 -X\_7,5,9 0
- X\_2,5,9 -X\_8,5,9 0
- X\_2,5,9 -X\_9,5,9 0
- X\_3,5,9 -X\_4,5,9 0
- X\_3,5,9 -X\_5,5,9 0
- X\_3,5,9 -X\_6,5,9 0
- X\_3,5,9 -X\_7,5,9 0
- X\_3,5,9 -X\_8,5,9 0
- X\_3,5,9 -X\_9,5,9 0
- X\_4,5,9 -X\_5,5,9 0
- X\_4,5,9 -X\_6,5,9 0
- X\_4,5,9 -X\_7,5,9 0
- X\_4,5,9 -X\_8,5,9 0
- X\_4,5,9 -X\_9,5,9 0
- X\_5,5,9 -X\_6,5,9 0
- X\_5,5,9 -X\_7,5,9 0
- X\_5,5,9 -X\_8,5,9 0
- X\_5,5,9 -X\_9,5,9 0
- X\_6,5,9 -X\_7,5,9 0
- X\_6,5,9 -X\_8,5,9 0
- X\_6,5,9 -X\_9,5,9 0
- X\_7,5,9 -X\_8,5,9 0
- X\_7,5,9 -X\_9,5,9 0
- X\_8,5,9 -X\_9,5,9 0

X\_1,6,1 X\_2,6,1 X\_3,6,1 X\_4,6,1 X\_5,6,1 X\_6,6,1 X\_7,6,1 X\_8,6,1 X\_9,6,1 0

- X\_1,6,1 -X\_2,6,1 0
- X\_1,6,1 -X\_3,6,1 0
- X\_1,6,1 -X\_4,6,1 0
- X\_1,6,1 -X\_5,6,1 0
- X\_1,6,1 -X\_6,6,1 0
- X\_1,6,1 -X\_7,6,1 0
- X\_1,6,1 -X\_8,6,1 0
- X\_1,6,1 -X\_9,6,1 0
- X\_2,6,1 -X\_3,6,1 0
- X\_2,6,1 -X\_4,6,1 0
- X\_2,6,1 -X\_5,6,1 0
- X\_2,6,1 -X\_6,6,1 0
- X\_2,6,1 -X\_7,6,1 0
- X\_2,6,1 -X\_8,6,1 0
- X\_2,6,1 -X\_9,6,1 0
- X\_3,6,1 -X\_4,6,1 0
- X\_3,6,1 -X\_5,6,1 0
- X\_3,6,1 -X\_6,6,1 0
- X\_3,6,1 -X\_7,6,1 0
- X\_3,6,1 -X\_8,6,1 0
- X\_3,6,1 -X\_9,6,1 0
- X\_4,6,1 -X\_5,6,1 0
- X\_4,6,1 -X\_6,6,1 0
- X\_4,6,1 -X\_7,6,1 0
- X\_4,6,1 -X\_8,6,1 0
- X\_4,6,1 -X\_9,6,1 0
- X\_5,6,1 -X\_6,6,1 0
- X\_5,6,1 -X\_7,6,1 0
- X\_5,6,1 -X\_8,6,1 0
- X\_5,6,1 -X\_9,6,1 0
- X\_6,6,1 -X\_7,6,1 0
- X\_6,6,1 -X\_8,6,1 0
- X\_6,6,1 -X\_9,6,1 0
- X\_7,6,1 -X\_8,6,1 0
- X\_7,6,1 -X\_9,6,1 0
- X\_8,6,1 -X\_9,6,1 0

X\_1,6,2 X\_2,6,2 X\_3,6,2 X\_4,6,2 X\_5,6,2 X\_6,6,2 X\_7,6,2 X\_8,6,2 X\_9,6,2 0

- X\_1,6,2 -X\_2,6,2 0
- X\_1,6,2 -X\_3,6,2 0
- X\_1,6,2 -X\_4,6,2 0
- X\_1,6,2 -X\_5,6,2 0
- X\_1,6,2 -X\_6,6,2 0
- X\_1,6,2 -X\_7,6,2 0
- X\_1,6,2 -X\_8,6,2 0
- X\_1,6,2 -X\_9,6,2 0
- X\_2,6,2 -X\_3,6,2 0
- X\_2,6,2 -X\_4,6,2 0
- X\_2,6,2 -X\_5,6,2 0
- X\_2,6,2 -X\_6,6,2 0
- X\_2,6,2 -X\_7,6,2 0
- X\_2,6,2 -X\_8,6,2 0
- X\_2,6,2 -X\_9,6,2 0
- X\_3,6,2 -X\_4,6,2 0
- X\_3,6,2 -X\_5,6,2 0
- X\_3,6,2 -X\_6,6,2 0
- X\_3,6,2 -X\_7,6,2 0
- X\_3,6,2 -X\_8,6,2 0
- X\_3,6,2 -X\_9,6,2 0
- X\_4,6,2 -X\_5,6,2 0
- X\_4,6,2 -X\_6,6,2 0
- X\_4,6,2 -X\_7,6,2 0
- X\_4,6,2 -X\_8,6,2 0
- X\_4,6,2 -X\_9,6,2 0
- X\_5,6,2 -X\_6,6,2 0
- X\_5,6,2 -X\_7,6,2 0
- X\_5,6,2 -X\_8,6,2 0
- X\_5,6,2 -X\_9,6,2 0
- X\_6,6,2 -X\_7,6,2 0
- X\_6,6,2 -X\_8,6,2 0
- X\_6,6,2 -X\_9,6,2 0
- X\_7,6,2 -X\_8,6,2 0
- X\_7,6,2 -X\_9,6,2 0
- X\_8,6,2 -X\_9,6,2 0

X\_1,6,3 X\_2,6,3 X\_3,6,3 X\_4,6,3 X\_5,6,3 X\_6,6,3 X\_7,6,3 X\_8,6,3 X\_9,6,3 0

- X\_1,6,3 -X\_2,6,3 0
- X\_1,6,3 -X\_3,6,3 0
- X\_1,6,3 -X\_4,6,3 0
- X\_1,6,3 -X\_5,6,3 0
- X\_1,6,3 -X\_6,6,3 0
- X\_1,6,3 -X\_7,6,3 0
- X\_1,6,3 -X\_8,6,3 0
- X\_1,6,3 -X\_9,6,3 0
- X\_2,6,3 -X\_3,6,3 0
- X\_2,6,3 -X\_4,6,3 0
- X\_2,6,3 -X\_5,6,3 0
- X\_2,6,3 -X\_6,6,3 0
- X\_2,6,3 -X\_7,6,3 0
- X\_2,6,3 -X\_8,6,3 0
- X\_2,6,3 -X\_9,6,3 0
- X\_3,6,3 -X\_4,6,3 0
- X\_3,6,3 -X\_5,6,3 0
- X\_3,6,3 -X\_6,6,3 0
- X\_3,6,3 -X\_7,6,3 0
- X\_3,6,3 -X\_8,6,3 0
- X\_3,6,3 -X\_9,6,3 0
- X\_4,6,3 -X\_5,6,3 0
- X\_4,6,3 -X\_6,6,3 0
- X\_4,6,3 -X\_7,6,3 0
- X\_4,6,3 -X\_8,6,3 0
- X\_4,6,3 -X\_9,6,3 0
- X\_5,6,3 -X\_6,6,3 0
- X\_5,6,3 -X\_7,6,3 0
- X\_5,6,3 -X\_8,6,3 0
- X\_5,6,3 -X\_9,6,3 0
- X\_6,6,3 -X\_7,6,3 0
- X\_6,6,3 -X\_8,6,3 0
- X\_6,6,3 -X\_9,6,3 0
- X\_7,6,3 -X\_8,6,3 0
- X\_7,6,3 -X\_9,6,3 0
- X\_8,6,3 -X\_9,6,3 0

X\_1,6,4 X\_2,6,4 X\_3,6,4 X\_4,6,4 X\_5,6,4 X\_6,6,4 X\_7,6,4 X\_8,6,4 X\_9,6,4 0

- X\_1,6,4 -X\_2,6,4 0
- X\_1,6,4 -X\_3,6,4 0
- X\_1,6,4 -X\_4,6,4 0
- X\_1,6,4 -X\_5,6,4 0
- X\_1,6,4 -X\_6,6,4 0
- X\_1,6,4 -X\_7,6,4 0
- X\_1,6,4 -X\_8,6,4 0
- X\_1,6,4 -X\_9,6,4 0
- X\_2,6,4 -X\_3,6,4 0
- X\_2,6,4 -X\_4,6,4 0
- X\_2,6,4 -X\_5,6,4 0
- X\_2,6,4 -X\_6,6,4 0
- X\_2,6,4 -X\_7,6,4 0
- X\_2,6,4 -X\_8,6,4 0
- X\_2,6,4 -X\_9,6,4 0
- X\_3,6,4 -X\_4,6,4 0
- X\_3,6,4 -X\_5,6,4 0
- X\_3,6,4 -X\_6,6,4 0
- X\_3,6,4 -X\_7,6,4 0
- X\_3,6,4 -X\_8,6,4 0
- X\_3,6,4 -X\_9,6,4 0
- X\_4,6,4 -X\_5,6,4 0
- X\_4,6,4 -X\_6,6,4 0
- X\_4,6,4 -X\_7,6,4 0
- X\_4,6,4 -X\_8,6,4 0
- X\_4,6,4 -X\_9,6,4 0
- X\_5,6,4 -X\_6,6,4 0
- X\_5,6,4 -X\_7,6,4 0
- X\_5,6,4 -X\_8,6,4 0
- X\_5,6,4 -X\_9,6,4 0
- X\_6,6,4 -X\_7,6,4 0
- X\_6,6,4 -X\_8,6,4 0
- X\_6,6,4 -X\_9,6,4 0
- X\_7,6,4 -X\_8,6,4 0
- X\_7,6,4 -X\_9,6,4 0
- X\_8,6,4 -X\_9,6,4 0

X\_1,6,5 X\_2,6,5 X\_3,6,5 X\_4,6,5 X\_5,6,5 X\_6,6,5 X\_7,6,5 X\_8,6,5 X\_9,6,5 0

- X\_1,6,5 -X\_2,6,5 0
- X\_1,6,5 -X\_3,6,5 0
- X\_1,6,5 -X\_4,6,5 0
- X\_1,6,5 -X\_5,6,5 0
- X\_1,6,5 -X\_6,6,5 0
- X\_1,6,5 -X\_7,6,5 0
- X\_1,6,5 -X\_8,6,5 0
- X\_1,6,5 -X\_9,6,5 0
- X\_2,6,5 -X\_3,6,5 0
- X\_2,6,5 -X\_4,6,5 0
- X\_2,6,5 -X\_5,6,5 0
- X\_2,6,5 -X\_6,6,5 0
- X\_2,6,5 -X\_7,6,5 0
- X\_2,6,5 -X\_8,6,5 0
- X\_2,6,5 -X\_9,6,5 0
- X\_3,6,5 -X\_4,6,5 0
- X\_3,6,5 -X\_5,6,5 0
- X\_3,6,5 -X\_6,6,5 0
- X\_3,6,5 -X\_7,6,5 0
- X\_3,6,5 -X\_8,6,5 0
- X\_3,6,5 -X\_9,6,5 0
- X\_4,6,5 -X\_5,6,5 0
- X\_4,6,5 -X\_6,6,5 0
- X\_4,6,5 -X\_7,6,5 0
- X\_4,6,5 -X\_8,6,5 0
- X\_4,6,5 -X\_9,6,5 0
- X\_5,6,5 -X\_6,6,5 0
- X\_5,6,5 -X\_7,6,5 0
- X\_5,6,5 -X\_8,6,5 0
- X\_5,6,5 -X\_9,6,5 0
- X\_6,6,5 -X\_7,6,5 0
- X\_6,6,5 -X\_8,6,5 0
- X\_6,6,5 -X\_9,6,5 0
- X\_7,6,5 -X\_8,6,5 0
- X\_7,6,5 -X\_9,6,5 0
- X\_8,6,5 -X\_9,6,5 0

X\_1,6,6 X\_2,6,6 X\_3,6,6 X\_4,6,6 X\_5,6,6 X\_6,6,6 X\_7,6,6 X\_8,6,6 X\_9,6,6 0

- X\_1,6,6 -X\_2,6,6 0
- X\_1,6,6 -X\_3,6,6 0
- X\_1,6,6 -X\_4,6,6 0
- X\_1,6,6 -X\_5,6,6 0
- X\_1,6,6 -X\_6,6,6 0
- X\_1,6,6 -X\_7,6,6 0
- X\_1,6,6 -X\_8,6,6 0
- X\_1,6,6 -X\_9,6,6 0
- X\_2,6,6 -X\_3,6,6 0
- X\_2,6,6 -X\_4,6,6 0
- X\_2,6,6 -X\_5,6,6 0
- X\_2,6,6 -X\_6,6,6 0
- X\_2,6,6 -X\_7,6,6 0
- X\_2,6,6 -X\_8,6,6 0
- X\_2,6,6 -X\_9,6,6 0
- X\_3,6,6 -X\_4,6,6 0
- X\_3,6,6 -X\_5,6,6 0
- X\_3,6,6 -X\_6,6,6 0
- X\_3,6,6 -X\_7,6,6 0
- X\_3,6,6 -X\_8,6,6 0
- X\_3,6,6 -X\_9,6,6 0
- X\_4,6,6 -X\_5,6,6 0
- X\_4,6,6 -X\_6,6,6 0
- X\_4,6,6 -X\_7,6,6 0
- X\_4,6,6 -X\_8,6,6 0
- X\_4,6,6 -X\_9,6,6 0
- X\_5,6,6 -X\_6,6,6 0
- X\_5,6,6 -X\_7,6,6 0
- X\_5,6,6 -X\_8,6,6 0
- X\_5,6,6 -X\_9,6,6 0
- X\_6,6,6 -X\_7,6,6 0
- X\_6,6,6 -X\_8,6,6 0
- X\_6,6,6 -X\_9,6,6 0
- X\_7,6,6 -X\_8,6,6 0
- X\_7,6,6 -X\_9,6,6 0
- X\_8,6,6 -X\_9,6,6 0

X\_1,6,7 X\_2,6,7 X\_3,6,7 X\_4,6,7 X\_5,6,7 X\_6,6,7 X\_7,6,7 X\_8,6,7 X\_9,6,7 0

- X\_1,6,7 -X\_2,6,7 0
- X\_1,6,7 -X\_3,6,7 0
- X\_1,6,7 -X\_4,6,7 0
- X\_1,6,7 -X\_5,6,7 0
- X\_1,6,7 -X\_6,6,7 0
- X\_1,6,7 -X\_7,6,7 0
- X\_1,6,7 -X\_8,6,7 0
- X\_1,6,7 -X\_9,6,7 0
- X\_2,6,7 -X\_3,6,7 0
- X\_2,6,7 -X\_4,6,7 0
- X\_2,6,7 -X\_5,6,7 0
- X\_2,6,7 -X\_6,6,7 0
- X\_2,6,7 -X\_7,6,7 0
- X\_2,6,7 -X\_8,6,7 0
- X\_2,6,7 -X\_9,6,7 0
- X\_3,6,7 -X\_4,6,7 0
- X\_3,6,7 -X\_5,6,7 0
- X\_3,6,7 -X\_6,6,7 0
- X\_3,6,7 -X\_7,6,7 0
- X\_3,6,7 -X\_8,6,7 0
- X\_3,6,7 -X\_9,6,7 0
- X\_4,6,7 -X\_5,6,7 0
- X\_4,6,7 -X\_6,6,7 0
- X\_4,6,7 -X\_7,6,7 0
- X\_4,6,7 -X\_8,6,7 0
- X\_4,6,7 -X\_9,6,7 0
- X\_5,6,7 -X\_6,6,7 0
- X\_5,6,7 -X\_7,6,7 0
- X\_5,6,7 -X\_8,6,7 0
- X\_5,6,7 -X\_9,6,7 0
- X\_6,6,7 -X\_7,6,7 0
- X\_6,6,7 -X\_8,6,7 0
- X\_6,6,7 -X\_9,6,7 0
- X\_7,6,7 -X\_8,6,7 0
- X\_7,6,7 -X\_9,6,7 0
- X\_8,6,7 -X\_9,6,7 0

X\_1,6,8 X\_2,6,8 X\_3,6,8 X\_4,6,8 X\_5,6,8 X\_6,6,8 X\_7,6,8 X\_8,6,8 X\_9,6,8 0

- X\_1,6,8 -X\_2,6,8 0
- X\_1,6,8 -X\_3,6,8 0
- X\_1,6,8 -X\_4,6,8 0
- X\_1,6,8 -X\_5,6,8 0
- X\_1,6,8 -X\_6,6,8 0
- X\_1,6,8 -X\_7,6,8 0
- X\_1,6,8 -X\_8,6,8 0
- X\_1,6,8 -X\_9,6,8 0
- X\_2,6,8 -X\_3,6,8 0
- X\_2,6,8 -X\_4,6,8 0
- X\_2,6,8 -X\_5,6,8 0
- X\_2,6,8 -X\_6,6,8 0
- X\_2,6,8 -X\_7,6,8 0
- X\_2,6,8 -X\_8,6,8 0
- X\_2,6,8 -X\_9,6,8 0
- X\_3,6,8 -X\_4,6,8 0
- X\_3,6,8 -X\_5,6,8 0
- X\_3,6,8 -X\_6,6,8 0
- X\_3,6,8 -X\_7,6,8 0
- X\_3,6,8 -X\_8,6,8 0
- X\_3,6,8 -X\_9,6,8 0
- X\_4,6,8 -X\_5,6,8 0
- X\_4,6,8 -X\_6,6,8 0
- X\_4,6,8 -X\_7,6,8 0
- X\_4,6,8 -X\_8,6,8 0
- X\_4,6,8 -X\_9,6,8 0
- X\_5,6,8 -X\_6,6,8 0
- X\_5,6,8 -X\_7,6,8 0
- X\_5,6,8 -X\_8,6,8 0
- X\_5,6,8 -X\_9,6,8 0
- X\_6,6,8 -X\_7,6,8 0
- X\_6,6,8 -X\_8,6,8 0
- X\_6,6,8 -X\_9,6,8 0
- X\_7,6,8 -X\_8,6,8 0
- X\_7,6,8 -X\_9,6,8 0
- X\_8,6,8 -X\_9,6,8 0

X\_1,6,9 X\_2,6,9 X\_3,6,9 X\_4,6,9 X\_5,6,9 X\_6,6,9 X\_7,6,9 X\_8,6,9 X\_9,6,9 0

- X\_1,6,9 -X\_2,6,9 0
- X\_1,6,9 -X\_3,6,9 0
- X\_1,6,9 -X\_4,6,9 0
- X\_1,6,9 -X\_5,6,9 0
- X\_1,6,9 -X\_6,6,9 0
- X\_1,6,9 -X\_7,6,9 0
- X\_1,6,9 -X\_8,6,9 0
- X\_1,6,9 -X\_9,6,9 0
- X\_2,6,9 -X\_3,6,9 0
- X\_2,6,9 -X\_4,6,9 0
- X\_2,6,9 -X\_5,6,9 0
- X\_2,6,9 -X\_6,6,9 0
- X\_2,6,9 -X\_7,6,9 0
- X\_2,6,9 -X\_8,6,9 0
- X\_2,6,9 -X\_9,6,9 0
- X\_3,6,9 -X\_4,6,9 0
- X\_3,6,9 -X\_5,6,9 0
- X\_3,6,9 -X\_6,6,9 0
- X\_3,6,9 -X\_7,6,9 0
- X\_3,6,9 -X\_8,6,9 0
- X\_3,6,9 -X\_9,6,9 0
- X\_4,6,9 -X\_5,6,9 0
- X\_4,6,9 -X\_6,6,9 0
- X\_4,6,9 -X\_7,6,9 0
- X\_4,6,9 -X\_8,6,9 0
- X\_4,6,9 -X\_9,6,9 0
- X\_5,6,9 -X\_6,6,9 0
- X\_5,6,9 -X\_7,6,9 0
- X\_5,6,9 -X\_8,6,9 0
- X\_5,6,9 -X\_9,6,9 0
- X\_6,6,9 -X\_7,6,9 0
- X\_6,6,9 -X\_8,6,9 0
- X\_6,6,9 -X\_9,6,9 0
- X\_7,6,9 -X\_8,6,9 0
- X\_7,6,9 -X\_9,6,9 0
- X\_8,6,9 -X\_9,6,9 0

X\_1,7,1 X\_2,7,1 X\_3,7,1 X\_4,7,1 X\_5,7,1 X\_6,7,1 X\_7,7,1 X\_8,7,1 X\_9,7,1 0

- X\_1,7,1 -X\_2,7,1 0
- X\_1,7,1 -X\_3,7,1 0
- X\_1,7,1 -X\_4,7,1 0
- X\_1,7,1 -X\_5,7,1 0
- X\_1,7,1 -X\_6,7,1 0
- X\_1,7,1 -X\_7,7,1 0
- X\_1,7,1 -X\_8,7,1 0
- X\_1,7,1 -X\_9,7,1 0
- X\_2,7,1 -X\_3,7,1 0
- X\_2,7,1 -X\_4,7,1 0
- X\_2,7,1 -X\_5,7,1 0
- X\_2,7,1 -X\_6,7,1 0
- X\_2,7,1 -X\_7,7,1 0
- X\_2,7,1 -X\_8,7,1 0
- X\_2,7,1 -X\_9,7,1 0
- X\_3,7,1 -X\_4,7,1 0
- X\_3,7,1 -X\_5,7,1 0
- X\_3,7,1 -X\_6,7,1 0
- X\_3,7,1 -X\_7,7,1 0
- X\_3,7,1 -X\_8,7,1 0
- X\_3,7,1 -X\_9,7,1 0
- X\_4,7,1 -X\_5,7,1 0
- X\_4,7,1 -X\_6,7,1 0
- X\_4,7,1 -X\_7,7,1 0
- X\_4,7,1 -X\_8,7,1 0
- X\_4,7,1 -X\_9,7,1 0
- X\_5,7,1 -X\_6,7,1 0
- X\_5,7,1 -X\_7,7,1 0
- X\_5,7,1 -X\_8,7,1 0
- X\_5,7,1 -X\_9,7,1 0
- X\_6,7,1 -X\_7,7,1 0
- X\_6,7,1 -X\_8,7,1 0
- X\_6,7,1 -X\_9,7,1 0
- X\_7,7,1 -X\_8,7,1 0
- X\_7,7,1 -X\_9,7,1 0
- X\_8,7,1 -X\_9,7,1 0

X\_1,7,2 X\_2,7,2 X\_3,7,2 X\_4,7,2 X\_5,7,2 X\_6,7,2 X\_7,7,2 X\_8,7,2 X\_9,7,2 0

- X\_1,7,2 -X\_2,7,2 0
- X\_1,7,2 -X\_3,7,2 0
- X\_1,7,2 -X\_4,7,2 0
- X\_1,7,2 -X\_5,7,2 0
- X\_1,7,2 -X\_6,7,2 0
- X\_1,7,2 -X\_7,7,2 0
- X\_1,7,2 -X\_8,7,2 0
- X\_1,7,2 -X\_9,7,2 0
- X\_2,7,2 -X\_3,7,2 0
- X\_2,7,2 -X\_4,7,2 0
- X\_2,7,2 -X\_5,7,2 0
- X\_2,7,2 -X\_6,7,2 0
- X\_2,7,2 -X\_7,7,2 0
- X\_2,7,2 -X\_8,7,2 0
- X\_2,7,2 -X\_9,7,2 0
- X\_3,7,2 -X\_4,7,2 0
- X\_3,7,2 -X\_5,7,2 0
- X\_3,7,2 -X\_6,7,2 0
- X\_3,7,2 -X\_7,7,2 0
- X\_3,7,2 -X\_8,7,2 0
- X\_3,7,2 -X\_9,7,2 0
- X\_4,7,2 -X\_5,7,2 0
- X\_4,7,2 -X\_6,7,2 0
- X\_4,7,2 -X\_7,7,2 0
- X\_4,7,2 -X\_8,7,2 0
- X\_4,7,2 -X\_9,7,2 0
- X\_5,7,2 -X\_6,7,2 0
- X\_5,7,2 -X\_7,7,2 0
- X\_5,7,2 -X\_8,7,2 0
- X\_5,7,2 -X\_9,7,2 0
- X\_6,7,2 -X\_7,7,2 0
- X\_6,7,2 -X\_8,7,2 0
- X\_6,7,2 -X\_9,7,2 0
- X\_7,7,2 -X\_8,7,2 0
- X\_7,7,2 -X\_9,7,2 0
- X\_8,7,2 -X\_9,7,2 0

X\_1,7,3 X\_2,7,3 X\_3,7,3 X\_4,7,3 X\_5,7,3 X\_6,7,3 X\_7,7,3 X\_8,7,3 X\_9,7,3 0

- X\_1,7,3 -X\_2,7,3 0
- X\_1,7,3 -X\_3,7,3 0
- X\_1,7,3 -X\_4,7,3 0
- X\_1,7,3 -X\_5,7,3 0
- X\_1,7,3 -X\_6,7,3 0
- X\_1,7,3 -X\_7,7,3 0
- X\_1,7,3 -X\_8,7,3 0
- X\_1,7,3 -X\_9,7,3 0
- X\_2,7,3 -X\_3,7,3 0
- X\_2,7,3 -X\_4,7,3 0
- X\_2,7,3 -X\_5,7,3 0
- X\_2,7,3 -X\_6,7,3 0
- X\_2,7,3 -X\_7,7,3 0
- X\_2,7,3 -X\_8,7,3 0
- X\_2,7,3 -X\_9,7,3 0
- X\_3,7,3 -X\_4,7,3 0
- X\_3,7,3 -X\_5,7,3 0
- X\_3,7,3 -X\_6,7,3 0
- X\_3,7,3 -X\_7,7,3 0
- X\_3,7,3 -X\_8,7,3 0
- X\_3,7,3 -X\_9,7,3 0
- X\_4,7,3 -X\_5,7,3 0
- X\_4,7,3 -X\_6,7,3 0
- X\_4,7,3 -X\_7,7,3 0
- X\_4,7,3 -X\_8,7,3 0
- X\_4,7,3 -X\_9,7,3 0
- X\_5,7,3 -X\_6,7,3 0
- X\_5,7,3 -X\_7,7,3 0
- X\_5,7,3 -X\_8,7,3 0
- X\_5,7,3 -X\_9,7,3 0
- X\_6,7,3 -X\_7,7,3 0
- X\_6,7,3 -X\_8,7,3 0
- X\_6,7,3 -X\_9,7,3 0
- X\_7,7,3 -X\_8,7,3 0
- X\_7,7,3 -X\_9,7,3 0
- X\_8,7,3 -X\_9,7,3 0

X\_1,7,4 X\_2,7,4 X\_3,7,4 X\_4,7,4 X\_5,7,4 X\_6,7,4 X\_7,7,4 X\_8,7,4 X\_9,7,4 0

- X\_1,7,4 -X\_2,7,4 0
- X\_1,7,4 -X\_3,7,4 0
- X\_1,7,4 -X\_4,7,4 0
- X\_1,7,4 -X\_5,7,4 0
- X\_1,7,4 -X\_6,7,4 0
- X\_1,7,4 -X\_7,7,4 0
- X\_1,7,4 -X\_8,7,4 0
- X\_1,7,4 -X\_9,7,4 0
- X\_2,7,4 -X\_3,7,4 0
- X\_2,7,4 -X\_4,7,4 0
- X\_2,7,4 -X\_5,7,4 0
- X\_2,7,4 -X\_6,7,4 0
- X\_2,7,4 -X\_7,7,4 0
- X\_2,7,4 -X\_8,7,4 0
- X\_2,7,4 -X\_9,7,4 0
- X\_3,7,4 -X\_4,7,4 0
- X\_3,7,4 -X\_5,7,4 0
- X\_3,7,4 -X\_6,7,4 0
- X\_3,7,4 -X\_7,7,4 0
- X\_3,7,4 -X\_8,7,4 0
- X\_3,7,4 -X\_9,7,4 0
- X\_4,7,4 -X\_5,7,4 0
- X\_4,7,4 -X\_6,7,4 0
- X\_4,7,4 -X\_7,7,4 0
- X\_4,7,4 -X\_8,7,4 0
- X\_4,7,4 -X\_9,7,4 0
- X\_5,7,4 -X\_6,7,4 0
- X\_5,7,4 -X\_7,7,4 0
- X\_5,7,4 -X\_8,7,4 0
- X\_5,7,4 -X\_9,7,4 0
- X\_6,7,4 -X\_7,7,4 0
- X\_6,7,4 -X\_8,7,4 0
- X\_6,7,4 -X\_9,7,4 0
- X\_7,7,4 -X\_8,7,4 0
- X\_7,7,4 -X\_9,7,4 0
- X\_8,7,4 -X\_9,7,4 0

X\_1,7,5 X\_2,7,5 X\_3,7,5 X\_4,7,5 X\_5,7,5 X\_6,7,5 X\_7,7,5 X\_8,7,5 X\_9,7,5 0

- X\_1,7,5 -X\_2,7,5 0
- X\_1,7,5 -X\_3,7,5 0
- X\_1,7,5 -X\_4,7,5 0
- X\_1,7,5 -X\_5,7,5 0
- X\_1,7,5 -X\_6,7,5 0
- X\_1,7,5 -X\_7,7,5 0
- X\_1,7,5 -X\_8,7,5 0
- X\_1,7,5 -X\_9,7,5 0
- X\_2,7,5 -X\_3,7,5 0
- X\_2,7,5 -X\_4,7,5 0
- X\_2,7,5 -X\_5,7,5 0
- X\_2,7,5 -X\_6,7,5 0
- X\_2,7,5 -X\_7,7,5 0
- X\_2,7,5 -X\_8,7,5 0
- X\_2,7,5 -X\_9,7,5 0
- X\_3,7,5 -X\_4,7,5 0
- X\_3,7,5 -X\_5,7,5 0
- X\_3,7,5 -X\_6,7,5 0
- X\_3,7,5 -X\_7,7,5 0
- X\_3,7,5 -X\_8,7,5 0
- X\_3,7,5 -X\_9,7,5 0
- X\_4,7,5 -X\_5,7,5 0
- X\_4,7,5 -X\_6,7,5 0
- X\_4,7,5 -X\_7,7,5 0
- X\_4,7,5 -X\_8,7,5 0
- X\_4,7,5 -X\_9,7,5 0
- X\_5,7,5 -X\_6,7,5 0
- X\_5,7,5 -X\_7,7,5 0
- X\_5,7,5 -X\_8,7,5 0
- X\_5,7,5 -X\_9,7,5 0
- X\_6,7,5 -X\_7,7,5 0
- X\_6,7,5 -X\_8,7,5 0
- X\_6,7,5 -X\_9,7,5 0
- X\_7,7,5 -X\_8,7,5 0
- X\_7,7,5 -X\_9,7,5 0
- X\_8,7,5 -X\_9,7,5 0

X\_1,7,6 X\_2,7,6 X\_3,7,6 X\_4,7,6 X\_5,7,6 X\_6,7,6 X\_7,7,6 X\_8,7,6 X\_9,7,6 0

- X\_1,7,6 -X\_2,7,6 0
- X\_1,7,6 -X\_3,7,6 0
- X\_1,7,6 -X\_4,7,6 0
- X\_1,7,6 -X\_5,7,6 0
- X\_1,7,6 -X\_6,7,6 0
- X\_1,7,6 -X\_7,7,6 0
- X\_1,7,6 -X\_8,7,6 0
- X\_1,7,6 -X\_9,7,6 0
- X\_2,7,6 -X\_3,7,6 0
- X\_2,7,6 -X\_4,7,6 0
- X\_2,7,6 -X\_5,7,6 0
- X\_2,7,6 -X\_6,7,6 0
- X\_2,7,6 -X\_7,7,6 0
- X\_2,7,6 -X\_8,7,6 0
- X\_2,7,6 -X\_9,7,6 0
- X\_3,7,6 -X\_4,7,6 0
- X\_3,7,6 -X\_5,7,6 0
- X\_3,7,6 -X\_6,7,6 0
- X\_3,7,6 -X\_7,7,6 0
- X\_3,7,6 -X\_8,7,6 0
- X\_3,7,6 -X\_9,7,6 0
- X\_4,7,6 -X\_5,7,6 0
- X\_4,7,6 -X\_6,7,6 0
- X\_4,7,6 -X\_7,7,6 0
- X\_4,7,6 -X\_8,7,6 0
- X\_4,7,6 -X\_9,7,6 0
- X\_5,7,6 -X\_6,7,6 0
- X\_5,7,6 -X\_7,7,6 0
- X\_5,7,6 -X\_8,7,6 0
- X\_5,7,6 -X\_9,7,6 0
- X\_6,7,6 -X\_7,7,6 0
- X\_6,7,6 -X\_8,7,6 0
- X\_6,7,6 -X\_9,7,6 0
- X\_7,7,6 -X\_8,7,6 0
- X\_7,7,6 -X\_9,7,6 0
- X\_8,7,6 -X\_9,7,6 0

X\_1,7,7 X\_2,7,7 X\_3,7,7 X\_4,7,7 X\_5,7,7 X\_6,7,7 X\_7,7,7 X\_8,7,7 X\_9,7,7 0

- X\_1,7,7 -X\_2,7,7 0
- X\_1,7,7 -X\_3,7,7 0
- X\_1,7,7 -X\_4,7,7 0
- X\_1,7,7 -X\_5,7,7 0
- X\_1,7,7 -X\_6,7,7 0
- X\_1,7,7 -X\_7,7,7 0
- X\_1,7,7 -X\_8,7,7 0
- X\_1,7,7 -X\_9,7,7 0
- X\_2,7,7 -X\_3,7,7 0
- X\_2,7,7 -X\_4,7,7 0
- X\_2,7,7 -X\_5,7,7 0
- X\_2,7,7 -X\_6,7,7 0
- X\_2,7,7 -X\_7,7,7 0
- X\_2,7,7 -X\_8,7,7 0
- X\_2,7,7 -X\_9,7,7 0
- X\_3,7,7 -X\_4,7,7 0
- X\_3,7,7 -X\_5,7,7 0
- X\_3,7,7 -X\_6,7,7 0
- X\_3,7,7 -X\_7,7,7 0
- X\_3,7,7 -X\_8,7,7 0
- X\_3,7,7 -X\_9,7,7 0
- X\_4,7,7 -X\_5,7,7 0
- X\_4,7,7 -X\_6,7,7 0
- X\_4,7,7 -X\_7,7,7 0
- X\_4,7,7 -X\_8,7,7 0
- X\_4,7,7 -X\_9,7,7 0
- X\_5,7,7 -X\_6,7,7 0
- X\_5,7,7 -X\_7,7,7 0
- X\_5,7,7 -X\_8,7,7 0
- X\_5,7,7 -X\_9,7,7 0
- X\_6,7,7 -X\_7,7,7 0
- X\_6,7,7 -X\_8,7,7 0
- X\_6,7,7 -X\_9,7,7 0
- X\_7,7,7 -X\_8,7,7 0
- X\_7,7,7 -X\_9,7,7 0
- X\_8,7,7 -X\_9,7,7 0

X\_1,7,8 X\_2,7,8 X\_3,7,8 X\_4,7,8 X\_5,7,8 X\_6,7,8 X\_7,7,8 X\_8,7,8 X\_9,7,8 0

- X\_1,7,8 -X\_2,7,8 0
- X\_1,7,8 -X\_3,7,8 0
- X\_1,7,8 -X\_4,7,8 0
- X\_1,7,8 -X\_5,7,8 0
- X\_1,7,8 -X\_6,7,8 0
- X\_1,7,8 -X\_7,7,8 0
- X\_1,7,8 -X\_8,7,8 0
- X\_1,7,8 -X\_9,7,8 0
- X\_2,7,8 -X\_3,7,8 0
- X\_2,7,8 -X\_4,7,8 0
- X\_2,7,8 -X\_5,7,8 0
- X\_2,7,8 -X\_6,7,8 0
- X\_2,7,8 -X\_7,7,8 0
- X\_2,7,8 -X\_8,7,8 0
- X\_2,7,8 -X\_9,7,8 0
- X\_3,7,8 -X\_4,7,8 0
- X\_3,7,8 -X\_5,7,8 0
- X\_3,7,8 -X\_6,7,8 0
- X\_3,7,8 -X\_7,7,8 0
- X\_3,7,8 -X\_8,7,8 0
- X\_3,7,8 -X\_9,7,8 0
- X\_4,7,8 -X\_5,7,8 0
- X\_4,7,8 -X\_6,7,8 0
- X\_4,7,8 -X\_7,7,8 0
- X\_4,7,8 -X\_8,7,8 0
- X\_4,7,8 -X\_9,7,8 0
- X\_5,7,8 -X\_6,7,8 0
- X\_5,7,8 -X\_7,7,8 0
- X\_5,7,8 -X\_8,7,8 0
- X\_5,7,8 -X\_9,7,8 0
- X\_6,7,8 -X\_7,7,8 0
- X\_6,7,8 -X\_8,7,8 0
- X\_6,7,8 -X\_9,7,8 0
- X\_7,7,8 -X\_8,7,8 0
- X\_7,7,8 -X\_9,7,8 0
- X\_8,7,8 -X\_9,7,8 0

X\_1,7,9 X\_2,7,9 X\_3,7,9 X\_4,7,9 X\_5,7,9 X\_6,7,9 X\_7,7,9 X\_8,7,9 X\_9,7,9 0

- X\_1,7,9 -X\_2,7,9 0
- X\_1,7,9 -X\_3,7,9 0
- X\_1,7,9 -X\_4,7,9 0
- X\_1,7,9 -X\_5,7,9 0
- X\_1,7,9 -X\_6,7,9 0
- X\_1,7,9 -X\_7,7,9 0
- X\_1,7,9 -X\_8,7,9 0
- X\_1,7,9 -X\_9,7,9 0
- X\_2,7,9 -X\_3,7,9 0
- X\_2,7,9 -X\_4,7,9 0
- X\_2,7,9 -X\_5,7,9 0
- X\_2,7,9 -X\_6,7,9 0
- X\_2,7,9 -X\_7,7,9 0
- X\_2,7,9 -X\_8,7,9 0
- X\_2,7,9 -X\_9,7,9 0
- X\_3,7,9 -X\_4,7,9 0
- X\_3,7,9 -X\_5,7,9 0
- X\_3,7,9 -X\_6,7,9 0
- X\_3,7,9 -X\_7,7,9 0
- X\_3,7,9 -X\_8,7,9 0
- X\_3,7,9 -X\_9,7,9 0
- X\_4,7,9 -X\_5,7,9 0
- X\_4,7,9 -X\_6,7,9 0
- X\_4,7,9 -X\_7,7,9 0
- X\_4,7,9 -X\_8,7,9 0
- X\_4,7,9 -X\_9,7,9 0
- X\_5,7,9 -X\_6,7,9 0
- X\_5,7,9 -X\_7,7,9 0
- X\_5,7,9 -X\_8,7,9 0
- X\_5,7,9 -X\_9,7,9 0
- X\_6,7,9 -X\_7,7,9 0
- X\_6,7,9 -X\_8,7,9 0
- X\_6,7,9 -X\_9,7,9 0
- X\_7,7,9 -X\_8,7,9 0
- X\_7,7,9 -X\_9,7,9 0
- X\_8,7,9 -X\_9,7,9 0

X\_1,8,1 X\_2,8,1 X\_3,8,1 X\_4,8,1 X\_5,8,1 X\_6,8,1 X\_7,8,1 X\_8,8,1 X\_9,8,1 0

- X\_1,8,1 -X\_2,8,1 0
- X\_1,8,1 -X\_3,8,1 0
- X\_1,8,1 -X\_4,8,1 0
- X\_1,8,1 -X\_5,8,1 0
- X\_1,8,1 -X\_6,8,1 0
- X\_1,8,1 -X\_7,8,1 0
- X\_1,8,1 -X\_8,8,1 0
- X\_1,8,1 -X\_9,8,1 0
- X\_2,8,1 -X\_3,8,1 0
- X\_2,8,1 -X\_4,8,1 0
- X\_2,8,1 -X\_5,8,1 0
- X\_2,8,1 -X\_6,8,1 0
- X\_2,8,1 -X\_7,8,1 0
- X\_2,8,1 -X\_8,8,1 0
- X\_2,8,1 -X\_9,8,1 0
- X\_3,8,1 -X\_4,8,1 0
- X\_3,8,1 -X\_5,8,1 0
- X\_3,8,1 -X\_6,8,1 0
- X\_3,8,1 -X\_7,8,1 0
- X\_3,8,1 -X\_8,8,1 0
- X\_3,8,1 -X\_9,8,1 0
- X\_4,8,1 -X\_5,8,1 0
- X\_4,8,1 -X\_6,8,1 0
- X\_4,8,1 -X\_7,8,1 0
- X\_4,8,1 -X\_8,8,1 0
- X\_4,8,1 -X\_9,8,1 0
- X\_5,8,1 -X\_6,8,1 0
- X\_5,8,1 -X\_7,8,1 0
- X\_5,8,1 -X\_8,8,1 0
- X\_5,8,1 -X\_9,8,1 0
- X\_6,8,1 -X\_7,8,1 0
- X\_6,8,1 -X\_8,8,1 0
- X\_6,8,1 -X\_9,8,1 0
- X\_7,8,1 -X\_8,8,1 0
- X\_7,8,1 -X\_9,8,1 0
- X\_8,8,1 -X\_9,8,1 0

X\_1,8,2 X\_2,8,2 X\_3,8,2 X\_4,8,2 X\_5,8,2 X\_6,8,2 X\_7,8,2 X\_8,8,2 X\_9,8,2 0

- X\_1,8,2 -X\_2,8,2 0
- X\_1,8,2 -X\_3,8,2 0
- X\_1,8,2 -X\_4,8,2 0
- X\_1,8,2 -X\_5,8,2 0
- X\_1,8,2 -X\_6,8,2 0
- X\_1,8,2 -X\_7,8,2 0
- X\_1,8,2 -X\_8,8,2 0
- X\_1,8,2 -X\_9,8,2 0
- X\_2,8,2 -X\_3,8,2 0
- X\_2,8,2 -X\_4,8,2 0
- X\_2,8,2 -X\_5,8,2 0
- X\_2,8,2 -X\_6,8,2 0
- X\_2,8,2 -X\_7,8,2 0
- X\_2,8,2 -X\_8,8,2 0
- X\_2,8,2 -X\_9,8,2 0
- X\_3,8,2 -X\_4,8,2 0
- X\_3,8,2 -X\_5,8,2 0
- X\_3,8,2 -X\_6,8,2 0
- X\_3,8,2 -X\_7,8,2 0
- X\_3,8,2 -X\_8,8,2 0
- X\_3,8,2 -X\_9,8,2 0
- X\_4,8,2 -X\_5,8,2 0
- X\_4,8,2 -X\_6,8,2 0
- X\_4,8,2 -X\_7,8,2 0
- X\_4,8,2 -X\_8,8,2 0
- X\_4,8,2 -X\_9,8,2 0
- X\_5,8,2 -X\_6,8,2 0
- X\_5,8,2 -X\_7,8,2 0
- X\_5,8,2 -X\_8,8,2 0
- X\_5,8,2 -X\_9,8,2 0
- X\_6,8,2 -X\_7,8,2 0
- X\_6,8,2 -X\_8,8,2 0
- X\_6,8,2 -X\_9,8,2 0
- X\_7,8,2 -X\_8,8,2 0
- X\_7,8,2 -X\_9,8,2 0
- X\_8,8,2 -X\_9,8,2 0

X\_1,8,3 X\_2,8,3 X\_3,8,3 X\_4,8,3 X\_5,8,3 X\_6,8,3 X\_7,8,3 X\_8,8,3 X\_9,8,3 0

- X\_1,8,3 -X\_2,8,3 0
- X\_1,8,3 -X\_3,8,3 0
- X\_1,8,3 -X\_4,8,3 0
- X\_1,8,3 -X\_5,8,3 0
- X\_1,8,3 -X\_6,8,3 0
- X\_1,8,3 -X\_7,8,3 0
- X\_1,8,3 -X\_8,8,3 0
- X\_1,8,3 -X\_9,8,3 0
- X\_2,8,3 -X\_3,8,3 0
- X\_2,8,3 -X\_4,8,3 0
- X\_2,8,3 -X\_5,8,3 0
- X\_2,8,3 -X\_6,8,3 0
- X\_2,8,3 -X\_7,8,3 0
- X\_2,8,3 -X\_8,8,3 0
- X\_2,8,3 -X\_9,8,3 0
- X\_3,8,3 -X\_4,8,3 0
- X\_3,8,3 -X\_5,8,3 0
- X\_3,8,3 -X\_6,8,3 0
- X\_3,8,3 -X\_7,8,3 0
- X\_3,8,3 -X\_8,8,3 0
- X\_3,8,3 -X\_9,8,3 0
- X\_4,8,3 -X\_5,8,3 0
- X\_4,8,3 -X\_6,8,3 0
- X\_4,8,3 -X\_7,8,3 0
- X\_4,8,3 -X\_8,8,3 0
- X\_4,8,3 -X\_9,8,3 0
- X\_5,8,3 -X\_6,8,3 0
- X\_5,8,3 -X\_7,8,3 0
- X\_5,8,3 -X\_8,8,3 0
- X\_5,8,3 -X\_9,8,3 0
- X\_6,8,3 -X\_7,8,3 0
- X\_6,8,3 -X\_8,8,3 0
- X\_6,8,3 -X\_9,8,3 0
- X\_7,8,3 -X\_8,8,3 0
- X\_7,8,3 -X\_9,8,3 0
- X\_8,8,3 -X\_9,8,3 0

X\_1,8,4 X\_2,8,4 X\_3,8,4 X\_4,8,4 X\_5,8,4 X\_6,8,4 X\_7,8,4 X\_8,8,4 X\_9,8,4 0

- X\_1,8,4 -X\_2,8,4 0
- X\_1,8,4 -X\_3,8,4 0
- X\_1,8,4 -X\_4,8,4 0
- X\_1,8,4 -X\_5,8,4 0
- X\_1,8,4 -X\_6,8,4 0
- X\_1,8,4 -X\_7,8,4 0
- X\_1,8,4 -X\_8,8,4 0
- X\_1,8,4 -X\_9,8,4 0
- X\_2,8,4 -X\_3,8,4 0
- X\_2,8,4 -X\_4,8,4 0
- X\_2,8,4 -X\_5,8,4 0
- X\_2,8,4 -X\_6,8,4 0
- X\_2,8,4 -X\_7,8,4 0
- X\_2,8,4 -X\_8,8,4 0
- X\_2,8,4 -X\_9,8,4 0
- X\_3,8,4 -X\_4,8,4 0
- X\_3,8,4 -X\_5,8,4 0
- X\_3,8,4 -X\_6,8,4 0
- X\_3,8,4 -X\_7,8,4 0
- X\_3,8,4 -X\_8,8,4 0
- X\_3,8,4 -X\_9,8,4 0
- X\_4,8,4 -X\_5,8,4 0
- X\_4,8,4 -X\_6,8,4 0
- X\_4,8,4 -X\_7,8,4 0
- X\_4,8,4 -X\_8,8,4 0
- X\_4,8,4 -X\_9,8,4 0
- X\_5,8,4 -X\_6,8,4 0
- X\_5,8,4 -X\_7,8,4 0
- X\_5,8,4 -X\_8,8,4 0
- X\_5,8,4 -X\_9,8,4 0
- X\_6,8,4 -X\_7,8,4 0
- X\_6,8,4 -X\_8,8,4 0
- X\_6,8,4 -X\_9,8,4 0
- X\_7,8,4 -X\_8,8,4 0
- X\_7,8,4 -X\_9,8,4 0
- X\_8,8,4 -X\_9,8,4 0

X\_1,8,5 X\_2,8,5 X\_3,8,5 X\_4,8,5 X\_5,8,5 X\_6,8,5 X\_7,8,5 X\_8,8,5 X\_9,8,5 0

- X\_1,8,5 -X\_2,8,5 0
- X\_1,8,5 -X\_3,8,5 0
- X\_1,8,5 -X\_4,8,5 0
- X\_1,8,5 -X\_5,8,5 0
- X\_1,8,5 -X\_6,8,5 0
- X\_1,8,5 -X\_7,8,5 0
- X\_1,8,5 -X\_8,8,5 0
- X\_1,8,5 -X\_9,8,5 0
- X\_2,8,5 -X\_3,8,5 0
- X\_2,8,5 -X\_4,8,5 0
- X\_2,8,5 -X\_5,8,5 0
- X\_2,8,5 -X\_6,8,5 0
- X\_2,8,5 -X\_7,8,5 0
- X\_2,8,5 -X\_8,8,5 0
- X\_2,8,5 -X\_9,8,5 0
- X\_3,8,5 -X\_4,8,5 0
- X\_3,8,5 -X\_5,8,5 0
- X\_3,8,5 -X\_6,8,5 0
- X\_3,8,5 -X\_7,8,5 0
- X\_3,8,5 -X\_8,8,5 0
- X\_3,8,5 -X\_9,8,5 0
- X\_4,8,5 -X\_5,8,5 0
- X\_4,8,5 -X\_6,8,5 0
- X\_4,8,5 -X\_7,8,5 0
- X\_4,8,5 -X\_8,8,5 0
- X\_4,8,5 -X\_9,8,5 0
- X\_5,8,5 -X\_6,8,5 0
- X\_5,8,5 -X\_7,8,5 0
- X\_5,8,5 -X\_8,8,5 0
- X\_5,8,5 -X\_9,8,5 0
- X\_6,8,5 -X\_7,8,5 0
- X\_6,8,5 -X\_8,8,5 0
- X\_6,8,5 -X\_9,8,5 0
- X\_7,8,5 -X\_8,8,5 0
- X\_7,8,5 -X\_9,8,5 0
- X\_8,8,5 -X\_9,8,5 0

X\_1,8,6 X\_2,8,6 X\_3,8,6 X\_4,8,6 X\_5,8,6 X\_6,8,6 X\_7,8,6 X\_8,8,6 X\_9,8,6 0

- X\_1,8,6 -X\_2,8,6 0
- X\_1,8,6 -X\_3,8,6 0
- X\_1,8,6 -X\_4,8,6 0
- X\_1,8,6 -X\_5,8,6 0
- X\_1,8,6 -X\_6,8,6 0
- X\_1,8,6 -X\_7,8,6 0
- X\_1,8,6 -X\_8,8,6 0
- X\_1,8,6 -X\_9,8,6 0
- X\_2,8,6 -X\_3,8,6 0
- X\_2,8,6 -X\_4,8,6 0
- X\_2,8,6 -X\_5,8,6 0
- X\_2,8,6 -X\_6,8,6 0
- X\_2,8,6 -X\_7,8,6 0
- X\_2,8,6 -X\_8,8,6 0
- X\_2,8,6 -X\_9,8,6 0
- X\_3,8,6 -X\_4,8,6 0
- X\_3,8,6 -X\_5,8,6 0
- X\_3,8,6 -X\_6,8,6 0
- X\_3,8,6 -X\_7,8,6 0
- X\_3,8,6 -X\_8,8,6 0
- X\_3,8,6 -X\_9,8,6 0
- X\_4,8,6 -X\_5,8,6 0
- X\_4,8,6 -X\_6,8,6 0
- X\_4,8,6 -X\_7,8,6 0
- X\_4,8,6 -X\_8,8,6 0
- X\_4,8,6 -X\_9,8,6 0
- X\_5,8,6 -X\_6,8,6 0
- X\_5,8,6 -X\_7,8,6 0
- X\_5,8,6 -X\_8,8,6 0
- X\_5,8,6 -X\_9,8,6 0
- X\_6,8,6 -X\_7,8,6 0
- X\_6,8,6 -X\_8,8,6 0
- X\_6,8,6 -X\_9,8,6 0
- X\_7,8,6 -X\_8,8,6 0
- X\_7,8,6 -X\_9,8,6 0
- X\_8,8,6 -X\_9,8,6 0

X\_1,8,7 X\_2,8,7 X\_3,8,7 X\_4,8,7 X\_5,8,7 X\_6,8,7 X\_7,8,7 X\_8,8,7 X\_9,8,7 0

- X\_1,8,7 -X\_2,8,7 0
- X\_1,8,7 -X\_3,8,7 0
- X\_1,8,7 -X\_4,8,7 0
- X\_1,8,7 -X\_5,8,7 0
- X\_1,8,7 -X\_6,8,7 0
- X\_1,8,7 -X\_7,8,7 0
- X\_1,8,7 -X\_8,8,7 0
- X\_1,8,7 -X\_9,8,7 0
- X\_2,8,7 -X\_3,8,7 0
- X\_2,8,7 -X\_4,8,7 0
- X\_2,8,7 -X\_5,8,7 0
- X\_2,8,7 -X\_6,8,7 0
- X\_2,8,7 -X\_7,8,7 0
- X\_2,8,7 -X\_8,8,7 0
- X\_2,8,7 -X\_9,8,7 0
- X\_3,8,7 -X\_4,8,7 0
- X\_3,8,7 -X\_5,8,7 0
- X\_3,8,7 -X\_6,8,7 0
- X\_3,8,7 -X\_7,8,7 0
- X\_3,8,7 -X\_8,8,7 0
- X\_3,8,7 -X\_9,8,7 0
- X\_4,8,7 -X\_5,8,7 0
- X\_4,8,7 -X\_6,8,7 0
- X\_4,8,7 -X\_7,8,7 0
- X\_4,8,7 -X\_8,8,7 0
- X\_4,8,7 -X\_9,8,7 0
- X\_5,8,7 -X\_6,8,7 0
- X\_5,8,7 -X\_7,8,7 0
- X\_5,8,7 -X\_8,8,7 0
- X\_5,8,7 -X\_9,8,7 0
- X\_6,8,7 -X\_7,8,7 0
- X\_6,8,7 -X\_8,8,7 0
- X\_6,8,7 -X\_9,8,7 0
- X\_7,8,7 -X\_8,8,7 0
- X\_7,8,7 -X\_9,8,7 0
- X\_8,8,7 -X\_9,8,7 0

X\_1,8,8 X\_2,8,8 X\_3,8,8 X\_4,8,8 X\_5,8,8 X\_6,8,8 X\_7,8,8 X\_8,8,8 X\_9,8,8 0

- X\_1,8,8 -X\_2,8,8 0
- X\_1,8,8 -X\_3,8,8 0
- X\_1,8,8 -X\_4,8,8 0
- X\_1,8,8 -X\_5,8,8 0
- X\_1,8,8 -X\_6,8,8 0
- X\_1,8,8 -X\_7,8,8 0
- X\_1,8,8 -X\_8,8,8 0
- X\_1,8,8 -X\_9,8,8 0
- X\_2,8,8 -X\_3,8,8 0
- X\_2,8,8 -X\_4,8,8 0
- X\_2,8,8 -X\_5,8,8 0
- X\_2,8,8 -X\_6,8,8 0
- X\_2,8,8 -X\_7,8,8 0
- X\_2,8,8 -X\_8,8,8 0
- X\_2,8,8 -X\_9,8,8 0
- X\_3,8,8 -X\_4,8,8 0
- X\_3,8,8 -X\_5,8,8 0
- X\_3,8,8 -X\_6,8,8 0
- X\_3,8,8 -X\_7,8,8 0
- X\_3,8,8 -X\_8,8,8 0
- X\_3,8,8 -X\_9,8,8 0
- X\_4,8,8 -X\_5,8,8 0
- X\_4,8,8 -X\_6,8,8 0
- X\_4,8,8 -X\_7,8,8 0
- X\_4,8,8 -X\_8,8,8 0
- X\_4,8,8 -X\_9,8,8 0
- X\_5,8,8 -X\_6,8,8 0
- X\_5,8,8 -X\_7,8,8 0
- X\_5,8,8 -X\_8,8,8 0
- X\_5,8,8 -X\_9,8,8 0
- X\_6,8,8 -X\_7,8,8 0
- X\_6,8,8 -X\_8,8,8 0
- X\_6,8,8 -X\_9,8,8 0
- X\_7,8,8 -X\_8,8,8 0
- X\_7,8,8 -X\_9,8,8 0
- X\_8,8,8 -X\_9,8,8 0

X\_1,8,9 X\_2,8,9 X\_3,8,9 X\_4,8,9 X\_5,8,9 X\_6,8,9 X\_7,8,9 X\_8,8,9 X\_9,8,9 0

- X\_1,8,9 -X\_2,8,9 0
- X\_1,8,9 -X\_3,8,9 0
- X\_1,8,9 -X\_4,8,9 0
- X\_1,8,9 -X\_5,8,9 0
- X\_1,8,9 -X\_6,8,9 0
- X\_1,8,9 -X\_7,8,9 0
- X\_1,8,9 -X\_8,8,9 0
- X\_1,8,9 -X\_9,8,9 0
- X\_2,8,9 -X\_3,8,9 0
- X\_2,8,9 -X\_4,8,9 0
- X\_2,8,9 -X\_5,8,9 0
- X\_2,8,9 -X\_6,8,9 0
- X\_2,8,9 -X\_7,8,9 0
- X\_2,8,9 -X\_8,8,9 0
- X\_2,8,9 -X\_9,8,9 0
- X\_3,8,9 -X\_4,8,9 0
- X\_3,8,9 -X\_5,8,9 0
- X\_3,8,9 -X\_6,8,9 0
- X\_3,8,9 -X\_7,8,9 0
- X\_3,8,9 -X\_8,8,9 0
- X\_3,8,9 -X\_9,8,9 0
- X\_4,8,9 -X\_5,8,9 0
- X\_4,8,9 -X\_6,8,9 0
- X\_4,8,9 -X\_7,8,9 0
- X\_4,8,9 -X\_8,8,9 0
- X\_4,8,9 -X\_9,8,9 0
- X\_5,8,9 -X\_6,8,9 0
- X\_5,8,9 -X\_7,8,9 0
- X\_5,8,9 -X\_8,8,9 0
- X\_5,8,9 -X\_9,8,9 0
- X\_6,8,9 -X\_7,8,9 0
- X\_6,8,9 -X\_8,8,9 0
- X\_6,8,9 -X\_9,8,9 0
- X\_7,8,9 -X\_8,8,9 0
- X\_7,8,9 -X\_9,8,9 0
- X\_8,8,9 -X\_9,8,9 0

X\_1,9,1 X\_2,9,1 X\_3,9,1 X\_4,9,1 X\_5,9,1 X\_6,9,1 X\_7,9,1 X\_8,9,1 X\_9,9,1 0

- X\_1,9,1 -X\_2,9,1 0
- X\_1,9,1 -X\_3,9,1 0
- X\_1,9,1 -X\_4,9,1 0
- X\_1,9,1 -X\_5,9,1 0
- X\_1,9,1 -X\_6,9,1 0
- X\_1,9,1 -X\_7,9,1 0
- X\_1,9,1 -X\_8,9,1 0
- X\_1,9,1 -X\_9,9,1 0
- X\_2,9,1 -X\_3,9,1 0
- X\_2,9,1 -X\_4,9,1 0
- X\_2,9,1 -X\_5,9,1 0
- X\_2,9,1 -X\_6,9,1 0
- X\_2,9,1 -X\_7,9,1 0
- X\_2,9,1 -X\_8,9,1 0
- X\_2,9,1 -X\_9,9,1 0
- X\_3,9,1 -X\_4,9,1 0
- X\_3,9,1 -X\_5,9,1 0
- X\_3,9,1 -X\_6,9,1 0
- X\_3,9,1 -X\_7,9,1 0
- X\_3,9,1 -X\_8,9,1 0
- X\_3,9,1 -X\_9,9,1 0
- X\_4,9,1 -X\_5,9,1 0
- X\_4,9,1 -X\_6,9,1 0
- X\_4,9,1 -X\_7,9,1 0
- X\_4,9,1 -X\_8,9,1 0
- X\_4,9,1 -X\_9,9,1 0
- X\_5,9,1 -X\_6,9,1 0
- X\_5,9,1 -X\_7,9,1 0
- X\_5,9,1 -X\_8,9,1 0
- X\_5,9,1 -X\_9,9,1 0
- X\_6,9,1 -X\_7,9,1 0
- X\_6,9,1 -X\_8,9,1 0
- X\_6,9,1 -X\_9,9,1 0
- X\_7,9,1 -X\_8,9,1 0
- X\_7,9,1 -X\_9,9,1 0
- X\_8,9,1 -X\_9,9,1 0

X\_1,9,2 X\_2,9,2 X\_3,9,2 X\_4,9,2 X\_5,9,2 X\_6,9,2 X\_7,9,2 X\_8,9,2 X\_9,9,2 0

- X\_1,9,2 -X\_2,9,2 0
- X\_1,9,2 -X\_3,9,2 0
- X\_1,9,2 -X\_4,9,2 0
- X\_1,9,2 -X\_5,9,2 0
- X\_1,9,2 -X\_6,9,2 0
- X\_1,9,2 -X\_7,9,2 0
- X\_1,9,2 -X\_8,9,2 0
- X\_1,9,2 -X\_9,9,2 0
- X\_2,9,2 -X\_3,9,2 0
- X\_2,9,2 -X\_4,9,2 0
- X\_2,9,2 -X\_5,9,2 0
- X\_2,9,2 -X\_6,9,2 0
- X\_2,9,2 -X\_7,9,2 0
- X\_2,9,2 -X\_8,9,2 0
- X\_2,9,2 -X\_9,9,2 0
- X\_3,9,2 -X\_4,9,2 0
- X\_3,9,2 -X\_5,9,2 0
- X\_3,9,2 -X\_6,9,2 0
- X\_3,9,2 -X\_7,9,2 0
- X\_3,9,2 -X\_8,9,2 0
- X\_3,9,2 -X\_9,9,2 0
- X\_4,9,2 -X\_5,9,2 0
- X\_4,9,2 -X\_6,9,2 0
- X\_4,9,2 -X\_7,9,2 0
- X\_4,9,2 -X\_8,9,2 0
- X\_4,9,2 -X\_9,9,2 0
- X\_5,9,2 -X\_6,9,2 0
- X\_5,9,2 -X\_7,9,2 0
- X\_5,9,2 -X\_8,9,2 0
- X\_5,9,2 -X\_9,9,2 0
- X\_6,9,2 -X\_7,9,2 0
- X\_6,9,2 -X\_8,9,2 0
- X\_6,9,2 -X\_9,9,2 0
- X\_7,9,2 -X\_8,9,2 0
- X\_7,9,2 -X\_9,9,2 0
- X\_8,9,2 -X\_9,9,2 0

X\_1,9,3 X\_2,9,3 X\_3,9,3 X\_4,9,3 X\_5,9,3 X\_6,9,3 X\_7,9,3 X\_8,9,3 X\_9,9,3 0

- X\_1,9,3 -X\_2,9,3 0
- X\_1,9,3 -X\_3,9,3 0
- X\_1,9,3 -X\_4,9,3 0
- X\_1,9,3 -X\_5,9,3 0
- X\_1,9,3 -X\_6,9,3 0
- X\_1,9,3 -X\_7,9,3 0
- X\_1,9,3 -X\_8,9,3 0
- X\_1,9,3 -X\_9,9,3 0
- X\_2,9,3 -X\_3,9,3 0
- X\_2,9,3 -X\_4,9,3 0
- X\_2,9,3 -X\_5,9,3 0
- X\_2,9,3 -X\_6,9,3 0
- X\_2,9,3 -X\_7,9,3 0
- X\_2,9,3 -X\_8,9,3 0
- X\_2,9,3 -X\_9,9,3 0
- X\_3,9,3 -X\_4,9,3 0
- X\_3,9,3 -X\_5,9,3 0
- X\_3,9,3 -X\_6,9,3 0
- X\_3,9,3 -X\_7,9,3 0
- X\_3,9,3 -X\_8,9,3 0
- X\_3,9,3 -X\_9,9,3 0
- X\_4,9,3 -X\_5,9,3 0
- X\_4,9,3 -X\_6,9,3 0
- X\_4,9,3 -X\_7,9,3 0
- X\_4,9,3 -X\_8,9,3 0
- X\_4,9,3 -X\_9,9,3 0
- X\_5,9,3 -X\_6,9,3 0
- X\_5,9,3 -X\_7,9,3 0
- X\_5,9,3 -X\_8,9,3 0
- X\_5,9,3 -X\_9,9,3 0
- X\_6,9,3 -X\_7,9,3 0
- X\_6,9,3 -X\_8,9,3 0
- X\_6,9,3 -X\_9,9,3 0
- X\_7,9,3 -X\_8,9,3 0
- X\_7,9,3 -X\_9,9,3 0
- X\_8,9,3 -X\_9,9,3 0

X\_1,9,4 X\_2,9,4 X\_3,9,4 X\_4,9,4 X\_5,9,4 X\_6,9,4 X\_7,9,4 X\_8,9,4 X\_9,9,4 0

- X\_1,9,4 -X\_2,9,4 0
- X\_1,9,4 -X\_3,9,4 0
- X\_1,9,4 -X\_4,9,4 0
- X\_1,9,4 -X\_5,9,4 0
- X\_1,9,4 -X\_6,9,4 0
- X\_1,9,4 -X\_7,9,4 0
- X\_1,9,4 -X\_8,9,4 0
- X\_1,9,4 -X\_9,9,4 0
- X\_2,9,4 -X\_3,9,4 0
- X\_2,9,4 -X\_4,9,4 0
- X\_2,9,4 -X\_5,9,4 0
- X\_2,9,4 -X\_6,9,4 0
- X\_2,9,4 -X\_7,9,4 0
- X\_2,9,4 -X\_8,9,4 0
- X\_2,9,4 -X\_9,9,4 0
- X\_3,9,4 -X\_4,9,4 0
- X\_3,9,4 -X\_5,9,4 0
- X\_3,9,4 -X\_6,9,4 0
- X\_3,9,4 -X\_7,9,4 0
- X\_3,9,4 -X\_8,9,4 0
- X\_3,9,4 -X\_9,9,4 0
- X\_4,9,4 -X\_5,9,4 0
- X\_4,9,4 -X\_6,9,4 0
- X\_4,9,4 -X\_7,9,4 0
- X\_4,9,4 -X\_8,9,4 0
- X\_4,9,4 -X\_9,9,4 0
- X\_5,9,4 -X\_6,9,4 0
- X\_5,9,4 -X\_7,9,4 0
- X\_5,9,4 -X\_8,9,4 0
- X\_5,9,4 -X\_9,9,4 0
- X\_6,9,4 -X\_7,9,4 0
- X\_6,9,4 -X\_8,9,4 0
- X\_6,9,4 -X\_9,9,4 0
- X\_7,9,4 -X\_8,9,4 0
- X\_7,9,4 -X\_9,9,4 0
- X\_8,9,4 -X\_9,9,4 0

X\_1,9,5 X\_2,9,5 X\_3,9,5 X\_4,9,5 X\_5,9,5 X\_6,9,5 X\_7,9,5 X\_8,9,5 X\_9,9,5 0

- X\_1,9,5 -X\_2,9,5 0
- X\_1,9,5 -X\_3,9,5 0
- X\_1,9,5 -X\_4,9,5 0
- X\_1,9,5 -X\_5,9,5 0
- X\_1,9,5 -X\_6,9,5 0
- X\_1,9,5 -X\_7,9,5 0
- X\_1,9,5 -X\_8,9,5 0
- X\_1,9,5 -X\_9,9,5 0
- X\_2,9,5 -X\_3,9,5 0
- X\_2,9,5 -X\_4,9,5 0
- X\_2,9,5 -X\_5,9,5 0
- X\_2,9,5 -X\_6,9,5 0
- X\_2,9,5 -X\_7,9,5 0
- X\_2,9,5 -X\_8,9,5 0
- X\_2,9,5 -X\_9,9,5 0
- X\_3,9,5 -X\_4,9,5 0
- X\_3,9,5 -X\_5,9,5 0
- X\_3,9,5 -X\_6,9,5 0
- X\_3,9,5 -X\_7,9,5 0
- X\_3,9,5 -X\_8,9,5 0
- X\_3,9,5 -X\_9,9,5 0
- X\_4,9,5 -X\_5,9,5 0
- X\_4,9,5 -X\_6,9,5 0
- X\_4,9,5 -X\_7,9,5 0
- X\_4,9,5 -X\_8,9,5 0
- X\_4,9,5 -X\_9,9,5 0
- X\_5,9,5 -X\_6,9,5 0
- X\_5,9,5 -X\_7,9,5 0
- X\_5,9,5 -X\_8,9,5 0
- X\_5,9,5 -X\_9,9,5 0
- X\_6,9,5 -X\_7,9,5 0
- X\_6,9,5 -X\_8,9,5 0
- X\_6,9,5 -X\_9,9,5 0
- X\_7,9,5 -X\_8,9,5 0
- X\_7,9,5 -X\_9,9,5 0
- X\_8,9,5 -X\_9,9,5 0

X\_1,9,6 X\_2,9,6 X\_3,9,6 X\_4,9,6 X\_5,9,6 X\_6,9,6 X\_7,9,6 X\_8,9,6 X\_9,9,6 0

- X\_1,9,6 -X\_2,9,6 0
- X\_1,9,6 -X\_3,9,6 0
- X\_1,9,6 -X\_4,9,6 0
- X\_1,9,6 -X\_5,9,6 0
- X\_1,9,6 -X\_6,9,6 0
- X\_1,9,6 -X\_7,9,6 0
- X\_1,9,6 -X\_8,9,6 0
- X\_1,9,6 -X\_9,9,6 0
- X\_2,9,6 -X\_3,9,6 0
- X\_2,9,6 -X\_4,9,6 0
- X\_2,9,6 -X\_5,9,6 0
- X\_2,9,6 -X\_6,9,6 0
- X\_2,9,6 -X\_7,9,6 0
- X\_2,9,6 -X\_8,9,6 0
- X\_2,9,6 -X\_9,9,6 0
- X\_3,9,6 -X\_4,9,6 0
- X\_3,9,6 -X\_5,9,6 0
- X\_3,9,6 -X\_6,9,6 0
- X\_3,9,6 -X\_7,9,6 0
- X\_3,9,6 -X\_8,9,6 0
- X\_3,9,6 -X\_9,9,6 0
- X\_4,9,6 -X\_5,9,6 0
- X\_4,9,6 -X\_6,9,6 0
- X\_4,9,6 -X\_7,9,6 0
- X\_4,9,6 -X\_8,9,6 0
- X\_4,9,6 -X\_9,9,6 0
- X\_5,9,6 -X\_6,9,6 0
- X\_5,9,6 -X\_7,9,6 0
- X\_5,9,6 -X\_8,9,6 0
- X\_5,9,6 -X\_9,9,6 0
- X\_6,9,6 -X\_7,9,6 0
- X\_6,9,6 -X\_8,9,6 0
- X\_6,9,6 -X\_9,9,6 0
- X\_7,9,6 -X\_8,9,6 0
- X\_7,9,6 -X\_9,9,6 0
- X\_8,9,6 -X\_9,9,6 0

X\_1,9,7 X\_2,9,7 X\_3,9,7 X\_4,9,7 X\_5,9,7 X\_6,9,7 X\_7,9,7 X\_8,9,7 X\_9,9,7 0

- X\_1,9,7 -X\_2,9,7 0
- X\_1,9,7 -X\_3,9,7 0
- X\_1,9,7 -X\_4,9,7 0
- X\_1,9,7 -X\_5,9,7 0
- X\_1,9,7 -X\_6,9,7 0
- X\_1,9,7 -X\_7,9,7 0
- X\_1,9,7 -X\_8,9,7 0
- X\_1,9,7 -X\_9,9,7 0
- X\_2,9,7 -X\_3,9,7 0
- X\_2,9,7 -X\_4,9,7 0
- X\_2,9,7 -X\_5,9,7 0
- X\_2,9,7 -X\_6,9,7 0
- X\_2,9,7 -X\_7,9,7 0
- X\_2,9,7 -X\_8,9,7 0
- X\_2,9,7 -X\_9,9,7 0
- X\_3,9,7 -X\_4,9,7 0
- X\_3,9,7 -X\_5,9,7 0
- X\_3,9,7 -X\_6,9,7 0
- X\_3,9,7 -X\_7,9,7 0
- X\_3,9,7 -X\_8,9,7 0
- X\_3,9,7 -X\_9,9,7 0
- X\_4,9,7 -X\_5,9,7 0
- X\_4,9,7 -X\_6,9,7 0
- X\_4,9,7 -X\_7,9,7 0
- X\_4,9,7 -X\_8,9,7 0
- X\_4,9,7 -X\_9,9,7 0
- X\_5,9,7 -X\_6,9,7 0
- X\_5,9,7 -X\_7,9,7 0
- X\_5,9,7 -X\_8,9,7 0
- X\_5,9,7 -X\_9,9,7 0
- X\_6,9,7 -X\_7,9,7 0
- X\_6,9,7 -X\_8,9,7 0
- X\_6,9,7 -X\_9,9,7 0
- X\_7,9,7 -X\_8,9,7 0
- X\_7,9,7 -X\_9,9,7 0
- X\_8,9,7 -X\_9,9,7 0

X\_1,9,8 X\_2,9,8 X\_3,9,8 X\_4,9,8 X\_5,9,8 X\_6,9,8 X\_7,9,8 X\_8,9,8 X\_9,9,8 0

- X\_1,9,8 -X\_2,9,8 0
- X\_1,9,8 -X\_3,9,8 0
- X\_1,9,8 -X\_4,9,8 0
- X\_1,9,8 -X\_5,9,8 0
- X\_1,9,8 -X\_6,9,8 0
- X\_1,9,8 -X\_7,9,8 0
- X\_1,9,8 -X\_8,9,8 0
- X\_1,9,8 -X\_9,9,8 0
- X\_2,9,8 -X\_3,9,8 0
- X\_2,9,8 -X\_4,9,8 0
- X\_2,9,8 -X\_5,9,8 0
- X\_2,9,8 -X\_6,9,8 0
- X\_2,9,8 -X\_7,9,8 0
- X\_2,9,8 -X\_8,9,8 0
- X\_2,9,8 -X\_9,9,8 0
- X\_3,9,8 -X\_4,9,8 0
- X\_3,9,8 -X\_5,9,8 0
- X\_3,9,8 -X\_6,9,8 0
- X\_3,9,8 -X\_7,9,8 0
- X\_3,9,8 -X\_8,9,8 0
- X\_3,9,8 -X\_9,9,8 0
- X\_4,9,8 -X\_5,9,8 0
- X\_4,9,8 -X\_6,9,8 0
- X\_4,9,8 -X\_7,9,8 0
- X\_4,9,8 -X\_8,9,8 0
- X\_4,9,8 -X\_9,9,8 0
- X\_5,9,8 -X\_6,9,8 0
- X\_5,9,8 -X\_7,9,8 0
- X\_5,9,8 -X\_8,9,8 0
- X\_5,9,8 -X\_9,9,8 0
- X\_6,9,8 -X\_7,9,8 0
- X\_6,9,8 -X\_8,9,8 0
- X\_6,9,8 -X\_9,9,8 0
- X\_7,9,8 -X\_8,9,8 0
- X\_7,9,8 -X\_9,9,8 0
- X\_8,9,8 -X\_9,9,8 0

X\_1,9,9 X\_2,9,9 X\_3,9,9 X\_4,9,9 X\_5,9,9 X\_6,9,9 X\_7,9,9 X\_8,9,9 X\_9,9,9 0

- X\_1,9,9 -X\_2,9,9 0
- X\_1,9,9 -X\_3,9,9 0
- X\_1,9,9 -X\_4,9,9 0
- X\_1,9,9 -X\_5,9,9 0
- X\_1,9,9 -X\_6,9,9 0
- X\_1,9,9 -X\_7,9,9 0
- X\_1,9,9 -X\_8,9,9 0
- X\_1,9,9 -X\_9,9,9 0
- X\_2,9,9 -X\_3,9,9 0
- X\_2,9,9 -X\_4,9,9 0
- X\_2,9,9 -X\_5,9,9 0
- X\_2,9,9 -X\_6,9,9 0
- X\_2,9,9 -X\_7,9,9 0
- X\_2,9,9 -X\_8,9,9 0
- X\_2,9,9 -X\_9,9,9 0
- X\_3,9,9 -X\_4,9,9 0
- X\_3,9,9 -X\_5,9,9 0
- X\_3,9,9 -X\_6,9,9 0
- X\_3,9,9 -X\_7,9,9 0
- X\_3,9,9 -X\_8,9,9 0
- X\_3,9,9 -X\_9,9,9 0
- X\_4,9,9 -X\_5,9,9 0
- X\_4,9,9 -X\_6,9,9 0
- X\_4,9,9 -X\_7,9,9 0
- X\_4,9,9 -X\_8,9,9 0
- X\_4,9,9 -X\_9,9,9 0
- X\_5,9,9 -X\_6,9,9 0
- X\_5,9,9 -X\_7,9,9 0
- X\_5,9,9 -X\_8,9,9 0
- X\_5,9,9 -X\_9,9,9 0
- X\_6,9,9 -X\_7,9,9 0
- X\_6,9,9 -X\_8,9,9 0
- X\_6,9,9 -X\_9,9,9 0
- X\_7,9,9 -X\_8,9,9 0
- X\_7,9,9 -X\_9,9,9 0
- X\_8,9,9 -X\_9,9,9 0

X\_1,1,1 X\_1,2,1 X\_1,3,1 X\_2,1,1 X\_2,2,1 X\_2,3,1 X\_3,1,1 X\_3,2,1 X\_3,3,1 0

- X\_1,1,1 -X\_1,2,1 0
- X\_1,1,1 -X\_1,3,1 0
- X\_1,1,1 -X\_2,1,1 0
- X\_1,1,1 -X\_2,2,1 0
- X\_1,1,1 -X\_2,3,1 0
- X\_1,1,1 -X\_3,1,1 0
- X\_1,1,1 -X\_3,2,1 0
- X\_1,1,1 -X\_3,3,1 0
- X\_1,2,1 -X\_1,3,1 0
- X\_1,2,1 -X\_2,1,1 0
- X\_1,2,1 -X\_2,2,1 0
- X\_1,2,1 -X\_2,3,1 0
- X\_1,2,1 -X\_3,1,1 0
- X\_1,2,1 -X\_3,2,1 0
- X\_1,2,1 -X\_3,3,1 0
- X\_1,3,1 -X\_2,1,1 0
- X\_1,3,1 -X\_2,2,1 0
- X\_1,3,1 -X\_2,3,1 0
- X\_1,3,1 -X\_3,1,1 0
- X\_1,3,1 -X\_3,2,1 0
- X\_1,3,1 -X\_3,3,1 0
- X\_2,1,1 -X\_2,2,1 0
- X\_2,1,1 -X\_2,3,1 0
- X\_2,1,1 -X\_3,1,1 0
- X\_2,1,1 -X\_3,2,1 0
- X\_2,1,1 -X\_3,3,1 0
- X\_2,2,1 -X\_2,3,1 0
- X\_2,2,1 -X\_3,1,1 0
- X\_2,2,1 -X\_3,2,1 0
- X\_2,2,1 -X\_3,3,1 0
- X\_2,3,1 -X\_3,1,1 0
- X\_2,3,1 -X\_3,2,1 0
- X\_2,3,1 -X\_3,3,1 0
- X\_3,1,1 -X\_3,2,1 0
- X\_3,1,1 -X\_3,3,1 0
- X\_3,2,1 -X\_3,3,1 0

X\_1,4,1 X\_1,5,1 X\_1,6,1 X\_2,4,1 X\_2,5,1 X\_2,6,1 X\_3,4,1 X\_3,5,1 X\_3,6,1 0

- X\_1,4,1 -X\_1,5,1 0
- X\_1,4,1 -X\_1,6,1 0
- X\_1,4,1 -X\_2,4,1 0
- X\_1,4,1 -X\_2,5,1 0
- X\_1,4,1 -X\_2,6,1 0
- X\_1,4,1 -X\_3,4,1 0
- X\_1,4,1 -X\_3,5,1 0
- X\_1,4,1 -X\_3,6,1 0
- X\_1,5,1 -X\_1,6,1 0
- X\_1,5,1 -X\_2,4,1 0
- X\_1,5,1 -X\_2,5,1 0
- X\_1,5,1 -X\_2,6,1 0
- X\_1,5,1 -X\_3,4,1 0
- X\_1,5,1 -X\_3,5,1 0
- X\_1,5,1 -X\_3,6,1 0
- X\_1,6,1 -X\_2,4,1 0
- X\_1,6,1 -X\_2,5,1 0
- X\_1,6,1 -X\_2,6,1 0
- X\_1,6,1 -X\_3,4,1 0
- X\_1,6,1 -X\_3,5,1 0
- X\_1,6,1 -X\_3,6,1 0
- X\_2,4,1 -X\_2,5,1 0
- X\_2,4,1 -X\_2,6,1 0
- X\_2,4,1 -X\_3,4,1 0
- X\_2,4,1 -X\_3,5,1 0
- X\_2,4,1 -X\_3,6,1 0
- X\_2,5,1 -X\_2,6,1 0
- X\_2,5,1 -X\_3,4,1 0
- X\_2,5,1 -X\_3,5,1 0
- X\_2,5,1 -X\_3,6,1 0
- X\_2,6,1 -X\_3,4,1 0
- X\_2,6,1 -X\_3,5,1 0
- X\_2,6,1 -X\_3,6,1 0
- X\_3,4,1 -X\_3,5,1 0
- X\_3,4,1 -X\_3,6,1 0
- X\_3,5,1 -X\_3,6,1 0

X\_1,7,1 X\_1,8,1 X\_1,9,1 X\_2,7,1 X\_2,8,1 X\_2,9,1 X\_3,7,1 X\_3,8,1 X\_3,9,1 0

- X\_1,7,1 -X\_1,8,1 0
- X\_1,7,1 -X\_1,9,1 0
- X\_1,7,1 -X\_2,7,1 0
- X\_1,7,1 -X\_2,8,1 0
- X\_1,7,1 -X\_2,9,1 0
- X\_1,7,1 -X\_3,7,1 0
- X\_1,7,1 -X\_3,8,1 0
- X\_1,7,1 -X\_3,9,1 0
- X\_1,8,1 -X\_1,9,1 0
- X\_1,8,1 -X\_2,7,1 0
- X\_1,8,1 -X\_2,8,1 0
- X\_1,8,1 -X\_2,9,1 0
- X\_1,8,1 -X\_3,7,1 0
- X\_1,8,1 -X\_3,8,1 0
- X\_1,8,1 -X\_3,9,1 0
- X\_1,9,1 -X\_2,7,1 0
- X\_1,9,1 -X\_2,8,1 0
- X\_1,9,1 -X\_2,9,1 0
- X\_1,9,1 -X\_3,7,1 0
- X\_1,9,1 -X\_3,8,1 0
- X\_1,9,1 -X\_3,9,1 0
- X\_2,7,1 -X\_2,8,1 0
- X\_2,7,1 -X\_2,9,1 0
- X\_2,7,1 -X\_3,7,1 0
- X\_2,7,1 -X\_3,8,1 0
- X\_2,7,1 -X\_3,9,1 0
- X\_2,8,1 -X\_2,9,1 0
- X\_2,8,1 -X\_3,7,1 0
- X\_2,8,1 -X\_3,8,1 0
- X\_2,8,1 -X\_3,9,1 0
- X\_2,9,1 -X\_3,7,1 0
- X\_2,9,1 -X\_3,8,1 0
- X\_2,9,1 -X\_3,9,1 0
- X\_3,7,1 -X\_3,8,1 0
- X\_3,7,1 -X\_3,9,1 0
- X\_3,8,1 -X\_3,9,1 0

X\_4,1,1 X\_4,2,1 X\_4,3,1 X\_5,1,1 X\_5,2,1 X\_5,3,1 X\_6,1,1 X\_6,2,1 X\_6,3,1 0

- X\_4,1,1 -X\_4,2,1 0
- X\_4,1,1 -X\_4,3,1 0
- X\_4,1,1 -X\_5,1,1 0
- X\_4,1,1 -X\_5,2,1 0
- X\_4,1,1 -X\_5,3,1 0
- X\_4,1,1 -X\_6,1,1 0
- X\_4,1,1 -X\_6,2,1 0
- X\_4,1,1 -X\_6,3,1 0
- X\_4,2,1 -X\_4,3,1 0
- X\_4,2,1 -X\_5,1,1 0
- X\_4,2,1 -X\_5,2,1 0
- X\_4,2,1 -X\_5,3,1 0
- X\_4,2,1 -X\_6,1,1 0
- X\_4,2,1 -X\_6,2,1 0
- X\_4,2,1 -X\_6,3,1 0
- X\_4,3,1 -X\_5,1,1 0
- X\_4,3,1 -X\_5,2,1 0
- X\_4,3,1 -X\_5,3,1 0
- X\_4,3,1 -X\_6,1,1 0
- X\_4,3,1 -X\_6,2,1 0
- X\_4,3,1 -X\_6,3,1 0
- X\_5,1,1 -X\_5,2,1 0
- X\_5,1,1 -X\_5,3,1 0
- X\_5,1,1 -X\_6,1,1 0
- X\_5,1,1 -X\_6,2,1 0
- X\_5,1,1 -X\_6,3,1 0
- X\_5,2,1 -X\_5,3,1 0
- X\_5,2,1 -X\_6,1,1 0
- X\_5,2,1 -X\_6,2,1 0
- X\_5,2,1 -X\_6,3,1 0
- X\_5,3,1 -X\_6,1,1 0
- X\_5,3,1 -X\_6,2,1 0
- X\_5,3,1 -X\_6,3,1 0
- X\_6,1,1 -X\_6,2,1 0
- X\_6,1,1 -X\_6,3,1 0
- X\_6,2,1 -X\_6,3,1 0

X\_4,4,1 X\_4,5,1 X\_4,6,1 X\_5,4,1 X\_5,5,1 X\_5,6,1 X\_6,4,1 X\_6,5,1 X\_6,6,1 0

- X\_4,4,1 -X\_4,5,1 0
- X\_4,4,1 -X\_4,6,1 0
- X\_4,4,1 -X\_5,4,1 0
- X\_4,4,1 -X\_5,5,1 0
- X\_4,4,1 -X\_5,6,1 0
- X\_4,4,1 -X\_6,4,1 0
- X\_4,4,1 -X\_6,5,1 0
- X\_4,4,1 -X\_6,6,1 0
- X\_4,5,1 -X\_4,6,1 0
- X\_4,5,1 -X\_5,4,1 0
- X\_4,5,1 -X\_5,5,1 0
- X\_4,5,1 -X\_5,6,1 0
- X\_4,5,1 -X\_6,4,1 0
- X\_4,5,1 -X\_6,5,1 0
- X\_4,5,1 -X\_6,6,1 0
- X\_4,6,1 -X\_5,4,1 0
- X\_4,6,1 -X\_5,5,1 0
- X\_4,6,1 -X\_5,6,1 0
- X\_4,6,1 -X\_6,4,1 0
- X\_4,6,1 -X\_6,5,1 0
- X\_4,6,1 -X\_6,6,1 0
- X\_5,4,1 -X\_5,5,1 0
- X\_5,4,1 -X\_5,6,1 0
- X\_5,4,1 -X\_6,4,1 0
- X\_5,4,1 -X\_6,5,1 0
- X\_5,4,1 -X\_6,6,1 0
- X\_5,5,1 -X\_5,6,1 0
- X\_5,5,1 -X\_6,4,1 0
- X\_5,5,1 -X\_6,5,1 0
- X\_5,5,1 -X\_6,6,1 0
- X\_5,6,1 -X\_6,4,1 0
- X\_5,6,1 -X\_6,5,1 0
- X\_5,6,1 -X\_6,6,1 0
- X\_6,4,1 -X\_6,5,1 0
- X\_6,4,1 -X\_6,6,1 0
- X\_6,5,1 -X\_6,6,1 0

X\_4,7,1 X\_4,8,1 X\_4,9,1 X\_5,7,1 X\_5,8,1 X\_5,9,1 X\_6,7,1 X\_6,8,1 X\_6,9,1 0

- X\_4,7,1 -X\_4,8,1 0
- X\_4,7,1 -X\_4,9,1 0
- X\_4,7,1 -X\_5,7,1 0
- X\_4,7,1 -X\_5,8,1 0
- X\_4,7,1 -X\_5,9,1 0
- X\_4,7,1 -X\_6,7,1 0
- X\_4,7,1 -X\_6,8,1 0
- X\_4,7,1 -X\_6,9,1 0
- X\_4,8,1 -X\_4,9,1 0
- X\_4,8,1 -X\_5,7,1 0
- X\_4,8,1 -X\_5,8,1 0
- X\_4,8,1 -X\_5,9,1 0
- X\_4,8,1 -X\_6,7,1 0
- X\_4,8,1 -X\_6,8,1 0
- X\_4,8,1 -X\_6,9,1 0
- X\_4,9,1 -X\_5,7,1 0
- X\_4,9,1 -X\_5,8,1 0
- X\_4,9,1 -X\_5,9,1 0
- X\_4,9,1 -X\_6,7,1 0
- X\_4,9,1 -X\_6,8,1 0
- X\_4,9,1 -X\_6,9,1 0
- X\_5,7,1 -X\_5,8,1 0
- X\_5,7,1 -X\_5,9,1 0
- X\_5,7,1 -X\_6,7,1 0
- X\_5,7,1 -X\_6,8,1 0
- X\_5,7,1 -X\_6,9,1 0
- X\_5,8,1 -X\_5,9,1 0
- X\_5,8,1 -X\_6,7,1 0
- X\_5,8,1 -X\_6,8,1 0
- X\_5,8,1 -X\_6,9,1 0
- X\_5,9,1 -X\_6,7,1 0
- X\_5,9,1 -X\_6,8,1 0
- X\_5,9,1 -X\_6,9,1 0
- X\_6,7,1 -X\_6,8,1 0
- X\_6,7,1 -X\_6,9,1 0
- X\_6,8,1 -X\_6,9,1 0

X\_7,1,1 X\_7,2,1 X\_7,3,1 X\_8,1,1 X\_8,2,1 X\_8,3,1 X\_9,1,1 X\_9,2,1 X\_9,3,1 0

- X\_7,1,1 -X\_7,2,1 0
- X\_7,1,1 -X\_7,3,1 0
- X\_7,1,1 -X\_8,1,1 0
- X\_7,1,1 -X\_8,2,1 0
- X\_7,1,1 -X\_8,3,1 0
- X\_7,1,1 -X\_9,1,1 0
- X\_7,1,1 -X\_9,2,1 0
- X\_7,1,1 -X\_9,3,1 0
- X\_7,2,1 -X\_7,3,1 0
- X\_7,2,1 -X\_8,1,1 0
- X\_7,2,1 -X\_8,2,1 0
- X\_7,2,1 -X\_8,3,1 0
- X\_7,2,1 -X\_9,1,1 0
- X\_7,2,1 -X\_9,2,1 0
- X\_7,2,1 -X\_9,3,1 0
- X\_7,3,1 -X\_8,1,1 0
- X\_7,3,1 -X\_8,2,1 0
- X\_7,3,1 -X\_8,3,1 0
- X\_7,3,1 -X\_9,1,1 0
- X\_7,3,1 -X\_9,2,1 0
- X\_7,3,1 -X\_9,3,1 0
- X\_8,1,1 -X\_8,2,1 0
- X\_8,1,1 -X\_8,3,1 0
- X\_8,1,1 -X\_9,1,1 0
- X\_8,1,1 -X\_9,2,1 0
- X\_8,1,1 -X\_9,3,1 0
- X\_8,2,1 -X\_8,3,1 0
- X\_8,2,1 -X\_9,1,1 0
- X\_8,2,1 -X\_9,2,1 0
- X\_8,2,1 -X\_9,3,1 0
- X\_8,3,1 -X\_9,1,1 0
- X\_8,3,1 -X\_9,2,1 0
- X\_8,3,1 -X\_9,3,1 0
- X\_9,1,1 -X\_9,2,1 0
- X\_9,1,1 -X\_9,3,1 0
- X\_9,2,1 -X\_9,3,1 0

X\_7,4,1 X\_7,5,1 X\_7,6,1 X\_8,4,1 X\_8,5,1 X\_8,6,1 X\_9,4,1 X\_9,5,1 X\_9,6,1 0

- X\_7,4,1 -X\_7,5,1 0
- X\_7,4,1 -X\_7,6,1 0
- X\_7,4,1 -X\_8,4,1 0
- X\_7,4,1 -X\_8,5,1 0
- X\_7,4,1 -X\_8,6,1 0
- X\_7,4,1 -X\_9,4,1 0
- X\_7,4,1 -X\_9,5,1 0
- X\_7,4,1 -X\_9,6,1 0
- X\_7,5,1 -X\_7,6,1 0
- X\_7,5,1 -X\_8,4,1 0
- X\_7,5,1 -X\_8,5,1 0
- X\_7,5,1 -X\_8,6,1 0
- X\_7,5,1 -X\_9,4,1 0
- X\_7,5,1 -X\_9,5,1 0
- X\_7,5,1 -X\_9,6,1 0
- X\_7,6,1 -X\_8,4,1 0
- X\_7,6,1 -X\_8,5,1 0
- X\_7,6,1 -X\_8,6,1 0
- X\_7,6,1 -X\_9,4,1 0
- X\_7,6,1 -X\_9,5,1 0
- X\_7,6,1 -X\_9,6,1 0
- X\_8,4,1 -X\_8,5,1 0
- X\_8,4,1 -X\_8,6,1 0
- X\_8,4,1 -X\_9,4,1 0
- X\_8,4,1 -X\_9,5,1 0
- X\_8,4,1 -X\_9,6,1 0
- X\_8,5,1 -X\_8,6,1 0
- X\_8,5,1 -X\_9,4,1 0
- X\_8,5,1 -X\_9,5,1 0
- X\_8,5,1 -X\_9,6,1 0
- X\_8,6,1 -X\_9,4,1 0
- X\_8,6,1 -X\_9,5,1 0
- X\_8,6,1 -X\_9,6,1 0
- X\_9,4,1 -X\_9,5,1 0
- X\_9,4,1 -X\_9,6,1 0
- X\_9,5,1 -X\_9,6,1 0

X\_7,7,1 X\_7,8,1 X\_7,9,1 X\_8,7,1 X\_8,8,1 X\_8,9,1 X\_9,7,1 X\_9,8,1 X\_9,9,1 0

- X\_7,7,1 -X\_7,8,1 0
- X\_7,7,1 -X\_7,9,1 0
- X\_7,7,1 -X\_8,7,1 0
- X\_7,7,1 -X\_8,8,1 0
- X\_7,7,1 -X\_8,9,1 0
- X\_7,7,1 -X\_9,7,1 0
- X\_7,7,1 -X\_9,8,1 0
- X\_7,7,1 -X\_9,9,1 0
- X\_7,8,1 -X\_7,9,1 0
- X\_7,8,1 -X\_8,7,1 0
- X\_7,8,1 -X\_8,8,1 0
- X\_7,8,1 -X\_8,9,1 0
- X\_7,8,1 -X\_9,7,1 0
- X\_7,8,1 -X\_9,8,1 0
- X\_7,8,1 -X\_9,9,1 0
- X\_7,9,1 -X\_8,7,1 0
- X\_7,9,1 -X\_8,8,1 0
- X\_7,9,1 -X\_8,9,1 0
- X\_7,9,1 -X\_9,7,1 0
- X\_7,9,1 -X\_9,8,1 0
- X\_7,9,1 -X\_9,9,1 0
- X\_8,7,1 -X\_8,8,1 0
- X\_8,7,1 -X\_8,9,1 0
- X\_8,7,1 -X\_9,7,1 0
- X\_8,7,1 -X\_9,8,1 0
- X\_8,7,1 -X\_9,9,1 0
- X\_8,8,1 -X\_8,9,1 0
- X\_8,8,1 -X\_9,7,1 0
- X\_8,8,1 -X\_9,8,1 0
- X\_8,8,1 -X\_9,9,1 0
- X\_8,9,1 -X\_9,7,1 0
- X\_8,9,1 -X\_9,8,1 0
- X\_8,9,1 -X\_9,9,1 0
- X\_9,7,1 -X\_9,8,1 0
- X\_9,7,1 -X\_9,9,1 0
- X\_9,8,1 -X\_9,9,1 0

X\_1,1,2 X\_1,2,2 X\_1,3,2 X\_2,1,2 X\_2,2,2 X\_2,3,2 X\_3,1,2 X\_3,2,2 X\_3,3,2 0

- X\_1,1,2 -X\_1,2,2 0
- X\_1,1,2 -X\_1,3,2 0
- X\_1,1,2 -X\_2,1,2 0
- X\_1,1,2 -X\_2,2,2 0
- X\_1,1,2 -X\_2,3,2 0
- X\_1,1,2 -X\_3,1,2 0
- X\_1,1,2 -X\_3,2,2 0
- X\_1,1,2 -X\_3,3,2 0
- X\_1,2,2 -X\_1,3,2 0
- X\_1,2,2 -X\_2,1,2 0
- X\_1,2,2 -X\_2,2,2 0
- X\_1,2,2 -X\_2,3,2 0
- X\_1,2,2 -X\_3,1,2 0
- X\_1,2,2 -X\_3,2,2 0
- X\_1,2,2 -X\_3,3,2 0
- X\_1,3,2 -X\_2,1,2 0
- X\_1,3,2 -X\_2,2,2 0
- X\_1,3,2 -X\_2,3,2 0
- X\_1,3,2 -X\_3,1,2 0
- X\_1,3,2 -X\_3,2,2 0
- X\_1,3,2 -X\_3,3,2 0
- X\_2,1,2 -X\_2,2,2 0
- X\_2,1,2 -X\_2,3,2 0
- X\_2,1,2 -X\_3,1,2 0
- X\_2,1,2 -X\_3,2,2 0
- X\_2,1,2 -X\_3,3,2 0
- X\_2,2,2 -X\_2,3,2 0
- X\_2,2,2 -X\_3,1,2 0
- X\_2,2,2 -X\_3,2,2 0
- X\_2,2,2 -X\_3,3,2 0
- X\_2,3,2 -X\_3,1,2 0
- X\_2,3,2 -X\_3,2,2 0
- X\_2,3,2 -X\_3,3,2 0
- X\_3,1,2 -X\_3,2,2 0
- X\_3,1,2 -X\_3,3,2 0
- X\_3,2,2 -X\_3,3,2 0

X\_1,4,2 X\_1,5,2 X\_1,6,2 X\_2,4,2 X\_2,5,2 X\_2,6,2 X\_3,4,2 X\_3,5,2 X\_3,6,2 0

- X\_1,4,2 -X\_1,5,2 0
- X\_1,4,2 -X\_1,6,2 0
- X\_1,4,2 -X\_2,4,2 0
- X\_1,4,2 -X\_2,5,2 0
- X\_1,4,2 -X\_2,6,2 0
- X\_1,4,2 -X\_3,4,2 0
- X\_1,4,2 -X\_3,5,2 0
- X\_1,4,2 -X\_3,6,2 0
- X\_1,5,2 -X\_1,6,2 0
- X\_1,5,2 -X\_2,4,2 0
- X\_1,5,2 -X\_2,5,2 0
- X\_1,5,2 -X\_2,6,2 0
- X\_1,5,2 -X\_3,4,2 0
- X\_1,5,2 -X\_3,5,2 0
- X\_1,5,2 -X\_3,6,2 0
- X\_1,6,2 -X\_2,4,2 0
- X\_1,6,2 -X\_2,5,2 0
- X\_1,6,2 -X\_2,6,2 0
- X\_1,6,2 -X\_3,4,2 0
- X\_1,6,2 -X\_3,5,2 0
- X\_1,6,2 -X\_3,6,2 0
- X\_2,4,2 -X\_2,5,2 0
- X\_2,4,2 -X\_2,6,2 0
- X\_2,4,2 -X\_3,4,2 0
- X\_2,4,2 -X\_3,5,2 0
- X\_2,4,2 -X\_3,6,2 0
- X\_2,5,2 -X\_2,6,2 0
- X\_2,5,2 -X\_3,4,2 0
- X\_2,5,2 -X\_3,5,2 0
- X\_2,5,2 -X\_3,6,2 0
- X\_2,6,2 -X\_3,4,2 0
- X\_2,6,2 -X\_3,5,2 0
- X\_2,6,2 -X\_3,6,2 0
- X\_3,4,2 -X\_3,5,2 0
- X\_3,4,2 -X\_3,6,2 0
- X\_3,5,2 -X\_3,6,2 0

X\_1,7,2 X\_1,8,2 X\_1,9,2 X\_2,7,2 X\_2,8,2 X\_2,9,2 X\_3,7,2 X\_3,8,2 X\_3,9,2 0

- X\_1,7,2 -X\_1,8,2 0
- X\_1,7,2 -X\_1,9,2 0
- X\_1,7,2 -X\_2,7,2 0
- X\_1,7,2 -X\_2,8,2 0
- X\_1,7,2 -X\_2,9,2 0
- X\_1,7,2 -X\_3,7,2 0
- X\_1,7,2 -X\_3,8,2 0
- X\_1,7,2 -X\_3,9,2 0
- X\_1,8,2 -X\_1,9,2 0
- X\_1,8,2 -X\_2,7,2 0
- X\_1,8,2 -X\_2,8,2 0
- X\_1,8,2 -X\_2,9,2 0
- X\_1,8,2 -X\_3,7,2 0
- X\_1,8,2 -X\_3,8,2 0
- X\_1,8,2 -X\_3,9,2 0
- X\_1,9,2 -X\_2,7,2 0
- X\_1,9,2 -X\_2,8,2 0
- X\_1,9,2 -X\_2,9,2 0
- X\_1,9,2 -X\_3,7,2 0
- X\_1,9,2 -X\_3,8,2 0
- X\_1,9,2 -X\_3,9,2 0
- X\_2,7,2 -X\_2,8,2 0
- X\_2,7,2 -X\_2,9,2 0
- X\_2,7,2 -X\_3,7,2 0
- X\_2,7,2 -X\_3,8,2 0
- X\_2,7,2 -X\_3,9,2 0
- X\_2,8,2 -X\_2,9,2 0
- X\_2,8,2 -X\_3,7,2 0
- X\_2,8,2 -X\_3,8,2 0
- X\_2,8,2 -X\_3,9,2 0
- X\_2,9,2 -X\_3,7,2 0
- X\_2,9,2 -X\_3,8,2 0
- X\_2,9,2 -X\_3,9,2 0
- X\_3,7,2 -X\_3,8,2 0
- X\_3,7,2 -X\_3,9,2 0
- X\_3,8,2 -X\_3,9,2 0

X\_4,1,2 X\_4,2,2 X\_4,3,2 X\_5,1,2 X\_5,2,2 X\_5,3,2 X\_6,1,2 X\_6,2,2 X\_6,3,2 0

- X\_4,1,2 -X\_4,2,2 0
- X\_4,1,2 -X\_4,3,2 0
- X\_4,1,2 -X\_5,1,2 0
- X\_4,1,2 -X\_5,2,2 0
- X\_4,1,2 -X\_5,3,2 0
- X\_4,1,2 -X\_6,1,2 0
- X\_4,1,2 -X\_6,2,2 0
- X\_4,1,2 -X\_6,3,2 0
- X\_4,2,2 -X\_4,3,2 0
- X\_4,2,2 -X\_5,1,2 0
- X\_4,2,2 -X\_5,2,2 0
- X\_4,2,2 -X\_5,3,2 0
- X\_4,2,2 -X\_6,1,2 0
- X\_4,2,2 -X\_6,2,2 0
- X\_4,2,2 -X\_6,3,2 0
- X\_4,3,2 -X\_5,1,2 0
- X\_4,3,2 -X\_5,2,2 0
- X\_4,3,2 -X\_5,3,2 0
- X\_4,3,2 -X\_6,1,2 0
- X\_4,3,2 -X\_6,2,2 0
- X\_4,3,2 -X\_6,3,2 0
- X\_5,1,2 -X\_5,2,2 0
- X\_5,1,2 -X\_5,3,2 0
- X\_5,1,2 -X\_6,1,2 0
- X\_5,1,2 -X\_6,2,2 0
- X\_5,1,2 -X\_6,3,2 0
- X\_5,2,2 -X\_5,3,2 0
- X\_5,2,2 -X\_6,1,2 0
- X\_5,2,2 -X\_6,2,2 0
- X\_5,2,2 -X\_6,3,2 0
- X\_5,3,2 -X\_6,1,2 0
- X\_5,3,2 -X\_6,2,2 0
- X\_5,3,2 -X\_6,3,2 0
- X\_6,1,2 -X\_6,2,2 0
- X\_6,1,2 -X\_6,3,2 0
- X\_6,2,2 -X\_6,3,2 0

X\_4,4,2 X\_4,5,2 X\_4,6,2 X\_5,4,2 X\_5,5,2 X\_5,6,2 X\_6,4,2 X\_6,5,2 X\_6,6,2 0

- X\_4,4,2 -X\_4,5,2 0
- X\_4,4,2 -X\_4,6,2 0
- X\_4,4,2 -X\_5,4,2 0
- X\_4,4,2 -X\_5,5,2 0
- X\_4,4,2 -X\_5,6,2 0
- X\_4,4,2 -X\_6,4,2 0
- X\_4,4,2 -X\_6,5,2 0
- X\_4,4,2 -X\_6,6,2 0
- X\_4,5,2 -X\_4,6,2 0
- X\_4,5,2 -X\_5,4,2 0
- X\_4,5,2 -X\_5,5,2 0
- X\_4,5,2 -X\_5,6,2 0
- X\_4,5,2 -X\_6,4,2 0
- X\_4,5,2 -X\_6,5,2 0
- X\_4,5,2 -X\_6,6,2 0
- X\_4,6,2 -X\_5,4,2 0
- X\_4,6,2 -X\_5,5,2 0
- X\_4,6,2 -X\_5,6,2 0
- X\_4,6,2 -X\_6,4,2 0
- X\_4,6,2 -X\_6,5,2 0
- X\_4,6,2 -X\_6,6,2 0
- X\_5,4,2 -X\_5,5,2 0
- X\_5,4,2 -X\_5,6,2 0
- X\_5,4,2 -X\_6,4,2 0
- X\_5,4,2 -X\_6,5,2 0
- X\_5,4,2 -X\_6,6,2 0
- X\_5,5,2 -X\_5,6,2 0
- X\_5,5,2 -X\_6,4,2 0
- X\_5,5,2 -X\_6,5,2 0
- X\_5,5,2 -X\_6,6,2 0
- X\_5,6,2 -X\_6,4,2 0
- X\_5,6,2 -X\_6,5,2 0
- X\_5,6,2 -X\_6,6,2 0
- X\_6,4,2 -X\_6,5,2 0
- X\_6,4,2 -X\_6,6,2 0
- X\_6,5,2 -X\_6,6,2 0

X\_4,7,2 X\_4,8,2 X\_4,9,2 X\_5,7,2 X\_5,8,2 X\_5,9,2 X\_6,7,2 X\_6,8,2 X\_6,9,2 0

- X\_4,7,2 -X\_4,8,2 0
- X\_4,7,2 -X\_4,9,2 0
- X\_4,7,2 -X\_5,7,2 0
- X\_4,7,2 -X\_5,8,2 0
- X\_4,7,2 -X\_5,9,2 0
- X\_4,7,2 -X\_6,7,2 0
- X\_4,7,2 -X\_6,8,2 0
- X\_4,7,2 -X\_6,9,2 0
- X\_4,8,2 -X\_4,9,2 0
- X\_4,8,2 -X\_5,7,2 0
- X\_4,8,2 -X\_5,8,2 0
- X\_4,8,2 -X\_5,9,2 0
- X\_4,8,2 -X\_6,7,2 0
- X\_4,8,2 -X\_6,8,2 0
- X\_4,8,2 -X\_6,9,2 0
- X\_4,9,2 -X\_5,7,2 0
- X\_4,9,2 -X\_5,8,2 0
- X\_4,9,2 -X\_5,9,2 0
- X\_4,9,2 -X\_6,7,2 0
- X\_4,9,2 -X\_6,8,2 0
- X\_4,9,2 -X\_6,9,2 0
- X\_5,7,2 -X\_5,8,2 0
- X\_5,7,2 -X\_5,9,2 0
- X\_5,7,2 -X\_6,7,2 0
- X\_5,7,2 -X\_6,8,2 0
- X\_5,7,2 -X\_6,9,2 0
- X\_5,8,2 -X\_5,9,2 0
- X\_5,8,2 -X\_6,7,2 0
- X\_5,8,2 -X\_6,8,2 0
- X\_5,8,2 -X\_6,9,2 0
- X\_5,9,2 -X\_6,7,2 0
- X\_5,9,2 -X\_6,8,2 0
- X\_5,9,2 -X\_6,9,2 0
- X\_6,7,2 -X\_6,8,2 0
- X\_6,7,2 -X\_6,9,2 0
- X\_6,8,2 -X\_6,9,2 0

X\_7,1,2 X\_7,2,2 X\_7,3,2 X\_8,1,2 X\_8,2,2 X\_8,3,2 X\_9,1,2 X\_9,2,2 X\_9,3,2 0

- X\_7,1,2 -X\_7,2,2 0
- X\_7,1,2 -X\_7,3,2 0
- X\_7,1,2 -X\_8,1,2 0
- X\_7,1,2 -X\_8,2,2 0
- X\_7,1,2 -X\_8,3,2 0
- X\_7,1,2 -X\_9,1,2 0
- X\_7,1,2 -X\_9,2,2 0
- X\_7,1,2 -X\_9,3,2 0
- X\_7,2,2 -X\_7,3,2 0
- X\_7,2,2 -X\_8,1,2 0
- X\_7,2,2 -X\_8,2,2 0
- X\_7,2,2 -X\_8,3,2 0
- X\_7,2,2 -X\_9,1,2 0
- X\_7,2,2 -X\_9,2,2 0
- X\_7,2,2 -X\_9,3,2 0
- X\_7,3,2 -X\_8,1,2 0
- X\_7,3,2 -X\_8,2,2 0
- X\_7,3,2 -X\_8,3,2 0
- X\_7,3,2 -X\_9,1,2 0
- X\_7,3,2 -X\_9,2,2 0
- X\_7,3,2 -X\_9,3,2 0
- X\_8,1,2 -X\_8,2,2 0
- X\_8,1,2 -X\_8,3,2 0
- X\_8,1,2 -X\_9,1,2 0
- X\_8,1,2 -X\_9,2,2 0
- X\_8,1,2 -X\_9,3,2 0
- X\_8,2,2 -X\_8,3,2 0
- X\_8,2,2 -X\_9,1,2 0
- X\_8,2,2 -X\_9,2,2 0
- X\_8,2,2 -X\_9,3,2 0
- X\_8,3,2 -X\_9,1,2 0
- X\_8,3,2 -X\_9,2,2 0
- X\_8,3,2 -X\_9,3,2 0
- X\_9,1,2 -X\_9,2,2 0
- X\_9,1,2 -X\_9,3,2 0
- X\_9,2,2 -X\_9,3,2 0

X\_7,4,2 X\_7,5,2 X\_7,6,2 X\_8,4,2 X\_8,5,2 X\_8,6,2 X\_9,4,2 X\_9,5,2 X\_9,6,2 0

- X\_7,4,2 -X\_7,5,2 0
- X\_7,4,2 -X\_7,6,2 0
- X\_7,4,2 -X\_8,4,2 0
- X\_7,4,2 -X\_8,5,2 0
- X\_7,4,2 -X\_8,6,2 0
- X\_7,4,2 -X\_9,4,2 0
- X\_7,4,2 -X\_9,5,2 0
- X\_7,4,2 -X\_9,6,2 0
- X\_7,5,2 -X\_7,6,2 0
- X\_7,5,2 -X\_8,4,2 0
- X\_7,5,2 -X\_8,5,2 0
- X\_7,5,2 -X\_8,6,2 0
- X\_7,5,2 -X\_9,4,2 0
- X\_7,5,2 -X\_9,5,2 0
- X\_7,5,2 -X\_9,6,2 0
- X\_7,6,2 -X\_8,4,2 0
- X\_7,6,2 -X\_8,5,2 0
- X\_7,6,2 -X\_8,6,2 0
- X\_7,6,2 -X\_9,4,2 0
- X\_7,6,2 -X\_9,5,2 0
- X\_7,6,2 -X\_9,6,2 0
- X\_8,4,2 -X\_8,5,2 0
- X\_8,4,2 -X\_8,6,2 0
- X\_8,4,2 -X\_9,4,2 0
- X\_8,4,2 -X\_9,5,2 0
- X\_8,4,2 -X\_9,6,2 0
- X\_8,5,2 -X\_8,6,2 0
- X\_8,5,2 -X\_9,4,2 0
- X\_8,5,2 -X\_9,5,2 0
- X\_8,5,2 -X\_9,6,2 0
- X\_8,6,2 -X\_9,4,2 0
- X\_8,6,2 -X\_9,5,2 0
- X\_8,6,2 -X\_9,6,2 0
- X\_9,4,2 -X\_9,5,2 0
- X\_9,4,2 -X\_9,6,2 0
- X\_9,5,2 -X\_9,6,2 0

X\_7,7,2 X\_7,8,2 X\_7,9,2 X\_8,7,2 X\_8,8,2 X\_8,9,2 X\_9,7,2 X\_9,8,2 X\_9,9,2 0

- X\_7,7,2 -X\_7,8,2 0
- X\_7,7,2 -X\_7,9,2 0
- X\_7,7,2 -X\_8,7,2 0
- X\_7,7,2 -X\_8,8,2 0
- X\_7,7,2 -X\_8,9,2 0
- X\_7,7,2 -X\_9,7,2 0
- X\_7,7,2 -X\_9,8,2 0
- X\_7,7,2 -X\_9,9,2 0
- X\_7,8,2 -X\_7,9,2 0
- X\_7,8,2 -X\_8,7,2 0
- X\_7,8,2 -X\_8,8,2 0
- X\_7,8,2 -X\_8,9,2 0
- X\_7,8,2 -X\_9,7,2 0
- X\_7,8,2 -X\_9,8,2 0
- X\_7,8,2 -X\_9,9,2 0
- X\_7,9,2 -X\_8,7,2 0
- X\_7,9,2 -X\_8,8,2 0
- X\_7,9,2 -X\_8,9,2 0
- X\_7,9,2 -X\_9,7,2 0
- X\_7,9,2 -X\_9,8,2 0
- X\_7,9,2 -X\_9,9,2 0
- X\_8,7,2 -X\_8,8,2 0
- X\_8,7,2 -X\_8,9,2 0
- X\_8,7,2 -X\_9,7,2 0
- X\_8,7,2 -X\_9,8,2 0
- X\_8,7,2 -X\_9,9,2 0
- X\_8,8,2 -X\_8,9,2 0
- X\_8,8,2 -X\_9,7,2 0
- X\_8,8,2 -X\_9,8,2 0
- X\_8,8,2 -X\_9,9,2 0
- X\_8,9,2 -X\_9,7,2 0
- X\_8,9,2 -X\_9,8,2 0
- X\_8,9,2 -X\_9,9,2 0
- X\_9,7,2 -X\_9,8,2 0
- X\_9,7,2 -X\_9,9,2 0
- X\_9,8,2 -X\_9,9,2 0

X\_1,1,3 X\_1,2,3 X\_1,3,3 X\_2,1,3 X\_2,2,3 X\_2,3,3 X\_3,1,3 X\_3,2,3 X\_3,3,3 0

- X\_1,1,3 -X\_1,2,3 0
- X\_1,1,3 -X\_1,3,3 0
- X\_1,1,3 -X\_2,1,3 0
- X\_1,1,3 -X\_2,2,3 0
- X\_1,1,3 -X\_2,3,3 0
- X\_1,1,3 -X\_3,1,3 0
- X\_1,1,3 -X\_3,2,3 0
- X\_1,1,3 -X\_3,3,3 0
- X\_1,2,3 -X\_1,3,3 0
- X\_1,2,3 -X\_2,1,3 0
- X\_1,2,3 -X\_2,2,3 0
- X\_1,2,3 -X\_2,3,3 0
- X\_1,2,3 -X\_3,1,3 0
- X\_1,2,3 -X\_3,2,3 0
- X\_1,2,3 -X\_3,3,3 0
- X\_1,3,3 -X\_2,1,3 0
- X\_1,3,3 -X\_2,2,3 0
- X\_1,3,3 -X\_2,3,3 0
- X\_1,3,3 -X\_3,1,3 0
- X\_1,3,3 -X\_3,2,3 0
- X\_1,3,3 -X\_3,3,3 0
- X\_2,1,3 -X\_2,2,3 0
- X\_2,1,3 -X\_2,3,3 0
- X\_2,1,3 -X\_3,1,3 0
- X\_2,1,3 -X\_3,2,3 0
- X\_2,1,3 -X\_3,3,3 0
- X\_2,2,3 -X\_2,3,3 0
- X\_2,2,3 -X\_3,1,3 0
- X\_2,2,3 -X\_3,2,3 0
- X\_2,2,3 -X\_3,3,3 0
- X\_2,3,3 -X\_3,1,3 0
- X\_2,3,3 -X\_3,2,3 0
- X\_2,3,3 -X\_3,3,3 0
- X\_3,1,3 -X\_3,2,3 0
- X\_3,1,3 -X\_3,3,3 0
- X\_3,2,3 -X\_3,3,3 0

X\_1,4,3 X\_1,5,3 X\_1,6,3 X\_2,4,3 X\_2,5,3 X\_2,6,3 X\_3,4,3 X\_3,5,3 X\_3,6,3 0

- X\_1,4,3 -X\_1,5,3 0
- X\_1,4,3 -X\_1,6,3 0
- X\_1,4,3 -X\_2,4,3 0
- X\_1,4,3 -X\_2,5,3 0
- X\_1,4,3 -X\_2,6,3 0
- X\_1,4,3 -X\_3,4,3 0
- X\_1,4,3 -X\_3,5,3 0
- X\_1,4,3 -X\_3,6,3 0
- X\_1,5,3 -X\_1,6,3 0
- X\_1,5,3 -X\_2,4,3 0
- X\_1,5,3 -X\_2,5,3 0
- X\_1,5,3 -X\_2,6,3 0
- X\_1,5,3 -X\_3,4,3 0
- X\_1,5,3 -X\_3,5,3 0
- X\_1,5,3 -X\_3,6,3 0
- X\_1,6,3 -X\_2,4,3 0
- X\_1,6,3 -X\_2,5,3 0
- X\_1,6,3 -X\_2,6,3 0
- X\_1,6,3 -X\_3,4,3 0
- X\_1,6,3 -X\_3,5,3 0
- X\_1,6,3 -X\_3,6,3 0
- X\_2,4,3 -X\_2,5,3 0
- X\_2,4,3 -X\_2,6,3 0
- X\_2,4,3 -X\_3,4,3 0
- X\_2,4,3 -X\_3,5,3 0
- X\_2,4,3 -X\_3,6,3 0
- X\_2,5,3 -X\_2,6,3 0
- X\_2,5,3 -X\_3,4,3 0
- X\_2,5,3 -X\_3,5,3 0
- X\_2,5,3 -X\_3,6,3 0
- X\_2,6,3 -X\_3,4,3 0
- X\_2,6,3 -X\_3,5,3 0
- X\_2,6,3 -X\_3,6,3 0
- X\_3,4,3 -X\_3,5,3 0
- X\_3,4,3 -X\_3,6,3 0
- X\_3,5,3 -X\_3,6,3 0

X\_1,7,3 X\_1,8,3 X\_1,9,3 X\_2,7,3 X\_2,8,3 X\_2,9,3 X\_3,7,3 X\_3,8,3 X\_3,9,3 0

- X\_1,7,3 -X\_1,8,3 0
- X\_1,7,3 -X\_1,9,3 0
- X\_1,7,3 -X\_2,7,3 0
- X\_1,7,3 -X\_2,8,3 0
- X\_1,7,3 -X\_2,9,3 0
- X\_1,7,3 -X\_3,7,3 0
- X\_1,7,3 -X\_3,8,3 0
- X\_1,7,3 -X\_3,9,3 0
- X\_1,8,3 -X\_1,9,3 0
- X\_1,8,3 -X\_2,7,3 0
- X\_1,8,3 -X\_2,8,3 0
- X\_1,8,3 -X\_2,9,3 0
- X\_1,8,3 -X\_3,7,3 0
- X\_1,8,3 -X\_3,8,3 0
- X\_1,8,3 -X\_3,9,3 0
- X\_1,9,3 -X\_2,7,3 0
- X\_1,9,3 -X\_2,8,3 0
- X\_1,9,3 -X\_2,9,3 0
- X\_1,9,3 -X\_3,7,3 0
- X\_1,9,3 -X\_3,8,3 0
- X\_1,9,3 -X\_3,9,3 0
- X\_2,7,3 -X\_2,8,3 0
- X\_2,7,3 -X\_2,9,3 0
- X\_2,7,3 -X\_3,7,3 0
- X\_2,7,3 -X\_3,8,3 0
- X\_2,7,3 -X\_3,9,3 0
- X\_2,8,3 -X\_2,9,3 0
- X\_2,8,3 -X\_3,7,3 0
- X\_2,8,3 -X\_3,8,3 0
- X\_2,8,3 -X\_3,9,3 0
- X\_2,9,3 -X\_3,7,3 0
- X\_2,9,3 -X\_3,8,3 0
- X\_2,9,3 -X\_3,9,3 0
- X\_3,7,3 -X\_3,8,3 0
- X\_3,7,3 -X\_3,9,3 0
- X\_3,8,3 -X\_3,9,3 0

X\_4,1,3 X\_4,2,3 X\_4,3,3 X\_5,1,3 X\_5,2,3 X\_5,3,3 X\_6,1,3 X\_6,2,3 X\_6,3,3 0

- X\_4,1,3 -X\_4,2,3 0
- X\_4,1,3 -X\_4,3,3 0
- X\_4,1,3 -X\_5,1,3 0
- X\_4,1,3 -X\_5,2,3 0
- X\_4,1,3 -X\_5,3,3 0
- X\_4,1,3 -X\_6,1,3 0
- X\_4,1,3 -X\_6,2,3 0
- X\_4,1,3 -X\_6,3,3 0
- X\_4,2,3 -X\_4,3,3 0
- X\_4,2,3 -X\_5,1,3 0
- X\_4,2,3 -X\_5,2,3 0
- X\_4,2,3 -X\_5,3,3 0
- X\_4,2,3 -X\_6,1,3 0
- X\_4,2,3 -X\_6,2,3 0
- X\_4,2,3 -X\_6,3,3 0
- X\_4,3,3 -X\_5,1,3 0
- X\_4,3,3 -X\_5,2,3 0
- X\_4,3,3 -X\_5,3,3 0
- X\_4,3,3 -X\_6,1,3 0
- X\_4,3,3 -X\_6,2,3 0
- X\_4,3,3 -X\_6,3,3 0
- X\_5,1,3 -X\_5,2,3 0
- X\_5,1,3 -X\_5,3,3 0
- X\_5,1,3 -X\_6,1,3 0
- X\_5,1,3 -X\_6,2,3 0
- X\_5,1,3 -X\_6,3,3 0
- X\_5,2,3 -X\_5,3,3 0
- X\_5,2,3 -X\_6,1,3 0
- X\_5,2,3 -X\_6,2,3 0
- X\_5,2,3 -X\_6,3,3 0
- X\_5,3,3 -X\_6,1,3 0
- X\_5,3,3 -X\_6,2,3 0
- X\_5,3,3 -X\_6,3,3 0
- X\_6,1,3 -X\_6,2,3 0
- X\_6,1,3 -X\_6,3,3 0
- X\_6,2,3 -X\_6,3,3 0

X\_4,4,3 X\_4,5,3 X\_4,6,3 X\_5,4,3 X\_5,5,3 X\_5,6,3 X\_6,4,3 X\_6,5,3 X\_6,6,3 0

- X\_4,4,3 -X\_4,5,3 0
- X\_4,4,3 -X\_4,6,3 0
- X\_4,4,3 -X\_5,4,3 0
- X\_4,4,3 -X\_5,5,3 0
- X\_4,4,3 -X\_5,6,3 0
- X\_4,4,3 -X\_6,4,3 0
- X\_4,4,3 -X\_6,5,3 0
- X\_4,4,3 -X\_6,6,3 0
- X\_4,5,3 -X\_4,6,3 0
- X\_4,5,3 -X\_5,4,3 0
- X\_4,5,3 -X\_5,5,3 0
- X\_4,5,3 -X\_5,6,3 0
- X\_4,5,3 -X\_6,4,3 0
- X\_4,5,3 -X\_6,5,3 0
- X\_4,5,3 -X\_6,6,3 0
- X\_4,6,3 -X\_5,4,3 0
- X\_4,6,3 -X\_5,5,3 0
- X\_4,6,3 -X\_5,6,3 0
- X\_4,6,3 -X\_6,4,3 0
- X\_4,6,3 -X\_6,5,3 0
- X\_4,6,3 -X\_6,6,3 0
- X\_5,4,3 -X\_5,5,3 0
- X\_5,4,3 -X\_5,6,3 0
- X\_5,4,3 -X\_6,4,3 0
- X\_5,4,3 -X\_6,5,3 0
- X\_5,4,3 -X\_6,6,3 0
- X\_5,5,3 -X\_5,6,3 0
- X\_5,5,3 -X\_6,4,3 0
- X\_5,5,3 -X\_6,5,3 0
- X\_5,5,3 -X\_6,6,3 0
- X\_5,6,3 -X\_6,4,3 0
- X\_5,6,3 -X\_6,5,3 0
- X\_5,6,3 -X\_6,6,3 0
- X\_6,4,3 -X\_6,5,3 0
- X\_6,4,3 -X\_6,6,3 0
- X\_6,5,3 -X\_6,6,3 0

X\_4,7,3 X\_4,8,3 X\_4,9,3 X\_5,7,3 X\_5,8,3 X\_5,9,3 X\_6,7,3 X\_6,8,3 X\_6,9,3 0

- X\_4,7,3 -X\_4,8,3 0
- X\_4,7,3 -X\_4,9,3 0
- X\_4,7,3 -X\_5,7,3 0
- X\_4,7,3 -X\_5,8,3 0
- X\_4,7,3 -X\_5,9,3 0
- X\_4,7,3 -X\_6,7,3 0
- X\_4,7,3 -X\_6,8,3 0
- X\_4,7,3 -X\_6,9,3 0
- X\_4,8,3 -X\_4,9,3 0
- X\_4,8,3 -X\_5,7,3 0
- X\_4,8,3 -X\_5,8,3 0
- X\_4,8,3 -X\_5,9,3 0
- X\_4,8,3 -X\_6,7,3 0
- X\_4,8,3 -X\_6,8,3 0
- X\_4,8,3 -X\_6,9,3 0
- X\_4,9,3 -X\_5,7,3 0
- X\_4,9,3 -X\_5,8,3 0
- X\_4,9,3 -X\_5,9,3 0
- X\_4,9,3 -X\_6,7,3 0
- X\_4,9,3 -X\_6,8,3 0
- X\_4,9,3 -X\_6,9,3 0
- X\_5,7,3 -X\_5,8,3 0
- X\_5,7,3 -X\_5,9,3 0
- X\_5,7,3 -X\_6,7,3 0
- X\_5,7,3 -X\_6,8,3 0
- X\_5,7,3 -X\_6,9,3 0
- X\_5,8,3 -X\_5,9,3 0
- X\_5,8,3 -X\_6,7,3 0
- X\_5,8,3 -X\_6,8,3 0
- X\_5,8,3 -X\_6,9,3 0
- X\_5,9,3 -X\_6,7,3 0
- X\_5,9,3 -X\_6,8,3 0
- X\_5,9,3 -X\_6,9,3 0
- X\_6,7,3 -X\_6,8,3 0
- X\_6,7,3 -X\_6,9,3 0
- X\_6,8,3 -X\_6,9,3 0

X\_7,1,3 X\_7,2,3 X\_7,3,3 X\_8,1,3 X\_8,2,3 X\_8,3,3 X\_9,1,3 X\_9,2,3 X\_9,3,3 0

- X\_7,1,3 -X\_7,2,3 0
- X\_7,1,3 -X\_7,3,3 0
- X\_7,1,3 -X\_8,1,3 0
- X\_7,1,3 -X\_8,2,3 0
- X\_7,1,3 -X\_8,3,3 0
- X\_7,1,3 -X\_9,1,3 0
- X\_7,1,3 -X\_9,2,3 0
- X\_7,1,3 -X\_9,3,3 0
- X\_7,2,3 -X\_7,3,3 0
- X\_7,2,3 -X\_8,1,3 0
- X\_7,2,3 -X\_8,2,3 0
- X\_7,2,3 -X\_8,3,3 0
- X\_7,2,3 -X\_9,1,3 0
- X\_7,2,3 -X\_9,2,3 0
- X\_7,2,3 -X\_9,3,3 0
- X\_7,3,3 -X\_8,1,3 0
- X\_7,3,3 -X\_8,2,3 0
- X\_7,3,3 -X\_8,3,3 0
- X\_7,3,3 -X\_9,1,3 0
- X\_7,3,3 -X\_9,2,3 0
- X\_7,3,3 -X\_9,3,3 0
- X\_8,1,3 -X\_8,2,3 0
- X\_8,1,3 -X\_8,3,3 0
- X\_8,1,3 -X\_9,1,3 0
- X\_8,1,3 -X\_9,2,3 0
- X\_8,1,3 -X\_9,3,3 0
- X\_8,2,3 -X\_8,3,3 0
- X\_8,2,3 -X\_9,1,3 0
- X\_8,2,3 -X\_9,2,3 0
- X\_8,2,3 -X\_9,3,3 0
- X\_8,3,3 -X\_9,1,3 0
- X\_8,3,3 -X\_9,2,3 0
- X\_8,3,3 -X\_9,3,3 0
- X\_9,1,3 -X\_9,2,3 0
- X\_9,1,3 -X\_9,3,3 0
- X\_9,2,3 -X\_9,3,3 0

X\_7,4,3 X\_7,5,3 X\_7,6,3 X\_8,4,3 X\_8,5,3 X\_8,6,3 X\_9,4,3 X\_9,5,3 X\_9,6,3 0

- X\_7,4,3 -X\_7,5,3 0
- X\_7,4,3 -X\_7,6,3 0
- X\_7,4,3 -X\_8,4,3 0
- X\_7,4,3 -X\_8,5,3 0
- X\_7,4,3 -X\_8,6,3 0
- X\_7,4,3 -X\_9,4,3 0
- X\_7,4,3 -X\_9,5,3 0
- X\_7,4,3 -X\_9,6,3 0
- X\_7,5,3 -X\_7,6,3 0
- X\_7,5,3 -X\_8,4,3 0
- X\_7,5,3 -X\_8,5,3 0
- X\_7,5,3 -X\_8,6,3 0
- X\_7,5,3 -X\_9,4,3 0
- X\_7,5,3 -X\_9,5,3 0
- X\_7,5,3 -X\_9,6,3 0
- X\_7,6,3 -X\_8,4,3 0
- X\_7,6,3 -X\_8,5,3 0
- X\_7,6,3 -X\_8,6,3 0
- X\_7,6,3 -X\_9,4,3 0
- X\_7,6,3 -X\_9,5,3 0
- X\_7,6,3 -X\_9,6,3 0
- X\_8,4,3 -X\_8,5,3 0
- X\_8,4,3 -X\_8,6,3 0
- X\_8,4,3 -X\_9,4,3 0
- X\_8,4,3 -X\_9,5,3 0
- X\_8,4,3 -X\_9,6,3 0
- X\_8,5,3 -X\_8,6,3 0
- X\_8,5,3 -X\_9,4,3 0
- X\_8,5,3 -X\_9,5,3 0
- X\_8,5,3 -X\_9,6,3 0
- X\_8,6,3 -X\_9,4,3 0
- X\_8,6,3 -X\_9,5,3 0
- X\_8,6,3 -X\_9,6,3 0
- X\_9,4,3 -X\_9,5,3 0
- X\_9,4,3 -X\_9,6,3 0
- X\_9,5,3 -X\_9,6,3 0

X\_7,7,3 X\_7,8,3 X\_7,9,3 X\_8,7,3 X\_8,8,3 X\_8,9,3 X\_9,7,3 X\_9,8,3 X\_9,9,3 0

- X\_7,7,3 -X\_7,8,3 0
- X\_7,7,3 -X\_7,9,3 0
- X\_7,7,3 -X\_8,7,3 0
- X\_7,7,3 -X\_8,8,3 0
- X\_7,7,3 -X\_8,9,3 0
- X\_7,7,3 -X\_9,7,3 0
- X\_7,7,3 -X\_9,8,3 0
- X\_7,7,3 -X\_9,9,3 0
- X\_7,8,3 -X\_7,9,3 0
- X\_7,8,3 -X\_8,7,3 0
- X\_7,8,3 -X\_8,8,3 0
- X\_7,8,3 -X\_8,9,3 0
- X\_7,8,3 -X\_9,7,3 0
- X\_7,8,3 -X\_9,8,3 0
- X\_7,8,3 -X\_9,9,3 0
- X\_7,9,3 -X\_8,7,3 0
- X\_7,9,3 -X\_8,8,3 0
- X\_7,9,3 -X\_8,9,3 0
- X\_7,9,3 -X\_9,7,3 0
- X\_7,9,3 -X\_9,8,3 0
- X\_7,9,3 -X\_9,9,3 0
- X\_8,7,3 -X\_8,8,3 0
- X\_8,7,3 -X\_8,9,3 0
- X\_8,7,3 -X\_9,7,3 0
- X\_8,7,3 -X\_9,8,3 0
- X\_8,7,3 -X\_9,9,3 0
- X\_8,8,3 -X\_8,9,3 0
- X\_8,8,3 -X\_9,7,3 0
- X\_8,8,3 -X\_9,8,3 0
- X\_8,8,3 -X\_9,9,3 0
- X\_8,9,3 -X\_9,7,3 0
- X\_8,9,3 -X\_9,8,3 0
- X\_8,9,3 -X\_9,9,3 0
- X\_9,7,3 -X\_9,8,3 0
- X\_9,7,3 -X\_9,9,3 0
- X\_9,8,3 -X\_9,9,3 0

X\_1,1,4 X\_1,2,4 X\_1,3,4 X\_2,1,4 X\_2,2,4 X\_2,3,4 X\_3,1,4 X\_3,2,4 X\_3,3,4 0

- X\_1,1,4 -X\_1,2,4 0
- X\_1,1,4 -X\_1,3,4 0
- X\_1,1,4 -X\_2,1,4 0
- X\_1,1,4 -X\_2,2,4 0
- X\_1,1,4 -X\_2,3,4 0
- X\_1,1,4 -X\_3,1,4 0
- X\_1,1,4 -X\_3,2,4 0
- X\_1,1,4 -X\_3,3,4 0
- X\_1,2,4 -X\_1,3,4 0
- X\_1,2,4 -X\_2,1,4 0
- X\_1,2,4 -X\_2,2,4 0
- X\_1,2,4 -X\_2,3,4 0
- X\_1,2,4 -X\_3,1,4 0
- X\_1,2,4 -X\_3,2,4 0
- X\_1,2,4 -X\_3,3,4 0
- X\_1,3,4 -X\_2,1,4 0
- X\_1,3,4 -X\_2,2,4 0
- X\_1,3,4 -X\_2,3,4 0
- X\_1,3,4 -X\_3,1,4 0
- X\_1,3,4 -X\_3,2,4 0
- X\_1,3,4 -X\_3,3,4 0
- X\_2,1,4 -X\_2,2,4 0
- X\_2,1,4 -X\_2,3,4 0
- X\_2,1,4 -X\_3,1,4 0
- X\_2,1,4 -X\_3,2,4 0
- X\_2,1,4 -X\_3,3,4 0
- X\_2,2,4 -X\_2,3,4 0
- X\_2,2,4 -X\_3,1,4 0
- X\_2,2,4 -X\_3,2,4 0
- X\_2,2,4 -X\_3,3,4 0
- X\_2,3,4 -X\_3,1,4 0
- X\_2,3,4 -X\_3,2,4 0
- X\_2,3,4 -X\_3,3,4 0
- X\_3,1,4 -X\_3,2,4 0
- X\_3,1,4 -X\_3,3,4 0
- X\_3,2,4 -X\_3,3,4 0

X\_1,4,4 X\_1,5,4 X\_1,6,4 X\_2,4,4 X\_2,5,4 X\_2,6,4 X\_3,4,4 X\_3,5,4 X\_3,6,4 0

- X\_1,4,4 -X\_1,5,4 0
- X\_1,4,4 -X\_1,6,4 0
- X\_1,4,4 -X\_2,4,4 0
- X\_1,4,4 -X\_2,5,4 0
- X\_1,4,4 -X\_2,6,4 0
- X\_1,4,4 -X\_3,4,4 0
- X\_1,4,4 -X\_3,5,4 0
- X\_1,4,4 -X\_3,6,4 0
- X\_1,5,4 -X\_1,6,4 0
- X\_1,5,4 -X\_2,4,4 0
- X\_1,5,4 -X\_2,5,4 0
- X\_1,5,4 -X\_2,6,4 0
- X\_1,5,4 -X\_3,4,4 0
- X\_1,5,4 -X\_3,5,4 0
- X\_1,5,4 -X\_3,6,4 0
- X\_1,6,4 -X\_2,4,4 0
- X\_1,6,4 -X\_2,5,4 0
- X\_1,6,4 -X\_2,6,4 0
- X\_1,6,4 -X\_3,4,4 0
- X\_1,6,4 -X\_3,5,4 0
- X\_1,6,4 -X\_3,6,4 0
- X\_2,4,4 -X\_2,5,4 0
- X\_2,4,4 -X\_2,6,4 0
- X\_2,4,4 -X\_3,4,4 0
- X\_2,4,4 -X\_3,5,4 0
- X\_2,4,4 -X\_3,6,4 0
- X\_2,5,4 -X\_2,6,4 0
- X\_2,5,4 -X\_3,4,4 0
- X\_2,5,4 -X\_3,5,4 0
- X\_2,5,4 -X\_3,6,4 0
- X\_2,6,4 -X\_3,4,4 0
- X\_2,6,4 -X\_3,5,4 0
- X\_2,6,4 -X\_3,6,4 0
- X\_3,4,4 -X\_3,5,4 0
- X\_3,4,4 -X\_3,6,4 0
- X\_3,5,4 -X\_3,6,4 0

X\_1,7,4 X\_1,8,4 X\_1,9,4 X\_2,7,4 X\_2,8,4 X\_2,9,4 X\_3,7,4 X\_3,8,4 X\_3,9,4 0

- X\_1,7,4 -X\_1,8,4 0
- X\_1,7,4 -X\_1,9,4 0
- X\_1,7,4 -X\_2,7,4 0
- X\_1,7,4 -X\_2,8,4 0
- X\_1,7,4 -X\_2,9,4 0
- X\_1,7,4 -X\_3,7,4 0
- X\_1,7,4 -X\_3,8,4 0
- X\_1,7,4 -X\_3,9,4 0
- X\_1,8,4 -X\_1,9,4 0
- X\_1,8,4 -X\_2,7,4 0
- X\_1,8,4 -X\_2,8,4 0
- X\_1,8,4 -X\_2,9,4 0
- X\_1,8,4 -X\_3,7,4 0
- X\_1,8,4 -X\_3,8,4 0
- X\_1,8,4 -X\_3,9,4 0
- X\_1,9,4 -X\_2,7,4 0
- X\_1,9,4 -X\_2,8,4 0
- X\_1,9,4 -X\_2,9,4 0
- X\_1,9,4 -X\_3,7,4 0
- X\_1,9,4 -X\_3,8,4 0
- X\_1,9,4 -X\_3,9,4 0
- X\_2,7,4 -X\_2,8,4 0
- X\_2,7,4 -X\_2,9,4 0
- X\_2,7,4 -X\_3,7,4 0
- X\_2,7,4 -X\_3,8,4 0
- X\_2,7,4 -X\_3,9,4 0
- X\_2,8,4 -X\_2,9,4 0
- X\_2,8,4 -X\_3,7,4 0
- X\_2,8,4 -X\_3,8,4 0
- X\_2,8,4 -X\_3,9,4 0
- X\_2,9,4 -X\_3,7,4 0
- X\_2,9,4 -X\_3,8,4 0
- X\_2,9,4 -X\_3,9,4 0
- X\_3,7,4 -X\_3,8,4 0
- X\_3,7,4 -X\_3,9,4 0
- X\_3,8,4 -X\_3,9,4 0

X\_4,1,4 X\_4,2,4 X\_4,3,4 X\_5,1,4 X\_5,2,4 X\_5,3,4 X\_6,1,4 X\_6,2,4 X\_6,3,4 0

- X\_4,1,4 -X\_4,2,4 0
- X\_4,1,4 -X\_4,3,4 0
- X\_4,1,4 -X\_5,1,4 0
- X\_4,1,4 -X\_5,2,4 0
- X\_4,1,4 -X\_5,3,4 0
- X\_4,1,4 -X\_6,1,4 0
- X\_4,1,4 -X\_6,2,4 0
- X\_4,1,4 -X\_6,3,4 0
- X\_4,2,4 -X\_4,3,4 0
- X\_4,2,4 -X\_5,1,4 0
- X\_4,2,4 -X\_5,2,4 0
- X\_4,2,4 -X\_5,3,4 0
- X\_4,2,4 -X\_6,1,4 0
- X\_4,2,4 -X\_6,2,4 0
- X\_4,2,4 -X\_6,3,4 0
- X\_4,3,4 -X\_5,1,4 0
- X\_4,3,4 -X\_5,2,4 0
- X\_4,3,4 -X\_5,3,4 0
- X\_4,3,4 -X\_6,1,4 0
- X\_4,3,4 -X\_6,2,4 0
- X\_4,3,4 -X\_6,3,4 0
- X\_5,1,4 -X\_5,2,4 0
- X\_5,1,4 -X\_5,3,4 0
- X\_5,1,4 -X\_6,1,4 0
- X\_5,1,4 -X\_6,2,4 0
- X\_5,1,4 -X\_6,3,4 0
- X\_5,2,4 -X\_5,3,4 0
- X\_5,2,4 -X\_6,1,4 0
- X\_5,2,4 -X\_6,2,4 0
- X\_5,2,4 -X\_6,3,4 0
- X\_5,3,4 -X\_6,1,4 0
- X\_5,3,4 -X\_6,2,4 0
- X\_5,3,4 -X\_6,3,4 0
- X\_6,1,4 -X\_6,2,4 0
- X\_6,1,4 -X\_6,3,4 0
- X\_6,2,4 -X\_6,3,4 0

X\_4,4,4 X\_4,5,4 X\_4,6,4 X\_5,4,4 X\_5,5,4 X\_5,6,4 X\_6,4,4 X\_6,5,4 X\_6,6,4 0

- X\_4,4,4 -X\_4,5,4 0
- X\_4,4,4 -X\_4,6,4 0
- X\_4,4,4 -X\_5,4,4 0
- X\_4,4,4 -X\_5,5,4 0
- X\_4,4,4 -X\_5,6,4 0
- X\_4,4,4 -X\_6,4,4 0
- X\_4,4,4 -X\_6,5,4 0
- X\_4,4,4 -X\_6,6,4 0
- X\_4,5,4 -X\_4,6,4 0
- X\_4,5,4 -X\_5,4,4 0
- X\_4,5,4 -X\_5,5,4 0
- X\_4,5,4 -X\_5,6,4 0
- X\_4,5,4 -X\_6,4,4 0
- X\_4,5,4 -X\_6,5,4 0
- X\_4,5,4 -X\_6,6,4 0
- X\_4,6,4 -X\_5,4,4 0
- X\_4,6,4 -X\_5,5,4 0
- X\_4,6,4 -X\_5,6,4 0
- X\_4,6,4 -X\_6,4,4 0
- X\_4,6,4 -X\_6,5,4 0
- X\_4,6,4 -X\_6,6,4 0
- X\_5,4,4 -X\_5,5,4 0
- X\_5,4,4 -X\_5,6,4 0
- X\_5,4,4 -X\_6,4,4 0
- X\_5,4,4 -X\_6,5,4 0
- X\_5,4,4 -X\_6,6,4 0
- X\_5,5,4 -X\_5,6,4 0
- X\_5,5,4 -X\_6,4,4 0
- X\_5,5,4 -X\_6,5,4 0
- X\_5,5,4 -X\_6,6,4 0
- X\_5,6,4 -X\_6,4,4 0
- X\_5,6,4 -X\_6,5,4 0
- X\_5,6,4 -X\_6,6,4 0
- X\_6,4,4 -X\_6,5,4 0
- X\_6,4,4 -X\_6,6,4 0
- X\_6,5,4 -X\_6,6,4 0

X\_4,7,4 X\_4,8,4 X\_4,9,4 X\_5,7,4 X\_5,8,4 X\_5,9,4 X\_6,7,4 X\_6,8,4 X\_6,9,4 0

- X\_4,7,4 -X\_4,8,4 0
- X\_4,7,4 -X\_4,9,4 0
- X\_4,7,4 -X\_5,7,4 0
- X\_4,7,4 -X\_5,8,4 0
- X\_4,7,4 -X\_5,9,4 0
- X\_4,7,4 -X\_6,7,4 0
- X\_4,7,4 -X\_6,8,4 0
- X\_4,7,4 -X\_6,9,4 0
- X\_4,8,4 -X\_4,9,4 0
- X\_4,8,4 -X\_5,7,4 0
- X\_4,8,4 -X\_5,8,4 0
- X\_4,8,4 -X\_5,9,4 0
- X\_4,8,4 -X\_6,7,4 0
- X\_4,8,4 -X\_6,8,4 0
- X\_4,8,4 -X\_6,9,4 0
- X\_4,9,4 -X\_5,7,4 0
- X\_4,9,4 -X\_5,8,4 0
- X\_4,9,4 -X\_5,9,4 0
- X\_4,9,4 -X\_6,7,4 0
- X\_4,9,4 -X\_6,8,4 0
- X\_4,9,4 -X\_6,9,4 0
- X\_5,7,4 -X\_5,8,4 0
- X\_5,7,4 -X\_5,9,4 0
- X\_5,7,4 -X\_6,7,4 0
- X\_5,7,4 -X\_6,8,4 0
- X\_5,7,4 -X\_6,9,4 0
- X\_5,8,4 -X\_5,9,4 0
- X\_5,8,4 -X\_6,7,4 0
- X\_5,8,4 -X\_6,8,4 0
- X\_5,8,4 -X\_6,9,4 0
- X\_5,9,4 -X\_6,7,4 0
- X\_5,9,4 -X\_6,8,4 0
- X\_5,9,4 -X\_6,9,4 0
- X\_6,7,4 -X\_6,8,4 0
- X\_6,7,4 -X\_6,9,4 0
- X\_6,8,4 -X\_6,9,4 0

X\_7,1,4 X\_7,2,4 X\_7,3,4 X\_8,1,4 X\_8,2,4 X\_8,3,4 X\_9,1,4 X\_9,2,4 X\_9,3,4 0

- X\_7,1,4 -X\_7,2,4 0
- X\_7,1,4 -X\_7,3,4 0
- X\_7,1,4 -X\_8,1,4 0
- X\_7,1,4 -X\_8,2,4 0
- X\_7,1,4 -X\_8,3,4 0
- X\_7,1,4 -X\_9,1,4 0
- X\_7,1,4 -X\_9,2,4 0
- X\_7,1,4 -X\_9,3,4 0
- X\_7,2,4 -X\_7,3,4 0
- X\_7,2,4 -X\_8,1,4 0
- X\_7,2,4 -X\_8,2,4 0
- X\_7,2,4 -X\_8,3,4 0
- X\_7,2,4 -X\_9,1,4 0
- X\_7,2,4 -X\_9,2,4 0
- X\_7,2,4 -X\_9,3,4 0
- X\_7,3,4 -X\_8,1,4 0
- X\_7,3,4 -X\_8,2,4 0
- X\_7,3,4 -X\_8,3,4 0
- X\_7,3,4 -X\_9,1,4 0
- X\_7,3,4 -X\_9,2,4 0
- X\_7,3,4 -X\_9,3,4 0
- X\_8,1,4 -X\_8,2,4 0
- X\_8,1,4 -X\_8,3,4 0
- X\_8,1,4 -X\_9,1,4 0
- X\_8,1,4 -X\_9,2,4 0
- X\_8,1,4 -X\_9,3,4 0
- X\_8,2,4 -X\_8,3,4 0
- X\_8,2,4 -X\_9,1,4 0
- X\_8,2,4 -X\_9,2,4 0
- X\_8,2,4 -X\_9,3,4 0
- X\_8,3,4 -X\_9,1,4 0
- X\_8,3,4 -X\_9,2,4 0
- X\_8,3,4 -X\_9,3,4 0
- X\_9,1,4 -X\_9,2,4 0
- X\_9,1,4 -X\_9,3,4 0
- X\_9,2,4 -X\_9,3,4 0

X\_7,4,4 X\_7,5,4 X\_7,6,4 X\_8,4,4 X\_8,5,4 X\_8,6,4 X\_9,4,4 X\_9,5,4 X\_9,6,4 0

- X\_7,4,4 -X\_7,5,4 0
- X\_7,4,4 -X\_7,6,4 0
- X\_7,4,4 -X\_8,4,4 0
- X\_7,4,4 -X\_8,5,4 0
- X\_7,4,4 -X\_8,6,4 0
- X\_7,4,4 -X\_9,4,4 0
- X\_7,4,4 -X\_9,5,4 0
- X\_7,4,4 -X\_9,6,4 0
- X\_7,5,4 -X\_7,6,4 0
- X\_7,5,4 -X\_8,4,4 0
- X\_7,5,4 -X\_8,5,4 0
- X\_7,5,4 -X\_8,6,4 0
- X\_7,5,4 -X\_9,4,4 0
- X\_7,5,4 -X\_9,5,4 0
- X\_7,5,4 -X\_9,6,4 0
- X\_7,6,4 -X\_8,4,4 0
- X\_7,6,4 -X\_8,5,4 0
- X\_7,6,4 -X\_8,6,4 0
- X\_7,6,4 -X\_9,4,4 0
- X\_7,6,4 -X\_9,5,4 0
- X\_7,6,4 -X\_9,6,4 0
- X\_8,4,4 -X\_8,5,4 0
- X\_8,4,4 -X\_8,6,4 0
- X\_8,4,4 -X\_9,4,4 0
- X\_8,4,4 -X\_9,5,4 0
- X\_8,4,4 -X\_9,6,4 0
- X\_8,5,4 -X\_8,6,4 0
- X\_8,5,4 -X\_9,4,4 0
- X\_8,5,4 -X\_9,5,4 0
- X\_8,5,4 -X\_9,6,4 0
- X\_8,6,4 -X\_9,4,4 0
- X\_8,6,4 -X\_9,5,4 0
- X\_8,6,4 -X\_9,6,4 0
- X\_9,4,4 -X\_9,5,4 0
- X\_9,4,4 -X\_9,6,4 0
- X\_9,5,4 -X\_9,6,4 0

X\_7,7,4 X\_7,8,4 X\_7,9,4 X\_8,7,4 X\_8,8,4 X\_8,9,4 X\_9,7,4 X\_9,8,4 X\_9,9,4 0

- X\_7,7,4 -X\_7,8,4 0
- X\_7,7,4 -X\_7,9,4 0
- X\_7,7,4 -X\_8,7,4 0
- X\_7,7,4 -X\_8,8,4 0
- X\_7,7,4 -X\_8,9,4 0
- X\_7,7,4 -X\_9,7,4 0
- X\_7,7,4 -X\_9,8,4 0
- X\_7,7,4 -X\_9,9,4 0
- X\_7,8,4 -X\_7,9,4 0
- X\_7,8,4 -X\_8,7,4 0
- X\_7,8,4 -X\_8,8,4 0
- X\_7,8,4 -X\_8,9,4 0
- X\_7,8,4 -X\_9,7,4 0
- X\_7,8,4 -X\_9,8,4 0
- X\_7,8,4 -X\_9,9,4 0
- X\_7,9,4 -X\_8,7,4 0
- X\_7,9,4 -X\_8,8,4 0
- X\_7,9,4 -X\_8,9,4 0
- X\_7,9,4 -X\_9,7,4 0
- X\_7,9,4 -X\_9,8,4 0
- X\_7,9,4 -X\_9,9,4 0
- X\_8,7,4 -X\_8,8,4 0
- X\_8,7,4 -X\_8,9,4 0
- X\_8,7,4 -X\_9,7,4 0
- X\_8,7,4 -X\_9,8,4 0
- X\_8,7,4 -X\_9,9,4 0
- X\_8,8,4 -X\_8,9,4 0
- X\_8,8,4 -X\_9,7,4 0
- X\_8,8,4 -X\_9,8,4 0
- X\_8,8,4 -X\_9,9,4 0
- X\_8,9,4 -X\_9,7,4 0
- X\_8,9,4 -X\_9,8,4 0
- X\_8,9,4 -X\_9,9,4 0
- X\_9,7,4 -X\_9,8,4 0
- X\_9,7,4 -X\_9,9,4 0
- X\_9,8,4 -X\_9,9,4 0

X\_1,1,5 X\_1,2,5 X\_1,3,5 X\_2,1,5 X\_2,2,5 X\_2,3,5 X\_3,1,5 X\_3,2,5 X\_3,3,5 0

- X\_1,1,5 -X\_1,2,5 0
- X\_1,1,5 -X\_1,3,5 0
- X\_1,1,5 -X\_2,1,5 0
- X\_1,1,5 -X\_2,2,5 0
- X\_1,1,5 -X\_2,3,5 0
- X\_1,1,5 -X\_3,1,5 0
- X\_1,1,5 -X\_3,2,5 0
- X\_1,1,5 -X\_3,3,5 0
- X\_1,2,5 -X\_1,3,5 0
- X\_1,2,5 -X\_2,1,5 0
- X\_1,2,5 -X\_2,2,5 0
- X\_1,2,5 -X\_2,3,5 0
- X\_1,2,5 -X\_3,1,5 0
- X\_1,2,5 -X\_3,2,5 0
- X\_1,2,5 -X\_3,3,5 0
- X\_1,3,5 -X\_2,1,5 0
- X\_1,3,5 -X\_2,2,5 0
- X\_1,3,5 -X\_2,3,5 0
- X\_1,3,5 -X\_3,1,5 0
- X\_1,3,5 -X\_3,2,5 0
- X\_1,3,5 -X\_3,3,5 0
- X\_2,1,5 -X\_2,2,5 0
- X\_2,1,5 -X\_2,3,5 0
- X\_2,1,5 -X\_3,1,5 0
- X\_2,1,5 -X\_3,2,5 0
- X\_2,1,5 -X\_3,3,5 0
- X\_2,2,5 -X\_2,3,5 0
- X\_2,2,5 -X\_3,1,5 0
- X\_2,2,5 -X\_3,2,5 0
- X\_2,2,5 -X\_3,3,5 0
- X\_2,3,5 -X\_3,1,5 0
- X\_2,3,5 -X\_3,2,5 0
- X\_2,3,5 -X\_3,3,5 0
- X\_3,1,5 -X\_3,2,5 0
- X\_3,1,5 -X\_3,3,5 0
- X\_3,2,5 -X\_3,3,5 0

X\_1,4,5 X\_1,5,5 X\_1,6,5 X\_2,4,5 X\_2,5,5 X\_2,6,5 X\_3,4,5 X\_3,5,5 X\_3,6,5 0

- X\_1,4,5 -X\_1,5,5 0
- X\_1,4,5 -X\_1,6,5 0
- X\_1,4,5 -X\_2,4,5 0
- X\_1,4,5 -X\_2,5,5 0
- X\_1,4,5 -X\_2,6,5 0
- X\_1,4,5 -X\_3,4,5 0
- X\_1,4,5 -X\_3,5,5 0
- X\_1,4,5 -X\_3,6,5 0
- X\_1,5,5 -X\_1,6,5 0
- X\_1,5,5 -X\_2,4,5 0
- X\_1,5,5 -X\_2,5,5 0
- X\_1,5,5 -X\_2,6,5 0
- X\_1,5,5 -X\_3,4,5 0
- X\_1,5,5 -X\_3,5,5 0
- X\_1,5,5 -X\_3,6,5 0
- X\_1,6,5 -X\_2,4,5 0
- X\_1,6,5 -X\_2,5,5 0
- X\_1,6,5 -X\_2,6,5 0
- X\_1,6,5 -X\_3,4,5 0
- X\_1,6,5 -X\_3,5,5 0
- X\_1,6,5 -X\_3,6,5 0
- X\_2,4,5 -X\_2,5,5 0
- X\_2,4,5 -X\_2,6,5 0
- X\_2,4,5 -X\_3,4,5 0
- X\_2,4,5 -X\_3,5,5 0
- X\_2,4,5 -X\_3,6,5 0
- X\_2,5,5 -X\_2,6,5 0
- X\_2,5,5 -X\_3,4,5 0
- X\_2,5,5 -X\_3,5,5 0
- X\_2,5,5 -X\_3,6,5 0
- X\_2,6,5 -X\_3,4,5 0
- X\_2,6,5 -X\_3,5,5 0
- X\_2,6,5 -X\_3,6,5 0
- X\_3,4,5 -X\_3,5,5 0
- X\_3,4,5 -X\_3,6,5 0
- X\_3,5,5 -X\_3,6,5 0

X\_1,7,5 X\_1,8,5 X\_1,9,5 X\_2,7,5 X\_2,8,5 X\_2,9,5 X\_3,7,5 X\_3,8,5 X\_3,9,5 0

- X\_1,7,5 -X\_1,8,5 0
- X\_1,7,5 -X\_1,9,5 0
- X\_1,7,5 -X\_2,7,5 0
- X\_1,7,5 -X\_2,8,5 0
- X\_1,7,5 -X\_2,9,5 0
- X\_1,7,5 -X\_3,7,5 0
- X\_1,7,5 -X\_3,8,5 0
- X\_1,7,5 -X\_3,9,5 0
- X\_1,8,5 -X\_1,9,5 0
- X\_1,8,5 -X\_2,7,5 0
- X\_1,8,5 -X\_2,8,5 0
- X\_1,8,5 -X\_2,9,5 0
- X\_1,8,5 -X\_3,7,5 0
- X\_1,8,5 -X\_3,8,5 0
- X\_1,8,5 -X\_3,9,5 0
- X\_1,9,5 -X\_2,7,5 0
- X\_1,9,5 -X\_2,8,5 0
- X\_1,9,5 -X\_2,9,5 0
- X\_1,9,5 -X\_3,7,5 0
- X\_1,9,5 -X\_3,8,5 0
- X\_1,9,5 -X\_3,9,5 0
- X\_2,7,5 -X\_2,8,5 0
- X\_2,7,5 -X\_2,9,5 0
- X\_2,7,5 -X\_3,7,5 0
- X\_2,7,5 -X\_3,8,5 0
- X\_2,7,5 -X\_3,9,5 0
- X\_2,8,5 -X\_2,9,5 0
- X\_2,8,5 -X\_3,7,5 0
- X\_2,8,5 -X\_3,8,5 0
- X\_2,8,5 -X\_3,9,5 0
- X\_2,9,5 -X\_3,7,5 0
- X\_2,9,5 -X\_3,8,5 0
- X\_2,9,5 -X\_3,9,5 0
- X\_3,7,5 -X\_3,8,5 0
- X\_3,7,5 -X\_3,9,5 0
- X\_3,8,5 -X\_3,9,5 0

X\_4,1,5 X\_4,2,5 X\_4,3,5 X\_5,1,5 X\_5,2,5 X\_5,3,5 X\_6,1,5 X\_6,2,5 X\_6,3,5 0

- X\_4,1,5 -X\_4,2,5 0
- X\_4,1,5 -X\_4,3,5 0
- X\_4,1,5 -X\_5,1,5 0
- X\_4,1,5 -X\_5,2,5 0
- X\_4,1,5 -X\_5,3,5 0
- X\_4,1,5 -X\_6,1,5 0
- X\_4,1,5 -X\_6,2,5 0
- X\_4,1,5 -X\_6,3,5 0
- X\_4,2,5 -X\_4,3,5 0
- X\_4,2,5 -X\_5,1,5 0
- X\_4,2,5 -X\_5,2,5 0
- X\_4,2,5 -X\_5,3,5 0
- X\_4,2,5 -X\_6,1,5 0
- X\_4,2,5 -X\_6,2,5 0
- X\_4,2,5 -X\_6,3,5 0
- X\_4,3,5 -X\_5,1,5 0
- X\_4,3,5 -X\_5,2,5 0
- X\_4,3,5 -X\_5,3,5 0
- X\_4,3,5 -X\_6,1,5 0
- X\_4,3,5 -X\_6,2,5 0
- X\_4,3,5 -X\_6,3,5 0
- X\_5,1,5 -X\_5,2,5 0
- X\_5,1,5 -X\_5,3,5 0
- X\_5,1,5 -X\_6,1,5 0
- X\_5,1,5 -X\_6,2,5 0
- X\_5,1,5 -X\_6,3,5 0
- X\_5,2,5 -X\_5,3,5 0
- X\_5,2,5 -X\_6,1,5 0
- X\_5,2,5 -X\_6,2,5 0
- X\_5,2,5 -X\_6,3,5 0
- X\_5,3,5 -X\_6,1,5 0
- X\_5,3,5 -X\_6,2,5 0
- X\_5,3,5 -X\_6,3,5 0
- X\_6,1,5 -X\_6,2,5 0
- X\_6,1,5 -X\_6,3,5 0
- X\_6,2,5 -X\_6,3,5 0

X\_4,4,5 X\_4,5,5 X\_4,6,5 X\_5,4,5 X\_5,5,5 X\_5,6,5 X\_6,4,5 X\_6,5,5 X\_6,6,5 0

- X\_4,4,5 -X\_4,5,5 0
- X\_4,4,5 -X\_4,6,5 0
- X\_4,4,5 -X\_5,4,5 0
- X\_4,4,5 -X\_5,5,5 0
- X\_4,4,5 -X\_5,6,5 0
- X\_4,4,5 -X\_6,4,5 0
- X\_4,4,5 -X\_6,5,5 0
- X\_4,4,5 -X\_6,6,5 0
- X\_4,5,5 -X\_4,6,5 0
- X\_4,5,5 -X\_5,4,5 0
- X\_4,5,5 -X\_5,5,5 0
- X\_4,5,5 -X\_5,6,5 0
- X\_4,5,5 -X\_6,4,5 0
- X\_4,5,5 -X\_6,5,5 0
- X\_4,5,5 -X\_6,6,5 0
- X\_4,6,5 -X\_5,4,5 0
- X\_4,6,5 -X\_5,5,5 0
- X\_4,6,5 -X\_5,6,5 0
- X\_4,6,5 -X\_6,4,5 0
- X\_4,6,5 -X\_6,5,5 0
- X\_4,6,5 -X\_6,6,5 0
- X\_5,4,5 -X\_5,5,5 0
- X\_5,4,5 -X\_5,6,5 0
- X\_5,4,5 -X\_6,4,5 0
- X\_5,4,5 -X\_6,5,5 0
- X\_5,4,5 -X\_6,6,5 0
- X\_5,5,5 -X\_5,6,5 0
- X\_5,5,5 -X\_6,4,5 0
- X\_5,5,5 -X\_6,5,5 0
- X\_5,5,5 -X\_6,6,5 0
- X\_5,6,5 -X\_6,4,5 0
- X\_5,6,5 -X\_6,5,5 0
- X\_5,6,5 -X\_6,6,5 0
- X\_6,4,5 -X\_6,5,5 0
- X\_6,4,5 -X\_6,6,5 0
- X\_6,5,5 -X\_6,6,5 0

X\_4,7,5 X\_4,8,5 X\_4,9,5 X\_5,7,5 X\_5,8,5 X\_5,9,5 X\_6,7,5 X\_6,8,5 X\_6,9,5 0

- X\_4,7,5 -X\_4,8,5 0
- X\_4,7,5 -X\_4,9,5 0
- X\_4,7,5 -X\_5,7,5 0
- X\_4,7,5 -X\_5,8,5 0
- X\_4,7,5 -X\_5,9,5 0
- X\_4,7,5 -X\_6,7,5 0
- X\_4,7,5 -X\_6,8,5 0
- X\_4,7,5 -X\_6,9,5 0
- X\_4,8,5 -X\_4,9,5 0
- X\_4,8,5 -X\_5,7,5 0
- X\_4,8,5 -X\_5,8,5 0
- X\_4,8,5 -X\_5,9,5 0
- X\_4,8,5 -X\_6,7,5 0
- X\_4,8,5 -X\_6,8,5 0
- X\_4,8,5 -X\_6,9,5 0
- X\_4,9,5 -X\_5,7,5 0
- X\_4,9,5 -X\_5,8,5 0
- X\_4,9,5 -X\_5,9,5 0
- X\_4,9,5 -X\_6,7,5 0
- X\_4,9,5 -X\_6,8,5 0
- X\_4,9,5 -X\_6,9,5 0
- X\_5,7,5 -X\_5,8,5 0
- X\_5,7,5 -X\_5,9,5 0
- X\_5,7,5 -X\_6,7,5 0
- X\_5,7,5 -X\_6,8,5 0
- X\_5,7,5 -X\_6,9,5 0
- X\_5,8,5 -X\_5,9,5 0
- X\_5,8,5 -X\_6,7,5 0
- X\_5,8,5 -X\_6,8,5 0
- X\_5,8,5 -X\_6,9,5 0
- X\_5,9,5 -X\_6,7,5 0
- X\_5,9,5 -X\_6,8,5 0
- X\_5,9,5 -X\_6,9,5 0
- X\_6,7,5 -X\_6,8,5 0
- X\_6,7,5 -X\_6,9,5 0
- X\_6,8,5 -X\_6,9,5 0

X\_7,1,5 X\_7,2,5 X\_7,3,5 X\_8,1,5 X\_8,2,5 X\_8,3,5 X\_9,1,5 X\_9,2,5 X\_9,3,5 0

- X\_7,1,5 -X\_7,2,5 0
- X\_7,1,5 -X\_7,3,5 0
- X\_7,1,5 -X\_8,1,5 0
- X\_7,1,5 -X\_8,2,5 0
- X\_7,1,5 -X\_8,3,5 0
- X\_7,1,5 -X\_9,1,5 0
- X\_7,1,5 -X\_9,2,5 0
- X\_7,1,5 -X\_9,3,5 0
- X\_7,2,5 -X\_7,3,5 0
- X\_7,2,5 -X\_8,1,5 0
- X\_7,2,5 -X\_8,2,5 0
- X\_7,2,5 -X\_8,3,5 0
- X\_7,2,5 -X\_9,1,5 0
- X\_7,2,5 -X\_9,2,5 0
- X\_7,2,5 -X\_9,3,5 0
- X\_7,3,5 -X\_8,1,5 0
- X\_7,3,5 -X\_8,2,5 0
- X\_7,3,5 -X\_8,3,5 0
- X\_7,3,5 -X\_9,1,5 0
- X\_7,3,5 -X\_9,2,5 0
- X\_7,3,5 -X\_9,3,5 0
- X\_8,1,5 -X\_8,2,5 0
- X\_8,1,5 -X\_8,3,5 0
- X\_8,1,5 -X\_9,1,5 0
- X\_8,1,5 -X\_9,2,5 0
- X\_8,1,5 -X\_9,3,5 0
- X\_8,2,5 -X\_8,3,5 0
- X\_8,2,5 -X\_9,1,5 0
- X\_8,2,5 -X\_9,2,5 0
- X\_8,2,5 -X\_9,3,5 0
- X\_8,3,5 -X\_9,1,5 0
- X\_8,3,5 -X\_9,2,5 0
- X\_8,3,5 -X\_9,3,5 0
- X\_9,1,5 -X\_9,2,5 0
- X\_9,1,5 -X\_9,3,5 0
- X\_9,2,5 -X\_9,3,5 0

X\_7,4,5 X\_7,5,5 X\_7,6,5 X\_8,4,5 X\_8,5,5 X\_8,6,5 X\_9,4,5 X\_9,5,5 X\_9,6,5 0

- X\_7,4,5 -X\_7,5,5 0
- X\_7,4,5 -X\_7,6,5 0
- X\_7,4,5 -X\_8,4,5 0
- X\_7,4,5 -X\_8,5,5 0
- X\_7,4,5 -X\_8,6,5 0
- X\_7,4,5 -X\_9,4,5 0
- X\_7,4,5 -X\_9,5,5 0
- X\_7,4,5 -X\_9,6,5 0
- X\_7,5,5 -X\_7,6,5 0
- X\_7,5,5 -X\_8,4,5 0
- X\_7,5,5 -X\_8,5,5 0
- X\_7,5,5 -X\_8,6,5 0
- X\_7,5,5 -X\_9,4,5 0
- X\_7,5,5 -X\_9,5,5 0
- X\_7,5,5 -X\_9,6,5 0
- X\_7,6,5 -X\_8,4,5 0
- X\_7,6,5 -X\_8,5,5 0
- X\_7,6,5 -X\_8,6,5 0
- X\_7,6,5 -X\_9,4,5 0
- X\_7,6,5 -X\_9,5,5 0
- X\_7,6,5 -X\_9,6,5 0
- X\_8,4,5 -X\_8,5,5 0
- X\_8,4,5 -X\_8,6,5 0
- X\_8,4,5 -X\_9,4,5 0
- X\_8,4,5 -X\_9,5,5 0
- X\_8,4,5 -X\_9,6,5 0
- X\_8,5,5 -X\_8,6,5 0
- X\_8,5,5 -X\_9,4,5 0
- X\_8,5,5 -X\_9,5,5 0
- X\_8,5,5 -X\_9,6,5 0
- X\_8,6,5 -X\_9,4,5 0
- X\_8,6,5 -X\_9,5,5 0
- X\_8,6,5 -X\_9,6,5 0
- X\_9,4,5 -X\_9,5,5 0
- X\_9,4,5 -X\_9,6,5 0
- X\_9,5,5 -X\_9,6,5 0

X\_7,7,5 X\_7,8,5 X\_7,9,5 X\_8,7,5 X\_8,8,5 X\_8,9,5 X\_9,7,5 X\_9,8,5 X\_9,9,5 0

- X\_7,7,5 -X\_7,8,5 0
- X\_7,7,5 -X\_7,9,5 0
- X\_7,7,5 -X\_8,7,5 0
- X\_7,7,5 -X\_8,8,5 0
- X\_7,7,5 -X\_8,9,5 0
- X\_7,7,5 -X\_9,7,5 0
- X\_7,7,5 -X\_9,8,5 0
- X\_7,7,5 -X\_9,9,5 0
- X\_7,8,5 -X\_7,9,5 0
- X\_7,8,5 -X\_8,7,5 0
- X\_7,8,5 -X\_8,8,5 0
- X\_7,8,5 -X\_8,9,5 0
- X\_7,8,5 -X\_9,7,5 0
- X\_7,8,5 -X\_9,8,5 0
- X\_7,8,5 -X\_9,9,5 0
- X\_7,9,5 -X\_8,7,5 0
- X\_7,9,5 -X\_8,8,5 0
- X\_7,9,5 -X\_8,9,5 0
- X\_7,9,5 -X\_9,7,5 0
- X\_7,9,5 -X\_9,8,5 0
- X\_7,9,5 -X\_9,9,5 0
- X\_8,7,5 -X\_8,8,5 0
- X\_8,7,5 -X\_8,9,5 0
- X\_8,7,5 -X\_9,7,5 0
- X\_8,7,5 -X\_9,8,5 0
- X\_8,7,5 -X\_9,9,5 0
- X\_8,8,5 -X\_8,9,5 0
- X\_8,8,5 -X\_9,7,5 0
- X\_8,8,5 -X\_9,8,5 0
- X\_8,8,5 -X\_9,9,5 0
- X\_8,9,5 -X\_9,7,5 0
- X\_8,9,5 -X\_9,8,5 0
- X\_8,9,5 -X\_9,9,5 0
- X\_9,7,5 -X\_9,8,5 0
- X\_9,7,5 -X\_9,9,5 0
- X\_9,8,5 -X\_9,9,5 0

X\_1,1,6 X\_1,2,6 X\_1,3,6 X\_2,1,6 X\_2,2,6 X\_2,3,6 X\_3,1,6 X\_3,2,6 X\_3,3,6 0

- X\_1,1,6 -X\_1,2,6 0
- X\_1,1,6 -X\_1,3,6 0
- X\_1,1,6 -X\_2,1,6 0
- X\_1,1,6 -X\_2,2,6 0
- X\_1,1,6 -X\_2,3,6 0
- X\_1,1,6 -X\_3,1,6 0
- X\_1,1,6 -X\_3,2,6 0
- X\_1,1,6 -X\_3,3,6 0
- X\_1,2,6 -X\_1,3,6 0
- X\_1,2,6 -X\_2,1,6 0
- X\_1,2,6 -X\_2,2,6 0
- X\_1,2,6 -X\_2,3,6 0
- X\_1,2,6 -X\_3,1,6 0
- X\_1,2,6 -X\_3,2,6 0
- X\_1,2,6 -X\_3,3,6 0
- X\_1,3,6 -X\_2,1,6 0
- X\_1,3,6 -X\_2,2,6 0
- X\_1,3,6 -X\_2,3,6 0
- X\_1,3,6 -X\_3,1,6 0
- X\_1,3,6 -X\_3,2,6 0
- X\_1,3,6 -X\_3,3,6 0
- X\_2,1,6 -X\_2,2,6 0
- X\_2,1,6 -X\_2,3,6 0
- X\_2,1,6 -X\_3,1,6 0
- X\_2,1,6 -X\_3,2,6 0
- X\_2,1,6 -X\_3,3,6 0
- X\_2,2,6 -X\_2,3,6 0
- X\_2,2,6 -X\_3,1,6 0
- X\_2,2,6 -X\_3,2,6 0
- X\_2,2,6 -X\_3,3,6 0
- X\_2,3,6 -X\_3,1,6 0
- X\_2,3,6 -X\_3,2,6 0
- X\_2,3,6 -X\_3,3,6 0
- X\_3,1,6 -X\_3,2,6 0
- X\_3,1,6 -X\_3,3,6 0
- X\_3,2,6 -X\_3,3,6 0

X\_1,4,6 X\_1,5,6 X\_1,6,6 X\_2,4,6 X\_2,5,6 X\_2,6,6 X\_3,4,6 X\_3,5,6 X\_3,6,6 0

- X\_1,4,6 -X\_1,5,6 0
- X\_1,4,6 -X\_1,6,6 0
- X\_1,4,6 -X\_2,4,6 0
- X\_1,4,6 -X\_2,5,6 0
- X\_1,4,6 -X\_2,6,6 0
- X\_1,4,6 -X\_3,4,6 0
- X\_1,4,6 -X\_3,5,6 0
- X\_1,4,6 -X\_3,6,6 0
- X\_1,5,6 -X\_1,6,6 0
- X\_1,5,6 -X\_2,4,6 0
- X\_1,5,6 -X\_2,5,6 0
- X\_1,5,6 -X\_2,6,6 0
- X\_1,5,6 -X\_3,4,6 0
- X\_1,5,6 -X\_3,5,6 0
- X\_1,5,6 -X\_3,6,6 0
- X\_1,6,6 -X\_2,4,6 0
- X\_1,6,6 -X\_2,5,6 0
- X\_1,6,6 -X\_2,6,6 0
- X\_1,6,6 -X\_3,4,6 0
- X\_1,6,6 -X\_3,5,6 0
- X\_1,6,6 -X\_3,6,6 0
- X\_2,4,6 -X\_2,5,6 0
- X\_2,4,6 -X\_2,6,6 0
- X\_2,4,6 -X\_3,4,6 0
- X\_2,4,6 -X\_3,5,6 0
- X\_2,4,6 -X\_3,6,6 0
- X\_2,5,6 -X\_2,6,6 0
- X\_2,5,6 -X\_3,4,6 0
- X\_2,5,6 -X\_3,5,6 0
- X\_2,5,6 -X\_3,6,6 0
- X\_2,6,6 -X\_3,4,6 0
- X\_2,6,6 -X\_3,5,6 0
- X\_2,6,6 -X\_3,6,6 0
- X\_3,4,6 -X\_3,5,6 0
- X\_3,4,6 -X\_3,6,6 0
- X\_3,5,6 -X\_3,6,6 0

X\_1,7,6 X\_1,8,6 X\_1,9,6 X\_2,7,6 X\_2,8,6 X\_2,9,6 X\_3,7,6 X\_3,8,6 X\_3,9,6 0

- X\_1,7,6 -X\_1,8,6 0
- X\_1,7,6 -X\_1,9,6 0
- X\_1,7,6 -X\_2,7,6 0
- X\_1,7,6 -X\_2,8,6 0
- X\_1,7,6 -X\_2,9,6 0
- X\_1,7,6 -X\_3,7,6 0
- X\_1,7,6 -X\_3,8,6 0
- X\_1,7,6 -X\_3,9,6 0
- X\_1,8,6 -X\_1,9,6 0
- X\_1,8,6 -X\_2,7,6 0
- X\_1,8,6 -X\_2,8,6 0
- X\_1,8,6 -X\_2,9,6 0
- X\_1,8,6 -X\_3,7,6 0
- X\_1,8,6 -X\_3,8,6 0
- X\_1,8,6 -X\_3,9,6 0
- X\_1,9,6 -X\_2,7,6 0
- X\_1,9,6 -X\_2,8,6 0
- X\_1,9,6 -X\_2,9,6 0
- X\_1,9,6 -X\_3,7,6 0
- X\_1,9,6 -X\_3,8,6 0
- X\_1,9,6 -X\_3,9,6 0
- X\_2,7,6 -X\_2,8,6 0
- X\_2,7,6 -X\_2,9,6 0
- X\_2,7,6 -X\_3,7,6 0
- X\_2,7,6 -X\_3,8,6 0
- X\_2,7,6 -X\_3,9,6 0
- X\_2,8,6 -X\_2,9,6 0
- X\_2,8,6 -X\_3,7,6 0
- X\_2,8,6 -X\_3,8,6 0
- X\_2,8,6 -X\_3,9,6 0
- X\_2,9,6 -X\_3,7,6 0
- X\_2,9,6 -X\_3,8,6 0
- X\_2,9,6 -X\_3,9,6 0
- X\_3,7,6 -X\_3,8,6 0
- X\_3,7,6 -X\_3,9,6 0
- X\_3,8,6 -X\_3,9,6 0

X\_4,1,6 X\_4,2,6 X\_4,3,6 X\_5,1,6 X\_5,2,6 X\_5,3,6 X\_6,1,6 X\_6,2,6 X\_6,3,6 0

- X\_4,1,6 -X\_4,2,6 0
- X\_4,1,6 -X\_4,3,6 0
- X\_4,1,6 -X\_5,1,6 0
- X\_4,1,6 -X\_5,2,6 0
- X\_4,1,6 -X\_5,3,6 0
- X\_4,1,6 -X\_6,1,6 0
- X\_4,1,6 -X\_6,2,6 0
- X\_4,1,6 -X\_6,3,6 0
- X\_4,2,6 -X\_4,3,6 0
- X\_4,2,6 -X\_5,1,6 0
- X\_4,2,6 -X\_5,2,6 0
- X\_4,2,6 -X\_5,3,6 0
- X\_4,2,6 -X\_6,1,6 0
- X\_4,2,6 -X\_6,2,6 0
- X\_4,2,6 -X\_6,3,6 0
- X\_4,3,6 -X\_5,1,6 0
- X\_4,3,6 -X\_5,2,6 0
- X\_4,3,6 -X\_5,3,6 0
- X\_4,3,6 -X\_6,1,6 0
- X\_4,3,6 -X\_6,2,6 0
- X\_4,3,6 -X\_6,3,6 0
- X\_5,1,6 -X\_5,2,6 0
- X\_5,1,6 -X\_5,3,6 0
- X\_5,1,6 -X\_6,1,6 0
- X\_5,1,6 -X\_6,2,6 0
- X\_5,1,6 -X\_6,3,6 0
- X\_5,2,6 -X\_5,3,6 0
- X\_5,2,6 -X\_6,1,6 0
- X\_5,2,6 -X\_6,2,6 0
- X\_5,2,6 -X\_6,3,6 0
- X\_5,3,6 -X\_6,1,6 0
- X\_5,3,6 -X\_6,2,6 0
- X\_5,3,6 -X\_6,3,6 0
- X\_6,1,6 -X\_6,2,6 0
- X\_6,1,6 -X\_6,3,6 0
- X\_6,2,6 -X\_6,3,6 0

X\_4,4,6 X\_4,5,6 X\_4,6,6 X\_5,4,6 X\_5,5,6 X\_5,6,6 X\_6,4,6 X\_6,5,6 X\_6,6,6 0

- X\_4,4,6 -X\_4,5,6 0
- X\_4,4,6 -X\_4,6,6 0
- X\_4,4,6 -X\_5,4,6 0
- X\_4,4,6 -X\_5,5,6 0
- X\_4,4,6 -X\_5,6,6 0
- X\_4,4,6 -X\_6,4,6 0
- X\_4,4,6 -X\_6,5,6 0
- X\_4,4,6 -X\_6,6,6 0
- X\_4,5,6 -X\_4,6,6 0
- X\_4,5,6 -X\_5,4,6 0
- X\_4,5,6 -X\_5,5,6 0
- X\_4,5,6 -X\_5,6,6 0
- X\_4,5,6 -X\_6,4,6 0
- X\_4,5,6 -X\_6,5,6 0
- X\_4,5,6 -X\_6,6,6 0
- X\_4,6,6 -X\_5,4,6 0
- X\_4,6,6 -X\_5,5,6 0
- X\_4,6,6 -X\_5,6,6 0
- X\_4,6,6 -X\_6,4,6 0
- X\_4,6,6 -X\_6,5,6 0
- X\_4,6,6 -X\_6,6,6 0
- X\_5,4,6 -X\_5,5,6 0
- X\_5,4,6 -X\_5,6,6 0
- X\_5,4,6 -X\_6,4,6 0
- X\_5,4,6 -X\_6,5,6 0
- X\_5,4,6 -X\_6,6,6 0
- X\_5,5,6 -X\_5,6,6 0
- X\_5,5,6 -X\_6,4,6 0
- X\_5,5,6 -X\_6,5,6 0
- X\_5,5,6 -X\_6,6,6 0
- X\_5,6,6 -X\_6,4,6 0
- X\_5,6,6 -X\_6,5,6 0
- X\_5,6,6 -X\_6,6,6 0
- X\_6,4,6 -X\_6,5,6 0
- X\_6,4,6 -X\_6,6,6 0
- X\_6,5,6 -X\_6,6,6 0

X\_4,7,6 X\_4,8,6 X\_4,9,6 X\_5,7,6 X\_5,8,6 X\_5,9,6 X\_6,7,6 X\_6,8,6 X\_6,9,6 0

- X\_4,7,6 -X\_4,8,6 0
- X\_4,7,6 -X\_4,9,6 0
- X\_4,7,6 -X\_5,7,6 0
- X\_4,7,6 -X\_5,8,6 0
- X\_4,7,6 -X\_5,9,6 0
- X\_4,7,6 -X\_6,7,6 0
- X\_4,7,6 -X\_6,8,6 0
- X\_4,7,6 -X\_6,9,6 0
- X\_4,8,6 -X\_4,9,6 0
- X\_4,8,6 -X\_5,7,6 0
- X\_4,8,6 -X\_5,8,6 0
- X\_4,8,6 -X\_5,9,6 0
- X\_4,8,6 -X\_6,7,6 0
- X\_4,8,6 -X\_6,8,6 0
- X\_4,8,6 -X\_6,9,6 0
- X\_4,9,6 -X\_5,7,6 0
- X\_4,9,6 -X\_5,8,6 0
- X\_4,9,6 -X\_5,9,6 0
- X\_4,9,6 -X\_6,7,6 0
- X\_4,9,6 -X\_6,8,6 0
- X\_4,9,6 -X\_6,9,6 0
- X\_5,7,6 -X\_5,8,6 0
- X\_5,7,6 -X\_5,9,6 0
- X\_5,7,6 -X\_6,7,6 0
- X\_5,7,6 -X\_6,8,6 0
- X\_5,7,6 -X\_6,9,6 0
- X\_5,8,6 -X\_5,9,6 0
- X\_5,8,6 -X\_6,7,6 0
- X\_5,8,6 -X\_6,8,6 0
- X\_5,8,6 -X\_6,9,6 0
- X\_5,9,6 -X\_6,7,6 0
- X\_5,9,6 -X\_6,8,6 0
- X\_5,9,6 -X\_6,9,6 0
- X\_6,7,6 -X\_6,8,6 0
- X\_6,7,6 -X\_6,9,6 0
- X\_6,8,6 -X\_6,9,6 0

X\_7,1,6 X\_7,2,6 X\_7,3,6 X\_8,1,6 X\_8,2,6 X\_8,3,6 X\_9,1,6 X\_9,2,6 X\_9,3,6 0

- X\_7,1,6 -X\_7,2,6 0
- X\_7,1,6 -X\_7,3,6 0
- X\_7,1,6 -X\_8,1,6 0
- X\_7,1,6 -X\_8,2,6 0
- X\_7,1,6 -X\_8,3,6 0
- X\_7,1,6 -X\_9,1,6 0
- X\_7,1,6 -X\_9,2,6 0
- X\_7,1,6 -X\_9,3,6 0
- X\_7,2,6 -X\_7,3,6 0
- X\_7,2,6 -X\_8,1,6 0
- X\_7,2,6 -X\_8,2,6 0
- X\_7,2,6 -X\_8,3,6 0
- X\_7,2,6 -X\_9,1,6 0
- X\_7,2,6 -X\_9,2,6 0
- X\_7,2,6 -X\_9,3,6 0
- X\_7,3,6 -X\_8,1,6 0
- X\_7,3,6 -X\_8,2,6 0
- X\_7,3,6 -X\_8,3,6 0
- X\_7,3,6 -X\_9,1,6 0
- X\_7,3,6 -X\_9,2,6 0
- X\_7,3,6 -X\_9,3,6 0
- X\_8,1,6 -X\_8,2,6 0
- X\_8,1,6 -X\_8,3,6 0
- X\_8,1,6 -X\_9,1,6 0
- X\_8,1,6 -X\_9,2,6 0
- X\_8,1,6 -X\_9,3,6 0
- X\_8,2,6 -X\_8,3,6 0
- X\_8,2,6 -X\_9,1,6 0
- X\_8,2,6 -X\_9,2,6 0
- X\_8,2,6 -X\_9,3,6 0
- X\_8,3,6 -X\_9,1,6 0
- X\_8,3,6 -X\_9,2,6 0
- X\_8,3,6 -X\_9,3,6 0
- X\_9,1,6 -X\_9,2,6 0
- X\_9,1,6 -X\_9,3,6 0
- X\_9,2,6 -X\_9,3,6 0

X\_7,4,6 X\_7,5,6 X\_7,6,6 X\_8,4,6 X\_8,5,6 X\_8,6,6 X\_9,4,6 X\_9,5,6 X\_9,6,6 0

- X\_7,4,6 -X\_7,5,6 0
- X\_7,4,6 -X\_7,6,6 0
- X\_7,4,6 -X\_8,4,6 0
- X\_7,4,6 -X\_8,5,6 0
- X\_7,4,6 -X\_8,6,6 0
- X\_7,4,6 -X\_9,4,6 0
- X\_7,4,6 -X\_9,5,6 0
- X\_7,4,6 -X\_9,6,6 0
- X\_7,5,6 -X\_7,6,6 0
- X\_7,5,6 -X\_8,4,6 0
- X\_7,5,6 -X\_8,5,6 0
- X\_7,5,6 -X\_8,6,6 0
- X\_7,5,6 -X\_9,4,6 0
- X\_7,5,6 -X\_9,5,6 0
- X\_7,5,6 -X\_9,6,6 0
- X\_7,6,6 -X\_8,4,6 0
- X\_7,6,6 -X\_8,5,6 0
- X\_7,6,6 -X\_8,6,6 0
- X\_7,6,6 -X\_9,4,6 0
- X\_7,6,6 -X\_9,5,6 0
- X\_7,6,6 -X\_9,6,6 0
- X\_8,4,6 -X\_8,5,6 0
- X\_8,4,6 -X\_8,6,6 0
- X\_8,4,6 -X\_9,4,6 0
- X\_8,4,6 -X\_9,5,6 0
- X\_8,4,6 -X\_9,6,6 0
- X\_8,5,6 -X\_8,6,6 0
- X\_8,5,6 -X\_9,4,6 0
- X\_8,5,6 -X\_9,5,6 0
- X\_8,5,6 -X\_9,6,6 0
- X\_8,6,6 -X\_9,4,6 0
- X\_8,6,6 -X\_9,5,6 0
- X\_8,6,6 -X\_9,6,6 0
- X\_9,4,6 -X\_9,5,6 0
- X\_9,4,6 -X\_9,6,6 0
- X\_9,5,6 -X\_9,6,6 0

X\_7,7,6 X\_7,8,6 X\_7,9,6 X\_8,7,6 X\_8,8,6 X\_8,9,6 X\_9,7,6 X\_9,8,6 X\_9,9,6 0

- X\_7,7,6 -X\_7,8,6 0
- X\_7,7,6 -X\_7,9,6 0
- X\_7,7,6 -X\_8,7,6 0
- X\_7,7,6 -X\_8,8,6 0
- X\_7,7,6 -X\_8,9,6 0
- X\_7,7,6 -X\_9,7,6 0
- X\_7,7,6 -X\_9,8,6 0
- X\_7,7,6 -X\_9,9,6 0
- X\_7,8,6 -X\_7,9,6 0
- X\_7,8,6 -X\_8,7,6 0
- X\_7,8,6 -X\_8,8,6 0
- X\_7,8,6 -X\_8,9,6 0
- X\_7,8,6 -X\_9,7,6 0
- X\_7,8,6 -X\_9,8,6 0
- X\_7,8,6 -X\_9,9,6 0
- X\_7,9,6 -X\_8,7,6 0
- X\_7,9,6 -X\_8,8,6 0
- X\_7,9,6 -X\_8,9,6 0
- X\_7,9,6 -X\_9,7,6 0
- X\_7,9,6 -X\_9,8,6 0
- X\_7,9,6 -X\_9,9,6 0
- X\_8,7,6 -X\_8,8,6 0
- X\_8,7,6 -X\_8,9,6 0
- X\_8,7,6 -X\_9,7,6 0
- X\_8,7,6 -X\_9,8,6 0
- X\_8,7,6 -X\_9,9,6 0
- X\_8,8,6 -X\_8,9,6 0
- X\_8,8,6 -X\_9,7,6 0
- X\_8,8,6 -X\_9,8,6 0
- X\_8,8,6 -X\_9,9,6 0
- X\_8,9,6 -X\_9,7,6 0
- X\_8,9,6 -X\_9,8,6 0
- X\_8,9,6 -X\_9,9,6 0
- X\_9,7,6 -X\_9,8,6 0
- X\_9,7,6 -X\_9,9,6 0
- X\_9,8,6 -X\_9,9,6 0

X\_1,1,7 X\_1,2,7 X\_1,3,7 X\_2,1,7 X\_2,2,7 X\_2,3,7 X\_3,1,7 X\_3,2,7 X\_3,3,7 0

- X\_1,1,7 -X\_1,2,7 0
- X\_1,1,7 -X\_1,3,7 0
- X\_1,1,7 -X\_2,1,7 0
- X\_1,1,7 -X\_2,2,7 0
- X\_1,1,7 -X\_2,3,7 0
- X\_1,1,7 -X\_3,1,7 0
- X\_1,1,7 -X\_3,2,7 0
- X\_1,1,7 -X\_3,3,7 0
- X\_1,2,7 -X\_1,3,7 0
- X\_1,2,7 -X\_2,1,7 0
- X\_1,2,7 -X\_2,2,7 0
- X\_1,2,7 -X\_2,3,7 0
- X\_1,2,7 -X\_3,1,7 0
- X\_1,2,7 -X\_3,2,7 0
- X\_1,2,7 -X\_3,3,7 0
- X\_1,3,7 -X\_2,1,7 0
- X\_1,3,7 -X\_2,2,7 0
- X\_1,3,7 -X\_2,3,7 0
- X\_1,3,7 -X\_3,1,7 0
- X\_1,3,7 -X\_3,2,7 0
- X\_1,3,7 -X\_3,3,7 0
- X\_2,1,7 -X\_2,2,7 0
- X\_2,1,7 -X\_2,3,7 0
- X\_2,1,7 -X\_3,1,7 0
- X\_2,1,7 -X\_3,2,7 0
- X\_2,1,7 -X\_3,3,7 0
- X\_2,2,7 -X\_2,3,7 0
- X\_2,2,7 -X\_3,1,7 0
- X\_2,2,7 -X\_3,2,7 0
- X\_2,2,7 -X\_3,3,7 0
- X\_2,3,7 -X\_3,1,7 0
- X\_2,3,7 -X\_3,2,7 0
- X\_2,3,7 -X\_3,3,7 0
- X\_3,1,7 -X\_3,2,7 0
- X\_3,1,7 -X\_3,3,7 0
- X\_3,2,7 -X\_3,3,7 0

X\_1,4,7 X\_1,5,7 X\_1,6,7 X\_2,4,7 X\_2,5,7 X\_2,6,7 X\_3,4,7 X\_3,5,7 X\_3,6,7 0

- X\_1,4,7 -X\_1,5,7 0
- X\_1,4,7 -X\_1,6,7 0
- X\_1,4,7 -X\_2,4,7 0
- X\_1,4,7 -X\_2,5,7 0
- X\_1,4,7 -X\_2,6,7 0
- X\_1,4,7 -X\_3,4,7 0
- X\_1,4,7 -X\_3,5,7 0
- X\_1,4,7 -X\_3,6,7 0
- X\_1,5,7 -X\_1,6,7 0
- X\_1,5,7 -X\_2,4,7 0
- X\_1,5,7 -X\_2,5,7 0
- X\_1,5,7 -X\_2,6,7 0
- X\_1,5,7 -X\_3,4,7 0
- X\_1,5,7 -X\_3,5,7 0
- X\_1,5,7 -X\_3,6,7 0
- X\_1,6,7 -X\_2,4,7 0
- X\_1,6,7 -X\_2,5,7 0
- X\_1,6,7 -X\_2,6,7 0
- X\_1,6,7 -X\_3,4,7 0
- X\_1,6,7 -X\_3,5,7 0
- X\_1,6,7 -X\_3,6,7 0
- X\_2,4,7 -X\_2,5,7 0
- X\_2,4,7 -X\_2,6,7 0
- X\_2,4,7 -X\_3,4,7 0
- X\_2,4,7 -X\_3,5,7 0
- X\_2,4,7 -X\_3,6,7 0
- X\_2,5,7 -X\_2,6,7 0
- X\_2,5,7 -X\_3,4,7 0
- X\_2,5,7 -X\_3,5,7 0
- X\_2,5,7 -X\_3,6,7 0
- X\_2,6,7 -X\_3,4,7 0
- X\_2,6,7 -X\_3,5,7 0
- X\_2,6,7 -X\_3,6,7 0
- X\_3,4,7 -X\_3,5,7 0
- X\_3,4,7 -X\_3,6,7 0
- X\_3,5,7 -X\_3,6,7 0

X\_1,7,7 X\_1,8,7 X\_1,9,7 X\_2,7,7 X\_2,8,7 X\_2,9,7 X\_3,7,7 X\_3,8,7 X\_3,9,7 0

- X\_1,7,7 -X\_1,8,7 0
- X\_1,7,7 -X\_1,9,7 0
- X\_1,7,7 -X\_2,7,7 0
- X\_1,7,7 -X\_2,8,7 0
- X\_1,7,7 -X\_2,9,7 0
- X\_1,7,7 -X\_3,7,7 0
- X\_1,7,7 -X\_3,8,7 0
- X\_1,7,7 -X\_3,9,7 0
- X\_1,8,7 -X\_1,9,7 0
- X\_1,8,7 -X\_2,7,7 0
- X\_1,8,7 -X\_2,8,7 0
- X\_1,8,7 -X\_2,9,7 0
- X\_1,8,7 -X\_3,7,7 0
- X\_1,8,7 -X\_3,8,7 0
- X\_1,8,7 -X\_3,9,7 0
- X\_1,9,7 -X\_2,7,7 0
- X\_1,9,7 -X\_2,8,7 0
- X\_1,9,7 -X\_2,9,7 0
- X\_1,9,7 -X\_3,7,7 0
- X\_1,9,7 -X\_3,8,7 0
- X\_1,9,7 -X\_3,9,7 0
- X\_2,7,7 -X\_2,8,7 0
- X\_2,7,7 -X\_2,9,7 0
- X\_2,7,7 -X\_3,7,7 0
- X\_2,7,7 -X\_3,8,7 0
- X\_2,7,7 -X\_3,9,7 0
- X\_2,8,7 -X\_2,9,7 0
- X\_2,8,7 -X\_3,7,7 0
- X\_2,8,7 -X\_3,8,7 0
- X\_2,8,7 -X\_3,9,7 0
- X\_2,9,7 -X\_3,7,7 0
- X\_2,9,7 -X\_3,8,7 0
- X\_2,9,7 -X\_3,9,7 0
- X\_3,7,7 -X\_3,8,7 0
- X\_3,7,7 -X\_3,9,7 0
- X\_3,8,7 -X\_3,9,7 0

X\_4,1,7 X\_4,2,7 X\_4,3,7 X\_5,1,7 X\_5,2,7 X\_5,3,7 X\_6,1,7 X\_6,2,7 X\_6,3,7 0

- X\_4,1,7 -X\_4,2,7 0
- X\_4,1,7 -X\_4,3,7 0
- X\_4,1,7 -X\_5,1,7 0
- X\_4,1,7 -X\_5,2,7 0
- X\_4,1,7 -X\_5,3,7 0
- X\_4,1,7 -X\_6,1,7 0
- X\_4,1,7 -X\_6,2,7 0
- X\_4,1,7 -X\_6,3,7 0
- X\_4,2,7 -X\_4,3,7 0
- X\_4,2,7 -X\_5,1,7 0
- X\_4,2,7 -X\_5,2,7 0
- X\_4,2,7 -X\_5,3,7 0
- X\_4,2,7 -X\_6,1,7 0
- X\_4,2,7 -X\_6,2,7 0
- X\_4,2,7 -X\_6,3,7 0
- X\_4,3,7 -X\_5,1,7 0
- X\_4,3,7 -X\_5,2,7 0
- X\_4,3,7 -X\_5,3,7 0
- X\_4,3,7 -X\_6,1,7 0
- X\_4,3,7 -X\_6,2,7 0
- X\_4,3,7 -X\_6,3,7 0
- X\_5,1,7 -X\_5,2,7 0
- X\_5,1,7 -X\_5,3,7 0
- X\_5,1,7 -X\_6,1,7 0
- X\_5,1,7 -X\_6,2,7 0
- X\_5,1,7 -X\_6,3,7 0
- X\_5,2,7 -X\_5,3,7 0
- X\_5,2,7 -X\_6,1,7 0
- X\_5,2,7 -X\_6,2,7 0
- X\_5,2,7 -X\_6,3,7 0
- X\_5,3,7 -X\_6,1,7 0
- X\_5,3,7 -X\_6,2,7 0
- X\_5,3,7 -X\_6,3,7 0
- X\_6,1,7 -X\_6,2,7 0
- X\_6,1,7 -X\_6,3,7 0
- X\_6,2,7 -X\_6,3,7 0

X\_4,4,7 X\_4,5,7 X\_4,6,7 X\_5,4,7 X\_5,5,7 X\_5,6,7 X\_6,4,7 X\_6,5,7 X\_6,6,7 0

- X\_4,4,7 -X\_4,5,7 0
- X\_4,4,7 -X\_4,6,7 0
- X\_4,4,7 -X\_5,4,7 0
- X\_4,4,7 -X\_5,5,7 0
- X\_4,4,7 -X\_5,6,7 0
- X\_4,4,7 -X\_6,4,7 0
- X\_4,4,7 -X\_6,5,7 0
- X\_4,4,7 -X\_6,6,7 0
- X\_4,5,7 -X\_4,6,7 0
- X\_4,5,7 -X\_5,4,7 0
- X\_4,5,7 -X\_5,5,7 0
- X\_4,5,7 -X\_5,6,7 0
- X\_4,5,7 -X\_6,4,7 0
- X\_4,5,7 -X\_6,5,7 0
- X\_4,5,7 -X\_6,6,7 0
- X\_4,6,7 -X\_5,4,7 0
- X\_4,6,7 -X\_5,5,7 0
- X\_4,6,7 -X\_5,6,7 0
- X\_4,6,7 -X\_6,4,7 0
- X\_4,6,7 -X\_6,5,7 0
- X\_4,6,7 -X\_6,6,7 0
- X\_5,4,7 -X\_5,5,7 0
- X\_5,4,7 -X\_5,6,7 0
- X\_5,4,7 -X\_6,4,7 0
- X\_5,4,7 -X\_6,5,7 0
- X\_5,4,7 -X\_6,6,7 0
- X\_5,5,7 -X\_5,6,7 0
- X\_5,5,7 -X\_6,4,7 0
- X\_5,5,7 -X\_6,5,7 0
- X\_5,5,7 -X\_6,6,7 0
- X\_5,6,7 -X\_6,4,7 0
- X\_5,6,7 -X\_6,5,7 0
- X\_5,6,7 -X\_6,6,7 0
- X\_6,4,7 -X\_6,5,7 0
- X\_6,4,7 -X\_6,6,7 0
- X\_6,5,7 -X\_6,6,7 0

X\_4,7,7 X\_4,8,7 X\_4,9,7 X\_5,7,7 X\_5,8,7 X\_5,9,7 X\_6,7,7 X\_6,8,7 X\_6,9,7 0

- X\_4,7,7 -X\_4,8,7 0
- X\_4,7,7 -X\_4,9,7 0
- X\_4,7,7 -X\_5,7,7 0
- X\_4,7,7 -X\_5,8,7 0
- X\_4,7,7 -X\_5,9,7 0
- X\_4,7,7 -X\_6,7,7 0
- X\_4,7,7 -X\_6,8,7 0
- X\_4,7,7 -X\_6,9,7 0
- X\_4,8,7 -X\_4,9,7 0
- X\_4,8,7 -X\_5,7,7 0
- X\_4,8,7 -X\_5,8,7 0
- X\_4,8,7 -X\_5,9,7 0
- X\_4,8,7 -X\_6,7,7 0
- X\_4,8,7 -X\_6,8,7 0
- X\_4,8,7 -X\_6,9,7 0
- X\_4,9,7 -X\_5,7,7 0
- X\_4,9,7 -X\_5,8,7 0
- X\_4,9,7 -X\_5,9,7 0
- X\_4,9,7 -X\_6,7,7 0
- X\_4,9,7 -X\_6,8,7 0
- X\_4,9,7 -X\_6,9,7 0
- X\_5,7,7 -X\_5,8,7 0
- X\_5,7,7 -X\_5,9,7 0
- X\_5,7,7 -X\_6,7,7 0
- X\_5,7,7 -X\_6,8,7 0
- X\_5,7,7 -X\_6,9,7 0
- X\_5,8,7 -X\_5,9,7 0
- X\_5,8,7 -X\_6,7,7 0
- X\_5,8,7 -X\_6,8,7 0
- X\_5,8,7 -X\_6,9,7 0
- X\_5,9,7 -X\_6,7,7 0
- X\_5,9,7 -X\_6,8,7 0
- X\_5,9,7 -X\_6,9,7 0
- X\_6,7,7 -X\_6,8,7 0
- X\_6,7,7 -X\_6,9,7 0
- X\_6,8,7 -X\_6,9,7 0

X\_7,1,7 X\_7,2,7 X\_7,3,7 X\_8,1,7 X\_8,2,7 X\_8,3,7 X\_9,1,7 X\_9,2,7 X\_9,3,7 0

- X\_7,1,7 -X\_7,2,7 0
- X\_7,1,7 -X\_7,3,7 0
- X\_7,1,7 -X\_8,1,7 0
- X\_7,1,7 -X\_8,2,7 0
- X\_7,1,7 -X\_8,3,7 0
- X\_7,1,7 -X\_9,1,7 0
- X\_7,1,7 -X\_9,2,7 0
- X\_7,1,7 -X\_9,3,7 0
- X\_7,2,7 -X\_7,3,7 0
- X\_7,2,7 -X\_8,1,7 0
- X\_7,2,7 -X\_8,2,7 0
- X\_7,2,7 -X\_8,3,7 0
- X\_7,2,7 -X\_9,1,7 0
- X\_7,2,7 -X\_9,2,7 0
- X\_7,2,7 -X\_9,3,7 0
- X\_7,3,7 -X\_8,1,7 0
- X\_7,3,7 -X\_8,2,7 0
- X\_7,3,7 -X\_8,3,7 0
- X\_7,3,7 -X\_9,1,7 0
- X\_7,3,7 -X\_9,2,7 0
- X\_7,3,7 -X\_9,3,7 0
- X\_8,1,7 -X\_8,2,7 0
- X\_8,1,7 -X\_8,3,7 0
- X\_8,1,7 -X\_9,1,7 0
- X\_8,1,7 -X\_9,2,7 0
- X\_8,1,7 -X\_9,3,7 0
- X\_8,2,7 -X\_8,3,7 0
- X\_8,2,7 -X\_9,1,7 0
- X\_8,2,7 -X\_9,2,7 0
- X\_8,2,7 -X\_9,3,7 0
- X\_8,3,7 -X\_9,1,7 0
- X\_8,3,7 -X\_9,2,7 0
- X\_8,3,7 -X\_9,3,7 0
- X\_9,1,7 -X\_9,2,7 0
- X\_9,1,7 -X\_9,3,7 0
- X\_9,2,7 -X\_9,3,7 0

X\_7,4,7 X\_7,5,7 X\_7,6,7 X\_8,4,7 X\_8,5,7 X\_8,6,7 X\_9,4,7 X\_9,5,7 X\_9,6,7 0

- X\_7,4,7 -X\_7,5,7 0
- X\_7,4,7 -X\_7,6,7 0
- X\_7,4,7 -X\_8,4,7 0
- X\_7,4,7 -X\_8,5,7 0
- X\_7,4,7 -X\_8,6,7 0
- X\_7,4,7 -X\_9,4,7 0
- X\_7,4,7 -X\_9,5,7 0
- X\_7,4,7 -X\_9,6,7 0
- X\_7,5,7 -X\_7,6,7 0
- X\_7,5,7 -X\_8,4,7 0
- X\_7,5,7 -X\_8,5,7 0
- X\_7,5,7 -X\_8,6,7 0
- X\_7,5,7 -X\_9,4,7 0
- X\_7,5,7 -X\_9,5,7 0
- X\_7,5,7 -X\_9,6,7 0
- X\_7,6,7 -X\_8,4,7 0
- X\_7,6,7 -X\_8,5,7 0
- X\_7,6,7 -X\_8,6,7 0
- X\_7,6,7 -X\_9,4,7 0
- X\_7,6,7 -X\_9,5,7 0
- X\_7,6,7 -X\_9,6,7 0
- X\_8,4,7 -X\_8,5,7 0
- X\_8,4,7 -X\_8,6,7 0
- X\_8,4,7 -X\_9,4,7 0
- X\_8,4,7 -X\_9,5,7 0
- X\_8,4,7 -X\_9,6,7 0
- X\_8,5,7 -X\_8,6,7 0
- X\_8,5,7 -X\_9,4,7 0
- X\_8,5,7 -X\_9,5,7 0
- X\_8,5,7 -X\_9,6,7 0
- X\_8,6,7 -X\_9,4,7 0
- X\_8,6,7 -X\_9,5,7 0
- X\_8,6,7 -X\_9,6,7 0
- X\_9,4,7 -X\_9,5,7 0
- X\_9,4,7 -X\_9,6,7 0
- X\_9,5,7 -X\_9,6,7 0

X\_7,7,7 X\_7,8,7 X\_7,9,7 X\_8,7,7 X\_8,8,7 X\_8,9,7 X\_9,7,7 X\_9,8,7 X\_9,9,7 0

- X\_7,7,7 -X\_7,8,7 0
- X\_7,7,7 -X\_7,9,7 0
- X\_7,7,7 -X\_8,7,7 0
- X\_7,7,7 -X\_8,8,7 0
- X\_7,7,7 -X\_8,9,7 0
- X\_7,7,7 -X\_9,7,7 0
- X\_7,7,7 -X\_9,8,7 0
- X\_7,7,7 -X\_9,9,7 0
- X\_7,8,7 -X\_7,9,7 0
- X\_7,8,7 -X\_8,7,7 0
- X\_7,8,7 -X\_8,8,7 0
- X\_7,8,7 -X\_8,9,7 0
- X\_7,8,7 -X\_9,7,7 0
- X\_7,8,7 -X\_9,8,7 0
- X\_7,8,7 -X\_9,9,7 0
- X\_7,9,7 -X\_8,7,7 0
- X\_7,9,7 -X\_8,8,7 0
- X\_7,9,7 -X\_8,9,7 0
- X\_7,9,7 -X\_9,7,7 0
- X\_7,9,7 -X\_9,8,7 0
- X\_7,9,7 -X\_9,9,7 0
- X\_8,7,7 -X\_8,8,7 0
- X\_8,7,7 -X\_8,9,7 0
- X\_8,7,7 -X\_9,7,7 0
- X\_8,7,7 -X\_9,8,7 0
- X\_8,7,7 -X\_9,9,7 0
- X\_8,8,7 -X\_8,9,7 0
- X\_8,8,7 -X\_9,7,7 0
- X\_8,8,7 -X\_9,8,7 0
- X\_8,8,7 -X\_9,9,7 0
- X\_8,9,7 -X\_9,7,7 0
- X\_8,9,7 -X\_9,8,7 0
- X\_8,9,7 -X\_9,9,7 0
- X\_9,7,7 -X\_9,8,7 0
- X\_9,7,7 -X\_9,9,7 0
- X\_9,8,7 -X\_9,9,7 0

X\_1,1,8 X\_1,2,8 X\_1,3,8 X\_2,1,8 X\_2,2,8 X\_2,3,8 X\_3,1,8 X\_3,2,8 X\_3,3,8 0

- X\_1,1,8 -X\_1,2,8 0
- X\_1,1,8 -X\_1,3,8 0
- X\_1,1,8 -X\_2,1,8 0
- X\_1,1,8 -X\_2,2,8 0
- X\_1,1,8 -X\_2,3,8 0
- X\_1,1,8 -X\_3,1,8 0
- X\_1,1,8 -X\_3,2,8 0
- X\_1,1,8 -X\_3,3,8 0
- X\_1,2,8 -X\_1,3,8 0
- X\_1,2,8 -X\_2,1,8 0
- X\_1,2,8 -X\_2,2,8 0
- X\_1,2,8 -X\_2,3,8 0
- X\_1,2,8 -X\_3,1,8 0
- X\_1,2,8 -X\_3,2,8 0
- X\_1,2,8 -X\_3,3,8 0
- X\_1,3,8 -X\_2,1,8 0
- X\_1,3,8 -X\_2,2,8 0
- X\_1,3,8 -X\_2,3,8 0
- X\_1,3,8 -X\_3,1,8 0
- X\_1,3,8 -X\_3,2,8 0
- X\_1,3,8 -X\_3,3,8 0
- X\_2,1,8 -X\_2,2,8 0
- X\_2,1,8 -X\_2,3,8 0
- X\_2,1,8 -X\_3,1,8 0
- X\_2,1,8 -X\_3,2,8 0
- X\_2,1,8 -X\_3,3,8 0
- X\_2,2,8 -X\_2,3,8 0
- X\_2,2,8 -X\_3,1,8 0
- X\_2,2,8 -X\_3,2,8 0
- X\_2,2,8 -X\_3,3,8 0
- X\_2,3,8 -X\_3,1,8 0
- X\_2,3,8 -X\_3,2,8 0
- X\_2,3,8 -X\_3,3,8 0
- X\_3,1,8 -X\_3,2,8 0
- X\_3,1,8 -X\_3,3,8 0
- X\_3,2,8 -X\_3,3,8 0

X\_1,4,8 X\_1,5,8 X\_1,6,8 X\_2,4,8 X\_2,5,8 X\_2,6,8 X\_3,4,8 X\_3,5,8 X\_3,6,8 0

- X\_1,4,8 -X\_1,5,8 0
- X\_1,4,8 -X\_1,6,8 0
- X\_1,4,8 -X\_2,4,8 0
- X\_1,4,8 -X\_2,5,8 0
- X\_1,4,8 -X\_2,6,8 0
- X\_1,4,8 -X\_3,4,8 0
- X\_1,4,8 -X\_3,5,8 0
- X\_1,4,8 -X\_3,6,8 0
- X\_1,5,8 -X\_1,6,8 0
- X\_1,5,8 -X\_2,4,8 0
- X\_1,5,8 -X\_2,5,8 0
- X\_1,5,8 -X\_2,6,8 0
- X\_1,5,8 -X\_3,4,8 0
- X\_1,5,8 -X\_3,5,8 0
- X\_1,5,8 -X\_3,6,8 0
- X\_1,6,8 -X\_2,4,8 0
- X\_1,6,8 -X\_2,5,8 0
- X\_1,6,8 -X\_2,6,8 0
- X\_1,6,8 -X\_3,4,8 0
- X\_1,6,8 -X\_3,5,8 0
- X\_1,6,8 -X\_3,6,8 0
- X\_2,4,8 -X\_2,5,8 0
- X\_2,4,8 -X\_2,6,8 0
- X\_2,4,8 -X\_3,4,8 0
- X\_2,4,8 -X\_3,5,8 0
- X\_2,4,8 -X\_3,6,8 0
- X\_2,5,8 -X\_2,6,8 0
- X\_2,5,8 -X\_3,4,8 0
- X\_2,5,8 -X\_3,5,8 0
- X\_2,5,8 -X\_3,6,8 0
- X\_2,6,8 -X\_3,4,8 0
- X\_2,6,8 -X\_3,5,8 0
- X\_2,6,8 -X\_3,6,8 0
- X\_3,4,8 -X\_3,5,8 0
- X\_3,4,8 -X\_3,6,8 0
- X\_3,5,8 -X\_3,6,8 0

X\_1,7,8 X\_1,8,8 X\_1,9,8 X\_2,7,8 X\_2,8,8 X\_2,9,8 X\_3,7,8 X\_3,8,8 X\_3,9,8 0

- X\_1,7,8 -X\_1,8,8 0
- X\_1,7,8 -X\_1,9,8 0
- X\_1,7,8 -X\_2,7,8 0
- X\_1,7,8 -X\_2,8,8 0
- X\_1,7,8 -X\_2,9,8 0
- X\_1,7,8 -X\_3,7,8 0
- X\_1,7,8 -X\_3,8,8 0
- X\_1,7,8 -X\_3,9,8 0
- X\_1,8,8 -X\_1,9,8 0
- X\_1,8,8 -X\_2,7,8 0
- X\_1,8,8 -X\_2,8,8 0
- X\_1,8,8 -X\_2,9,8 0
- X\_1,8,8 -X\_3,7,8 0
- X\_1,8,8 -X\_3,8,8 0
- X\_1,8,8 -X\_3,9,8 0
- X\_1,9,8 -X\_2,7,8 0
- X\_1,9,8 -X\_2,8,8 0
- X\_1,9,8 -X\_2,9,8 0
- X\_1,9,8 -X\_3,7,8 0
- X\_1,9,8 -X\_3,8,8 0
- X\_1,9,8 -X\_3,9,8 0
- X\_2,7,8 -X\_2,8,8 0
- X\_2,7,8 -X\_2,9,8 0
- X\_2,7,8 -X\_3,7,8 0
- X\_2,7,8 -X\_3,8,8 0
- X\_2,7,8 -X\_3,9,8 0
- X\_2,8,8 -X\_2,9,8 0
- X\_2,8,8 -X\_3,7,8 0
- X\_2,8,8 -X\_3,8,8 0
- X\_2,8,8 -X\_3,9,8 0
- X\_2,9,8 -X\_3,7,8 0
- X\_2,9,8 -X\_3,8,8 0
- X\_2,9,8 -X\_3,9,8 0
- X\_3,7,8 -X\_3,8,8 0
- X\_3,7,8 -X\_3,9,8 0
- X\_3,8,8 -X\_3,9,8 0

X\_4,1,8 X\_4,2,8 X\_4,3,8 X\_5,1,8 X\_5,2,8 X\_5,3,8 X\_6,1,8 X\_6,2,8 X\_6,3,8 0

- X\_4,1,8 -X\_4,2,8 0
- X\_4,1,8 -X\_4,3,8 0
- X\_4,1,8 -X\_5,1,8 0
- X\_4,1,8 -X\_5,2,8 0
- X\_4,1,8 -X\_5,3,8 0
- X\_4,1,8 -X\_6,1,8 0
- X\_4,1,8 -X\_6,2,8 0
- X\_4,1,8 -X\_6,3,8 0
- X\_4,2,8 -X\_4,3,8 0
- X\_4,2,8 -X\_5,1,8 0
- X\_4,2,8 -X\_5,2,8 0
- X\_4,2,8 -X\_5,3,8 0
- X\_4,2,8 -X\_6,1,8 0
- X\_4,2,8 -X\_6,2,8 0
- X\_4,2,8 -X\_6,3,8 0
- X\_4,3,8 -X\_5,1,8 0
- X\_4,3,8 -X\_5,2,8 0
- X\_4,3,8 -X\_5,3,8 0
- X\_4,3,8 -X\_6,1,8 0
- X\_4,3,8 -X\_6,2,8 0
- X\_4,3,8 -X\_6,3,8 0
- X\_5,1,8 -X\_5,2,8 0
- X\_5,1,8 -X\_5,3,8 0
- X\_5,1,8 -X\_6,1,8 0
- X\_5,1,8 -X\_6,2,8 0
- X\_5,1,8 -X\_6,3,8 0
- X\_5,2,8 -X\_5,3,8 0
- X\_5,2,8 -X\_6,1,8 0
- X\_5,2,8 -X\_6,2,8 0
- X\_5,2,8 -X\_6,3,8 0
- X\_5,3,8 -X\_6,1,8 0
- X\_5,3,8 -X\_6,2,8 0
- X\_5,3,8 -X\_6,3,8 0
- X\_6,1,8 -X\_6,2,8 0
- X\_6,1,8 -X\_6,3,8 0
- X\_6,2,8 -X\_6,3,8 0

X\_4,4,8 X\_4,5,8 X\_4,6,8 X\_5,4,8 X\_5,5,8 X\_5,6,8 X\_6,4,8 X\_6,5,8 X\_6,6,8 0

- X\_4,4,8 -X\_4,5,8 0
- X\_4,4,8 -X\_4,6,8 0
- X\_4,4,8 -X\_5,4,8 0
- X\_4,4,8 -X\_5,5,8 0
- X\_4,4,8 -X\_5,6,8 0
- X\_4,4,8 -X\_6,4,8 0
- X\_4,4,8 -X\_6,5,8 0
- X\_4,4,8 -X\_6,6,8 0
- X\_4,5,8 -X\_4,6,8 0
- X\_4,5,8 -X\_5,4,8 0
- X\_4,5,8 -X\_5,5,8 0
- X\_4,5,8 -X\_5,6,8 0
- X\_4,5,8 -X\_6,4,8 0
- X\_4,5,8 -X\_6,5,8 0
- X\_4,5,8 -X\_6,6,8 0
- X\_4,6,8 -X\_5,4,8 0
- X\_4,6,8 -X\_5,5,8 0
- X\_4,6,8 -X\_5,6,8 0
- X\_4,6,8 -X\_6,4,8 0
- X\_4,6,8 -X\_6,5,8 0
- X\_4,6,8 -X\_6,6,8 0
- X\_5,4,8 -X\_5,5,8 0
- X\_5,4,8 -X\_5,6,8 0
- X\_5,4,8 -X\_6,4,8 0
- X\_5,4,8 -X\_6,5,8 0
- X\_5,4,8 -X\_6,6,8 0
- X\_5,5,8 -X\_5,6,8 0
- X\_5,5,8 -X\_6,4,8 0
- X\_5,5,8 -X\_6,5,8 0
- X\_5,5,8 -X\_6,6,8 0
- X\_5,6,8 -X\_6,4,8 0
- X\_5,6,8 -X\_6,5,8 0
- X\_5,6,8 -X\_6,6,8 0
- X\_6,4,8 -X\_6,5,8 0
- X\_6,4,8 -X\_6,6,8 0
- X\_6,5,8 -X\_6,6,8 0

X\_4,7,8 X\_4,8,8 X\_4,9,8 X\_5,7,8 X\_5,8,8 X\_5,9,8 X\_6,7,8 X\_6,8,8 X\_6,9,8 0

- X\_4,7,8 -X\_4,8,8 0
- X\_4,7,8 -X\_4,9,8 0
- X\_4,7,8 -X\_5,7,8 0
- X\_4,7,8 -X\_5,8,8 0
- X\_4,7,8 -X\_5,9,8 0
- X\_4,7,8 -X\_6,7,8 0
- X\_4,7,8 -X\_6,8,8 0
- X\_4,7,8 -X\_6,9,8 0
- X\_4,8,8 -X\_4,9,8 0
- X\_4,8,8 -X\_5,7,8 0
- X\_4,8,8 -X\_5,8,8 0
- X\_4,8,8 -X\_5,9,8 0
- X\_4,8,8 -X\_6,7,8 0
- X\_4,8,8 -X\_6,8,8 0
- X\_4,8,8 -X\_6,9,8 0
- X\_4,9,8 -X\_5,7,8 0
- X\_4,9,8 -X\_5,8,8 0
- X\_4,9,8 -X\_5,9,8 0
- X\_4,9,8 -X\_6,7,8 0
- X\_4,9,8 -X\_6,8,8 0
- X\_4,9,8 -X\_6,9,8 0
- X\_5,7,8 -X\_5,8,8 0
- X\_5,7,8 -X\_5,9,8 0
- X\_5,7,8 -X\_6,7,8 0
- X\_5,7,8 -X\_6,8,8 0
- X\_5,7,8 -X\_6,9,8 0
- X\_5,8,8 -X\_5,9,8 0
- X\_5,8,8 -X\_6,7,8 0
- X\_5,8,8 -X\_6,8,8 0
- X\_5,8,8 -X\_6,9,8 0
- X\_5,9,8 -X\_6,7,8 0
- X\_5,9,8 -X\_6,8,8 0
- X\_5,9,8 -X\_6,9,8 0
- X\_6,7,8 -X\_6,8,8 0
- X\_6,7,8 -X\_6,9,8 0
- X\_6,8,8 -X\_6,9,8 0

X\_7,1,8 X\_7,2,8 X\_7,3,8 X\_8,1,8 X\_8,2,8 X\_8,3,8 X\_9,1,8 X\_9,2,8 X\_9,3,8 0

- X\_7,1,8 -X\_7,2,8 0
- X\_7,1,8 -X\_7,3,8 0
- X\_7,1,8 -X\_8,1,8 0
- X\_7,1,8 -X\_8,2,8 0
- X\_7,1,8 -X\_8,3,8 0
- X\_7,1,8 -X\_9,1,8 0
- X\_7,1,8 -X\_9,2,8 0
- X\_7,1,8 -X\_9,3,8 0
- X\_7,2,8 -X\_7,3,8 0
- X\_7,2,8 -X\_8,1,8 0
- X\_7,2,8 -X\_8,2,8 0
- X\_7,2,8 -X\_8,3,8 0
- X\_7,2,8 -X\_9,1,8 0
- X\_7,2,8 -X\_9,2,8 0
- X\_7,2,8 -X\_9,3,8 0
- X\_7,3,8 -X\_8,1,8 0
- X\_7,3,8 -X\_8,2,8 0
- X\_7,3,8 -X\_8,3,8 0
- X\_7,3,8 -X\_9,1,8 0
- X\_7,3,8 -X\_9,2,8 0
- X\_7,3,8 -X\_9,3,8 0
- X\_8,1,8 -X\_8,2,8 0
- X\_8,1,8 -X\_8,3,8 0
- X\_8,1,8 -X\_9,1,8 0
- X\_8,1,8 -X\_9,2,8 0
- X\_8,1,8 -X\_9,3,8 0
- X\_8,2,8 -X\_8,3,8 0
- X\_8,2,8 -X\_9,1,8 0
- X\_8,2,8 -X\_9,2,8 0
- X\_8,2,8 -X\_9,3,8 0
- X\_8,3,8 -X\_9,1,8 0
- X\_8,3,8 -X\_9,2,8 0
- X\_8,3,8 -X\_9,3,8 0
- X\_9,1,8 -X\_9,2,8 0
- X\_9,1,8 -X\_9,3,8 0
- X\_9,2,8 -X\_9,3,8 0

X\_7,4,8 X\_7,5,8 X\_7,6,8 X\_8,4,8 X\_8,5,8 X\_8,6,8 X\_9,4,8 X\_9,5,8 X\_9,6,8 0

- X\_7,4,8 -X\_7,5,8 0
- X\_7,4,8 -X\_7,6,8 0
- X\_7,4,8 -X\_8,4,8 0
- X\_7,4,8 -X\_8,5,8 0
- X\_7,4,8 -X\_8,6,8 0
- X\_7,4,8 -X\_9,4,8 0
- X\_7,4,8 -X\_9,5,8 0
- X\_7,4,8 -X\_9,6,8 0
- X\_7,5,8 -X\_7,6,8 0
- X\_7,5,8 -X\_8,4,8 0
- X\_7,5,8 -X\_8,5,8 0
- X\_7,5,8 -X\_8,6,8 0
- X\_7,5,8 -X\_9,4,8 0
- X\_7,5,8 -X\_9,5,8 0
- X\_7,5,8 -X\_9,6,8 0
- X\_7,6,8 -X\_8,4,8 0
- X\_7,6,8 -X\_8,5,8 0
- X\_7,6,8 -X\_8,6,8 0
- X\_7,6,8 -X\_9,4,8 0
- X\_7,6,8 -X\_9,5,8 0
- X\_7,6,8 -X\_9,6,8 0
- X\_8,4,8 -X\_8,5,8 0
- X\_8,4,8 -X\_8,6,8 0
- X\_8,4,8 -X\_9,4,8 0
- X\_8,4,8 -X\_9,5,8 0
- X\_8,4,8 -X\_9,6,8 0
- X\_8,5,8 -X\_8,6,8 0
- X\_8,5,8 -X\_9,4,8 0
- X\_8,5,8 -X\_9,5,8 0
- X\_8,5,8 -X\_9,6,8 0
- X\_8,6,8 -X\_9,4,8 0
- X\_8,6,8 -X\_9,5,8 0
- X\_8,6,8 -X\_9,6,8 0
- X\_9,4,8 -X\_9,5,8 0
- X\_9,4,8 -X\_9,6,8 0
- X\_9,5,8 -X\_9,6,8 0

X\_7,7,8 X\_7,8,8 X\_7,9,8 X\_8,7,8 X\_8,8,8 X\_8,9,8 X\_9,7,8 X\_9,8,8 X\_9,9,8 0

- X\_7,7,8 -X\_7,8,8 0
- X\_7,7,8 -X\_7,9,8 0
- X\_7,7,8 -X\_8,7,8 0
- X\_7,7,8 -X\_8,8,8 0
- X\_7,7,8 -X\_8,9,8 0
- X\_7,7,8 -X\_9,7,8 0
- X\_7,7,8 -X\_9,8,8 0
- X\_7,7,8 -X\_9,9,8 0
- X\_7,8,8 -X\_7,9,8 0
- X\_7,8,8 -X\_8,7,8 0
- X\_7,8,8 -X\_8,8,8 0
- X\_7,8,8 -X\_8,9,8 0
- X\_7,8,8 -X\_9,7,8 0
- X\_7,8,8 -X\_9,8,8 0
- X\_7,8,8 -X\_9,9,8 0
- X\_7,9,8 -X\_8,7,8 0
- X\_7,9,8 -X\_8,8,8 0
- X\_7,9,8 -X\_8,9,8 0
- X\_7,9,8 -X\_9,7,8 0
- X\_7,9,8 -X\_9,8,8 0
- X\_7,9,8 -X\_9,9,8 0
- X\_8,7,8 -X\_8,8,8 0
- X\_8,7,8 -X\_8,9,8 0
- X\_8,7,8 -X\_9,7,8 0
- X\_8,7,8 -X\_9,8,8 0
- X\_8,7,8 -X\_9,9,8 0
- X\_8,8,8 -X\_8,9,8 0
- X\_8,8,8 -X\_9,7,8 0
- X\_8,8,8 -X\_9,8,8 0
- X\_8,8,8 -X\_9,9,8 0
- X\_8,9,8 -X\_9,7,8 0
- X\_8,9,8 -X\_9,8,8 0
- X\_8,9,8 -X\_9,9,8 0
- X\_9,7,8 -X\_9,8,8 0
- X\_9,7,8 -X\_9,9,8 0
- X\_9,8,8 -X\_9,9,8 0

X\_1,1,9 X\_1,2,9 X\_1,3,9 X\_2,1,9 X\_2,2,9 X\_2,3,9 X\_3,1,9 X\_3,2,9 X\_3,3,9 0

- X\_1,1,9 -X\_1,2,9 0
- X\_1,1,9 -X\_1,3,9 0
- X\_1,1,9 -X\_2,1,9 0
- X\_1,1,9 -X\_2,2,9 0
- X\_1,1,9 -X\_2,3,9 0
- X\_1,1,9 -X\_3,1,9 0
- X\_1,1,9 -X\_3,2,9 0
- X\_1,1,9 -X\_3,3,9 0
- X\_1,2,9 -X\_1,3,9 0
- X\_1,2,9 -X\_2,1,9 0
- X\_1,2,9 -X\_2,2,9 0
- X\_1,2,9 -X\_2,3,9 0
- X\_1,2,9 -X\_3,1,9 0
- X\_1,2,9 -X\_3,2,9 0
- X\_1,2,9 -X\_3,3,9 0
- X\_1,3,9 -X\_2,1,9 0
- X\_1,3,9 -X\_2,2,9 0
- X\_1,3,9 -X\_2,3,9 0
- X\_1,3,9 -X\_3,1,9 0
- X\_1,3,9 -X\_3,2,9 0
- X\_1,3,9 -X\_3,3,9 0
- X\_2,1,9 -X\_2,2,9 0
- X\_2,1,9 -X\_2,3,9 0
- X\_2,1,9 -X\_3,1,9 0
- X\_2,1,9 -X\_3,2,9 0
- X\_2,1,9 -X\_3,3,9 0
- X\_2,2,9 -X\_2,3,9 0
- X\_2,2,9 -X\_3,1,9 0
- X\_2,2,9 -X\_3,2,9 0
- X\_2,2,9 -X\_3,3,9 0
- X\_2,3,9 -X\_3,1,9 0
- X\_2,3,9 -X\_3,2,9 0
- X\_2,3,9 -X\_3,3,9 0
- X\_3,1,9 -X\_3,2,9 0
- X\_3,1,9 -X\_3,3,9 0
- X\_3,2,9 -X\_3,3,9 0

X\_1,4,9 X\_1,5,9 X\_1,6,9 X\_2,4,9 X\_2,5,9 X\_2,6,9 X\_3,4,9 X\_3,5,9 X\_3,6,9 0

- X\_1,4,9 -X\_1,5,9 0
- X\_1,4,9 -X\_1,6,9 0
- X\_1,4,9 -X\_2,4,9 0
- X\_1,4,9 -X\_2,5,9 0
- X\_1,4,9 -X\_2,6,9 0
- X\_1,4,9 -X\_3,4,9 0
- X\_1,4,9 -X\_3,5,9 0
- X\_1,4,9 -X\_3,6,9 0
- X\_1,5,9 -X\_1,6,9 0
- X\_1,5,9 -X\_2,4,9 0
- X\_1,5,9 -X\_2,5,9 0
- X\_1,5,9 -X\_2,6,9 0
- X\_1,5,9 -X\_3,4,9 0
- X\_1,5,9 -X\_3,5,9 0
- X\_1,5,9 -X\_3,6,9 0
- X\_1,6,9 -X\_2,4,9 0
- X\_1,6,9 -X\_2,5,9 0
- X\_1,6,9 -X\_2,6,9 0
- X\_1,6,9 -X\_3,4,9 0
- X\_1,6,9 -X\_3,5,9 0
- X\_1,6,9 -X\_3,6,9 0
- X\_2,4,9 -X\_2,5,9 0
- X\_2,4,9 -X\_2,6,9 0
- X\_2,4,9 -X\_3,4,9 0
- X\_2,4,9 -X\_3,5,9 0
- X\_2,4,9 -X\_3,6,9 0
- X\_2,5,9 -X\_2,6,9 0
- X\_2,5,9 -X\_3,4,9 0
- X\_2,5,9 -X\_3,5,9 0
- X\_2,5,9 -X\_3,6,9 0
- X\_2,6,9 -X\_3,4,9 0
- X\_2,6,9 -X\_3,5,9 0
- X\_2,6,9 -X\_3,6,9 0
- X\_3,4,9 -X\_3,5,9 0
- X\_3,4,9 -X\_3,6,9 0
- X\_3,5,9 -X\_3,6,9 0

X\_1,7,9 X\_1,8,9 X\_1,9,9 X\_2,7,9 X\_2,8,9 X\_2,9,9 X\_3,7,9 X\_3,8,9 X\_3,9,9 0

- X\_1,7,9 -X\_1,8,9 0
- X\_1,7,9 -X\_1,9,9 0
- X\_1,7,9 -X\_2,7,9 0
- X\_1,7,9 -X\_2,8,9 0
- X\_1,7,9 -X\_2,9,9 0
- X\_1,7,9 -X\_3,7,9 0
- X\_1,7,9 -X\_3,8,9 0
- X\_1,7,9 -X\_3,9,9 0
- X\_1,8,9 -X\_1,9,9 0
- X\_1,8,9 -X\_2,7,9 0
- X\_1,8,9 -X\_2,8,9 0
- X\_1,8,9 -X\_2,9,9 0
- X\_1,8,9 -X\_3,7,9 0
- X\_1,8,9 -X\_3,8,9 0
- X\_1,8,9 -X\_3,9,9 0
- X\_1,9,9 -X\_2,7,9 0
- X\_1,9,9 -X\_2,8,9 0
- X\_1,9,9 -X\_2,9,9 0
- X\_1,9,9 -X\_3,7,9 0
- X\_1,9,9 -X\_3,8,9 0
- X\_1,9,9 -X\_3,9,9 0
- X\_2,7,9 -X\_2,8,9 0
- X\_2,7,9 -X\_2,9,9 0
- X\_2,7,9 -X\_3,7,9 0
- X\_2,7,9 -X\_3,8,9 0
- X\_2,7,9 -X\_3,9,9 0
- X\_2,8,9 -X\_2,9,9 0
- X\_2,8,9 -X\_3,7,9 0
- X\_2,8,9 -X\_3,8,9 0
- X\_2,8,9 -X\_3,9,9 0
- X\_2,9,9 -X\_3,7,9 0
- X\_2,9,9 -X\_3,8,9 0
- X\_2,9,9 -X\_3,9,9 0
- X\_3,7,9 -X\_3,8,9 0
- X\_3,7,9 -X\_3,9,9 0
- X\_3,8,9 -X\_3,9,9 0

X\_4,1,9 X\_4,2,9 X\_4,3,9 X\_5,1,9 X\_5,2,9 X\_5,3,9 X\_6,1,9 X\_6,2,9 X\_6,3,9 0

- X\_4,1,9 -X\_4,2,9 0
- X\_4,1,9 -X\_4,3,9 0
- X\_4,1,9 -X\_5,1,9 0
- X\_4,1,9 -X\_5,2,9 0
- X\_4,1,9 -X\_5,3,9 0
- X\_4,1,9 -X\_6,1,9 0
- X\_4,1,9 -X\_6,2,9 0
- X\_4,1,9 -X\_6,3,9 0
- X\_4,2,9 -X\_4,3,9 0
- X\_4,2,9 -X\_5,1,9 0
- X\_4,2,9 -X\_5,2,9 0
- X\_4,2,9 -X\_5,3,9 0
- X\_4,2,9 -X\_6,1,9 0
- X\_4,2,9 -X\_6,2,9 0
- X\_4,2,9 -X\_6,3,9 0
- X\_4,3,9 -X\_5,1,9 0
- X\_4,3,9 -X\_5,2,9 0
- X\_4,3,9 -X\_5,3,9 0
- X\_4,3,9 -X\_6,1,9 0
- X\_4,3,9 -X\_6,2,9 0
- X\_4,3,9 -X\_6,3,9 0
- X\_5,1,9 -X\_5,2,9 0
- X\_5,1,9 -X\_5,3,9 0
- X\_5,1,9 -X\_6,1,9 0
- X\_5,1,9 -X\_6,2,9 0
- X\_5,1,9 -X\_6,3,9 0
- X\_5,2,9 -X\_5,3,9 0
- X\_5,2,9 -X\_6,1,9 0
- X\_5,2,9 -X\_6,2,9 0
- X\_5,2,9 -X\_6,3,9 0
- X\_5,3,9 -X\_6,1,9 0
- X\_5,3,9 -X\_6,2,9 0
- X\_5,3,9 -X\_6,3,9 0
- X\_6,1,9 -X\_6,2,9 0
- X\_6,1,9 -X\_6,3,9 0
- X\_6,2,9 -X\_6,3,9 0

X\_4,4,9 X\_4,5,9 X\_4,6,9 X\_5,4,9 X\_5,5,9 X\_5,6,9 X\_6,4,9 X\_6,5,9 X\_6,6,9 0

- X\_4,4,9 -X\_4,5,9 0
- X\_4,4,9 -X\_4,6,9 0
- X\_4,4,9 -X\_5,4,9 0
- X\_4,4,9 -X\_5,5,9 0
- X\_4,4,9 -X\_5,6,9 0
- X\_4,4,9 -X\_6,4,9 0
- X\_4,4,9 -X\_6,5,9 0
- X\_4,4,9 -X\_6,6,9 0
- X\_4,5,9 -X\_4,6,9 0
- X\_4,5,9 -X\_5,4,9 0
- X\_4,5,9 -X\_5,5,9 0
- X\_4,5,9 -X\_5,6,9 0
- X\_4,5,9 -X\_6,4,9 0
- X\_4,5,9 -X\_6,5,9 0
- X\_4,5,9 -X\_6,6,9 0
- X\_4,6,9 -X\_5,4,9 0
- X\_4,6,9 -X\_5,5,9 0
- X\_4,6,9 -X\_5,6,9 0
- X\_4,6,9 -X\_6,4,9 0
- X\_4,6,9 -X\_6,5,9 0
- X\_4,6,9 -X\_6,6,9 0
- X\_5,4,9 -X\_5,5,9 0
- X\_5,4,9 -X\_5,6,9 0
- X\_5,4,9 -X\_6,4,9 0
- X\_5,4,9 -X\_6,5,9 0
- X\_5,4,9 -X\_6,6,9 0
- X\_5,5,9 -X\_5,6,9 0
- X\_5,5,9 -X\_6,4,9 0
- X\_5,5,9 -X\_6,5,9 0
- X\_5,5,9 -X\_6,6,9 0
- X\_5,6,9 -X\_6,4,9 0
- X\_5,6,9 -X\_6,5,9 0
- X\_5,6,9 -X\_6,6,9 0
- X\_6,4,9 -X\_6,5,9 0
- X\_6,4,9 -X\_6,6,9 0
- X\_6,5,9 -X\_6,6,9 0

X\_4,7,9 X\_4,8,9 X\_4,9,9 X\_5,7,9 X\_5,8,9 X\_5,9,9 X\_6,7,9 X\_6,8,9 X\_6,9,9 0

- X\_4,7,9 -X\_4,8,9 0
- X\_4,7,9 -X\_4,9,9 0
- X\_4,7,9 -X\_5,7,9 0
- X\_4,7,9 -X\_5,8,9 0
- X\_4,7,9 -X\_5,9,9 0
- X\_4,7,9 -X\_6,7,9 0
- X\_4,7,9 -X\_6,8,9 0
- X\_4,7,9 -X\_6,9,9 0
- X\_4,8,9 -X\_4,9,9 0
- X\_4,8,9 -X\_5,7,9 0
- X\_4,8,9 -X\_5,8,9 0
- X\_4,8,9 -X\_5,9,9 0
- X\_4,8,9 -X\_6,7,9 0
- X\_4,8,9 -X\_6,8,9 0
- X\_4,8,9 -X\_6,9,9 0
- X\_4,9,9 -X\_5,7,9 0
- X\_4,9,9 -X\_5,8,9 0
- X\_4,9,9 -X\_5,9,9 0
- X\_4,9,9 -X\_6,7,9 0
- X\_4,9,9 -X\_6,8,9 0
- X\_4,9,9 -X\_6,9,9 0
- X\_5,7,9 -X\_5,8,9 0
- X\_5,7,9 -X\_5,9,9 0
- X\_5,7,9 -X\_6,7,9 0
- X\_5,7,9 -X\_6,8,9 0
- X\_5,7,9 -X\_6,9,9 0
- X\_5,8,9 -X\_5,9,9 0
- X\_5,8,9 -X\_6,7,9 0
- X\_5,8,9 -X\_6,8,9 0
- X\_5,8,9 -X\_6,9,9 0
- X\_5,9,9 -X\_6,7,9 0
- X\_5,9,9 -X\_6,8,9 0
- X\_5,9,9 -X\_6,9,9 0
- X\_6,7,9 -X\_6,8,9 0
- X\_6,7,9 -X\_6,9,9 0
- X\_6,8,9 -X\_6,9,9 0

X\_7,1,9 X\_7,2,9 X\_7,3,9 X\_8,1,9 X\_8,2,9 X\_8,3,9 X\_9,1,9 X\_9,2,9 X\_9,3,9 0

- X\_7,1,9 -X\_7,2,9 0
- X\_7,1,9 -X\_7,3,9 0
- X\_7,1,9 -X\_8,1,9 0
- X\_7,1,9 -X\_8,2,9 0
- X\_7,1,9 -X\_8,3,9 0
- X\_7,1,9 -X\_9,1,9 0
- X\_7,1,9 -X\_9,2,9 0
- X\_7,1,9 -X\_9,3,9 0
- X\_7,2,9 -X\_7,3,9 0
- X\_7,2,9 -X\_8,1,9 0
- X\_7,2,9 -X\_8,2,9 0
- X\_7,2,9 -X\_8,3,9 0
- X\_7,2,9 -X\_9,1,9 0
- X\_7,2,9 -X\_9,2,9 0
- X\_7,2,9 -X\_9,3,9 0
- X\_7,3,9 -X\_8,1,9 0
- X\_7,3,9 -X\_8,2,9 0
- X\_7,3,9 -X\_8,3,9 0
- X\_7,3,9 -X\_9,1,9 0
- X\_7,3,9 -X\_9,2,9 0
- X\_7,3,9 -X\_9,3,9 0
- X\_8,1,9 -X\_8,2,9 0
- X\_8,1,9 -X\_8,3,9 0
- X\_8,1,9 -X\_9,1,9 0
- X\_8,1,9 -X\_9,2,9 0
- X\_8,1,9 -X\_9,3,9 0
- X\_8,2,9 -X\_8,3,9 0
- X\_8,2,9 -X\_9,1,9 0
- X\_8,2,9 -X\_9,2,9 0
- X\_8,2,9 -X\_9,3,9 0
- X\_8,3,9 -X\_9,1,9 0
- X\_8,3,9 -X\_9,2,9 0
- X\_8,3,9 -X\_9,3,9 0
- X\_9,1,9 -X\_9,2,9 0
- X\_9,1,9 -X\_9,3,9 0
- X\_9,2,9 -X\_9,3,9 0

X\_7,4,9 X\_7,5,9 X\_7,6,9 X\_8,4,9 X\_8,5,9 X\_8,6,9 X\_9,4,9 X\_9,5,9 X\_9,6,9 0

- X\_7,4,9 -X\_7,5,9 0
- X\_7,4,9 -X\_7,6,9 0
- X\_7,4,9 -X\_8,4,9 0
- X\_7,4,9 -X\_8,5,9 0
- X\_7,4,9 -X\_8,6,9 0
- X\_7,4,9 -X\_9,4,9 0
- X\_7,4,9 -X\_9,5,9 0
- X\_7,4,9 -X\_9,6,9 0
- X\_7,5,9 -X\_7,6,9 0
- X\_7,5,9 -X\_8,4,9 0
- X\_7,5,9 -X\_8,5,9 0
- X\_7,5,9 -X\_8,6,9 0
- X\_7,5,9 -X\_9,4,9 0
- X\_7,5,9 -X\_9,5,9 0
- X\_7,5,9 -X\_9,6,9 0
- X\_7,6,9 -X\_8,4,9 0
- X\_7,6,9 -X\_8,5,9 0
- X\_7,6,9 -X\_8,6,9 0
- X\_7,6,9 -X\_9,4,9 0
- X\_7,6,9 -X\_9,5,9 0
- X\_7,6,9 -X\_9,6,9 0
- X\_8,4,9 -X\_8,5,9 0
- X\_8,4,9 -X\_8,6,9 0
- X\_8,4,9 -X\_9,4,9 0
- X\_8,4,9 -X\_9,5,9 0
- X\_8,4,9 -X\_9,6,9 0
- X\_8,5,9 -X\_8,6,9 0
- X\_8,5,9 -X\_9,4,9 0
- X\_8,5,9 -X\_9,5,9 0
- X\_8,5,9 -X\_9,6,9 0
- X\_8,6,9 -X\_9,4,9 0
- X\_8,6,9 -X\_9,5,9 0
- X\_8,6,9 -X\_9,6,9 0
- X\_9,4,9 -X\_9,5,9 0
- X\_9,4,9 -X\_9,6,9 0
- X\_9,5,9 -X\_9,6,9 0

X\_7,7,9 X\_7,8,9 X\_7,9,9 X\_8,7,9 X\_8,8,9 X\_8,9,9 X\_9,7,9 X\_9,8,9 X\_9,9,9 0

- X\_7,7,9 -X\_7,8,9 0
- X\_7,7,9 -X\_7,9,9 0
- X\_7,7,9 -X\_8,7,9 0
- X\_7,7,9 -X\_8,8,9 0
- X\_7,7,9 -X\_8,9,9 0
- X\_7,7,9 -X\_9,7,9 0
- X\_7,7,9 -X\_9,8,9 0
- X\_7,7,9 -X\_9,9,9 0
- X\_7,8,9 -X\_7,9,9 0
- X\_7,8,9 -X\_8,7,9 0
- X\_7,8,9 -X\_8,8,9 0
- X\_7,8,9 -X\_8,9,9 0
- X\_7,8,9 -X\_9,7,9 0
- X\_7,8,9 -X\_9,8,9 0
- X\_7,8,9 -X\_9,9,9 0
- X\_7,9,9 -X\_8,7,9 0
- X\_7,9,9 -X\_8,8,9 0
- X\_7,9,9 -X\_8,9,9 0
- X\_7,9,9 -X\_9,7,9 0
- X\_7,9,9 -X\_9,8,9 0
- X\_7,9,9 -X\_9,9,9 0
- X\_8,7,9 -X\_8,8,9 0
- X\_8,7,9 -X\_8,9,9 0
- X\_8,7,9 -X\_9,7,9 0
- X\_8,7,9 -X\_9,8,9 0
- X\_8,7,9 -X\_9,9,9 0
- X\_8,8,9 -X\_8,9,9 0
- X\_8,8,9 -X\_9,7,9 0
- X\_8,8,9 -X\_9,8,9 0
- X\_8,8,9 -X\_9,9,9 0
- X\_8,9,9 -X\_9,7,9 0
- X\_8,9,9 -X\_9,8,9 0
- X\_8,9,9 -X\_9,9,9 0
- X\_9,7,9 -X\_9,8,9 0
- X\_9,7,9 -X\_9,9,9 0
- X\_9,8,9 -X\_9,9,9 0
