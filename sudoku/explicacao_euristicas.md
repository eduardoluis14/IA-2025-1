1. Explicar as regras heuristicas do Sudoku
Equipe E: 13 - 16

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

Essas técnicas são úteis para Sudokus **difíceis ou diabólicos**, onde métodos básicos (como naked pairs ou swordfish) não são suficientes. Praticar com exemplos é a melhor forma de dominá-las!
