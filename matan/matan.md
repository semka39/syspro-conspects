# Математический анализ: Конспект лекций

## Свойства действительных чисел и неравенств

* **13)** $(-x) \cdot y = -(x \cdot y)$

  **Доказательство.**

  $$
  x \cdot y + (-x) \cdot y = (x + (-x)) \cdot y = 0 \cdot y = 0
  $$

  Следовательно, $(-x) \cdot y = -(x \cdot y)$. $\blacksquare$

* **Определение.** Говорят, что $x < y$, если $x \le y$ и $x \neq y$.

* $x \ge y \iff y \le x$

* $x > y \iff y < x$

* **1)** $\forall x, y \in \mathbb{R}$ выполняется ровно одно из утверждений: либо $x = y$, либо $x < y$, либо $x > y$.

  **Доказательство.**

  Если $x \le y$ и $y \le x$, то $x = y$.

  Пусть $x \neq y$. Тогда если $x \le y$, то $y \not\le x$, и $x < y$.

  Если же $y \le x$, то $x \not\le y$, и $y < x$. $\blacksquare$

* **2)** $x > 0 \implies -x < 0$

  **Доказательство.**

  Пусть $x > 0$, то есть $x \ge 0$ и $x \neq 0$.

  По аксиоме 11:

  $$
  x + (-x) \ge 0 + (-x) \implies 0 \ge -x, \quad \text{то есть } -x \le 0
  $$

  Если бы $-x = 0$, то и $x = 0$, следовательно, $-x \neq 0$, значит, $-x < 0$. $\blacksquare$

* **3)** $x < 0, \; y < 0 \implies x \cdot y > 0$

  **Доказательство.**

  Пусть $x < 0$ и $y < 0$, тогда $-x > 0$ и $-y > 0$, то есть $-x \ge 0$, $-y \ge 0$, $-x \neq 0$, $-y \neq 0$.

  По аксиоме 12: $-x \cdot (-y) \ge 0$.

  По свойству 10: $(-x)(-y) \neq 0$, иначе было бы $-x = 0$ или $-y = 0$. То есть $-x(-y) > 0$.

  По свойствам 13) и 12):

  $$
  -x(-y) = -(x(-y)) = -(-yx) = -(-(yx)) = yx = xy > 0. \quad \blacksquare
  $$

* **3')** $x > 0, \; y > 0 \implies xy > 0$ (Аксиома 12: $x \ge 0, y \ge 0 \implies xy \ge 0$)

* **3'')** $x > 0, \; y < 0 \implies xy < 0$ (доказывается аналогично)

* **4)** $0 < 1$

  **Доказательство.**

  Мы знаем, что $0 \neq 1$. Предположим, что $1 < 0$.

  $$
  1 < 0, \; 1 < 0 \implies 1 \cdot 1 > 0 \implies 1 > 0 \quad \text{--- противоречие.}
  $$

  Следовательно, $0 < 1$. $\blacksquare$

* **5)**

  * $x < y, \; y \le z \implies x < z$ *(Упражнение)*

  * $x \le y, \; y < z \implies x < z$ *(Упражнение)*

* **6)** $x < y \implies x + z < y + z$ *(Упражнение)*

* **6')** $x \le y, \; z \le w \implies x + z \le y + w$

  *(Доказательство:* $x + z \le y + z \le y + w$ *по аксиоме 11)*

* **6'')** $x \le y, \; z < w \implies x + z < y + w$

* **7)**

  * $x < y, \; z > 0 \implies xz < yz$

  * $x < y, \; z < 0 \implies xz > yz$

  **Доказательство.**

  Пусть $x < y, \; z > 0$, то есть $y + (-x) > 0, \; z > 0$.

  По свойству 3): $(y + (-x)) \cdot z > 0$.

  $$
  yz + (-x)z > 0 \implies (yz + (-xz)) + xz > 0 + xz \implies yz + (-xz + xz) > xz \implies yz > xz \implies xz < yz. \quad \blacksquare
  $$

* **8)**

  * $x > 0 \implies \frac{1}{x} > 0$ *(Упражнение)*

  * $x > 0, \; x < y \implies \frac{1}{x} > \frac{1}{y}$

  **Доказательство.**

  Если бы $\frac{1}{x} = \frac{1}{y}$, то $\left(\frac{1}{x}\right)^{-1} = \left(\frac{1}{y}\right)^{-1}$, то есть $x = y$.

  Предположим, что $\frac{1}{x} < \frac{1}{y}$, тогда по свойству 7):

  $$
  x \cdot \frac{1}{x} < x \cdot \frac{1}{y} \implies 1 < x \frac{1}{y} \implies 1 \cdot y < \left(x \frac{1}{y}\right)y \implies y < x\left(\frac{1}{y} y\right) \implies y < x \quad \text{--- противоречие!}
  $$

  Следовательно, $\frac{1}{x} > \frac{1}{y}$. $\blacksquare$

## Промежутки на $\mathbb{R}$ и $\overline{\mathbb{R}}$

* **Отрезок:** $[a, b] = \{x \in \mathbb{R} \mid a \le x \le b\}, \quad a \le b, \; a, b \in \mathbb{R}$.

* **Интервал:** $(a, b) = \{x \in \mathbb{R} \mid a < x < b\}$.

* Если $a = b$, то $[a, a] = \{a\}$, $(a, a) = \emptyset$.

* **Неограниченные интервалы:**

  $$
  (a, +\infty) = \{x \in \mathbb{R} \mid x > a\} \quad \text{и} \quad (-\infty, b) = \{x \in \mathbb{R} \mid x < b\}
  $$

* $(-\infty, +\infty) = \mathbb{R}$

* **Полуинтервалы:**

  $$
  [a, b) = \{x \in \mathbb{R} \mid a \le x < b\} \quad \text{и} \quad (a, b] = \{x \in \mathbb{R} \mid a < x \le b\}
  $$

* **Неограниченные полуинтервалы:**

  $$
  [a, +\infty) = \{x \in \mathbb{R} \mid x \ge a\} \quad \text{и} \quad (-\infty, b] = \{x \in \mathbb{R} \mid x \le b\}
  $$

* Условимся обозначать промежуток через $\langle a, b \rangle$, если нам не важно, входят в него его концы или нет.

* На расширенной числовой прямой можно также рассмотреть промежутки вида:

  $$
  [a, +\infty], \quad [-\infty, b], \quad (a, +\infty], \quad [-\infty, b), \quad [-\infty, +\infty] = \overline{\mathbb{R}}
  $$

## §3. Модуль числа. Расстояние между числами

**Модуль (абсолютная величина):**

$$
|x| = \begin{cases} x, & x \ge 0 \\ -x, & x < 0 \end{cases}
$$

### Свойства модуля:

* **1)** $|x| \ge 0$, причём $|x| = 0 \iff x = 0$.

* **2)** $|x \cdot y| = |x| \cdot |y|, \quad \left|\frac{x}{y}\right| = \frac{|x|}{|y|}$.

* **3)** $-|x| \le x \le |x|$.

* **4)** Для $a > 0$: $|x| \le a \iff -a \le x \le a$ и $|x| < a \iff -a < x < a$ *(свойства 1–4 — Упражнение)*.

* **5)** **Неравенство треугольника:** $|x+y| \le |x| + |y|$.

  **Доказательство.** Из свойства 3):

  $$
  \begin{cases} -|x| \le x \le |x| \\ -|y| \le y \le |y| \end{cases} \implies -|x|-|y| \le x+y \le |x|+|y| \implies -(|x|+|y|) \le x+y \le |x|+|y|
  $$

  По свойству 4) (где $a = |x|+|y| \ge 0$): $|x+y| \le |x|+|y|$. $\blacksquare$

* **6)** $|x-y| \ge ||x| - |y||$.

  **Доказательство.** По свойству 5):

  $$
  |x| = |(x-y) + y| \le |x-y| + |y|, \quad \text{то есть } |x-y| \ge |x| - |y|
  $$

  Аналогично:

  $$
  |x-y| = |-(y-x)| = |y-x| \ge |y| - |x| = -(|x| - |y|)
  $$

  $$
  -|x-y| \le |x| - |y| \le |x-y|
  $$

  По свойству 4): $||x| - |y|| \le |x-y|$. $\blacksquare$

### Расстояние и знак

* **Определение.** Расстояние между числами $x, y \in \mathbb{R}$:

  $$
  d(x,y) = |x-y|
  $$

**Свойства расстояния:**

* **1)** $d(x,y) \ge 0$, причём $d(x,y) = 0 \iff x = y$.

* **2)** $d(x,y) = d(y,x)$.

* **3)** $d(x,z) \le d(x,y) + d(y,z)$ — *неравенство треугольника*.

  **Доказательство 3):**

  $$
  d(x,z) = |x-z| = |(x-y) + (y-z)| \le |x-y| + |y-z| = d(x,y) + d(y,z). \quad \blacksquare
  $$

* **Знак числа** $x \in \mathbb{R}$**:**

  $$
  \operatorname{sign} x = \begin{cases} 1, & x > 0 \\ 0, & x = 0 \\ -1, & x < 0 \end{cases}
  $$

* **Замечание.** $x = \operatorname{sign} x \cdot |x|$.

## §4. Верхние и нижние грани числовых множеств

* **Аксиома 13 (непрерывности, полноты):**

  Если $X \subset \mathbb{R}$, $Y \subset \mathbb{R}$, $X \neq \emptyset, \; Y \neq \emptyset$, и $\forall x \in X \quad \forall y \in Y \quad x \le y$, то:

  $$
  \exists c \in \mathbb{R}: \forall x \in X \quad \forall y \in Y \quad x \le c \le y
  $$

* **Определение.** Пусть $A \subset \mathbb{R}$, $A \neq \emptyset$.

  * Число $M \in A$ называется **наибольшим элементом множества** $A$ ($M = \max A$), если $\forall x \in A \quad x \le M$.

  * Число $m \in A$ называется **наименьшим элементом множества** $A$ ($m = \min A$), если $\forall x \in A \quad x \ge m$.

* **Замечание.** $\min A, \; \max A$ не всегда существуют.

* **Определение.** Множество $A \subset \mathbb{R}$, $A \neq \emptyset$ называется **ограниченным сверху**, если:

  $$
  \exists b \in \mathbb{R}: \forall x \in A \quad x \le b
  $$

  Любое число $b \in \mathbb{R}$ из этого определения называется **верхней гранью** множества $A$.

* **Определение.** Множество $A \subset \mathbb{R}$, $A \neq \emptyset$ называется **ограниченным снизу**, если:

  $$
  \exists a \in \mathbb{R}: \forall x \in A \quad x \ge a
  $$

  (здесь $a \in \mathbb{R}$ — **нижняя грань** множества $A$).

* **Определение.** Множество $A \subset \mathbb{R}$, $A \neq \emptyset$ называется **ограниченным**, если оно ограничено и снизу, и сверху, то есть:

  $$
  \exists a, b \in \mathbb{R}: \forall x \in A \quad a \le x \le b
  $$

* **Свойство.** $A \subset \mathbb{R}$ ограничено $\iff \exists M > 0: \forall x \in A \quad |x| \le M$ *(упражнение)*.

* **Определение.** **Точной верхней гранью** множества $A \neq \emptyset$ называется наименьшая среди всех его верхних граней, обозначается $\sup A$, supremum, то есть $b = \sup A$, если:

  * **1.** $\forall x \in A \quad x \le b$;

  * **2.** Если $b'$ — верхняя грань $A$, то $b \le b'$.

  * **2'.** Если $b' < b$, то $\exists x \in A: x > b'$.

  * **2''.** $\forall \varepsilon > 0 \quad \exists x \in A: x > b - \varepsilon$.

* **Замечание.** Если $\sup A \in A$, то $\max A = \sup A$.

* **Замечание.** Если $A \neq \emptyset$ не ограничено сверху, то полагаем $\sup A = +\infty$.

### Лемма (о точной верхней грани)

Любое ограниченное сверху множество $A \neq \emptyset$ имеет точную верхнюю грань $\sup A \in \mathbb{R}$.

**Доказательство.**

Пусть $A \neq \emptyset$ и ограничено сверху. Обозначим через $B \subset \mathbb{R}$ множество всех его конечных верхних граней:

$$
B = \{b \in \mathbb{R} \mid \forall x \in A \quad x \le b\}
$$

Заметим, что $B \neq \emptyset$, так как $A$ ограничено сверху.

Таким образом, $\forall x \in A \quad \forall b \in B \quad x \le b$.

По аксиоме полноты, $\exists c \in \mathbb{R}: \forall x \in A \quad \forall b \in B \quad x \le c \le b$.

Так как $\forall x \in A \quad x \le c$, то $c$ — верхняя грань $A$, то есть $c \in B$.

Так как $\forall b \in B \quad c \le b$, то $c = \min B$, то есть $c = \sup A$. $\blacksquare$

* **Следствие.** Любое множество $A \subset \mathbb{R}$ имеет (конечную или бесконечную) точную верхнюю грань:

  * $\sup A \in \mathbb{R}$, если $A$ ограничено сверху;

  * $\sup A = +\infty$, если $A$ не ограничено сверху;

  * $\sup A = -\infty$, если $A = \emptyset$.

### Точная нижняя грань

* **Определение.** **Точной нижней гранью** множества $A \neq \emptyset$ (обозначается $\inf A$, «infimum») называется наибольшая из всех его нижних граней: $a = \inf A$, если:

  * **1.** $\forall x \in A \quad x \ge a$;

  * **2.** Если $a'$ — нижняя грань $A$, то $a \ge a'$.

  * *(2', 2'' сформулируйте самостоятельно)*

* **Замечание.** Если $\inf A \in A$, то $\inf A = \min A$.

* **Замечание.** Если $A$ не ограничено снизу, то полагаем $\inf A = -\infty$.

* **Замечание.** Для $\emptyset$ полагаем $\sup \emptyset = -\infty, \; \inf \emptyset = +\infty$.

* **Замечание.** $\inf A \le \sup A$ для любого $A \neq \emptyset$.

* **Упражнение.** Сформулируйте и докажите лемму о точной нижней грани и её следствие.

* **Замечание.** Если $A \subset B$, то $\inf A \ge \inf B, \; \sup A \le \sup B$. (Следует из того, что $\sup B$ является верхней гранью для любого $A \subset B$, и для $\inf B$ — аналогично).

### Пример

* Для любого промежутка $\langle a, b \rangle \neq \emptyset$:

  $$
  \inf \langle a, b \rangle = a, \quad \sup \langle a, b \rangle = b
  $$

* Рассмотрим, например, $A = [a, b)$, где $a, b \in \mathbb{R}$.

  * $\inf A = \min A = a$, так как 1) $\forall x \in A \quad x \ge a$ и 2) $a \in A$.

  * $\sup A = b$, так как 1) $\forall x \in A \quad x \le b$ и 2'') $\forall \varepsilon > 0 \quad \exists x \in A: x > b - \varepsilon$.

    *(Выберем* $x = b - \frac{\varepsilon}{2}$*, если* $b - \frac{\varepsilon}{2} > a$*, и* $x = \frac{a+b}{2}$*, если* $b - \frac{\varepsilon}{2} \le a$*)*.

  * Так как $\sup A = b \notin A$, то $\max A$ не существует.

## §5. Индуктивные множества. Принцип математической индукции. Натуральные, целые и рациональные числа

* **Определение.** Множество $X \subset \mathbb{R}$ называется **индуктивным**, если:

  $$
  \forall x \in X \implies x+1 \in X
  $$

* **Примеры:** $\mathbb{R}, \; [0, +\infty), \; [a, +\infty)$.

* **Замечание.** Пересечение любой совокупности индуктивных множеств является индуктивным множеством.

  **Доказательство.** Пусть $\{X_\alpha\}$ — семейство индуктивных множеств, и $X = \bigcap_{\alpha \in A} X_\alpha$, где $A$ — множество индексов.

  Пусть $x \in X = \bigcap_{\alpha \in A} X_\alpha$, тогда $x \in X_\alpha \quad \forall \alpha \in A$.

  Так как все $X_\alpha$ индуктивные, то $x+1 \in X_\alpha \quad \forall \alpha \in A$, значит, $x+1 \in \bigcap_{\alpha \in A} X_\alpha$. $\blacksquare$

* **Определение.** **Множеством натуральных чисел** $\mathbb{N}$ называется наименьшее индуктивное множество, содержащее 1, то есть пересечение всех индуктивных множеств, содержащих 1:

  $$
  \mathbb{N} = \{1, 1+1, (1+1)+1, \dots\}
  $$

* **Определение.** **Множество целых чисел:**

  $$
  \mathbb{Z} = \{m - n \mid m, n \in \mathbb{N}\}
  $$

  *Эквивалентно:* $\mathbb{Z} = \mathbb{N} \cup \{0\} \cup \{-n \mid n \in \mathbb{N}\}$.

### Принципы индукции

* **Принцип математической индукции:**

  Если $E \subset \mathbb{N}$ таково, что:

  1. $1 \in E$;

  2. $\forall n \in E \implies n+1 \in E$,

  то $E = \mathbb{N}$.

  **Доказательство.** Из 2) и 1) следует, что $E$ — индуктивное множество, причём $1 \in E$.

  Так как $\mathbb{N}$ — пересечение всех индуктивных множеств, содержащих 1, то $\mathbb{N} \subset E$. Следовательно, $E = \mathbb{N}$. $\blacksquare$

* **Индукция вниз:**

  Если $F \subset \mathbb{N}$ таково, что 1) $n \in F$ и 2) $\forall x \in F, \; x > 1 \implies x-1 \in F$, то $\{1, 2, \dots, n\} \subset F$.

  *(Доказательство в пособии С.К. Водопьянова, стр. 28)*.

### Свойства натуральных и целых чисел

* **1)** Сумма и произведение натуральных чисел являются натуральными числами.

  **Доказательство.**

  * **а)** Пусть $m, n \in \mathbb{N}$, докажем, что $m+n \in \mathbb{N}$.

    Обозначим $E = \{n \in \mathbb{N} \mid m+n \in \mathbb{N} \quad \forall m \in \mathbb{N}\} \subset \mathbb{N}$.

    Докажем, что $1 \in E$, и что $E$ — индуктивное множество.

    Так как $\mathbb{N}$ индуктивно, то $\forall m \in \mathbb{N} \quad m+1 \in \mathbb{N}$, значит, $1 \in E$.

    Пусть $n \in E$, то есть $\forall m \in \mathbb{N} \quad m+n \in \mathbb{N}$. Но тогда и $\forall m \in \mathbb{N} \quad m+(n+1) = (m+n)+1 \in \mathbb{N}$, то есть $n+1 \in E$. Значит, $E$ — индуктивно.

    Из принципа математической индукции следует, что $E = \mathbb{N}$.

    То есть $\forall n \in \mathbb{N} \quad \forall m \in \mathbb{N} \quad m+n \in \mathbb{N}$.

  * **б)** Обозначим $E = \{n \in \mathbb{N} \mid \forall m \in \mathbb{N} \quad m \cdot n \in \mathbb{N}\} \subset \mathbb{N}$.

    Так как $\forall m \in \mathbb{N} \quad m \cdot 1 = m \in \mathbb{N}$, то $1 \in E$.

    Пусть $n \in E$, то есть $\forall m \in \mathbb{N} \quad m \cdot n \in \mathbb{N}$.

    Но тогда и $\forall m \in \mathbb{N} \quad m \cdot (n+1) = m \cdot n + m \in \mathbb{N}$ (из пункта (а)).

    Значит, $E$ — индуктивное множество. По принципу математической индукции, $E = \mathbb{N}$, то есть $\forall n \in \mathbb{N} \quad \forall m \in \mathbb{N} \quad m \cdot n \in \mathbb{N}$. $\blacksquare$

* **2)** Если $n \in \mathbb{N}$ и $n > 1$, то $n-1 \in \mathbb{N}$.

  **Доказательство.**

  Пусть $E = \{n \in \mathbb{N} \mid n > 1, \; n-1 \in \mathbb{N}\} \cup \{1\}$. Тогда $1 \in E$ и $E \subset \mathbb{N}$.

  Пусть $n \in E$.

  Если $n = 1$, то $n+1 = 2 \in E$, так как $2 > 1$, и $2-1 = 1 \in \mathbb{N}$.

  Если $n > 1$, то $n+1 > n > 1$, и $(n+1)-1 = n \in \mathbb{N}$. Следовательно, $n+1 \in E$.

  То есть $E$ — индуктивное множество. Из принципа математической индукции, $E = \mathbb{N}$.

  То есть для всех $n \in \mathbb{N}$ таких, что $n > 1$, верно $n-1 \in \mathbb{N}$. $\blacksquare$

* **3)** Если $n, m \in \mathbb{N}$ и $n < m$, то $m - n \in \mathbb{N}$.

  **Доказательство.**

  Пусть $E = \{n \in \mathbb{N} \mid \forall m \in \mathbb{N} \text{ из } m > n \implies m-n \in \mathbb{N}\} \subset \mathbb{N}$.

  $1 \in E$ по свойству (2): $\forall m \in \mathbb{N} \text{ из } m > 1 \implies m-1 \in \mathbb{N}$.

  Предположим, что $n \in E$, то есть $\forall m \in \mathbb{N}$ таких, что $m > n$, выполняется $m-n \in \mathbb{N}$. Докажем, что $n+1 \in E$.

  Пусть $m \in \mathbb{N}$ — произвольное, такое, что $m > n+1$. Тогда тем более $m > n$, следовательно, $m-n \in \mathbb{N}$.

  Кроме того, $m-n > 1$. По свойству (2): $(m-n)-1 = m-(n+1) \in \mathbb{N}$.

  То есть $\forall m \in \mathbb{N}$ из $m > n+1 \implies m-(n+1) \in \mathbb{N}$, а это означает, что $n+1 \in E$.

  По принципу математической индукции, $E = \mathbb{N}$, то есть $\forall n \in \mathbb{N} \quad \forall m \in \mathbb{N} \quad (m > n \implies m-n \in \mathbb{N})$. $\blacksquare$

* **4)** Если $x, y \in \mathbb{Z}$ и $x < y$, то $y - x \in \mathbb{N}$ и $x+1 \le y$.

  **Доказательство.**

  $\mathbb{Z} = \{m-n \mid m, n \in \mathbb{N}\}$.

  Пусть $x, y \in \mathbb{Z}$, то есть $x = p-q, \; y = r-s$, где $p, q, r, s \in \mathbb{N}$.

  Тогда $x < y$, если $p-q < r-s$, то есть $p+s < q+r$.

  Так как $p+s, \; q+r \in \mathbb{N}$, то по свойству 3):

  $$
  q+r - (p+s) = (r-s) - (p-q) = y - x \in \mathbb{N}, \quad \text{и, следовательно, } y - x \ge 1. \quad \blacksquare
  $$

* **5) (Принцип минимального числа)**

  Всякое ограниченное снизу непустое множество $E \subset \mathbb{Z}$ имеет наименьший элемент.

  **Доказательство.**

  По лемме о точной нижней грани существует $k = \inf E \in \mathbb{R}$.

  По свойству инфимума: $\forall \varepsilon > 0 \quad \exists x \in E: \quad k \le x < k + \varepsilon$.

  Для $\varepsilon = 1$: $\exists x \in E: \quad k \le x < k+1 \implies k > x-1$.

  Для любого $y \in E$: $y \ge k$, то есть $y \ge k > x-1 \quad \forall y \in E$.

  Следовательно, так как $y > x-1$, то по свойству (4): $y - (x-1) \ge 1 \implies y \ge x \quad \forall y \in E$.

  То есть $x = \min E$. $\blacksquare$

* **6) (Принцип максимального числа)**

  Всякое ограниченное сверху непустое множество $E \subset \mathbb{Z}$ имеет наибольший элемент.

  **Доказательство.**

  По лемме о точной верхней грани существует конечное число $k = \sup E \in \mathbb{R}$.

  По свойству точной верхней грани для $\varepsilon = 1$ найдётся элемент $x \in E$ такой, что:

  $$
  k - 1 < x \le k
  $$

  Возьмём произвольный элемент $y \in E$. Так как $k = \sup E$, то $y \le k$.

  С учётом $k < x + 1$ получаем неравенство $y \le k < x + 1$, откуда $y < x + 1$.

  Так как $x, y \in \mathbb{Z}$, по свойству 4 из $y < x+1$ следует, что $y + 1 \le x + 1$, то есть $y \le x$.

  Поскольку $y \le x$ верно для всех $y \in E$ и сам $x \in E$, то $x = \max E$. $\blacksquare$

### Принцип Архимеда

* **1)** Множество $\mathbb{N}$ не ограничено сверху.

  **Доказательство.** Если бы $\mathbb{N}$ было ограничено сверху, то по свойству (6) (принцип максимального числа) существовал бы наибольший элемент $n \in \mathbb{N}$:

  $$
  \exists n \in \mathbb{N}: \forall m \in \mathbb{N} \quad m \le n
  $$

  Но тогда $n+1 \in \mathbb{N}$, и $n+1 > n$ — противоречие.

  *Следствие.* Множество $\mathbb{Z}$ не ограничено ни снизу, ни сверху.

  **Доказательство.** Если $\mathbb{Z}$ ограничено снизу, то $-\mathbb{N} = \{-n \mid n \in \mathbb{N}\} \subset \mathbb{Z}$ ограничено снизу, но тогда $\mathbb{N}$ ограничено сверху — противоречие. $\blacksquare$

* **2) (Принцип Архимеда).** Если $x, y \in \mathbb{R}, \; y \ge 0, \; x > 0$, то $\exists n \in \mathbb{N}: y < nx$.

## Бином Ньютона

### Свойства биномиальных коэффициентов:

* **1)** $C_n^k = C_n^{n-k}$

* **2)** $C_n^0 = C_n^n = 1, \quad C_n^1 = C_n^{n-1} = n, \quad C_n^2 = \frac{n(n-1)}{2}$

* **3)** $C_n^k + C_n^{k-1} = C_{n+1}^k$

  **Доказательство 3).**

  $$
  C_n^k + C_n^{k-1} = \frac{n!}{k!(n-k)!} + \frac{n!}{(k-1)!(n-k+1)!} = \frac{n!(n-k+1) + n!k}{k!(n-k+1)!} = \frac{n!(n+1)}{k!(n+1-k)!} = C_{n+1}^k. \quad \blacksquare
  $$

### Формула бинома Ньютона:

$$
(x+y)^n = \sum_{k=0}^n C_n^k x^{n-k} y^k = C_n^0 x^n y^0 + C_n^1 x^{n-1} y^1 + C_n^2 x^{n-2} y^2 + \dots + C_n^{n-1} x^1 y^{n-1} + C_n^n x^0 y^n
$$

**Доказательство по индукции.**

Пусть $E = \{n \in \mathbb{N} \mid \text{верна формула бинома Ньютона}\}$.

* **База индукции:** $1 \in E$, так как:

  $$
  (x+y)^1 = x + y = C_1^0 x^1 y^0 + C_1^1 x^0 y^1
  $$

* **Индукционный переход:** пусть $n \in E$, то есть $(x+y)^n = \sum_{k=0}^n C_n^k x^{n-k} y^k$. Докажем, что $n+1 \in E$.

  Умножим обе части на $(x+y)$:

  $$
  (x+y)^{n+1} = (x+y) \sum_{k=0}^n C_n^k x^{n-k} y^k = x \sum_{k=0}^n C_n^k x^{n-k} y^k + y \sum_{k=0}^n C_n^k x^{n-k} y^k =
  $$

  $$
  = \sum_{k=0}^n C_n^k x^{n+1-k} y^k + \sum_{k=0}^n C_n^k x^{n-k} y^{k+1}
  $$

  Во второй сумме сделаем замену индекса суммирования $j = k+1$ (при этом $k = j-1$; когда $k$ меняется от $0$ до $n$, индекс $j$ пробегает значения от $1$ до $n+1$):

  $$
  \sum_{k=0}^n C_n^k x^{n-k} y^{k+1} = \sum_{j=1}^{n+1} C_n^{j-1} x^{n-(j-1)} y^j = \sum_{k=1}^{n+1} C_n^{k-1} x^{n+1-k} y^k
  $$

  Выделим слагаемое при $k=0$ из первой суммы и слагаемое при $k=n+1$ из второй суммы:

  $$
  (x+y)^{n+1} = C_n^0 x^{n+1} + \sum_{k=1}^n C_n^k x^{n+1-k} y^k + \sum_{k=1}^n C_n^{k-1} x^{n+1-k} y^k + C_n^n y^{n+1} =
  $$

  $$
  = C_n^0 x^{n+1} + \sum_{k=1}^n \left( C_n^k + C_n^{k-1} \right) x^{n+1-k} y^k + C_n^n y^{n+1}
  $$

  Используя свойства биномиальных коэффициентов: $C_n^0 = C_{n+1}^0 = 1$, $C_n^n = C_{n+1}^{n+1} = 1$, а по свойству 3: $C_n^k + C_n^{k-1} = C_{n+1}^k$, получаем:

  $$
  (x+y)^{n+1} = C_{n+1}^0 x^{n+1} + \sum_{k=1}^n C_{n+1}^k x^{n+1-k} y^k + C_{n+1}^{n+1} y^{n+1} = \sum_{k=0}^{n+1} C_{n+1}^k x^{n+1-k} y^k
  $$

  Следовательно, утверждение верно для $n+1$, то есть $n+1 \in E$.

По принципу математической индукции $E = \mathbb{N}$, и формула бинома Ньютона верна для всех $n \in \mathbb{N}$. $\blacksquare$

### Следствия и оценки:

Рассмотрим разложение:

$$
\left(1 + \frac{x}{m}\right)^m = \sum_{k=0}^m C_m^k \cdot 1 \cdot \left(\frac{x}{m}\right)^k = \sum_{k=0}^m \frac{m(m-1)(m-2)\dots(m-k+1)}{k!} \cdot \frac{x^k}{m^k} = \sum_{k=0}^m c_{m,k} \frac{x^k}{k!}
$$

где числовые множители $c_{m,k}$ определяются следующим образом:

$$
c_{m,0} = 1, \quad c_{m,1} = 1, \quad c_{m,k} = \left(1-\frac{1}{m}\right)\left(1-\frac{2}{m}\right)\dots\left(1-\frac{k-1}{m}\right) \quad (2 \le k \le m)
$$

Заметим, что для всех $0 \le k \le m$ выполняется $0 < c_{m,k} \le 1$ (причём $0 < c_{m,k} < 1$ при $2 \le k \le m$).

* **Предложение.** Пусть $u > 0, \; k_0 \in \mathbb{N}, \; u < k_0+1$. Тогда $\forall L \in \mathbb{N}: L \ge k_0$:

  $$
  \sum_{k=k_0}^L \frac{u^k}{k!} < \frac{u^{k_0}}{k_0!} \frac{1}{1 - \frac{u}{k_0+1}}
  $$

  **Доказательство.**

  $$
  \frac{u^{k_0}}{k_0!} + \frac{u^{k_0+1}}{(k_0+1)!} + \frac{u^{k_0+2}}{(k_0+2)!} + \dots + \frac{u^L}{L!} = \frac{u^{k_0}}{k_0!} \left(1 + \frac{u}{k_0+1} + \frac{u^2}{(k_0+1)(k_0+2)} + \dots + \frac{u^{L-k_0}}{(k_0+1)\dots L}\right) <
  $$

  $$
  < \frac{u^{k_0}}{k_0!} \left(1 + \frac{u}{k_0+1} + \left(\frac{u}{k_0+1}\right)^2 + \dots + \left(\frac{u}{k_0+1}\right)^{L-k_0}\right) = \frac{u^{k_0}}{k_0!} \frac{1 - \left(\frac{u}{k_0+1}\right)^{L-k_0+1}}{1 - \frac{u}{k_0+1}} < \frac{u^{k_0}}{k_0!} \frac{1}{1 - \frac{u}{k_0+1}}. \quad \blacksquare
  $$

  *(Сумма геометрической прогрессии* $b_1+b_2+\dots+b_m = \frac{b_1(1-q^m)}{1-q}$*, где* $b_1=1, \; q=\frac{u}{k_0+1} \in (0,1), \; m=L-k_0+1$*)*.

* **Следствие.** Так как $0 < c_{L,k} \le 1$, для любого $L \ge k_0$ имеем $\sum_{k=k_0}^L c_{L,k} \frac{u^k}{k!} \le \sum_{k=k_0}^L \frac{u^k}{k!}$, откуда:

  $$
  \sup_{L \in \mathbb{N}} \sum_{k=k_0}^L c_{L,k} \frac{u^k}{k!} \le \sup_{L \in \mathbb{N}} \sum_{k=k_0}^L \frac{u^k}{k!} \le \frac{u^{k_0}}{k_0!} \frac{1}{1 - \frac{u}{k_0+1}}, \quad 0 < u < k_0+1
  $$

## Принцип Архимеда и следствия

**Доказательство Принципа Архимеда (2):**

Найдём такое $n \in \mathbb{N}: \frac{y}{x} < n$, тогда $y < nx$.

Если бы такого $n$ не существовало, то оказалось бы, что $\forall n \in \mathbb{N} \quad n \le \frac{y}{x}$, то есть $\mathbb{N}$ ограничено сверху — противоречие. $\blacksquare$

### Следствия:

* **1)** $\forall \varepsilon > 0 \quad \exists n \in \mathbb{N}: \frac{1}{n} < \varepsilon$ *(при* $x = \varepsilon, \; y = 1$*)*.

* **2)**

  * Если $\forall n \in \mathbb{N} \quad a \le \frac{1}{n}$, то $a \le 0$.

  * Если $\forall n \in \mathbb{N} \quad 0 \le a \le \frac{1}{n}$, то $a = 0$.

* **3) (эквивалентная формулировка принципа Архимеда)**

  Пусть $x, y \in \mathbb{R}, \; x > 0$. Тогда существует единственное $m \in \mathbb{Z}$:

  $$
  (m-1)x \le y < mx
  $$

  **Доказательство.**

  Пусть $E = \{n \in \mathbb{Z} \mid \frac{y}{x} < n\} \subset \mathbb{Z}$.

  Заметим, что $E$ ограничено снизу, так как $\forall n \in E \quad n > \frac{y}{x}$, и $E \neq \emptyset$ (если $y \ge 0$, то $E \neq \emptyset$ в силу свойства (2); если $y < 0$, то $0 \in E$).

  По свойству (5) (принцип минимального числа) существует $\min E$, то есть:

  $$
  \exists m \in E: \forall n \in E \quad m \le n \implies \exists m \in \mathbb{Z}: \frac{y}{x} < m, \quad \text{но} \quad \frac{y}{x} \ge m-1
  $$

  (так как $m \in E$, но $m-1 \notin E$).

  Следовательно, $(m-1)x \le y < mx$ (так как $x > 0$).

  *Единственность:*

  Пусть $\exists m_1, m_2 \in \mathbb{Z}: \begin{cases} (m_1-1)x \le y < m_1x \\ (m_2-1)x \le y < m_2x \end{cases}$. Тогда:

  $$
  \begin{cases} (m_1-1)x < m_2x \\ (m_2-1)x < m_1x \end{cases} \implies \begin{cases} m_1-1 < m_2 \\ m_2-1 < m_1 \end{cases} \implies \begin{cases} m_1 < m_2+1 \\ m_2 < m_1+1 \end{cases} \implies \begin{cases} m_1 \le m_2 \\ m_2 \le m_1 \end{cases} \implies m_1 = m_2. \quad \blacksquare
  $$

* **Следствие при** $x = 1$**:**

  $$
  \forall y \in \mathbb{R} \quad \exists \text{ единственное } m \in \mathbb{Z}: \quad m-1 \le y < m
  $$

  Число $m-1$ называется **целой частью числа** $y$, обозначается $m-1 = [y] = E(y)$.

## Рациональные числа

$$
\mathbb{Q} = \left\{m \cdot \frac{1}{n} \;\middle|\; m \in \mathbb{Z}, \; n \in \mathbb{N}\right\}
$$

### Свойства:

* **1)** $m_1 \cdot \frac{1}{n} + m_2 \cdot \frac{1}{n} = (m_1+m_2) \cdot \frac{1}{n}$ *(всегда можно привести к общему знаменателю)*

* **2)** $\left(m \cdot \frac{1}{n}\right) \cdot \left(p \cdot \frac{1}{q}\right) = (mp) \cdot \frac{1}{nq}$

* **3)** $m_1 \frac{1}{n} < m_2 \frac{1}{n} \iff m_1 < m_2$ *(так как* $\frac{1}{n} > 0$*)*

* **Замечание.** $\frac{1}{xy} = \frac{1}{x} \cdot \frac{1}{y}, \quad x \neq 0, \; y \neq 0$.

  $$
  (xy)\left(\frac{1}{x} \frac{1}{y}\right) = y\left(x \frac{1}{x}\right) \frac{1}{y} = y \frac{1}{y} = 1 \implies \frac{1}{x} \frac{1}{y} = \frac{1}{xy}
  $$

* **Замечание (основное свойство дроби).** $xz \cdot \frac{1}{yz} = x \cdot \frac{1}{y}$ *(так как* $\frac{1}{yz} = \frac{1}{y} \frac{1}{z}$*)*.

### Свойства плотности рациональных и иррациональных чисел в $\mathbb{R}$

* **1)** Если $a, b \in \mathbb{R}, \; a < b$, то $\exists x \in \mathbb{Q}: x \in (a, b)$ *(множество* $\mathbb{Q}$ *плотно в* $\mathbb{R}$*)*.

  **Доказательство.**

  Применим принцип Архимеда (2): для $x = b-a, \; y = 1$:

  $$
  \exists n \in \mathbb{N}: 1 < (b-a)n \implies \frac{1}{n} < b-a
  $$

  Применим принцип Архимеда (3): для $x = \frac{1}{n}, \; y = a$:

  $$
  \exists m \in \mathbb{Z}: \quad (m-1)\frac{1}{n} \le a < m\frac{1}{n} \implies \frac{m}{n} - \frac{1}{n} \le a < \frac{m}{n}
  $$

  Тогда $a < \frac{m}{n}$, и $\frac{m}{n} \le a + \frac{1}{n} < a + (b-a) = b$, то есть:

  $$
  a < \frac{m}{n} < b, \quad x = \frac{m}{n} \in \mathbb{Q}. \quad \blacksquare
  $$

* **2)** Если $a, b \in \mathbb{R}, \; a < b$, то $\exists x \in \mathbb{R} \setminus \mathbb{Q} \text{ (иррациональное)}: x \in (a, b)$.

  **Доказательство.**

  Возьмём любое иррациональное число $\alpha > 0$, например, $\alpha = \sqrt{2}$.

  По принципу Архимеда (2): для $x = b-a, \; y = \alpha$:

  $$
  \exists n \in \mathbb{N}: \quad \alpha < (b-a)n \implies \frac{\alpha}{n} < b-a
  $$

  По принципу Архимеда (3): для $x = \frac{\alpha}{n}, \; y = a$:

  $$
  \exists m \in \mathbb{Z}: \quad (m-1)\frac{\alpha}{n} \le a < m\frac{\alpha}{n}
  $$

  $$
  a < m\frac{\alpha}{n}, \quad m\frac{\alpha}{n} \le a + \frac{\alpha}{n} < a + (b-a) = b \implies a < m\frac{\alpha}{n} < b
  $$

  Если $m \neq 0$, то $x = m\frac{\alpha}{n} \notin \mathbb{Q}$.

  Если $m = 0$, то $a < 0, \; b > 0$, и применим рассуждения к интервалу $(0, b)$. $\blacksquare$

### Пример (существование числа $\sqrt{2} \notin \mathbb{Q}$)

* Пусть $A = \{x \in \mathbb{R} \mid x > 0, \; x^2 < 2\}, \quad B = \{x \in \mathbb{R} \mid x > 0, \; x^2 > 2\}, \quad A \neq \emptyset, \; B \neq \emptyset \quad (1 \in A, \; 2 \in B)$.

* $\forall x \in A \quad \forall y \in B \quad x \le y$ (так как $x^2 < 2 < y^2$; если бы $x > y$, то $x^2 > xy > y^2$).

* По аксиоме непрерывности: $\exists c \in \mathbb{R}: \forall x \in A \quad \forall y \in B \quad x \le c \le y$.

* Почему $c^2 = 2$? Ясно, что $1 < c < 2$.

  * Если бы $c^2 < 2$, тогда $c \in A$, и $0 < \overbrace{2-c^2}^\delta < 1$.

    Рассмотрим:

    $$
    \left(c+\frac{\delta}{5}\right)^2 = c^2 + \frac{2c\delta}{5} + \left(\frac{\delta}{5}\right)^2 < c^2 + \frac{4\delta}{5} + \frac{\delta}{5} = c^2 + \delta = 2
    $$

    То есть $x = c+\frac{\delta}{5} \in A$, и $x = c+\frac{\delta}{5} > c$ — противоречие!

  * Аналогично опровергается предположение $c^2 > 2$.

    Следовательно, $c^2 = 2$. Обозначим $c = \sqrt{2}$.

* Предположим, что $c = \sqrt{2} = \frac{m}{n} \in \mathbb{Q}$ (несократимая дробь).

  Тогда $\frac{m^2}{n^2} = 2 \implies m^2 = 2n^2 \implies m$ — чётное, $m = 2k \implies 4k^2 = 2n^2 \implies n^2 = 2k^2 \implies n$ — чётное $\implies$ противоречие с несократимостью дроби $\frac{m}{n}$.

  Следовательно, $\sqrt{2} \notin \mathbb{Q}$. $\blacksquare$

## §6. Комплексные числа

Комплексные числа $z \in \mathbb{C}$ — это упорядоченные пары действительных чисел $(x,y)$, где $x, y \in \mathbb{R}$, для которых определены операции $+$ и $\cdot$ следующим образом:

* $(x_1, y_1) + (x_2, y_2) = (x_1+x_2, \; y_1+y_2)$

* $(x_1, y_1) \cdot (x_2, y_2) = (x_1x_2 - y_1y_2, \; x_1y_2 + x_2y_1)$

* **1)** Множество комплексных чисел $\mathbb{C}$ с этими операциями удовлетворяет аксиомам поля (1)–(9).

* **2)** Заметим, что $(x_1, 0) + (x_2, 0) = (x_1+x_2, 0)$ и $(x_1, 0) \cdot (x_2, 0) = (x_1x_2, 0)$.

  То есть мы можем отождествить комплексное число $(x, 0)$ с действительным числом $x \in \mathbb{R}$:

  $$
  0 = (0,0), \quad 1 = (1,0), \quad -(x,y) = (-x, -y), \quad \frac{1}{(x,y)} = ?
  $$

* **3)** Любое число $z = (x,y) \in \mathbb{C}$ можно представить в виде:

  $$
  z = (x,y) = (x,0) + (y,0) \cdot (0,1) = x + yi
  $$

  где $i = (0,1)$ — мнимая единица, $i^2 = i \cdot i = (0,1) \cdot (0,1) = (-1,0) = -1$.

  * $z = x + yi$ — **алгебраическая форма** комплексного числа.

  * Числа вида $(0, y) = yi$ будем называть **чисто мнимыми**.

  * Для числа $z = x+yi$ обозначим $\operatorname{Re} z = x$ (действительная часть), $\operatorname{Im} z = y$ (мнимая часть).

* **4)** **Комплексно сопряжённое число** для $z = x+yi$: $\bar{z} = x-iy$.

  **Свойства сопряжения:**

  * **1)** $\overline{z_1+z_2} = \bar{z}_1 + \bar{z}_2$

  * **2)** $\overline{z_1z_2} = \bar{z}_1\bar{z}_2$

  * **3)** $\overline{(\bar{z})} = z$

  * **4)** $\bar{z} = z \iff z \in \mathbb{R}$

  * **5)** $z + \bar{z} = 2x = 2 \operatorname{Re} z \in \mathbb{R}, \quad z \cdot \bar{z} = (x+iy)(x-iy) = x^2 - i^2y^2 = x^2+y^2 \ge 0, \quad z - \bar{z} = 2iy = 2i \operatorname{Im} z$

* **5) Деление:**

  $$
  \frac{z_1}{z_2} = \frac{z_1 \cdot \bar{z}_2}{z_2 \bar{z}_2} = \frac{(x_1+iy_1)(x_2-iy_2)}{x_2^2+y_2^2} = \dots \quad (z_2 \neq 0)
  $$

* **6) Модуль** $z$**:** $|z| = \sqrt{x^2+y^2} \ge 0$. Заметим: $z \cdot \bar{z} = |z|^2$.

* **7) Тригонометрическая форма записи комплексного числа:**

  $$
  z = x+iy = \sqrt{x^2+y^2} \left( \frac{x}{\sqrt{x^2+y^2}} + i \frac{y}{\sqrt{x^2+y^2}} \right) = |z|(\cos \varphi + i \sin \varphi)
  $$

  $$
  \varphi = \operatorname{Arg} z \quad \text{(аргумент комплексного числа), } z \neq 0
  $$

  $$
  \operatorname{Arg} z = \arg z + 2\pi k, \quad k \in \mathbb{Z}
  $$

  **Свойства:**

  * **1)** $r_1(\cos \varphi_1 + i \sin \varphi_1) \cdot r_2(\cos \varphi_2 + i \sin \varphi_2) = (r_1r_2)(\cos(\varphi_1+\varphi_2) + i \sin(\varphi_1+\varphi_2))$

    * $\operatorname{Arg}(z_1z_2) = \operatorname{Arg} z_1 + \operatorname{Arg} z_2$

  * **2)** $\overline{r(\cos \varphi + i \sin \varphi)} = r(\cos(-\varphi) + i \sin(-\varphi))$

    * $\operatorname{Arg}(\bar{z}) = -\operatorname{Arg} z$

  * **3)** $\frac{z_1}{z_2} = \frac{r_1(\cos \varphi_1 + i \sin \varphi_1)}{r_2(\cos \varphi_2 + i \sin \varphi_2)} = \frac{z_1 \bar{z}_2}{\vert{}z_2\vert{}^2} = \frac{r_1(\cos \varphi_1 + i \sin \varphi_1) \cdot r_2(\cos(-\varphi_2) + i \sin(-\varphi_2))}{r_2^2} = \frac{r_1}{r_2}(\cos(\varphi_1-\varphi_2) + i \sin(\varphi_1-\varphi_2))$

    * $\operatorname{Arg}\left(\frac{z_1}{z_2}\right) = \operatorname{Arg} z_1 - \operatorname{Arg} z_2$

  * **4)** $z^n = (r(\cos \varphi + i \sin \varphi))^n = r^n(\cos(n\varphi) + i \sin(n\varphi))$ — **формула Муавра**

    * $\operatorname{Arg}(z^n) = n\varphi + 2\pi k, \; k \in \mathbb{Z}$ *(заметим, что как равенство множеств $\operatorname{Arg}(z^n) = n\operatorname{Arg} z$ неверно при $n \ge 2$, поскольку $n \operatorname{Arg} z = \{n\varphi + 2\pi n k \mid k \in \mathbb{Z}\}$, в то время как $\operatorname{Arg}(z^n) = \{n\varphi + 2\pi k \mid k \in \mathbb{Z}\}$; равенство выполняется по модулю $2\pi$)*.

## Глава II. Множества. Отображения

### §1. Общее понятие отображения множеств

**Декартово произведение множеств** $A$ **и** $B$**:**

* $A \times B = \{(a, b) \mid a \in A, \; b \in B\}$ — множество упорядоченных пар $(a, b)$.

* $A_1 \times A_2 \times \dots \times A_n = \{(a_1, a_2, \dots, a_n) \mid a_1 \in A_1, \; a_2 \in A_2, \dots, a_n \in A_n\}$ (упорядоченный набор из $n$ элементов).

* $A^2 = A \times A, \quad A^n = \underbrace{A \times A \times \dots \times A}_{n \text{ раз}}$.

#### п. 1. Отображение. Образы и прообразы множеств

* Пусть $X$ и $Y$ — произвольные множества. **Отображением** $f: X \to Y$ называется правило, по которому каждому элементу $x \in X$ ставится в соответствие определённый (единственный) элемент $y = f(x) \in Y$.

* Множество $X$ называется **областью определения** отображения $f$, множество $Y$ — его **областью значений** (пространством прибытия).

  $$
  X = \operatorname{dom} f = \mathcal{D}(f) = D_f
  $$

* Как правило, если $X \subset \mathbb{R}, \; Y \subset \mathbb{R}$, то мы будем называть отображения **функциями**.

* Если $x \in X$, то элемент $y = f(x) \in Y$ — **образ элемента** $x$ при отображении $f$ (значение функции $f$ в точке $x$).

* **Образ множества** $A \subset X$ при отображении $f$:

  $$
  f(A) = \{f(x) \mid x \in A\} \subset Y
  $$

* **Множество значений функции / отображения** $f$:

  $$
  E(f) = E_f = f(X) \subset Y
  $$

* **Замечание.** Не обязательно $f(X) = Y$.

* **Пример.** $f(x) = x^2, \quad f: \mathbb{R} \to \mathbb{R}, \quad f(X) = [0, +\infty)$ — множество значений.

#### Прообразы множеств

* **Прообраз множества** $B \subset Y$ при отображении $f: X \to Y$:

  $$
  f^{-1}(B) = \{x \in X \mid f(x) \in B\}
  $$

* **Замечание.** Если $E = f(X)$ — множество значений, то $f^{-1}(B) = f^{-1}(B \cap E)$.

  * Если $B \cap E = \emptyset$, то $f^{-1}(B) = \emptyset$.

* Если множество $B = \{y\}$ состоит из одного элемента, то будем писать $f^{-1}(\{y\}) = f^{-1}(y)$, и называть это множество **прообразом элемента** $y \in Y$.

* Если $f^{-1}(B) = \{x\}$ состоит из одного элемента, то пишем $f^{-1}(B) = x \in X$.

**Примеры:**

* **1)** $f(x) = \frac{1}{x}, \quad X = \mathbb{R} \setminus \{0\}, \quad Y = \mathbb{R}, \quad f(X) = E = \mathbb{R} \setminus \{0\}$:

  * $C = [-3; 2)$: условие $\frac{1}{x} \in [-3; 2)$ означает $-3 \le \frac{1}{x} < 2$. При $x > 0$ имеем $\frac{1}{x} < 2 \iff x > \frac{1}{2}$; при $x < 0$ имеем $\frac{1}{x} \ge -3 \iff x \le -\frac{1}{3}$. Таким образом:

    $$
    f^{-1}(C) = \left(-\infty; -\frac{1}{3}\right] \cup \left(\frac{1}{2}; +\infty\right)
    $$

  * $C' = [-3; 0) \cup (0; 2)$: так как $0 \notin E$, то $C \cap E = C' \cap E$, и поэтому:

    $$
    f^{-1}(C') = f^{-1}(C) = \left(-\infty; -\frac{1}{3}\right] \cup \left(\frac{1}{2}; +\infty\right)
    $$

  * $M = \{4\}, \quad f^{-1}(M) = \left\{\frac{1}{4}\right\}$ или $f^{-1}(4) = \frac{1}{4}$

  * $f^{-1}(0) = \emptyset$, так как $0 \notin E$

* **2)** $f(x) = \sin x, \quad X = \mathbb{R}, \quad Y = \mathbb{R}, \quad E = f(X) = [-1; 1]$:

  * $A = [0; 1], \quad f^{-1}(A) = \bigcup_{n \in \mathbb{Z}} [0 + 2\pi n; \pi + 2\pi n]$

  * $A' = [0; 3), \quad f^{-1}(A') = f^{-1}(A)$

  * $f^{-1}(0) = \{\pi n \mid n \in \mathbb{Z}\}$

#### Виды отображений

* **Определение.** Отображение $f: X \to Y$ называется **инъективным** (инъекцией, взаимно однозначным), если:

  $$
  \forall x_1, x_2 \in X \quad \text{из } x_1 \neq x_2 \implies f(x_1) \neq f(x_2)
  $$

  *(Эквивалентно: из* $f(x_1) = f(x_2) \implies x_1 = x_2$*)*.

  * $\forall y \in Y$ прообраз $f^{-1}(y)$ состоит не более чем из одного элемента;

  * $\forall y \in Y$ уравнение $f(x) = y$ имеет не более одного решения.

* **Определение.** Отображение $f: X \to Y$ называется **сюръективным** (сюръекцией, отображением $X$ на $Y$), если множество значений $f(X) = Y$.

  *(Эквивалентно:* $\forall y \in Y$ *уравнение* $f(x) = y$ *имеет решение)*.

* **Определение.** Отображение $f: X \to Y$ называется **биективным** (биекцией), если оно одновременно инъективно и сюръективно.

  *(*$\forall y \in Y$ *уравнение* $f(x) = y$ *имеет ровно одно решение* $x \in X$*)*. Обозначается $f: X \leftrightarrow Y$.

#### Задачи (свойства) *(см. С.К. Водопьянов)*

* **1)** $f: A \to B$. Для $P, Q \subset B$:

  * $f^{-1}(P \cup Q) = f^{-1}(P) \cup f^{-1}(Q)$

  * $f^{-1}(P \cap Q) = f^{-1}(P) \cap f^{-1}(Q)$

  * $f^{-1}(P \setminus Q) = f^{-1}(P) \setminus f^{-1}(Q)$

* **2)** $f: A \to B$. $E_1, E_2 \subset A, \quad M_1, M_2 \subset B$:

  * Если $E_1 \subset E_2$, то $f(E_1) \subset f(E_2)$

  * Если $M_1 \subset M_2$, то $f^{-1}(M_1) \subset f^{-1}(M_2)$

* **3)** $f: A \to B$:

  * **а)** $\forall E \subset A \quad f^{-1}(f(E)) \supset E$

  * **б)** $f^{-1}(f(E)) = E \quad \forall E \subset A \iff f$ — инъекция

* **4)** $f: A \to B$. Следующие условия эквивалентны:

  * **а)** $f$ — инъекция

  * **б)** $\forall E_1, E_2 \subset A \quad f(E_1 \cap E_2) = f(E_1) \cap f(E_2)$

  * **в)** $\forall E_1, E_2 \subset A \quad \text{из } E_1 \cap E_2 = \emptyset \implies f(E_1) \cap f(E_2) = \emptyset$

  * **г)** $\forall E_1, E_2 \subset A \quad f(E_1 \setminus E_2) = f(E_1) \setminus f(E_2)$

#### п. 2. Суперпозиция отображений

* **Определение.** Пусть $f: A_1 \to B_1$, $g: A_2 \to B_2$ — отображения, причём будем считать, что $A_2 \subset B_1$.

  **Суперпозицией (композицией)** отображений $g$ и $f$ называется отображение:

  $$
  (g \circ f)(x) = g(f(x)), \quad g \circ f: f^{-1}(A_2) \to B_2
  $$

* **Замечание.** Если $f^{-1}(A_2) = \emptyset$, то $g \circ f$ не определено ни в одной точке.

* **Теорема об ассоциативности суперпозиции:**

  Пусть $f: A_1 \to B_1$, $g: A_2 \to B_2$, $h: A_3 \to B_3$, $A_2 \subset B_1$, $A_3 \subset B_2$.

  Тогда отображения $\varphi = h \circ (g \circ f)$ и $\psi = (h \circ g) \circ f$ совпадают, то есть $\operatorname{dom} \varphi = \operatorname{dom} \psi$, и $\forall x \in \operatorname{dom} \varphi \quad \varphi(x) = \psi(x)$.

  **Доказательство.**

  *Лемма (упражнение).* $f: A_1 \to B_1$, $g: A_2 \to B_2$. Для любого $C \subset B_2$:

  $$
  (g \circ f)^{-1}(C) = f^{-1}(g^{-1}(C))
  $$

  * **1)** Обозначим $g \circ f = h_1$, и рассмотрим отображение $\varphi = h \circ h_1$.

    Тогда $\operatorname{dom} \varphi = h_1^{-1}(A_3) = (g \circ f)^{-1}(A_3) = f^{-1}(g^{-1}(A_3))$, и $\forall x \in f^{-1}(g^{-1}(A_3)) \quad \varphi(x) = h(h_1(x)) = h(g(f(x)))$.

  * **2)** Обозначим $f_1 = h \circ g$, и рассмотрим отображение $\psi = f_1 \circ f$.

    Тогда $\operatorname{dom} \psi = f^{-1}(\operatorname{dom} f_1) = f^{-1}(g^{-1}(A_3))$, где $\operatorname{dom} f_1 = \operatorname{dom}(h \circ g) = g^{-1}(A_3)$, и $\forall x \in f^{-1}(g^{-1}(A_3)) \quad \psi(x) = f_1(f(x)) = (h \circ g)(f(x)) = h(g(f(x)))$. $\blacksquare$

#### п. 3. Обратное отображение

* **Определение.** Пусть $f: X \leftrightarrow Y$ — биективное отображение, $Y = f(X)$, и $f$ — взаимно однозначное. Тогда:

  $$
  \forall y \in Y \quad \exists \text{ единственное } x \in X: \quad f(x) = y
  $$

  **Обратным отображением** к отображению $f$ называется отображение $f^{-1} = g: Y \to X$, которое каждому $y \in Y$ ставит в соответствие то единственное значение $x \in X$, для которого $f(x) = y$.

* **Замечание.** $\forall x \in X \quad (f^{-1} \circ f)(x) = f^{-1}(f(x)) = x$, и $\forall y \in Y \quad (f \circ f^{-1})(y) = f(f^{-1}(y)) = y$.

#### п. 4. График отображения

* Пусть $f: X \to Y$ — отображение, $X \neq \emptyset, \; Y \neq \emptyset$.

  **График отображения** $f$**:** множество $\Gamma_f = \{(x, y) \in X \times Y \mid y = f(x)\}$.

* **Утверждение.** Множество $\Gamma \subset X \times Y$ является графиком некоторого отображения $f: X \to Y \iff$ для каждого $x \in X$ существует единственный элемент $y \in Y$ такой, что $(x, y) \in \Gamma$, то есть:

  1. $\forall x \in X \quad \exists y \in Y: (x, y) \in \Gamma$;
  2. если $(x, y_1) \in \Gamma$ и $(x, y_2) \in \Gamma$, то $y_1 = y_2$. *(Упражнение)*.

### §2. Мощность множества

#### п. 1. Равномощные множества

* **Определение.** Множества $A$ и $B$ называются **равномощными**, если существует биекция $f: A \leftrightarrow B$. Обозначается $A \sim B$.

* **Утверждение (отношение эквивалентности):**

  * **1)** $A \sim A$

  * **2)** Если $A \sim B$, то $B \sim A$

  * **3)** Если $A \sim B, \; B \sim C$, то $A \sim C$

  **Доказательство.**

  * **1)** $f(x) = x$ — биекция.

  * **2)** Пусть $A \sim B$, то есть существует биекция $f: A \leftrightarrow B$. Тогда и $f^{-1}: B \leftrightarrow A$ — биекция, то есть $B \sim A$.

    *Лемма.* Если $f: A \leftrightarrow B$ — биекция, то и $f^{-1}: B \leftrightarrow A$ — биекция.

    *(1)* Пусть $f^{-1}(y_1) = f^{-1}(y_2) = x$. Тогда $f(x) = y_1$ и $f(x) = y_2$, то есть $y_1 = y_2$.

    *(2)* Пусть $x \in A$, тогда $f(x) \in B$, то есть $x = f^{-1}(y)$ для некоторого $y \in B$.

  * **3)** Пусть $A \sim B, \; B \sim C$, тогда существуют биекции $f: A \leftrightarrow B, \; g: B \leftrightarrow C$. Тогда $(g \circ f): A \leftrightarrow C$ — биекция, следовательно, $A \sim C$. $\blacksquare$

    *Лемма.* Если $f: A \leftrightarrow B$ и $g: B \leftrightarrow C$ — биекции, то и $(g \circ f): A \leftrightarrow C$ — биекция *(упражнение)*.

* **Определение.** Множество $A$ называется **конечным**, если $\exists n \in \mathbb{N}: A \sim \{1, 2, 3, \dots, n\}$. Число $n$ здесь называется **мощностью множества** $A$.

* **Замечание.** Если $A \sim \{1, 2, \dots, n\}$ и $A \sim \{1, 2, \dots, m\}$, то $n = m$ (можно доказать от противного).

* **Упражнение.** Всякое непустое конечное множество $A \subset \mathbb{R}$:

  * а) ограничено;

  * б) имеет наибольший и наименьший элементы (по индукции).

* **Определение.** $A$ — **бесконечное множество**, если оно не является конечным.

  * *Замечание.* $A$ — бесконечное множество, если:

    $$
    \forall \{a_1, a_2, \dots, a_n\} \subset A \quad \exists a \in A: a \notin \{a_1, a_2, \dots, a_n\}
    $$

* **Определение.** $A$ — **счётное множество**, если $A \sim \mathbb{N}$.

* **Определение.** $A$ — **континуальное множество**, если $A \sim \mathbb{R}$.

#### п. 2. Счётные множества

* **Замечание.** $A$ — счётное, если существует биекция $f: \mathbb{N} \leftrightarrow A$ (нумерация множества $A$):

  $$
  A = \{a_1, a_2, a_3, a_4, \dots\}, \quad \text{здесь } a_n = f(n) \in A
  $$

  *(Подписано:* $f(1), f(2)$*)*.

**Свойства:**

* **1)** $\mathbb{Z}$ — счётное, то есть $\mathbb{Z} \sim \mathbb{N}$.

  Биекция $f: \mathbb{N} \leftrightarrow \mathbb{Z}$:

  * $f(2m) = m, \quad n = 2m \text{ --- чётное}, \; m = 1, 2, 3, \dots$

  * $f(2m+1) = -m, \quad n = 2m+1 \text{ --- нечётное}, \; m = 0, 1, 2, \dots$

* **2)** $\mathbb{N} \times \mathbb{N} \sim \mathbb{N}$ («гостиница Гильберта»).

  $$
  f(m,n) = (2m-1) \cdot 2^{n-1}
  $$

  * **1) Инъективность.** Пусть $f(m_1, n_1) = f(m_2, n_2)$, то есть:

    $$
    (2m_1-1) \cdot 2^{n_1-1} = (2m_2-1) \cdot 2^{n_2-1}
    $$

    Если $n_1 > n_2$, то $\underbrace{(2m_1-1) \cdot 2^{n_1-n_2}}_{\text{чётное}} = \underbrace{(2m_2-1)}_{\text{нечётное}}$ — противоречие.

    Если $n_1 < n_2$ — аналогично. Значит, $n_1 = n_2$.

    Тогда $2m_1-1 = 2m_2-1$, и $m_1 = m_2$.

  * **2) Сюръективность.** Пусть $x \in \mathbb{N}$.

    Если $x$ нечётное, то $x = (2m-1) \cdot 2^{1-1}, \quad m \in \mathbb{N}, \; n = 1 \in \mathbb{N}$.

    Если $x$ чётное, то $x = \underbrace{(2m-1)}_{\text{нечётное}} \cdot 2^k$, где $k$ — наибольшее такое, что $x \vdots 2^k, \quad n = k+1$.

* **Замечание.** $\emptyset$ — конечное, его мощность равна $0$.

* **3)** Если $A$ — счётное, $B \subset A$, то $B$ — конечное или счётное (не более чем счётное).

  **Доказательство.**

  * **1)** Пусть $A = \mathbb{N}, \; B \subset \mathbb{N}$.

    Если $B$ — конечное, то утверждение доказано.

    Пусть $B$ — бесконечное.

    По принципу минимального элемента: $\exists b_1 = \min B, \; b_2 = \min (B \setminus \{b_1\}), \; b_3 = \min (B \setminus \{b_1, b_2\}), \dots$

    Получим: $B = \{b_1, b_2, \dots\}$ — счётное.

  * **2)** Пусть $A$ — произвольное счётное множество, $B \subset A$.

    Пусть $f: A \leftrightarrow \mathbb{N}$ — биекция, и пусть $B' = f(B) \subset \mathbb{N}$. Тогда $B'$ — конечное или счётное, а так как $B \sim B'$, то и $B$ — конечное или счётное. $\blacksquare$

* **4)** $\mathbb{Q}$ — счётное.

  **Доказательство.**

  $\forall q \in \mathbb{Q} \quad \exists \text{единственные } m \in \mathbb{Z}, \; n \in \mathbb{N}: \quad q = \frac{m}{n}$, и $\frac{m}{n}$ — несократима.

  $$
  (m,n) \leftrightarrow \frac{m}{n}, \quad \mathbb{Q} \sim \left\{(m,n) \;\middle|\; m \in \mathbb{Z}, \; n \in \mathbb{N}, \; \frac{m}{n} \text{ --- несократима}\right\} = B \subset \mathbb{Z} \times \mathbb{N}
  $$

  *Лемма.* Если $A \sim A_1, \; B \sim B_1$, то $A \times B \sim A_1 \times B_1$ *(упражнение)*.

  Множество $\mathbb{Z} \times \mathbb{N} \sim \mathbb{N} \times \mathbb{N} \sim \mathbb{N}$ — счётно.

  Так как $\forall n \in \mathbb{N} \quad (1, n) \in B$, то $B$ — бесконечное.

  По свойству 3, $B$ — счётное, следовательно, и $\mathbb{Q}$ — счётное. $\blacksquare$

* **5)**

  * **1.** $A, B$ — счётные $\implies A \cup B$ — счётно.

  * **2.** $A_1, A_2, \dots, A_n, \dots$ — счётные $\implies \bigcup_{n=1}^\infty A_n$ — счётно.

  * **3.** Объединение не более чем счётного семейства не более чем счётных множеств — не более чем счётно.

    *(Если хотя бы одно из этих множеств счётно, то и объединение счётно)*.

  **Доказательство:** 1), 3) упражнение.

  **Доказательство 2:**

  $$
  B_1 = A_1, \quad B_2 = A_2 \setminus A_1, \quad B_3 = A_3 \setminus (A_1 \cup A_2), \dots, B_n = A_n \setminus (A_1 \cup A_2 \cup \dots \cup A_{n-1}), \dots
  $$

  $B_1$ — счётное, $B_n \; (n \ge 2)$ — не более чем счётные.

  $\bigcup_{n=1}^\infty A_n = \bigcup_{n=1}^\infty B_n$ по построению.

  * $B_1 = \{b_1^1, b_2^1, \dots, b_k^1, \dots\} \leftarrow \{(k,1) \mid k \in \mathbb{N}\}$ — счётное

  * $B_2 = \{b_1^2, b_2^2, \dots, b_k^2, \dots\} \leftarrow \{(k,2) \mid k \in K \subset \mathbb{N}\}$ — конечное или счётное

  * и так далее.

    По свойствам 2 и 3 получим, что $\bigcup_{n=1}^\infty B_n$ — счётное. $\blacksquare$

* **6)** Если $A$ и $B$ — счётные, то $A \times B$ — счётное.

  * Если $A$ счётно, $B$ конечно, то $A \times B$ — счётно *(упражнение)*.

  * Если $A_1, A_2, \dots, A_m$ — не более чем счётные, то $A_1 \times A_2 \times \dots \times A_m$ — не более чем счётно.

  * ($A \times B \sim \mathbb{N} \times \mathbb{N} \sim \mathbb{N}$).

#### п. 3. Континуальные множества

* **Свойство 1.** $(0; 1) \sim \mathbb{R}$.

  $f(x) = \frac{1}{x} + \frac{1}{x-1}: \quad (0; 1) \leftrightarrow \mathbb{R}$ — биекция.

  * **1) Инъективность.**

    Если $x_1 < x_2$, то $\frac{1}{x_1} > \frac{1}{x_2}$, $\frac{1}{x_1-1} > \frac{1}{x_2-1}$ и $f(x_1) > f(x_2)$.

    *(*$x_1, x_2 \in (0; 1)$*,* $x_1-1, x_2-1 \in (-1; 0)$*,* $1-x_1, 1-x_2 \in (0; 1)$*,* $1-x_1 > 1-x_2 \implies \frac{1}{1-x_1} < \frac{1}{1-x_2} \implies \frac{1}{x_1-1} > \frac{1}{x_2-1}$*)*.

  * **2) Сюръективность.**

    Пусть $y = \frac{1}{x} + \frac{1}{x-1} = \frac{2x-1}{x^2-x} \implies (x^2-x)y = 2x-1$.

    Если $y = 0$, то $x = \frac{1}{2}$.

    $$
    yx^2 - (y+2)x + 1 = 0
    $$

    $$
    D = (y+2)^2 - 4y = y^2 + 4 > 0
    $$

    $$
    x_{1,2} = \frac{y+2 \pm \sqrt{y^2+4}}{2y}
    $$

    Один из корней принадлежит $(0; 1)$? *(Упражнение)*.

* **Свойство 2.** $(a; b) \sim (0; 1)$ *(упражнение)*.

## Глава III. Понятие предела

### §1. Предел последовательности

#### п. 1. Определение последовательности. Ограниченность последовательности

* **Последовательность** элементов множества $X$ с индексами из множества $M \subset \mathbb{Z}$ — это отображение $f: M \to X$.

* Обычно $M = \mathbb{N}$ или $\mathbb{N} \cup \{0\}$ или $\mathbb{Z}$, а $X = \mathbb{R}$ или $\overline{\mathbb{R}}$ или $\mathbb{C}$.

* Если мы рассматриваем последовательность с натуральными индексами, то обозначаем её через $\{x_n\}_{n=1}^\infty$ вместо $x(n)$.

  * $x_n: \mathbb{N} \to \mathbb{R}$

  * $x_n$ — члены последовательности, $n$ — их номера.

**Примеры:**

* **1)** $x_n = c \quad \forall n \in \mathbb{N}$ — постоянная последовательность: $c, c, c, c, \dots$

* **2)** $x_n = \frac{1}{n}, \; n \in \mathbb{N}: \quad 1, \frac{1}{2}, \frac{1}{3}, \frac{1}{4}, \dots$

* **3)** $x_n = 1 + q + q^2 + \dots + q^{n-1} = \sum_{k=0}^{n-1} q^k$

* **4)** $x_n = \left(1 + \frac{1}{n}\right)^n$

**Ограниченность:**

* **Определение.** Последовательность $\{x_n\}$ ограничена сверху, если:

  $$
  \exists b \in \mathbb{R}: \forall n \in \mathbb{N} \quad x_n \le b
  $$

* Последовательность $\{x_n\}$ ограничена снизу, если:

  $$
  \exists a \in \mathbb{R}: \forall n \in \mathbb{N} \quad x_n \ge a
  $$

* Последовательность $\{x_n\}$ ограничена, если она ограничена и сверху, и снизу, то есть:

  $$
  \exists a, b \in \mathbb{R}: \forall n \quad a \le x_n \le b
  $$

* **Утверждение.** Последовательность $\{x_n\}$ ограничена $\iff \exists M > 0: \forall n \quad \vert{}x_n\vert{} \le M$.

  *(Ограниченность последовательности — то же самое, что ограниченность её множества значений)*.

#### п. 2. Определение предела последовательности

* **Определение.** Число $a \in \mathbb{R}$ называется **пределом последовательности** $\{x_n\}$, $x_n \in \mathbb{R}$ (обозначается $\lim_{n \to \infty} x_n = a$, $x_n \to a$ при $n \to \infty$), если:

  $$
  \forall \varepsilon > 0 \quad \exists N = N(\varepsilon) \in \mathbb{N}: \forall n \ge N \quad |x_n - a| < \varepsilon
  $$

  *(Последовательность, имеющая конечный предел, называется сходящейся)*.

**Примеры:**

* **1)** $\lim_{n \to \infty} \frac{1}{n} = 0$:

  $$
  \forall \varepsilon > 0 \quad \exists N = N(\varepsilon): \forall n \ge N \quad \left|\frac{1}{n} - 0\right| < \varepsilon \iff \frac{1}{n} < \varepsilon \iff n > \frac{1}{\varepsilon}
  $$

  Полагаем $N(\varepsilon) = \left[\frac{1}{\varepsilon}\right] + 1$.

* **2)** $\lim_{n \to \infty} \left(2 - \frac{1}{10^n}\right) = 2$:

  $$
  \forall \varepsilon > 0 \quad \exists N: \forall n \ge N \quad \left|\left(2 - \frac{1}{10^n}\right) - 2\right| < \varepsilon \iff \frac{1}{10^n} < \varepsilon \iff 10^n > \frac{1}{\varepsilon} \iff n > \lg \frac{1}{\varepsilon}
  $$

  Полагаем $N = \left[\lg \frac{1}{\varepsilon}\right] + 1$.

* **3)** $\lim_{n \to \infty} \frac{n^2}{2^n} = 0$:

  $$
  2^n = (1+1)^n = C_n^0 + C_n^1 + C_n^2 + C_n^3 + \dots + C_n^n \ge C_n^3 = \frac{n(n-1)(n-2)}{6} \quad \forall n \ge 3
  $$

  $$
  0 \le \frac{n^2}{2^n} \le \frac{n^2}{\frac{n(n-1)(n-2)}{6}} = \frac{6n}{(n-1)(n-2)} \le \frac{6n}{\frac{n}{2}(n-2)} = \frac{12}{n-2} < \varepsilon, \quad \text{если } n-2 > \frac{12}{\varepsilon}
  $$

  *(Пояснение:* $\frac{n}{2} \le n-1 \iff n \ge 2$*)*.

  $$
  n > \frac{12}{\varepsilon} + 2 \implies \text{полагаем } N = \left[\frac{12}{\varepsilon} + 2\right] + 1
  $$

* **4)** $x_n = (-1)^n$ не имеет предела.

  **Доказательство.** Предположим, что существует $\lim_{n \to \infty} (-1)^n = a$, тогда:

  $$
  \text{для } \varepsilon = \frac{1}{2} \quad \exists N: \forall n \ge N \quad |x_n - a| < \varepsilon = \frac{1}{2}
  $$

  В частности, для чётных $n$: $|1 - a| < \frac{1}{2}$, а для нечётных $n$: $|-1 - a| < \frac{1}{2}$.

  Тогда:

  $$
  2 = |1 - (-1)| = |1 - a + a - (-1)| \le |1 - a| + |a - (-1)| < \frac{1}{2} + \frac{1}{2} = 1 \quad \text{--- противоречие.}
  $$

**Бесконечный предел:**

* $\lim_{n \to \infty} x_n = +\infty$, если $\forall M > 0 \quad \exists N = N(M): \forall n \ge N \quad x_n > M$.

* $\lim_{n \to \infty} x_n = -\infty$, если $\forall M > 0 \quad \exists N = N(M): \forall n \ge N \quad x_n < -M$.

* **Определение.** **Элементарная окрестность (**$\varepsilon$**-окрестность)** точки $a \in \mathbb{R}$:

  Интервал $U_\varepsilon(a) = (a-\varepsilon; a+\varepsilon)$.

  Ясно, что $x \in U_\varepsilon(a) \iff |x - a| < \varepsilon$.

* Элементарная окрестность точки $+\infty$ в $\overline{\mathbb{R}}$: $U_\varepsilon(+\infty) = \left(\frac{1}{\varepsilon}; +\infty\right)$.

* Элементарная окрестность точки $-\infty$ в $\overline{\mathbb{R}}$: $U_\varepsilon(-\infty) = \left(-\infty; -\frac{1}{\varepsilon}\right)$.

* **Свойство 3.** Если $\lim_{n \to \infty} x_n = a$, то $\lim_{n \to \infty} \vert{}x_n\vert{} = \vert{}a\vert{}$.

  **Доказательство.** Для произвольного $\varepsilon > 0 \quad \exists N: \forall n \ge N \quad |x_n - a| < \varepsilon$, тогда $\forall n \ge N$:

  $$
  ||x_n| - |a|| \le |x_n - a| < \varepsilon. \quad \blacksquare
  $$

#### п. 3. Бесконечно малые и бесконечно большие последовательности

* **Определение.** Последовательность $\{x_n\}$ называется **бесконечно малой (б.м.)**, если $\lim_{n \to \infty} x_n = 0$.

* **Определение.** Последовательность $\{x_n\}$ называется **бесконечно большой (б.б.)**, если $\lim_{n \to \infty} \vert{}x_n\vert{} = +\infty$.

* **Замечание.** Всякая бесконечно большая последовательность является неограниченной, но не всякая неограниченная является бесконечно большой.

### Организационная информация о контрольной работе

* **Поточная контрольная работа:** «Введение + предел последовательности» $\approx$ конец октября — начало ноября (на полпары).

* **Содержание:** Определения, формулировки, доказательства, задача: $\lim_{n \to \infty} x_n = a$ (по определению).

* **Критерии:**

  * «3»: задача, определения, формулировки.

  * «4»–«5»: то же самое + доказательства.

* **Формула итоговой оценки:**

  $$
  \frac{\left(\frac{1}{3}\Pi + \frac{2}{3}Э\right) + C}{2}
  $$

### Свойства пределов последовательностей (продолжение)

* **Свойство 4.** Если $\lim_{n \to \infty} x_n = 0$ (б.м.), а последовательность $\{y_n\}$ ограничена, то $\lim_{n \to \infty} x_n y_n = 0$ (б.м.).

  **Доказательство.** Пусть $\{y_n\}$ ограничена, $|y_n| \le M \quad \forall n$. Пусть $\varepsilon > 0$ — произвольное.

  Так как $\lim_{n \to \infty} x_n = 0$, то $\exists N: \forall n \ge N \quad |x_n| < \frac{\varepsilon}{M}$.

  Тогда $\forall n \ge N$:

  $$
  |x_n y_n| = |x_n| \cdot |y_n| < \frac{\varepsilon}{M} \cdot M = \varepsilon, \quad \text{то есть } \lim_{n \to \infty} (x_n y_n) = 0. \quad \blacksquare
  $$

  *Пример:* $\lim_{n \to \infty} \frac{\sin n}{n} = \lim_{n \to \infty} \underbrace{\sin n}_{\text{ограничена}} \cdot \underbrace{\frac{1}{n}}_{\to 0} = 0$.

* **Свойство 5.** $\{x_n\}$ — б.б., то есть $\lim_{n \to \infty} \vert{}x_n\vert{} = +\infty \iff \lim_{n \to \infty} \frac{1}{x_n} = 0$ ($\{\frac{1}{x_n}\}$ — б.м.).

  *(Полагаем* $\frac{1}{+\infty} = \frac{1}{-\infty} = 0$ *формально,* $\{\frac{1}{\infty} = 0\}$*)*.

  **Доказательство (**$\implies$**).** Пусть $\lim_{n \to \infty} |x_n| = +\infty$, и пусть $\varepsilon > 0$ — произвольное.

  Для $M = \frac{1}{\varepsilon} \quad \exists N: \forall n \ge N \quad |x_n| > M = \frac{1}{\varepsilon}$, тогда:

  $$
  \forall n \ge N \quad \left|\frac{1}{x_n}\right| = \frac{1}{|x_n|} < \varepsilon, \quad \text{то есть } \lim_{n \to \infty} \frac{1}{x_n} = 0
  $$

  **Доказательство (**$\impliedby$**).** Пусть $\lim_{n \to \infty} \frac{1}{x_n} = 0$, и пусть $M > 0$ — произвольное.

  Для $\varepsilon = \frac{1}{M} > 0 \quad \exists N: \forall n \ge N \quad \left|\frac{1}{x_n}\right| < \varepsilon = \frac{1}{M} \implies 0 < \frac{1}{|x_n|} < \frac{1}{M}$, то есть $\forall n \ge N \quad |x_n| > M$. Значит, $\lim_{n \to \infty} |x_n| = +\infty$. $\blacksquare$

* **Свойство 6.** $\lim_{n \to \infty} x_n = a \in \mathbb{R} \iff x_n = a + \alpha_n$, где $\alpha_n$ — б.м. *(очевидно следует из арифметических свойств — см. свойство 8)*.

#### п. 3. Понятие подпоследовательности

* **Определение.** Пусть $\{x_n\}$ — последовательность, и пусть $\{n_k\}$ — строго возрастающая последовательность натуральных чисел ($n_k: \mathbb{N} \to \mathbb{N}$, $n_1 < n_2 < n_3 < \dots < n_k < \dots$).

  Тогда последовательность $\{x_{n_k}\}$ называется **подпоследовательностью** последовательности $\{x_n\}$.

  *Пример:* $\{x_n\}: 1, \frac{1}{2}, \frac{1}{3}, \frac{1}{4}, \dots, \frac{1}{n}, \dots \quad (x_n = \frac{1}{n})$.

  * $n_k = 2k$; подпоследовательность $x_{n_k} = x_{2k}: \frac{1}{2}, \frac{1}{4}, \frac{1}{6}, \dots$

  * $n_k = k^2$; $x_{n_k} = x_{k^2} = \frac{1}{k^2}: \frac{1}{1}, \frac{1}{4}, \frac{1}{9}, \frac{1}{16}, \dots$

    *(Замечание:* $\forall k \quad n_k \ge k$*)*.

* **Свойство 7.** Существует предел $\lim_{n \to \infty} x_n = a, \quad -\infty \le a \le +\infty \iff$ для любой подпоследовательности $\{x_{n_k}\}$: $\lim_{k \to \infty} x_{n_k} = a$.

  **Доказательство для** $a \in \mathbb{R}$**:**

  * ($\implies$) Пусть $\varepsilon > 0$ — произвольно. Тогда $\exists N: \forall n \ge N \quad \vert{}x_n - a\vert{} < \varepsilon$ *(что поменяется, если* $a = \pm\infty$*?)*.

    Тогда $\forall k \ge N \quad n_k \ge k \ge N$, и $|x_{n_k} - a| < \varepsilon$, то есть $\lim_{k \to \infty} x_{n_k} = a$. $\blacksquare$

  * ($\impliedby$) Если $\lim_{k \to \infty} x_{n_k} = a$ для любой подпоследовательности $\{x_{n_k}\}$, то возьмём в качестве подпоследовательности саму последовательность $\{x_n\}$. $\blacksquare$

* **Следствие.** Если две подпоследовательности последовательности $\{x_n\}$ имеют разные пределы, то $\lim_{n \to \infty} x_n$ не существует.

  *Пример:* $(-1)^n$.

  * Подпоследовательность чётных номеров $\{x_{2k}\}: 1, 1, 1, \dots \implies \lim_{k \to \infty} x_{2k} = 1$.

  * Подпоследовательность нечётных номеров $\{x_{2k-1}\}: -1, -1, -1, \dots \implies \lim_{k \to \infty} x_{2k-1} = -1$.

  * Так как $1 \neq -1$, предел $\lim_{n \to \infty} (-1)^n$ не существует.

### Арифметические свойства (продолжение замечаний и доказательств)

* **Замечание 1'.**

  * **а)** Если $\lim_{n \to \infty} x_n = +\infty$ и $\exists a \in \mathbb{R}: \forall n \quad y_n \ge a$ (ограничена снизу), то $\lim_{n \to \infty} (x_n + y_n) = +\infty$.

  * **б)** Если $\lim_{n \to \infty} x_n = -\infty$ и $\exists b \in \mathbb{R}: \forall n \quad y_n \le b$ (ограничена сверху), то $\lim_{n \to \infty} (x_n + y_n) = -\infty$.

  **Доказательство а).** Пусть $M > 0$ — произвольное. Тогда $\exists N: \forall n \ge N \quad x_n > M + |a|$.

  Тогда $\forall n \ge N \quad x_n + y_n > M + |a| + a \ge M$, то есть $\lim_{n \to \infty} (x_n + y_n) = +\infty$.

  **Доказательство б)** аналогично.

  Таким образом, формула справедлива и для случаев $a = \pm\infty, \; b \in \mathbb{R}$; $a = +\infty, \; b = +\infty$; $a = -\infty, \; b = -\infty$.

  Случай $a = +\infty, \; b = -\infty$ даёт неопределённость $\{\infty - \infty\}$.

  Правила: $+\infty + \infty = +\infty, \quad \pm\infty + C = \pm\infty \quad (C \in \mathbb{R})$.

* **Доказательство 2) Произведение пределов:**

  Рассмотрим:

  $$
  |x_n y_n - ab| = |x_n y_n - x_n b + x_n b - ab| = |x_n(y_n - b) + b(x_n - a)| \le |x_n(y_n - b)| + |b(x_n - a)| = |x_n| \cdot |y_n - b| + |b| \cdot |x_n - a|
  $$

  Пусть $\varepsilon > 0$ — произвольное.

  Так как $\lim_{n \to \infty} x_n = a$, то $\exists N_1: \forall n \ge N_1 \quad |x_n - a| < \frac{\varepsilon}{2(|b| + 1)}$.

  Кроме того, по свойству 2, последовательность $\{x_n\}$ ограничена, то есть $\exists M > 0: \forall n \quad |x_n| \le M$.

  Так как $\lim_{n \to \infty} y_n = b$, то $\exists N_2: \forall n \ge N_2 \quad |y_n - b| < \frac{\varepsilon}{2M}$.

  Положим $N = \max(N_1, N_2)$. Тогда $\forall n \ge N$:

  $$
  |x_n y_n - ab| \le |x_n| \cdot |y_n - b| + |b| \cdot |x_n - a| < M \cdot \frac{\varepsilon}{2M} + |b| \cdot \frac{\varepsilon}{2(|b| + 1)} < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon
  $$

  То есть $\lim_{n \to \infty} (x_n y_n) = ab$. $\blacksquare$

* **Замечание 2'.**

  * **а)** Если $\lim_{n \to \infty} x_n = +\infty$ и $\forall n \quad y_n \ge a > 0$, то $\lim_{n \to \infty} (x_n \cdot y_n) = +\infty$ *(в частности,* $\lim_{n \to \infty} y_n = c, \quad 0 < c \le +\infty$*)*.

  * **б)** Если $\lim_{n \to \infty} x_n = +\infty$ и $\forall n \quad y_n \le a < 0$, то $\lim_{n \to \infty} (x_n \cdot y_n) = -\infty$ *(в частности,* $\lim_{n \to \infty} y_n = c, \quad -\infty \le c < 0$*)*.

  * **в), г)** *(Сформулируйте аналогично для* $\lim_{n \to \infty} x_n = -\infty$*)*.

  Это позволяет нам распространить пункт (2) на случаи $a = \pm\infty, \quad b \neq 0$.

  **Доказательство а).** Пусть $M > 0$ — произвольное, тогда $\exists N: \forall n \ge N \quad x_n > \frac{M}{a}$.

  Тогда $\forall n \ge N \quad x_n \cdot y_n > \frac{M}{a} \cdot a = M$, то есть $\lim_{n \to \infty} (x_n \cdot y_n) = +\infty$. $\blacksquare$

* **Правила знаков с бесконечностями:**

  * $+\infty \cdot C = +\infty \quad (C > 0)$

  * $+\infty \cdot (+\infty) = +\infty$

  * $+\infty \cdot C = -\infty \quad (C < 0)$

  * $+\infty \cdot (-\infty) = -\infty$

  * $\{\pm\infty \cdot 0\}$ — неопределённость.

* **3) Предел частного.**

  Сначала докажем, что $\lim_{n \to \infty} \frac{1}{y_n} = \frac{1}{b}$, если $b \neq 0$.

  Рассмотрим:

  $$
  \left| \frac{1}{y_n} - \frac{1}{b} \right| = \left| \frac{b - y_n}{y_n b} \right| = \frac{|y_n - b|}{|y_n| \cdot |b|}
  $$

  Так как $\lim_{n \to \infty} y_n = b$, то по свойству 3: $\lim_{n \to \infty} |y_n| = |b| > \frac{|b|}{2} > 0$, поэтому по свойству (10) ниже:

  $$
  \exists N_1: \forall n \ge N_1 \quad |y_n| > \frac{|b|}{2}
  $$

  Кроме того, $\exists N_2: \forall n \ge N_2 \quad |y_n - b| < \varepsilon \cdot \frac{|b|^2}{2}$.

  Тогда $\forall n \ge N = \max(N_1, N_2)$:

  $$
  \left| \frac{1}{y_n} - \frac{1}{b} \right| = \frac{|y_n - b|}{|y_n| \cdot |b|} < \frac{\varepsilon \cdot \frac{|b|^2}{2}}{\frac{|b|}{2} \cdot |b|} = \varepsilon, \quad \text{то есть } \lim_{n \to \infty} \frac{1}{y_n} = \frac{1}{b}
  $$

  Далее:

  $$
  \lim_{n \to \infty} \left( \frac{x_n}{y_n} \right) = \lim_{n \to \infty} \left( x_n \cdot \frac{1}{y_n} \right) = a \cdot \frac{1}{b} = \frac{a}{b}. \quad \blacksquare
  $$

* **Замечание 3'.**

  Если $\lim_{n \to \infty} x_n = +\infty, \; \lim_{n \to \infty} y_n = b \in \mathbb{R}$, то:

  $$
  \lim_{n \to \infty} \frac{x_n}{y_n} = \begin{cases} +\infty, & \text{если } b > 0 \\ -\infty, & \text{если } b < 0 \end{cases}
  $$

  *(Для* $x_n \to -\infty$ *аналогично)*.

* **3''.** Если $\lim_{n \to \infty} x_n = a \in \mathbb{R}, \; \lim_{n \to \infty} y_n = \pm\infty$, то $\lim_{n \to \infty} \frac{x_n}{y_n} = 0$ *(следствие свойства 5)*.

* **3'''.**

  * Если $\lim_{n \to \infty} x_n = a, \quad 0 < a \le +\infty, \quad \lim_{n \to \infty} y_n = 0, \quad y_n > 0 \quad \forall n$, то $\lim_{n \to \infty} \frac{x_n}{y_n} = +\infty$.

  * Если $\lim_{n \to \infty} y_n = 0, \quad y_n < 0 \quad \forall n$, то $\lim_{n \to \infty} \frac{x_n}{y_n} = -\infty$.

  * Для $\lim_{n \to \infty} x_n = a, \quad -\infty \le a < 0$ — самостоятельно. Доказательство: упражнение.

  * $\left\{\frac{\infty}{\infty}\right\}, \quad \left\{\frac{0}{0}\right\}$ — неопределённости.

* **Пример:**

  $$
  \lim_{n \to \infty} \frac{2n^2 - n + 3}{3n^2 + n + 2} = \lim_{n \to \infty} \frac{n^2(2 - \frac{1}{n} + \frac{3}{n^2})}{n^2(3 + \frac{1}{n} + \frac{2}{n^2})} = \frac{2}{3}
  $$

* **Вспомогательная формула:**

  $$
  a^k - b^k = (a - b) \cdot (a^{k-1} + a^{k-2}b + a^{k-3}b^2 + \dots + b^{k-1})
  $$

  $$
  a - b = \frac{a^k - b^k}{a^{k-1} + a^{k-2}b + \dots + b^{k-1}}
  $$

* **Свойство 9.** Если $\lim_{n \to \infty} x_n = a \ge 0$, то:

  $$
  \lim_{n \to \infty} \sqrt[k]{x_n} = \sqrt[k]{a}, \quad k \in \mathbb{N}
  $$

  *(Для нечётных* $k$ *верно и при* $a < 0$*)*.

  **Доказательство.**

  * **1)** $a = 0$. Пусть $\varepsilon > 0$ — произвольное. Тогда $\exists N: \forall n \ge N \quad \vert{}x_n\vert{} < \varepsilon^k$.

    Тогда $\forall n \ge N \quad |\sqrt[k]{x_n}| < \varepsilon$, то есть $\lim_{n \to \infty} \sqrt[k]{x_n} = 0$.

  * **2)** $a > 0$. Пусть $\varepsilon > 0$ — произвольное. Тогда $\exists N_1: \forall n \ge N_1 \quad \vert{}x_n - a\vert{} < \varepsilon \cdot \sqrt[k]{a^{k-1}}$.

    Кроме того, по свойству (10) ниже: $\exists N_2: \forall n \ge N_2 \quad x_n > 0$.

    Тогда $\forall n \ge N = \max(N_1, N_2)$:

    $$
    |\sqrt[k]{x_n} - \sqrt[k]{a}| = \frac{|x_n - a|}{|\sqrt[k]{x_n^{k-1}} + \sqrt[k]{x_n^{k-2}}\sqrt[k]{a} + \dots + \sqrt[k]{a^{k-1}}|} \le \frac{|x_n - a|}{\sqrt[k]{a^{k-1}}} < \frac{\varepsilon \cdot \sqrt[k]{a^{k-1}}}{\sqrt[k]{a^{k-1}}} = \varepsilon
    $$

    То есть $\lim_{n \to \infty} \sqrt[k]{x_n} = \sqrt[k]{a}$. $\blacksquare$

* **Следствие.** Пусть $\lim_{n \to \infty} x_n = a$, $\alpha \in \mathbb{Q}$.

  * Если $a > 0$, то $\lim_{n \to \infty} x_n^\alpha = a^\alpha$ *(так как $x_n > 0$ при всех достаточно больших $n$ по свойству 10)*.

  * Если $a = 0$ и $\alpha > 0$ (при условии $x_n \ge 0$), то $\lim_{n \to \infty} x_n^\alpha = 0$.

  *(Замечание: при $a < 0$ рациональная степень определена только для дробей с нечётным знаменателем; при $a = 0$ и $\alpha \le 0$ предел не является конечным числом).*

#### п. 5. Порядковые свойства последовательностей, имеющих предел

* **Свойство 10.** Если $\lim_{n \to \infty} x_n = a$ (где $a \in \mathbb{R} \cup \{-\infty, +\infty\}$) и $a > \alpha$ ($\alpha \in \mathbb{R}$), то $\exists N: \forall n \ge N \quad x_n > \alpha$.

  *(Аналогично: если* $a < \beta \implies \exists N: \forall n \ge N \quad x_n < \beta$*)*.

* **Следствие.** Если $\lim_{n \to \infty} x_n = a, \; \lim_{n \to \infty} y_n = b, \; a > b$, то $\exists N: \forall n \ge N \quad x_n > y_n$.

  *(Доказывается рассмотрением последовательности* $z_n = x_n - y_n$*)*.

*Доказательство:*
Пусть $a \in \mathbb{R}$. Пусть $\varepsilon = \frac{a - \alpha}{2} > 0$, тогда $\exists N: \forall n \ge N \quad \vert{}x_n - a\vert{} < \varepsilon$, что эквивалентно $a - \varepsilon < x_n < a + \varepsilon$.
То есть $\forall n \ge N \quad x_n > a - \varepsilon = a - \frac{a - \alpha}{2} = \frac{a + \alpha}{2} > \frac{\alpha + \alpha}{2} = \alpha$.
Для $a = +\infty$ — аналогично. (Выбрать $M = 2\vert{}\alpha\vert{} > \alpha$). $\blacksquare$

**Свойство 11 (предельный переход в неравенствах).**
Пусть $\lim_{n \to \infty} x_n = a$, и пусть $\exists N: \forall n \ge N$ (начиная с некоторого номера, для достаточно больших $n$) выполняется $x_n \le c$ \[$x_n \ge c$\]. Тогда $a \le c$ \[$a \ge c$\].

*Следствие:* Пусть $\lim_{n \to \infty} x_n = a, \lim_{n \to \infty} y_n = b$, и $\exists N: \forall n \ge N \quad x_n \le y_n$. Тогда $a \le b$.
(Применим утверждение к последовательности $z_n = y_n - x_n \ge 0 \quad \forall n \ge N$, следовательно, $\lim_{n \to \infty} z_n = b - a \ge 0$).

*Доказательство свойства:*
Предположим, что $a > c$. Тогда по свойству 10, $\exists N_1: \forall n \ge N_1 \quad x_n > c$.
Тогда $\forall n \ge \max(N, N_1)$ условия $x_n > c$ и $x_n \le c$ выполняются одновременно — противоречие. Значит, $a \le c$. $\blacksquare$

*Замечание:* Если $x_n < y_n \quad \forall n$, то в пределе $\lim_{n \to \infty} x_n \le \lim_{n \to \infty} y_n$. Например, $x_n = -\frac{1}{n} < y_n = \frac{1}{n} \quad \forall n$, но $\lim_{n \to \infty} x_n = \lim_{n \to \infty} y_n = 0$.

**Свойство 12 (Теорема о зажатой последовательности, "о промежуточной последовательности", "о двух милиционерах").**
Пусть $\exists N_0: \forall n \ge N_0 \quad x_n \le y_n \le z_n$, и $\lim_{n \to \infty} x_n = \lim_{n \to \infty} z_n = a \in \mathbb{R}$. Тогда и $\lim_{n \to \infty} y_n = a$.

*Доказательство:*
Пусть $\varepsilon > 0$ — произвольное. Тогда:
$\exists N_1: \forall n \ge N_1 \quad \vert{}x_n - a\vert{} < \varepsilon$, то есть $a - \varepsilon < x_n < a + \varepsilon$, и
$\exists N_2: \forall n \ge N_2 \quad \vert{}z_n - a\vert{} < \varepsilon$, то есть $a - \varepsilon < z_n < a + \varepsilon$.
Тогда $\forall n \ge N = \max(N_0, N_1, N_2) \quad a - \varepsilon < x_n \le y_n \le z_n < a + \varepsilon$, то есть $\vert{}y_n - a\vert{} < \varepsilon$, значит, $\lim_{n \to \infty} y_n = a$. $\blacksquare$

*Замечание (Свойство 12'):* Пусть $\exists N_0: \forall n \ge N_0 \quad x_n \le y_n$. Тогда:
а) если $\lim_{n \to \infty} x_n = +\infty$, то и $\lim_{n \to \infty} y_n = +\infty$;
б) если $\lim_{n \to \infty} y_n = -\infty$, то и $\lim_{n \to \infty} x_n = -\infty$.

*Доказательство пункта а):*
Пусть $\lim_{n \to \infty} x_n = +\infty$, и пусть $M > 0$ — произвольное. Тогда $\exists N_1: \forall n \ge N_1 \quad x_n > M$.
Тогда $\forall n \ge N = \max(N_0, N_1) \quad y_n \ge x_n > M$, то есть $\lim_{n \to \infty} y_n = +\infty$. $\blacksquare$

*(Упражнение к лекции: Доказать, что* $\lim_{n \to \infty} \frac{\cos^2 n}{2n+1} = 0$*)*

### §3. Предел монотонной последовательности

#### п.1. Теорема Вейерштрасса

* **Определение.** Последовательность $\{x_n\}$ называется:

  * монотонно возрастающей, $\{x_n\}\nearrow$, если $\forall n \quad x_n \le x_{n+1}$

  * монотонно убывающей, $\{x_n\}\searrow$, если $\forall n \quad x_n \ge x_{n+1}$

  * строго монотонно возрастающей, если $\forall n \quad x_n < x_{n+1}$

  * строго монотонно убывающей, если $\forall n \quad x_n > x_{n+1}$

**Теорема (Вейерштрасса о пределе монотонной последовательности)**

1. Если последовательность $\{x_n\}$ монотонно возрастает \[убывает\] и ограничена сверху \[снизу\], то она имеет конечный предел:
   

   $$
   \lim_{n \to \infty} x_n = \sup \{x_n\} \in \mathbb{R} \quad \left[ \lim_{n \to \infty} x_n = \inf \{x_n\} \in \mathbb{R} \right]
   $$

2. Если последовательность $\{x_n\}$ монотонно возрастает \[убывает\] и не ограничена сверху \[снизу\], то:
   

   $$
   \lim_{n \to \infty} x_n = \sup \{x_n\} = +\infty \quad \left[ \lim_{n \to \infty} x_n = \inf \{x_n\} = -\infty \right]
   $$

*Доказательство для возрастающей* $\{x_n\}$ *(для убывающей — аналогично):*
Пусть $\{x_n\}$ возрастает, $\forall n \quad x_n \le x_{n+1}$.

1. Рассмотрим множество членов последовательности $A = \{x_n \mid n \in \mathbb{N}\} \subset \mathbb{R}$. Множество $A \neq \varnothing$ и ограничено сверху, следовательно, по лемме о супремуме, существует $\sup A = \sup \{x_n\} = a \in \mathbb{R}$.
   Для произвольного $\varepsilon > 0$ по определению супремума, $\exists N: x_N > a - \varepsilon$.
   Тогда в силу монотонности $a - \varepsilon < x_N \le x_{N+1} \le x_{N+2} \le \dots \le a < a + \varepsilon$, то есть
   $\forall n \ge N \quad a - \varepsilon < x_n < a + \varepsilon$, то есть $\vert{}x_n - a\vert{} < \varepsilon$.
   Значит, $\lim_{n \to \infty} x_n = a$.

2. Пусть $\{x_n\}$ не ограничена сверху. Для произвольного $M > 0 \quad \exists N: x_N > M$.
   В силу монотонности $M < x_N \le x_{N+1} \le x_{N+2} \dots$, то есть $\forall n \ge N \quad x_n > M$.
   Значит, $\lim_{n \to \infty} x_n = +\infty$. $\blacksquare$

#### п.2. Примеры (стандартные пределы)

**1)** $\lim_{n \to \infty} \frac{n}{q^n} = 0, \quad q > 1$
Рассмотрим последовательность $x_n = \frac{n}{q^n}$, тогда $x_{n+1} = \frac{n+1}{q^{n+1}}$.

$$
\frac{x_{n+1}}{x_n} = \frac{n+1}{q^{n+1}} \cdot \frac{q^n}{n} = \frac{n+1}{q \cdot n} = \frac{1 + \frac{1}{n}}{q} < 1
$$


Это выполняется, если $1 + \frac{1}{n} < q \iff \frac{1}{n} < q - 1 \iff n > \frac{1}{q-1}$.
Последовательность $\{x_n\}$ убывает $\forall n \ge N = \left[\frac{1}{q-1}\right] + 1$.
Кроме того, $\forall n \quad x_n \ge 0$ — последовательность ограничена снизу.
По теореме Вейерштрасса, существует $\lim_{n \to \infty} x_n = a \ge 0 \quad (a \in \mathbb{R})$.
Так как $x_{n+1} = \frac{1 + \frac{1}{n}}{q} \cdot x_n$, то переходя к пределу при $n \to \infty$ получаем: $a = \frac{1}{q} \cdot a$, то есть $a = 0$.

**2)** $\lim_{n \to \infty} \frac{n^\alpha}{q^n} = 0, \quad \alpha > 0, q > 1$
Пусть $k = [\alpha] + 1$, тогда $0 \le \frac{n^\alpha}{q^n} \le \frac{n^k}{q^n} = \left( \frac{n}{(\sqrt[k]{q})^n} \right)^k$.
Так как $\lim_{n \to \infty} \left( \frac{n}{(\sqrt[k]{q})^n} \right)^k = 0^k = 0$ (поскольку $\sqrt[k]{q} > 1$), то по теореме о зажатой последовательности $\lim_{n \to \infty} \frac{n^\alpha}{q^n} = 0$.

**3)** $\lim_{n \to \infty} \frac{q^n}{n!} = 0, \quad q \in \mathbb{R}$

1. Для $q = 0$ — очевидно.

2. Пусть $q > 0$. Рассмотрим $x_n = \frac{q^n}{n!}, \quad x_{n+1} = \frac{q^{n+1}}{(n+1)!}$.
   

   $$
   \frac{x_{n+1}}{x_n} = \frac{q^{n+1}}{(n+1)!} \cdot \frac{n!}{q^n} = \frac{q}{n+1} < 1
   $$

   
   если $n+1 > q$, то есть $n \ge N = [q-1] + 1$.
   Следовательно, последовательность $\{x_n\}$ убывает при $n \ge N$.
   Кроме того, $x_n \ge 0 \quad \forall n$, следовательно, существует $\lim_{n \to \infty} x_n = a \ge 0 \quad (a \in \mathbb{R})$.
   Из равенства $x_{n+1} = \frac{q}{n+1} \cdot x_n$ в пределе при $n \to \infty$ получаем: $a = 0 \cdot a$, то есть $a = 0$.

3. Для $q < 0$: $\left\vert{} \frac{q^n}{n!} \right\vert{} = \frac{\vert{}q\vert{}^n}{n!}$, то есть $\forall n \quad -\frac{\vert{}q\vert{}^n}{n!} \le \frac{q^n}{n!} \le \frac{\vert{}q\vert{}^n}{n!}$.
   Так как $\lim_{n \to \infty} \frac{\vert{}q\vert{}^n}{n!} = \lim_{n \to \infty} \left(-\frac{\vert{}q\vert{}^n}{n!}\right) = 0$, то по свойству 12 (о зажатой последовательности) $\lim_{n \to \infty} \frac{q^n}{n!} = 0$.

**4)** $\lim_{n \to \infty} \sqrt[n]{n} = 1$
Из примера **1)** (где $\lim_{n \to \infty} \frac{n}{q^n} = 0 \implies$ для $\varepsilon = 1 \ \exists N: \forall n \ge N \ \vert{}\frac{n}{q^n}\vert{} < 1$) следует, что для любого $\varepsilon > 0 \quad \exists N: \forall n \ge N \quad \frac{n}{(1+\varepsilon)^n} < 1$ (взяли $1+\varepsilon$ вместо $q$, и $1$ вместо $\varepsilon$).
Тогда $\forall n \ge N \quad 1 \le n < (1+\varepsilon)^n$.
Извлекаем корень $n$-ной степени:
$\forall n \ge N \quad \sqrt[n]{1} \le \sqrt[n]{n} < \sqrt[n]{(1+\varepsilon)^n}$, то есть $1 \le \sqrt[n]{n} < 1 + \varepsilon$.
Отсюда $-\varepsilon < 0 \le \sqrt[n]{n} - 1 < \varepsilon$, следовательно $\vert{}\sqrt[n]{n} - 1\vert{} < \varepsilon$.
То есть $\lim_{n \to \infty} \sqrt[n]{n} = 1$.

**5)** $\lim_{n \to \infty} \sqrt[n]{a} = 1, \quad a > 0$
Существует $N: \forall n \ge N \quad \frac{1}{n} < a < n$.
Тогда $\forall n \ge N \quad \sqrt[n]{\frac{1}{n}} < \sqrt[n]{a} < \sqrt[n]{n}$.
Так как $\lim_{n \to \infty} \sqrt[n]{n} = 1$ и $\lim_{n \to \infty} \sqrt[n]{\frac{1}{n}} = \lim_{n \to \infty} \frac{1}{\sqrt[n]{n}} = \frac{1}{\lim_{n \to \infty} \sqrt[n]{n}} = 1$, то по теореме о зажатой последовательности, $\lim_{n \to \infty} \sqrt[n]{a} = 1$.
*(Упражнение: доказать* $\lim_{n \to \infty} \sqrt[n]{\cos n + 2} = 1$*)*

#### п.3. Число Эйлера (число e)

**Теорема.** Существует $\lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n = e, \quad 2 < e < 3$.

*Доказательство.*
Рассмотрим $x_n = \left(1 + \frac{1}{n}\right)^n$. По биному Ньютона:

$$
x_n = \left(1 + \frac{1}{n}\right)^n = \sum_{k=0}^n C_n^k \left(\frac{1}{n}\right)^k = \sum_{k=0}^n \frac{n!}{k!(n-k)!} \cdot \frac{1}{n^k} = 1 + \sum_{k=1}^n \frac{\overbrace{n(n-1)\dots(n-k+1)}^{k \text{ множителей}}}{k! \cdot n^k} =
$$

$$
= 1 + \sum_{k=1}^n \frac{1}{k!} \cdot \underbrace{1 \cdot \left(1 - \frac{1}{n}\right) \cdot \dots \cdot \left(1 - \frac{k-1}{n}\right)}_{C_{n,k}} = 1 + \sum_{k=1}^n \frac{C_{n,k}}{k!}
$$

Где введено обозначение:

* $C_{n,0} = 1$

* $C_{n,1} = 1$

* $C_{n,k} = \left(1 - \frac{1}{n}\right)\left(1 - \frac{2}{n}\right)\dots\left(1 - \frac{k-1}{n}\right)$

Очевидно, что $0 < C_{n,k} < 1$ для $2 \le k \le n$.
Заметим, что $C_{n,k} < C_{n+1,k}$ при $k \ge 2$, так как:
$C_{n,k} = \left(1 - \frac{1}{n}\right)\left(1 - \frac{2}{n}\right)\dots\left(1 - \frac{k-1}{n}\right)$
$C_{n+1,k} = \left(1 - \frac{1}{n+1}\right)\left(1 - \frac{2}{n+1}\right)\dots\left(1 - \frac{k-1}{n+1}\right)$, а каждый множитель вида $\left(1 - \frac{m}{n}\right) < \left(1 - \frac{m}{n+1}\right)$.

Тогда:

$$
x_n = 1 + 1 + \sum_{k=2}^n \frac{1}{k!} C_{n,k}
$$

$$
x_{n+1} = 1 + 1 + \sum_{k=2}^{n+1} \frac{1}{k!} C_{n+1,k} = 1 + 1 + \sum_{k=2}^n \frac{1}{k!} C_{n+1,k} + \underbrace{\frac{1}{(n+1)!} C_{n+1,n+1}}_{> 0} >
$$

$$
> 1 + 1 + \sum_{k=2}^n \frac{1}{k!} \underbrace{C_{n,k}}_{C_{n,k} < C_{n+1,k}} = x_n
$$

Значит, $x_n < x_{n+1} \quad \forall n \ge 2$, то есть последовательность монотонно возрастает.

### Число $e$ как предел

$$
x_n = \left(1 + \frac{1}{n}\right)^n = \sum_{k=0}^n C_{n,k} \frac{1}{k!} = 1 + 1 + \sum_{k=2}^n C_{n,k} \frac{1}{k!}, \quad \text{где} \quad C_{n,k} = \left(1 - \frac{1}{n}\right)\left(1 - \frac{2}{n}\right)\dots\left(1 - \frac{k-1}{n}\right), \; 1 \le k \le n
$$

$$
C_{n,0} = C_{n,1} = 1
$$

$$
0 < C_{n,k} < 1, \quad k > 1
$$

$$
\forall n \quad x_n < x_{n+1}, \quad \{x_n\} \nearrow
$$

$$
2 \le x_n = 2 + \sum_{k=2}^n C_{n,k} \frac{1}{k!} < 2 + \sum_{k=2}^n \frac{1}{k!} \le 2 + \sum_{k=2}^n \frac{1}{2^{k-1}} = 2 + \frac{1}{2} + \frac{1}{2^2} + \dots + \frac{1}{2^{n-1}} = 2 + \frac{\frac{1}{2} \left(1 - \left(\frac{1}{2}\right)^{n-1}\right)}{1 - \frac{1}{2}} = 3 - \left(\frac{1}{2}\right)^{n-1} < 3 \quad \forall n
$$


*(При оценке суммы использована геометрическая прогрессия, где* $b_1 = 1/2$*,* $q = 1/2$*,* $n-1$ *слагаемых)*

* Последовательность $\{x_n\}$ ограничена сверху: $\forall n \quad x_n < 3$.

По теореме Вейерштрасса, существует конечный $\lim_{n \to \infty} x_n$, который называется числом $e$:

$$
\lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n = e, \quad 2 < e \le 3 \quad \blacksquare
$$

**Упражнение.** Доказать, что $x_n < 2 + \frac{3}{4} \quad \forall n$ (использовать оценку $k! \ge 2 \cdot 3^{k-2}, k \ge 2$).

**Теорема (Число** $e$ **как предел суммы):**

$$
e = \lim_{n \to \infty} \left(\sum_{k=0}^n \frac{1}{k!}\right)
$$

**Доказательство.**
Рассмотрим $x_n = \sum_{k=0}^n \frac{1}{k!} = 1 + 1 + \frac{1}{2!} + \dots + \frac{1}{n!}$, и $y_n = \left(1 + \frac{1}{n}\right)^n = \sum_{k=0}^n C_{n,k} \frac{1}{k!} = 1 + 1 + \sum_{k=2}^n C_{n,k} \frac{1}{k!}$.
Мы знаем, что $\lim_{n \to \infty} y_n = e$. Очевидно, что $y_n \le x_n \quad \forall n$. Докажем, что $\lim_{n \to \infty} (x_n - y_n) = 0$.

Рассмотрим $x_n - y_n = \sum_{k=2}^n (1 - C_{n,k}) \cdot \frac{1}{k!}$.

* **Лемма.** $\lim_{n \to \infty} C_{n,k} = 1$ для любого $k \in \mathbb{N}$.
  **Доказательство по индукции:**
  $k=1: \quad C_{n,1} = 1$
  $k=2: \quad C_{n,2} = 1 - \frac{1}{n} \to 1$ при $n \to \infty$
  Пусть для $k$ верно: $C_{n,k} = \left(1 - \frac{1}{n}\right)\left(1 - \frac{2}{n}\right)\dots\left(1 - \frac{k-1}{n}\right) \to 1$
  Тогда для $k+1$:
  $C_{n,k+1} = \left(1 - \frac{1}{n}\right)\dots\left(1 - \frac{k-1}{n}\right)\left(1 - \frac{k}{n}\right) = C_{n,k} \cdot \left(1 - \frac{k}{n}\right) \to 1$ при $n \to \infty$.
  *Лемма доказана.*

Пусть $\varepsilon > 0$ — произвольное, будем считать, что $0 < \varepsilon < 4$.
Зафиксируем $k_0 \in \mathbb{N}$ (выберем его ниже), и запишем:

$$
\vert{}x_n - y_n\vert{} = \left\vert{} \sum_{k=2}^{k_0-1} (1 - C_{n,k}) \cdot \frac{1}{k!} + \sum_{k=k_0}^n \frac{1}{k!} - \sum_{k=k_0}^n C_{n,k} \frac{1}{k!} \right\vert{} \le
$$

$$
\le \left\vert{} \sum_{k=2}^{k_0-1} (1 - C_{n,k}) \frac{1}{k!} \right\vert{} + \left\vert{} \sum_{k=k_0}^n (1 - C_{n,k}) \frac{1}{k!} \right\vert{} = \underbrace{\sum_{k=2}^{k_0-1} (1 - C_{n,k}) \frac{1}{k!}}_{\text{конечное число слагаемых}} + \underbrace{\sum_{k=k_0}^n (1 - C_{n,k}) \frac{1}{k!}}_{\text{число слагаемых зависит от } n} \le (*)
$$

Оценим второе слагаемое через геометрическую прогрессию:

$$
\sum_{k=k_0}^n \underbrace{(1 - C_{n,k})}_{<1} \cdot \frac{1}{k!} < \sum_{k=k_0}^n \frac{1}{k!} = \frac{1}{k_0!} + \frac{1}{k_0!(k_0+1)} + \frac{1}{k_0!(k_0+1)(k_0+2)} + \dots + \frac{1}{k_0!(k_0+1)\dots n} \le
$$

$$
\le \frac{1}{k_0!} \left( 1 + \frac{1}{k_0+1} + \frac{1}{(k_0+1)^2} + \dots + \frac{1}{(k_0+1)^{n-k_0}} \right) = \frac{1}{k_0!} \frac{1 \cdot \left(1 - \left( \frac{1}{k_0+1} \right)^{n-k_0+1}\right)}{1 - \frac{1}{k_0+1}} <
$$

$$
< \frac{1}{k_0!} \frac{1}{1 - \frac{1}{k_0+1}} \le \frac{1}{k_0!} \cdot 2 \le \frac{1}{2^{k_0-1}} \cdot 2 < \frac{\varepsilon}{2}, \quad \text{если выбрать } k_0 > \log_2 \frac{4}{\varepsilon}
$$

*(Пояснение к оценке)*:
$\frac{1}{1 - \frac{1}{k_0+1}} \le 2 \implies 1 - \frac{1}{k_0+1} \ge \frac{1}{2} \implies \frac{1}{k_0+1} \le \frac{1}{2} \implies k_0+1 \ge 2$

Так как $k_0$ — фиксированное, то для оценки первого слагаемого найдем $N$:
$\forall n \ge N \quad 1 - C_{n,k} < \frac{\varepsilon}{2k_0}$ для всех $k=2,3,\dots,k_0-1$
Тогда $\sum_{k=2}^{k_0-1} (1 - C_{n,k}) \cdot \frac{1}{k!} < \sum_{k=2}^{k_0-1} \frac{\varepsilon}{2k_0} \cdot \left( \frac{1}{k!} \right) \le \frac{\varepsilon}{2}$
Тогда $\forall n \ge N \quad \vert{}x_n - y_n\vert{} \le (*) < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon. \quad \blacksquare$

**Следствие.** Обозначим $R_n = e - \sum_{k=0}^n \frac{1}{k!} > 0 \quad \forall n$, так как $x_n = \sum_{k=0}^n \frac{1}{k!} \nearrow$, и $\lim_{n \to \infty} x_n = \sup \{x_n\}$.
Тогда $0 < R_n \le \frac{1}{(n+1)!} \cdot \frac{n+2}{n+1}, \quad n \ge 2.$

**Доказательство.**
Так как $e = \sup_{m \in \mathbb{N}} \sum_{k=0}^m \frac{1}{k!} = \sum_{k=0}^n \frac{1}{k!} + \sup_{m \ge n} \sum_{k=n+1}^m \frac{1}{k!}$, то $R_n = e - \sum_{k=0}^n \frac{1}{k!} = \sup_{m \ge n} \sum_{k=n+1}^m \frac{1}{k!} =$

$$
= \sup_{m \ge n} \left( \frac{1}{(n+1)!} + \frac{1}{(n+2)!} + \dots + \frac{1}{m!} \right) = \sup_{m \ge n} \left( \frac{1}{(n+1)!} + \frac{1}{(n+1)!(n+2)} + \frac{1}{(n+1)!(n+2)(n+3)} + \dots + \frac{1}{(n+1)!(n+2)\dots m} \right) \le
$$

$$
\le \sup_{m \ge n} \frac{1}{(n+1)!} \left( 1 + \frac{1}{n+2} + \frac{1}{(n+2)^2} + \dots + \frac{1}{(n+2)^{m-n-1}} \right) \le \sup_{m \ge n} \frac{1}{(n+1)!} \cdot \frac{1 \cdot \left( 1 - \overbrace{\left( \frac{1}{n+2} \right)^{m-n}}^{<1} \right)}{1 - \frac{1}{n+2}} \le
$$

$$
\le \frac{1}{(n+1)!} \cdot \frac{1}{1 - \frac{1}{n+2}} = \frac{1}{(n+1)!} \cdot \frac{n+2}{n+1} \quad \blacksquare
$$

**Замечание.** Можно записать $e = \sum_{k=0}^n \frac{1}{k!} + \underbrace{\theta_n \cdot \frac{1}{(n+1)!} \frac{n+2}{n+1}}_{= R_n}$, где $0 < \theta_n \le 1, \quad n \ge 2.$

**Следствие.** $e$ — иррациональное число.

**Доказательство.** Предположим, что $e = \frac{p}{q} \in \mathbb{Q}$, тогда для $n=q \quad (q \in \mathbb{N})$:

$$
e = \frac{p}{q} = \sum_{k=0}^q \frac{1}{k!} + \theta_q \cdot \frac{1}{(q+1)!} \frac{q+2}{q+1} \quad \bigg/ \cdot q!
$$

$$
\underbrace{p \cdot \frac{(q-1)!}{q}}_{\in \mathbb{Z}} - \underbrace{q! \sum_{k=0}^q \frac{1}{k!}}_{\in \mathbb{Z}} = \underbrace{\theta_q \cdot \frac{q+2}{(q+1)^2}}_{\in (0,1) \implies \notin \mathbb{Z}}
$$


Слева стоит разность двух целых чисел, а справа — дробное. Получили противоречие. $\blacksquare$

### п. 4. Длина окружности и число $\pi$

Обозначим через $L_n$ периметр вписанного в окружность правильного $2^n$-угольника, $n \ge 2$. Очевидно $L_n < L_{n+1}$.

Пусть $\omega = 180^\circ$ (развернутый угол).
Угол $\alpha = \frac{2\omega}{2^n}$.
Сторона вписанного многоугольника: $a_n = 2R \sin \frac{\alpha}{2} = 2R \sin \frac{\omega}{2^n}$.
Периметр: $L_n = 2^n \cdot a_n = 2^{n+1} R \sin \frac{\omega}{2^n}$.
При $n=2$: $L_2 = 2^3 R \sin \left(\frac{\omega}{4}\right) = 4\sqrt{2} R$.

Пусть $L'_n$ — периметр описанного правильного $2^n$-угольника. Очевидно, $L'_n > L'_{n+1}$.
Сторона описанного многоугольника: $b_n = 2R \text{tg} \frac{\alpha}{2} = 2R \text{tg} \frac{\omega}{2^n}$.
Периметр: $L'_n = 2^n \cdot b_n = 2^{n+1} R \text{tg} \frac{\omega}{2^n}$.
При $n=2$: $L'_2 = 8 R \text{tg} \frac{\omega}{4} = 8 R$.

Таким образом, $L_2 \le L_n < L'_n \le L'_2 \quad (4\sqrt{2} R \le L_n < L'_n \le 8R)$.
Последовательность $\{L_n\} \nearrow$, $\{L'_n\} \searrow$, следовательно, существуют пределы $\lim_{n \to \infty} \frac{L_n}{R} \in [4\sqrt{2}; 8]$ и $\lim_{n \to \infty} \frac{L'_n}{R} \in [4\sqrt{2}; 8]$.

$$
\lim_{n \to \infty} \frac{L'_n}{R} = \lim_{n \to \infty} 2^{n+1} \frac{\sin \frac{\omega}{2^n}}{\underbrace{\cos \frac{\omega}{2^n}}_{\to 1 \text{ (почему?)}}} = \lim_{n \to \infty} 2^{n+1} \sin \frac{\omega}{2^n} = \lim_{n \to \infty} \frac{L_n}{R}
$$

Обозначим этот предел через $2\pi$, а $\lim_{n \to \infty} L_n = \lim_{n \to \infty} L'_n = 2\pi R$ назовем длиной окружности.
Так как $4\sqrt{2} < 2\pi < 8$, то $2\sqrt{2} < \pi < 4$.

Обозначим $\omega = \pi$ (радиан), тогда:

$$
\lim_{n \to \infty} 2^{n+1} \sin \frac{\pi}{2^n} = 2\pi
$$


Длина дуги окружности: $L_\alpha = \frac{2\pi R}{2\pi} \alpha = R \cdot \alpha$.

**Свойство.** Для $0 < x < \frac{\pi}{2} \quad \sin x < x < \text{tg} x$.
**Доказательство.**
$2AB < L_{\text{дуги}} < 2 \cdot CD$
$2R \sin \frac{\alpha}{2} < 2R \cdot \frac{\alpha}{2} < 2R \cdot \text{tg} \frac{\alpha}{2}$
$\sin \frac{\alpha}{2} < \frac{\alpha}{2} < \text{tg} \frac{\alpha}{2} \quad \blacksquare$

### §4. Принцип вложенных отрезков

**Лемма о вложенных отрезках (принцип Коши - Кантора)**
Последовательность вложенных друг в друга отрезков $[a_1, b_1] \supset [a_2, b_2] \supset \dots \supset [a_n, b_n] \supset [a_{n+1}, b_{n+1}] \supset \dots$ имеет общую точку.
Если длины отрезков стремятся к 0: $\lim_{n \to \infty} (b_n - a_n) = 0$, то эта точка единственна.

**Доказательство.**

$$
a_1 \le a_2 \le \dots \le a_n \le a_{n+1} \le \dots \le b_{n+1} \le b_n \le \dots \le b_2 \le b_1
$$


Последовательность $\{a_n\} \nearrow$ и ограничена сверху: $\forall n \quad a_n \le b_1$, следовательно, существует $\lim_{n \to \infty} a_n = a$.
Последовательность $\{b_n\} \searrow$ и ограничена снизу: $\forall n \quad b_n \ge a_1$, следовательно, существует $\lim_{n \to \infty} b_n = b$.

Так как $a_n \le b_m \quad \forall n,m$, то
$a = \lim_{n \to \infty} a_n \le b_m \quad \forall m$, и
$b = \lim_{m \to \infty} b_m \ge a_n \quad \forall n$.

Так как $\forall n \quad a_n \le b_n$, то $a \le b$.
Следовательно, $\forall n \quad a_n \le a \le b \le b_n$, то есть $[a, b] \subset [a_n, b_n] \quad \forall n$.

Если $\lim_{n \to \infty} (b_n - a_n) = 0$, то $b - a = 0$, и $a = b$.
Пусть $a=b$, и существует $c \in [a_n, b_n] \quad \forall n$.
Тогда $0 \le \vert{}c - a\vert{} \le \underbrace{b_n - a_n}_{\to 0} \quad \forall n$.
Следовательно, $c = a$. $\blacksquare$

**Пример.**

* $\bigcap_{n=1}^\infty \left[-\frac{1}{n}, \frac{1}{n}\right] = \{0\}$, длина $\frac{2}{n} \to 0$.

* $\bigcap_{n=1}^\infty \left(0, \frac{1}{n}\right) = \emptyset$ (для интервалов и полуинтервалов утверждение неверно).

**Свойство.** Множество $[0; 1]$ несчётно.

**Доказательство.** От противного: предположим, что $[0; 1] = \{x_n \mid n \in \mathbb{N}\}$
Разделим отрезок $[0; 1]$ на 3 равные части: $[0; 1/3], [1/3; 2/3], [2/3; 1]$, обозначим через $[a_1, b_1]$ ту из них, которая не содержит $x_1$.
Далее разделим $[a_1, b_1]$ на 3 равные части, обозначим через $[a_2, b_2]$ ту из них, которая не содержит $x_2$.
и т.д.
Получим последовательность вложенных отрезков $[a_1, b_1] \supset [a_2, b_2] \supset \dots \supset [a_n, b_n] \supset \dots$,
длина отрезка $[a_n, b_n]$ равна $b_n - a_n = \frac{1-0}{3^n} \to 0$ при $n \to \infty$.
По лемме о вложенных отрезках, существует единственный $x \in [a_n, b_n] \; \forall n, \; x \in [0; 1]$.
Так как по построению $x_n \notin [a_n, b_n] \; \forall n$, то $x \neq x_n \; \forall n$ — противоречие. $\blacksquare$

### §5. Критерий Коши сходимости последовательностей.

**Лемма (Больцано-Вейерштрасса)**
Из каждой ограниченной последовательности можно выбрать сходящуюся подпоследовательность.

**Доказательство.** Пусть $\exists a, b \in \mathbb{R}: \forall n \quad a \le x_n \le b$.
Разделим $[a, b]$ пополам, и обозначим через $[a_1, b_1]$ ту из половин $[a; \frac{a+b}{2}]$ или $[\frac{a+b}{2}; b]$, в которой содержится бесконечное число членов последовательности (если в обеих половинах содержится бесконечное число членов, то выбираем любую из них).
Т.е. множество $\{n \in \mathbb{N} \mid x_n \in [a_1, b_1]\}$ бесконечно.
Обозначим $n_1 = \min \{n \in \mathbb{N} \mid x_n \in [a_1, b_1]\}$, т.е. $x_{n_1} \in [a_1, b_1]$.

Разделим $[a_1, b_1]$ пополам, обозначим через $[a_2, b_2]$ ту из половин отрезка $[a_1, b_1]$, для которой множество $\{n > n_1 \mid x_n \in [a_2, b_2]\}$ бесконечно.
Если обе половины подходят, то выбираем любую.
Обозначим $n_2 = \min \{n > n_1 \mid x_n \in [a_2, b_2]\}, \quad x_{n_2} \in [a_2, b_2]$.
и т.д.

На $k$-м шаге: $[a_k, b_k]$ — та половина $[a_{k-1}, b_{k-1}]$, для которой множество 
$\{n > n_{k-1} \mid x_n \in [a_k, b_k]\}$ бесконечно, и $n_k = \min \{n > n_{k-1} \mid x_n \in [a_k, b_k]\}$.
Т.е. получили последовательность вложенных отрезков $[a_1, b_1] \supset [a_2, b_2] \supset \dots \supset [a_k, b_k] \supset \dots$, длины которых: $b_k - a_k = \frac{b-a}{2^k} \to 0$ при $k \to \infty$, и подпоследовательность $\{x_{n_k}\}$ последовательности $\{x_n\}$,
$x_{n_k} \in [a_k, b_k], \; k=1,2,3,\dots$
По лемме о вложенных отрезках, существует $C = \lim_{k\to\infty} a_k = \lim_{k\to\infty} b_k$. Так как $a_k \le x_{n_k} \le b_k \; \forall k$, то по теореме о зажатой последовательности, существует $\lim_{k\to\infty} x_{n_k} = C$. $\blacksquare$

**Определение.** Последовательность $\{x_n\}$ называется фундаментальной (последовательностью Коши, сходящейся в себе), если
$$ \forall \varepsilon > 0 \;\; \exists N = N(\varepsilon): \forall n, m \ge N \quad |x_n - x_m| < \varepsilon $$
Или: 
$$ \forall \varepsilon > 0 \;\; \exists N = N(\varepsilon): \forall n \ge N \;\; \forall p \ge 1 \quad |x_{n+p} - x_n| < \varepsilon $$

**Теорема (Критерий Коши сходимости последовательностей)**
Последовательность $\{x_n\}$ сходится $\Leftrightarrow \{x_n\}$ фундаментальна. (существует $\lim_{n\to\infty} x_n \in \mathbb{R}$)

**Доказательство.**
$\Rightarrow$ Пусть $\lim_{n\to\infty} x_n = a \in \mathbb{R}$. Пусть $\varepsilon > 0$ — произвольное. Тогда $\exists N: \forall n > N \quad |x_n - a| < \frac{\varepsilon}{2}$.
Тогда $\forall m, n \ge N \quad |x_n - x_m| = |(x_n - a) + (a - x_m)| \le |x_n - a| + |a - x_m| < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon$, т.е. $\{x_n\}$ фундаментальная.

$\Leftarrow$ Пусть $\{x_n\}$ — фундаментальная последовательность.
- **1)** Если $\{x_n\}$ фундаментальная, то она — ограничена.
Действительно, для $\varepsilon = 1 \quad \exists N: \forall n, m \ge N \quad |x_n - x_m| < 1$.
Зафиксируем $m = N$, тогда $\forall n \ge N \quad |x_n - x_N| < 1$, 
$|x_n| = |(x_n - x_N) + x_N| \le |x_n - x_N| + |x_N| < |x_N| + 1 \quad \forall n \ge N$.
Полагаем $M = \max(|x_1|, |x_2|, \dots, |x_{N-1}|, |x_N| + 1)$, тогда $\forall n \quad |x_n| \le M$.

- **2)** По лемме Больцано-Вейерштрасса, из последовательности $\{x_n\}$ можно выбрать сходящуюся подпоследовательность $\{x_{n_k}\}$: 
$\lim_{k\to\infty} x_{n_k} = a \in \mathbb{R}$.

- **3)** Докажем, что сама последовательность $\{x_n\}$ сходится к тому же числу $a$, что и её подпоследовательность $\{x_{n_k}\}$.
Пусть $\varepsilon > 0$ — произвольное.
Так как $\{x_n\}$ фундаментальная, то $\exists N_1: \forall n, m \ge N_1 \quad |x_n - x_m| < \frac{\varepsilon}{2}$.
Так как $\lim_{k\to\infty} x_{n_k} = a$, то $\exists N_2: \forall k \ge N_2 \quad |x_{n_k} - a| < \frac{\varepsilon}{2}$.
Обозначим $N = \max(N_1, N_2)$, тогда для $\forall n \ge N$ выберем $k \ge N$, тогда тем более $n_k \ge k \ge N$,
и $|x_n - a| = |x_n - x_{n_k} + x_{n_k} - a| \le |x_n - x_{n_k}| + |x_{n_k} - a| < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon$,
т.е. $\lim_{n\to\infty} x_n = a$. $\blacksquare$

**Пример.** Последовательность $x_n = \sin n$ расходится (не имеет предела).
Предположим, что $\{x_n\}$ сходится, тогда она фундаментальная, т.е. $\forall \varepsilon > 0 \;\; \exists N: \forall n \ge N \;\; \forall p \ge 1 \quad |x_{n+p} - x_n| = |\sin(n+p) - \sin n| < \varepsilon$.
Для $p = 2: \quad \forall n \ge N \quad |\sin(n+2) - \sin n| = |2 \sin \frac{n+2-n}{2} \cos \frac{n+2+n}{2}| = 2 \sin 1 \cdot |\cos(n+1)| < \varepsilon$.
Т.е. $\forall n \ge N \quad |\cos(n+1)| < \frac{\varepsilon}{2 \sin 1}$, это значит, $\lim_{n\to\infty} \cos(n+1) = 0$, или $\lim_{m\to\infty} \cos m = 0$.
Далее, $\cos(n+1) = \cos n \cdot \cos 1 - \sin n \cdot \sin 1$, следовательно, $\lim_{n\to\infty} \sin n = 0$.
Тогда $\lim_{n\to\infty} (\sin^2 n + \cos^2 n) = 0$ — противоречие (т.к. равно 1). Значит, $\{x_n\}$ расходится.

### §6. Частичные пределы последовательности. Верхний и нижний пределы.

#### п.1. Частичные пределы.

**Определение.** Частичный предел последовательности $\{x_n\}$ — это предел какой-либо её подпоследовательности.

**Свойства:**
- **1)** Если существует $\lim_{n\to\infty} x_n$ (конечный или бесконечный), то все частичные пределы последовательности совпадают с ним.
Для $\lim_{n\to\infty} x_n = a \in \mathbb{R}$ — доказывали.
Для $\lim_{n\to\infty} x_n = +\infty$: Пусть $\{x_{n_k}\}$ — подпоследовательность. Для произвольного $M > 0 \;\; \exists N: \forall n > N \quad x_n > M$.
Тогда $\forall k \ge N \quad n_k \ge k \ge N$, и $x_{n_k} > M$, т.е. $\lim_{k\to\infty} x_{n_k} = +\infty$.

- **2)** Если $\{x_n\}$ монотонна, то она имеет предел (конечный или бесконечный), и все её частичные пределы совпадают. (Следует из теоремы Вейерштрасса).

**Лемма.** Если $\{x_n\}$ не ограничена сверху [снизу], то существует подпоследовательность $\{x_{n_k}\}$: $\lim_{k\to\infty} x_{n_k} = +\infty$ [$\lim_{k\to\infty} x_{n_k} = -\infty$].

**Доказательство.** Пусть $\{x_n\}$ не ограничена сверху, $\forall M > 0 \;\; \exists n: x_n > M$.
Для $M=1 \;\; \exists n_1: x_{n_1} > 1$.
Замечание: последовательность $\{x_n\}_{n > n_1}$ тоже не ограничена сверху (Если бы это было не так, то и $\{x_n\}_{n \in \mathbb{N}}$ была бы ограничена сверху).
Для $M=2 \;\; \exists n_2 > n_1: x_{n_2} > 2$
и т.д.
Для $M=k \;\; \exists n_k > n_{k-1}: x_{n_k} > k$, и т.д.
Получим подпоследовательность $\{x_{n_k}\}$. Так как $x_{n_k} > k \;\; \forall k$, то $\lim_{k\to\infty} x_{n_k} = +\infty$. $\blacksquare$

Замечание: $\{x_n\}$ не ограничена снизу $\implies \forall M > 0 \;\; \exists n: x_n < -M$
$M=1; \;\; x_{n_1} < -1$
...
$M=k; \;\; x_{n_k} < -k, \;\; n_k > n_{k-1}$
$\lim_{k\to\infty} x_{n_k} = -\infty$

**Теорема (Вейерштрасса о частичном пределе)**
Множество всех частичных пределов (конечных или бесконечных) последовательности $\{x_n\}$ представляет собой непустое множество.

**Доказательство.**
Если $\{x_n\}$ ограничена, то утверждение следует из леммы Больцано-Вейерштрасса, существует конечный частичный предел.
Если $\{x_n\}$ не ограничена, то утверждение следует из предыдущей леммы, существует бесконечный частичный предел. $\blacksquare$

#### п.2. Верхний и нижний пределы последовательности.

Пусть $\{x_n\}$ — последовательность. Рассмотрим последовательность $z_n = \sup \{x_n, x_{n+1}, x_{n+2}, \dots\} = \sup_{k \ge n} x_k, \quad z_n \in \mathbb{R} \cup \{+\infty\}$.
Если $\{x_n\}$ не ограничена сверху, то $z_n = +\infty \;\; \forall n$.
Если же $\{x_n\}$ ограничена сверху, то $z_{n+1} \le z_n \;\; \forall n$, так как $\{x_{n+1}, x_{n+2}, \dots\} \subset \{x_n, x_{n+1}, x_{n+2}, \dots\}$. (Если $A \subset B$, то $\sup A \le \sup B$).

Так как $\{z_n\}$ монотонно убывающая, то существует $\lim_{n\to\infty} z_n = \inf_{n} z_n = z$, где либо $z \in \mathbb{R}$, либо $z = -\infty$.
(Если $z_n = +\infty \;\; \forall n$, то $z = +\infty$.)

**Определение.** Верхним пределом последовательности $\{x_n\}$ называется 
$$ \overline{\lim_{n\to\infty}} x_n = \limsup_{n\to\infty} x_n = \lim_{n\to\infty} \sup_{k \ge n} x_k = \inf_{n} \sup_{k \ge n} x_k $$

Аналогично: обозначим $w_n = \inf_{k \ge n} x_k = \inf \{x_n, x_{n+1}, \dots\}$
Если $\{x_n\}$ не ограничена снизу, то $w_n = -\infty \;\; \forall n$, и $W = \lim_{n\to\infty} w_n = -\infty$.
Если $\{x_n\}$ ограничена снизу, то $\forall n \;\; w_{n+1} \ge w_n$, $\{w_n\} \nearrow$, и существует $W = \lim_{n\to\infty} w_n = \sup w_n, \quad W \in \mathbb{R}$ или $W = +\infty$.

**Определение.** Нижним пределом последовательности $\{x_n\}$ называется
$$ \underline{\lim}_{n\to\infty} x_n = \liminf_{n\to\infty} x_n = \lim_{n\to\infty} \inf_{k \ge n} x_k = \sup_{n} \inf_{k \ge n} x_k $$

**Пример.**
- **1)** $x_k = k^{(-1)^k}, \;\; k \in \mathbb{N}: \quad 1^{-1}; 2^{+1}; 3^{-1}; 4^{+1}; \dots$
$$ x_k = \begin{cases} 
k, & \text{k-четное} \\ 
\frac{1}{k}, & \text{k-нечетное} 
\end{cases} $$

$$ w_n = \inf_{k \ge n} x_k = \begin{cases} 
\inf \{n; \frac{1}{n+1}; n+2; \frac{1}{n+3}; \dots\} = 0, & \text{если n-четное} \\ 
\inf \{\frac{1}{n}; n+1; \frac{1}{n+2}; n+3; \dots\} = 0, & \text{если n-нечетное} 
\end{cases} $$
$$ w_n = 0 \;\; \forall n, \quad \underline{\lim}_{n\to\infty} x_n = \lim_{n\to\infty} w_n = 0 $$

$$ z_n = \sup_{k \ge n} x_k = \begin{cases} 
\sup \{n; \frac{1}{n+1}; n+2; \dots\} = +\infty, & \text{n-четное} \\ 
\sup \{\frac{1}{n}; n+1; \frac{1}{n+2}; \dots\} = +\infty, & \text{n-нечетное} 
\end{cases} $$
$$ z_n = +\infty \;\; \forall n, \quad \overline{\lim}_{n\to\infty} x_n = \lim_{n\to\infty} z_n = +\infty $$

**2)** $x_n = (-1)^n \left(1 + \frac{1}{n}\right)$

$$z_n = \sup_{k \ge n} x_k = \begin{cases} \sup \left\{ \left(1 + \frac{1}{n}\right); -\left(1 + \frac{1}{n+1}\right); 1 + \frac{1}{n+2}; \dots \right\} = 1 + \frac{1}{n}, & n \text{ — чётное} \\ \sup \left\{ \underbrace{-\left(1 + \frac{1}{n}\right)}_{< 0}; \left(1 + \frac{1}{n+1}\right); -\left(1 + \frac{1}{n+2}\right); \dots \right\} = 1 + \frac{1}{n+1}, & n \text{ — нечётное} \end{cases}$$

- $\{z_n\}: \quad \underset{n=1}{1 + \frac{1}{2}}; \; \underset{n=2}{1 + \frac{1}{2}}; \; \underset{n=3}{1 + \frac{1}{4}}; \; \underset{n=4}{1 + \frac{1}{4}}; \; 1 + \frac{1}{6}; \; 1 + \frac{1}{6}; \; \dots$

$$\overline{\lim_{n \to \infty}} x_n = \lim_{n \to \infty} z_n = \inf_n z_n = 1$$

$$w_n = \inf_{k \ge n} x_k = \begin{cases} \inf \left\{ 1 + \frac{1}{n}; -\left(1 + \frac{1}{n+1}\right); 1 + \frac{1}{n+2}; \dots \right\} = -\left(1 + \frac{1}{n+1}\right), & \text{если } n \text{ — чётное} \\ \inf \left\{ -\left(1 + \frac{1}{n}\right); 1 + \frac{1}{n+1}; -\left(1 + \frac{1}{n+2}\right); \dots \right\} = -\left(1 + \frac{1}{n}\right), & n \text{ — нечётное} \end{cases}$$

$$\underline{\lim}_{n \to \infty} x_n = \lim_{n \to \infty} w_n = \sup_n w_n = -1$$

#### п. 3. Свойства $\overline{\lim_{n \to \infty}} x_n$ и $\underline{\lim}_{n \to \infty} x_n$

- **Свойство 1.**
  * **1)** Если $\overline{\lim_{n \to \infty}} x_n = a$, то $\forall \varepsilon > 0 \quad \exists N : \forall n \ge N \quad x_n < a + \varepsilon$.
  * **2)** Если $\underline{\lim}_{n \to \infty} x_n = a$, то $\forall \varepsilon > 0 \quad \exists N : \forall n \ge N \quad x_n > a - \varepsilon$.

**Доказательство:**

- **1)** Для $a \in \mathbb{R}$. $\quad a = \lim_{n \to \infty} \sup_{k \ge n} x_k$.
  * Для произвольного $\varepsilon > 0 \quad \exists N : \forall n \ge N \quad \left| \overbrace{\sup_{k \ge n} x_k}^{z_n} - a \right| < \varepsilon, \quad \overbrace{\sup_{k \ge n} x_k}^{z_n} < a + \varepsilon$
    $$\left( |z_n - a| < \varepsilon \iff -\varepsilon < z_n - a < \varepsilon \iff a - \varepsilon < z_n < a + \varepsilon \right)$$
  * Тем более $\forall n \ge N \quad x_n \le \sup_{k \ge n} x_k < a + \varepsilon$. $\blacksquare$


- **Свойство 2.** Пусть $a = \overline{\lim_{n \to \infty}} x_n$. Тогда:
  * **1)** Если $\forall \varepsilon > 0 \quad \exists N : \forall n \ge N \quad x_n < b + \varepsilon$, то $a \le b$.
  * **2)** Если $\forall \varepsilon > 0$ множество $\{n : x_n > c - \varepsilon\}$ бесконечно, то $c \le a$.

**Доказательство (для $a \in \mathbb{R}$):**

- **1)** Предположим, что $a > b$. Выберем $\varepsilon > 0$ так, что $b + \varepsilon < a$, например, $\varepsilon = \frac{a - b}{2} > 0$.
  * Тогда $\exists N : \forall n \ge N \quad x_n < b + \varepsilon$, тогда и $\forall n \ge N \quad z_n = \sup_{k \ge n} x_k \le b + \varepsilon$, и
    $$a = \lim_{n \to \infty} z_n \le b + \varepsilon < a \text{ — противоречие. Значит, } a \le b.$$


- **2)** Предположим, что $c > a$. Выберем $\varepsilon > 0$ так, чтобы $c - \varepsilon > a$, например, $\varepsilon = \frac{c - a}{2} > 0$.
  * Так как множество $\{n : x_n > c - \varepsilon\}$ бесконечно, то $\forall n \quad z_n = \sup_{k \ge n} x_k \ge c - \varepsilon$.
  * Тогда $a = \lim_{n \to \infty} z_n \ge c - \varepsilon > a$ — противоречие. Значит, $c \le a$.


- **Свойство 3.** Пусть $a = \underline{\lim}_{n \to \infty} x_n$. Тогда:
  * **1)** Если $\forall \varepsilon > 0 \quad \exists N : \forall n \ge N \quad x_n > b - \varepsilon$, то $a \ge b$.
  * **2)** Если $\forall \varepsilon > 0$ множество $\{n : x_n < c + \varepsilon\}$ бесконечно, то $c \ge a$. *(аналогично)*


- **Свойство 4.** Пусть $\exists N : \forall n \ge N \quad x_n \le y_n$. Тогда $\overline{\lim_{n \to \infty}} x_n \le \overline{\lim_{n \to \infty}} y_n, \quad \underline{\lim}_{n \to \infty} x_n \le \underline{\lim}_{n \to \infty} y_n$.

**Доказательство:**

- Если $\forall n \ge N \quad x_n \le y_n$, то:
  $$\forall n \ge N \quad \forall m \ge n \quad x_m \le \sup_{k \ge n} y_k$$
  $$\forall n \ge N \quad \sup_{m \ge n} x_m \le \sup_{k \ge n} y_k$$
  $$\lim_{n \to \infty} \sup_{m \ge n} x_m \le \lim_{n \to \infty} \sup_{k \ge n} y_k, \text{ то есть } \overline{\lim_{n \to \infty}} x_n \le \overline{\lim_{n \to \infty}} y_n$$


- Для нижнего предела — аналогично. $\blacksquare$


- **Свойство 5 (арифметические свойства).** Пусть $\{x_n\}$ и $\{y_n\}$ — ограниченные последовательности.
  * **1)** $\overline{\lim_{n \to \infty}} (x_n + y_n) \le \overline{\lim_{n \to \infty}} x_n + \overline{\lim_{n \to \infty}} y_n$
    $$\underline{\lim}_{n \to \infty} (x_n + y_n) \ge \underline{\lim}_{n \to \infty} x_n + \underline{\lim}_{n \to \infty} y_n$$
    * **Пример:** $x_n = (-1)^n, \; y_n = (-1)^{n+1}, \quad \overline{\lim_{n \to \infty}} x_n = \overline{\lim_{n \to \infty}} y_n = 1$. При этом $x_n + y_n = 0, \quad \overline{\lim_{n \to \infty}} (x_n + y_n) = 0 \ne 2$.
    * **Упражнение:**
      $$\overline{\lim_{n \to \infty}} (x_n + y_n) \ge \overline{\lim_{n \to \infty}} x_n + \underline{\lim}_{n \to \infty} y_n$$
      $$\underline{\lim}_{n \to \infty} (x_n + y_n) \le \overline{\lim_{n \to \infty}} x_n + \underline{\lim}_{n \to \infty} y_n$$
  * **2)** Для $\lambda > 0$: $\quad \overline{\lim_{n \to \infty}} (\lambda \cdot x_n) = \lambda \cdot \overline{\lim_{n \to \infty}} x_n, \quad \underline{\lim}_{n \to \infty} (\lambda \cdot x_n) = \lambda \cdot \underline{\lim}_{n \to \infty} x_n$.
  * **3)** Пусть $x_n, y_n \ge 0 \quad \forall n$. Тогда:
    $$\overline{\lim_{n \to \infty}} (x_n \cdot y_n) \le \overline{\lim_{n \to \infty}} x_n \cdot \overline{\lim_{n \to \infty}} y_n$$
    $$\underline{\lim}_{n \to \infty} (x_n \cdot y_n) \ge \underline{\lim}_{n \to \infty} x_n \cdot \underline{\lim}_{n \to \infty} y_n$$
  * **4)** $\overline{\lim_{n \to \infty}} (-x_n) = -\underline{\lim}_{n \to \infty} x_n$.

**Доказательство:**

- **1)** Пусть $a = \overline{\lim_{n \to \infty}} (x_n + y_n), \; b = \overline{\lim_{n \to \infty}} x_n, \; c = \overline{\lim_{n \to \infty}} y_n, \quad a, b, c \in \mathbb{R}$.
  * Из свойства 1: для произвольного $\varepsilon > 0$
    $$\exists N_1 : \forall n \ge N_1 \quad x_n < b + \frac{\varepsilon}{2} \quad \text{и} \quad \exists N_2 : \forall n \ge N_2 \quad y_n < c + \frac{\varepsilon}{2}.$$
  * Тогда $\forall n \ge N = \max(N_1, N_2) \quad x_n + y_n < b + c + \varepsilon$.
  * По свойству 2, $a = \overline{\lim_{n \to \infty}} (x_n + y_n) \le b + c$.


- **2)** Используем свойства $\sup(\lambda \cdot A) = \lambda \cdot \sup A$ и $\inf(\lambda \cdot A) = \lambda \cdot \inf A, \; \lambda > 0$, где $\lambda \cdot A = \{\lambda x \mid x \in A\}$ *(упражнение)*.
  $$\sup_{k \ge n} (\lambda \cdot x_k) = \lambda \cdot \sup_{k \ge n} x_k$$
  $$\underbrace{\lim_{n \to \infty} \sup_{k \ge n} (\lambda \cdot x_k)}_{\overline{\lim_{n \to \infty}} (\lambda x_n)} = \lim_{n \to \infty} \left(\lambda \cdot \sup_{k \ge n} x_k\right) = \lambda \cdot \lim_{n \to \infty} \sup_{k \ge n} x_k = \lambda \cdot \overline{\lim_{n \to \infty}} x_n.$$


- **4)** Используем свойства $\sup(-A) = -\inf A, \; \inf(-A) = -\sup A$, где $-A = \{-x \mid x \in A\}$ — *упражнение*.
  $$\sup_{k \ge n} (-x_k) = -\inf_{k \ge n} x_k, \quad \underbrace{\lim_{n \to \infty} \sup_{k \ge n} (-x_k)}_{\overline{\lim_{n \to \infty}} (-x_n)} = \underbrace{-\lim_{n \to \infty} \inf_{k \ge n} x_k}_{-\underline{\lim}_{n \to \infty} x_n}.$$


- **3)** Пусть $x_n, y_n \ge 0 \quad \forall n$, и пусть $a = \overline{\lim_{n \to \infty}} (x_n \cdot y_n), \; b = \overline{\lim_{n \to \infty}} x_n, \; c = \overline{\lim_{n \to \infty}} y_n, \quad a, b, c \in \mathbb{R}, \; a, b, c \ge 0$.
  * По свойству 1, $\forall \varepsilon > 0 \quad \exists N : \forall n \ge N \quad x_n < b + \varepsilon$,
  * $\forall n \ge N \quad x_n \cdot y_n \le (b + \varepsilon) \cdot y_n$.
  * По свойствам 4 и 5 (2):
    $$a = \overline{\lim_{n \to \infty}} (x_n \cdot y_n) \le \overline{\lim_{n \to \infty}} (b + \varepsilon) y_n = (b + \varepsilon) \overline{\lim_{n \to \infty}} y_n = (b + \varepsilon) \cdot c.$$
  * Так как $a \le (b + \varepsilon) c \quad \forall \varepsilon > 0$, то $a \le b \cdot c$. $\blacksquare$

#### п. 4. Связь верхнего, нижнего и частичных пределов

- **Теорема.** Верхний и нижний пределы последовательности являются соответственно наибольшим и наименьшим частичными пределами последовательности.

**Доказательство (для верхнего предела; для нижнего — аналогично):**
$$\left( \{x_n, x_{n+1}, x_{n+2}, \dots\}, \quad z_n = \sup \{x_n, x_{n+1}, x_{n+2}, \dots\} \right)$$

- **1)** Если $\{x_n\}$ не ограничена сверху, то $z_n = \sup_{k \ge n} x_k = +\infty \quad \forall n, \quad \overline{\lim_{n \to \infty}} x_n = +\infty$, и при этом существует подпоследовательность $\{x_{n_k}\} : \lim_{k \to \infty} x_{n_k} = +\infty$.


- **2)** Пусть $\{x_n\}$ ограничена сверху. Тогда $z_n = \sup_{k \ge n} x_k, \; \{z_n\} \downarrow, \quad \overline{\lim_{n \to \infty}} x_n = \lim_{n \to \infty} z_n = \inf_n z_n = a \in \mathbb{R}$ или $-\infty$.
  * **2.1)** Пусть $a \in \mathbb{R}$:
    По свойству $\sup$: $\forall \varepsilon > 0 \quad \exists m > n : z_n - \varepsilon < x_m \le z_n$.
    * $n = 1, \; \varepsilon = 1, \quad \exists n_1 > 1 : \quad z_1 - 1 < x_{n_1} \le z_1$
    * $n = 2, \; \varepsilon = \frac{1}{2}, \quad \exists n_2 > 2, \; n_2 > n_1 : \quad z_2 - \frac{1}{2} < x_{n_2} \le z_2$
    * и так далее, $n = k, \; \varepsilon = \frac{1}{k}, \quad \exists n_k > k, \; n_k > n_{k-1} : \quad z_k - \frac{1}{k} < x_{n_k} \le z_k$.
    * Так как $\lim_{k \to \infty} z_k = \lim_{k \to \infty} \left(z_k - \frac{1}{k}\right) = a$, то $\lim_{k \to \infty} x_{n_k} = a = \overline{\lim_{n \to \infty}} x_n$.
    * Так как $\forall n \quad x_n \le \overbrace{z_n}^{\sup_{k \ge n} x_k}$, то для любой подпоследовательности $\{x_{n_k}\} : x_{n_k} \le z_{n_k} \quad \forall k$, следовательно, любой частичный предел
      $$\lim_{k \to \infty} x_{n_k} \le \lim_{k \to \infty} z_{n_k} = \overline{\lim_{n \to \infty}} x_n.$$
      То есть $\overline{\lim_{n \to \infty}} x_n$ — наибольший из частичных пределов.
  * **2.2)** Если $\lim_{n \to \infty} z_n = -\infty$, то из $x_n \le z_n$ следует, что $\lim_{n \to \infty} x_n = -\infty$. $\blacksquare$


- **Следствие.** Последовательность $\{x_n\}$ имеет конечный или бесконечный предел $\iff \overline{\lim_{n \to \infty}} x_n = \underline{\lim}_{n \to \infty} x_n$.

**Доказательство:**
$$\text{Если существует } \lim_{n \to \infty} x_n \in \overline{\mathbb{R}} \iff \text{все частичные пределы совпадают} \iff \underbrace{\overline{\lim_{n \to \infty}} x_n}_{\substack{\text{наибольший из} \\ \text{частичных}}} = \underbrace{\underline{\lim}_{n \to \infty} x_n}_{\substack{\text{наименьший из} \\ \text{частичных}}}.$$

### §7. Степень с действительным показателем

- **Теорема (об арифметическом корне).** Для любых $a \ge 0$ и $n \in \mathbb{N}$ существует единственный $x \ge 0 : x^n = a$. (Будем обозначать $x = \sqrt[n]{a}$.)

**Доказательство:** следует из того, что функция $y = x^n$ строго монотонно возрастает на $[0; +\infty)$ и теоремы об обратной функции (в следующей главе). $\blacksquare$


- **Теорема (функциональное задание степени).** Для любого $a > 0$ существует единственная функция $f_a : \mathbb{R} \to \mathbb{R}$, удовлетворяющая свойствам:
  * **1)** $f_a(x + y) = f_a(x) \cdot f_a(y)$;
  * **2)** $f_a(x)$ монотонна;
  * **3)** $f_a(1) = a$.
  * Эту функцию будем обозначать через $f_a(x) = a^x$, так как для $x \in \mathbb{Q}$ она будет совпадать с функцией $a^x$ в общеизвестном смысле.


- **Определение.** $f(x)$ монотонно возрастает (убывает) на $\langle a, b \rangle$, если $\forall x_1, x_2 \in \langle a, b \rangle$ из $x_1 < x_2 \implies f(x_1) \le f(x_2)$ ($f(x_1) \ge f(x_2)$).
  * Строго монотонно возрастает (строго монотонно убывает): $f(x_1) < f(x_2)$ ($f(x_1) > f(x_2)$).

**Доказательство:**

*(Примечание: далее в доказательстве свойства перенумерованы: 1) $f_a(x)$ монотонна; 2) $f_a(x+y) = f_a(x) \cdot f_a(y)$; 3) $f_a(1) = a$.)*

- **1)** $a = f_a(1) = f_a(1 + 0) = \overbrace{f_a(1)}^{a} \cdot f_a(0) = a \cdot f_a(0), \quad f_a(0) = 1$.
  * Для $x > 0$: $1 = f_a(0) = f_a(x + (-x)) = f_a(x) \cdot f_a(-x)$, то есть $f_a(-x) = \frac{1}{f_a(x)}, \quad \forall x$.
  * $f_a(n) = f_a(1 + 1 + \dots + 1) = f_a(1) \cdot f_a(1) \cdot \dots \cdot f_a(1) = a^n, \quad n \in \mathbb{N}$.
  * $f_a(-n) = \frac{1}{f_a(n)} = \frac{1}{a^n}, \quad n \in \mathbb{N}$.
  * Для $x = \frac{1}{n}, \; n \in \mathbb{N}$:
    $$a = f_a(1) = f_a\left(\overbrace{\frac{1}{n} + \frac{1}{n} + \dots + \frac{1}{n}}^{n \text{ раз}}\right) = \overbrace{f_a\left(\frac{1}{n}\right) \cdot \dots \cdot f_a\left(\frac{1}{n}\right)}^{n \text{ раз}} = \left(f_a\left(\frac{1}{n}\right)\right)^n, \quad f_a\left(\frac{1}{n}\right) = \sqrt[n]{a}.$$
  * Для $x = \frac{m}{n}, \; m, n \in \mathbb{N}$:
    $$f_a\left(\frac{m}{n}\right) = f_a\left(\overbrace{\frac{1}{n} + \dots + \frac{1}{n}}^{m \text{ раз}}\right) = \overbrace{f_a\left(\frac{1}{n}\right) \cdot \dots \cdot f_a\left(\frac{1}{n}\right)}^{m \text{ раз}} = \left(\sqrt[n]{a}\right)^m = \sqrt[n]{a^m}.$$
  * $x = -\frac{m}{n}, \; m, n \in \mathbb{N}$:
    $$f_a\left(-\frac{m}{n}\right) = \frac{1}{f_a\left(\frac{m}{n}\right)} = \frac{1}{\sqrt[n]{a^m}} = \sqrt[n]{a^{-m}}.$$
  * (Для $x \in \mathbb{Q} \quad f_a(x) = a^x$.)


- Если $a = 1$, то $f_a(n) = 1 \quad \forall n \in \mathbb{Z}$. Так как $f_a(x)$ должна быть монотонной, то $f_a(x) \equiv 1$.
- Если $a > 1$, то $f_a(x)$ возрастает для всех $x \in \mathbb{Q}$ (это следует из свойств степеней и корней).
- Если $0 < a < 1$, то $f_a(x)$ убывает для всех $x \in \mathbb{Q}$.


- Определим функцию $f_a(x)$ для $x \notin \mathbb{Q}$ так, чтобы сохранились свойства (1) и (2). Пусть $a > 1$ *(для $0 < a < 1$ — аналогично)*.
  * Пусть $r \notin \mathbb{Q}$, обозначим $A = \{f_a(q) \mid q \in \mathbb{Q}, \; q < r\}, \quad B = \{f_a(q) \mid q \in \mathbb{Q}, \; q > r\}$.
  * Тогда $\sup A \le \inf B$. Для выполнения свойства (1) должно быть $\sup A \le f_a(r) \le \inf B$. Покажем, что $\sup A = \inf B$.
  * Зафиксируем $n \in \mathbb{N}$. Тогда существует единственное $m \in \mathbb{Z} : \frac{m}{n} < r < \frac{m+1}{n}$. Следовательно,
    $$\underset{\in A}{\sqrt[n]{a^m}} \le \sup A \le \inf B \le \underset{\in B}{\sqrt[n]{a^{m+1}}} = \sqrt[n]{a^m} \cdot \sqrt[n]{a} \le \sup A \cdot \sqrt[n]{a}$$
    $$\sup A \le \inf B \le \sup A \cdot \underbrace{\sqrt[n]{a}}_{\to 1} \implies \text{из теоремы о зажатой последовательности: } \inf B = \sup A.$$
  * Полагаем $f_a(r) = \sup A = \inf B$, свойство (1) выполняется:
    Пусть $x < y$, тогда $\exists p \in \mathbb{Q} : x \le p < y, \quad f_a(x) \le f_a(p) \le f_a(y)$.


- Докажем свойство (2). Пусть $a > 1$. Пусть $x, y \in \mathbb{R}$. Зафиксируем $n \in \mathbb{N}$, тогда существуют $k, m \in \mathbb{Z}$:
  $$\frac{k}{n} \le x < \frac{k+1}{n}, \quad \frac{m}{n} \le y < \frac{m+1}{n}, \quad \text{тогда } \frac{k+m}{n} \le x + y < \frac{k+m+2}{n}.$$
  * Так как $f_a(x)$ монотонно возрастает, то
    $$f_a(x) \cdot f_a(y) \le \sqrt[n]{a^{k+1}} \cdot \sqrt[n]{a^{m+1}} = \sqrt[n]{a^{k+m}} \cdot \sqrt[n]{a^2} \le f_a(x+y) \cdot \underbrace{\sqrt[n]{a^2}}_{\to 1}.$$
  * При $n \to \infty$ получаем $f_a(x) \cdot f_a(y) \le f_a(x+y)$.
  * С другой стороны,
    $$f_a(x+y) \le \sqrt[n]{a^{k+m+2}} = \sqrt[n]{a^k} \cdot \sqrt[n]{a^m} \cdot \sqrt[n]{a^2} \le f_a(x) \cdot f_a(y) \cdot \underbrace{\sqrt[n]{a^2}}_{\to 1}.$$
  * Переходим к пределу при $n \to \infty$: $f_a(x+y) \le f_a(x) \cdot f_a(y)$, то есть $f_a(x+y) = f_a(x) \cdot f_a(y)$. $\blacksquare$


- **Замечание.** Если $a \ne 1$, то $f_a(x)$ строго монотонна: $\nearrow$ при $a > 1$, $\searrow$ при $0 < a < 1$.
  * Предположим, что $f_a(x+h) = f_a(x)$ для некоторого $h > 0$. Тогда $f_a(x) \cdot f_a(h) = f_a(x), \; f_a(h) = 1$, следовательно, $f_a(nh) = 1 \quad \forall n \in \mathbb{Z}$, и $f_a(x) \equiv 1$.


- **Следствие.** $\left(a^x\right)^y = a^{x \cdot y} \quad \forall x, y \in \mathbb{R}, \; a > 0$.

**Доказательство:**

- Для $a = 1$ — очевидно. Зафиксируем $a \ne 1, \; x \in \mathbb{R}$ и рассмотрим функцию $f(y) = a^{x \cdot y}$. Если $x = 0$, то $f(y) \equiv 1$, и утверждение верно.
- Пусть $x \ne 0$.
  * **1)** $f(y)$ монотонна:
    * Если $a > 1, \; x > 0$, то из $y_1 < y_2 \implies x \cdot y_1 < x \cdot y_2 \implies a^{x \cdot y_1} < a^{x \cdot y_2}, \quad f(y_1) < f(y_2)$.
    * $a > 1, \; x < 0$: $y_1 < y_2 \implies x \cdot y_1 > x \cdot y_2 \implies a^{x y_1} > a^{x y_2}, \quad f(y_1) > f(y_2)$.
    * $\left. \begin{array}{l} 0 < a < 1, \; x > 0 \\ 0 < a < 1, \; x < 0 \end{array} \right\}$ аналогично.
  * **2)** $f(y_1 + y_2) = a^{x \cdot (y_1 + y_2)} = a^{x y_1 + x y_2} = a^{x y_1} \cdot a^{x y_2} = f(y_1) \cdot f(y_2)$.
  * **3)** $f(1) = a^x$.
  * По теореме, $f(y) = f_{a^x}(y) = \left(a^x\right)^y$, то есть $a^{x \cdot y} = \left(a^x\right)^y$. $\blacksquare$


- **Теорема (о логарифме).** Для любых $a > 0, \; a \ne 1$, и $b > 0$ существует единственный $x \in \mathbb{R} : a^x = b$.
  * Это число $x$ называется **логарифмом числа $b$ по основанию $a$**, обозначается $x = \log_a b$.

**Доказательство:** следует из строгой монотонности функции $y = a^x$ и теоремы об обратной функции. $\blacksquare$

#### п. 2. Экспоненциальная функция

$$\left( e = \lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n \right)$$

- Рассмотрим последовательность $u_n(x) = \left(1 + \frac{x}{n}\right)^n, \; x \in \mathbb{R}$. Докажем, что $\forall x \in \mathbb{R}$ существует $\lim_{n \to \infty} \left(1 + \frac{x}{n}\right)^n \in \mathbb{R}$.
- При $x = 0$ — очевидно: $\lim_{n \to \infty} u_n(0) = 1$.
  $$u_n(x) = \sum_{k=0}^n \frac{n!}{k!(n-k)!} \cdot \frac{x^k}{n^k} = \sum_{k=0}^n c_{n,k} \cdot \frac{x^k}{k!}, \quad \text{где } c_{n,k} = \frac{n!}{(n-k)! n^k} = \begin{cases} 1, & k = 0 \text{ или } 1 \\ \left(1 - \frac{1}{n}\right)\left(1 - \frac{2}{n}\right)\dots\left(1 - \frac{k-1}{n}\right), & 1 < k \le n \end{cases}$$
  $$0 < c_{n,k} < 1, \; k > 1; \qquad \lim_{n \to \infty} c_{n,k} = 1.$$


- Используем критерий Коши:
  $$|u_m(x) - u_n(x)| = \left| \sum_{k=0}^m c_{m,k} \cdot \frac{x^k}{k!} - \sum_{k=0}^n c_{n,k} \cdot \frac{x^k}{k!} \right| \le \left\{ \begin{array}{c} k_0 \text{ выберем} \\ \text{позже} \end{array} \right\} \le$$
  $$\le \left| \sum_{k=1}^{k_0 - 1} (c_{m,k} - c_{n,k}) \cdot \frac{x^k}{k!} \right| + \left| \sum_{k=k_0}^m c_{m,k} \cdot \frac{x^k}{k!} \right| + \left| \sum_{k=k_0}^n c_{n,k} \cdot \frac{x^k}{k!} \right| \le$$
  $$\le \sum_{k=1}^{k_0 - 1} |c_{m,k} - c_{n,k}| \cdot \frac{|x|^k}{k!} + \sum_{k=k_0}^m \underbrace{|c_{m,k}|}_{< 1} \cdot \frac{|x|^k}{k!} + \sum_{k=k_0}^n \underbrace{|c_{n,k}|}_{< 1} \cdot \frac{|x|^k}{k!} \le$$
  $$\le \underbrace{\sum_{k=1}^{k_0 - 1} |c_{m,k} - c_{n,k}| \cdot \frac{|x|^k}{k!}}_{\substack{\text{в этой сумме} \\ \text{конечное число} \\ \text{слагаемых}}} + 2 \cdot \sum_{k=k_0}^{\max(m, n)} \frac{|x|^k}{k!}.$$


- Пусть $\varepsilon > 0$ — произвольное. Выберем $k_0$ так, чтобы $\frac{|x|^{k_0}}{k_0!} < \frac{\varepsilon}{8}$ и $\frac{|x|}{k_0 + 1} < \frac{\varepsilon}{8} < \frac{1}{2}$.
- Тогда (обозначив $L = \max(m, n)$):
  $$2 \sum_{k=k_0}^L \frac{|x|^k}{k!} = 2 \cdot \left( \frac{|x|^{k_0}}{k_0!} + \frac{|x|^{k_0 + 1}}{k_0!(k_0 + 1)} + \dots + \frac{|x|^L}{k_0! \underbrace{(k_0 + 1)\dots L}_{> (k_0 + 1)^{L - k_0}}} \right) < 2 \frac{|x|^{k_0}}{k_0!} \left( 1 + \frac{|x|}{k_0 + 1} + \frac{|x|^2}{(k_0 + 1)^2} + \dots + \frac{|x|^{L - k_0}}{(k_0 + 1)^{L - k_0}} \right) =$$
  *(геометрическая прогрессия, $q = \frac{|x|}{k_0 + 1} < 1$)*
  $$= 2 \cdot \frac{|x|^{k_0}}{k_0!} \cdot \frac{1 - \left(\frac{|x|}{k_0 + 1}\right)^{L + 1 - k_0}}{1 - \frac{|x|}{k_0 + 1}} < 2 \cdot \frac{|x|^{k_0}}{k_0!} \cdot \frac{1}{1 - \frac{|x|}{k_0 + 1}} < 2 \cdot \frac{\varepsilon}{8} \cdot \frac{1}{1 - \frac{1}{2}} = \frac{\varepsilon}{2}.$$


- Оценим первое слагаемое. Так как $c_{m,k} \to 1$ при $m \to \infty$, то $\exists N : \forall m, n \ge N$
  $$|c_{m,k} - c_{n,k}| = |(c_{m,k} - 1) + (1 - c_{n,k})| \le |c_{m,k} - 1| + |1 - c_{n,k}| < \frac{\varepsilon}{2 k_0 (|x| + 1)^{k_0}}.$$
- Тогда
  $$\sum_{k=1}^{k_0 - 1} |c_{m,k} - c_{n,k}| \cdot \frac{|x|^k}{k!} \le \sum_{k=1}^{k_0 - 1} \frac{\varepsilon}{2 k_0} \underbrace{\frac{|x|^k}{(|x| + 1)^{k_0}}}_{\le 1} \cdot \underbrace{\frac{1}{k!}}_{\le 1} \le \frac{\varepsilon}{2 k_0} \cdot \sum_{k=1}^{k_0 - 1} 1 < \frac{\varepsilon}{2}.$$
- То есть $\exists N : \forall n, m \ge N \quad |u_m(x) - u_n(x)| < \varepsilon$, то есть $\{u_n(x)\}$ — фундаментальна, и по критерию Коши она сходится. $\blacksquare$


- **Обозначение:** $\lim_{n \to \infty} \left(1 + \frac{x}{n}\right)^n = \exp x$ *(экспоненциальная функция)*.


- **Свойство:** $\exp x = \lim_{n \to \infty} \sum_{k=0}^n \frac{x^k}{k!}$.

**Доказательство:**
$$\left| \sum_{k=0}^n \frac{x^k}{k!} - u_n(x) \right| = \left| \sum_{k=0}^n \frac{x^k}{k!} - \sum_{k=0}^n \frac{c_{n,k} \cdot x^k}{k!} \right| = \left| \sum_{k=1}^n (1 - c_{n,k}) \cdot \frac{x^k}{k!} \right| \le \left\{ \begin{array}{c} k_0 \text{ выберем} \\ \text{позже} \end{array} \right\} \le$$
$$\le \sum_{k=1}^{k_0 - 1} |1 - c_{n,k}| \cdot \frac{|x|^k}{k!} + \sum_{k=k_0}^n \underbrace{|1 - c_{n,k}|}_{< 1} \cdot \frac{|x|^k}{k!} \le (?)$$

- $\text{Второе слагаемое} \le \sum_{k=k_0}^n \frac{|x|^k}{k!} = \frac{|x|^{k_0}}{k_0!} + \frac{|x|^{k_0 + 1}}{k_0!(k_0 + 1)} + \frac{|x|^{k_0 + 2}}{k_0!(k_0 + 1)(k_0 + 2)} + \dots + \frac{|x|^n}{k_0!(k_0 + 1)\dots n} \le$
  $$\le \frac{|x|^{k_0}}{k_0!} \left( 1 + \frac{|x|}{k_0 + 1} + \frac{|x|^2}{(k_0 + 1)^2} + \dots + \frac{|x|^{n - k_0}}{(k_0 + 1)^{n - k_0}} \right) = \frac{|x|^{k_0}}{k_0!} \cdot \frac{1 - \left(\frac{|x|}{k_0 + 1}\right)^{n + 1 - k_0}}{1 - \frac{|x|}{k_0 + 1}} < \frac{|x|^{k_0}}{k_0!} \cdot \frac{1}{1 - \frac{|x|}{k_0 + 1}} = (*)$$
  $$\left( q = \frac{|x|}{k_0 + 1} < 1 \right)$$
- Пусть $\varepsilon > 0$ — произвольное. Выберем $k_0$ так, чтобы $\frac{|x|^{k_0}}{k_0!} < \frac{\varepsilon}{4}$ и $\frac{|x|}{k_0 + 1} < \frac{1}{2} < 1$. Тогда
  $$(*) < \frac{\varepsilon}{4} \cdot \frac{1}{1 - \frac{1}{2}} = \frac{\varepsilon}{2}.$$


- Оценим 1-е слагаемое. Так как $\lim_{n \to \infty} c_{n,k} = 1$, то $\exists N : \forall n \ge N \quad |1 - c_{n,k}| < \frac{\varepsilon}{2 k_0 (|x| + 1)^{k_0}}$.
- Тогда
  $$\sum_{k=1}^{k_0 - 1} |1 - c_{n,k}| \cdot \frac{|x|^k}{k!} \le \sum_{k=1}^{k_0 - 1} \frac{\varepsilon}{2 k_0} \underbrace{\frac{|x|^k}{(|x| + 1)^{k_0}}}_{< 1} \cdot \underbrace{\frac{1}{k!}}_{\le 1} \le \frac{\varepsilon}{2 k_0} \cdot k_0 = \frac{\varepsilon}{2}.$$
- Следовательно, $\forall n \ge N \quad \left| \sum_{k=0}^n \frac{x^k}{k!} - u_n(x) \right| < \varepsilon$, то есть $\lim_{n \to \infty} \sum_{k=0}^n \frac{x^k}{k!} = \lim_{n \to \infty} u_n(x) = \exp x$. $\blacksquare$

- **Следствие.** $\left| \exp x - \sum_{k=0}^n \frac{x^k}{k!} \right| \le \frac{2}{(n+1)!} |x|^{n+1}$, если $\frac{|x|}{n+1} \le \frac{1}{2}$
  *(Упражнение: можно посмотреть у С.К. Водопьянова. Указание: оценить через геометрическую прогрессию).*


- **Теорема.** $\exp(u+v) = \exp u \cdot \exp v, \quad u,v \in \mathbb{R}$


- **Лемма.** Если $\lim_{n \to \infty} x_n = a \in \mathbb{R}$, то $\lim_{n \to \infty} \left(1+\frac{x_n}{n}\right)^n = \exp a$.

**Доказательство леммы:**

- **1)** Рассмотрим сначала случай, когда $\lim_{n \to \infty} x_n = 0$, докажем, что $\lim_{n \to \infty} \left(1+\frac{x_n}{n}\right)^n = \exp 0 = 1$.

  $\left(1+\frac{x_n}{n}\right)^n \ge 1+x_n$ по неравенству Бернулли (так как $x_n \to 0$, то существует $N_0$ такое, что для любого $n > N_0$ выполняется $\frac{x_n}{n} > -1$).

  С другой стороны:
  $$\left(1+\frac{x_n}{n}\right)^n = \frac{\left(1-\frac{x_n^2}{n^2}\right)^n}{\left(1-\frac{x_n}{n}\right)^n} \le \frac{1}{\left(1-\frac{x_n}{n}\right)^n} \le \frac{1}{1-x_n}$$
  (где $\left(1-\frac{x_n}{n}\right)^n \ge 1-x_n$, так как существует $N_1$ такое, что для любого $n > N_1$ выполняется $-\frac{x_n}{n} > -1$).

  Тогда для любого $n > \max(N_0, N_1)$ выполняется $1+x_n \le \left(1+\frac{x_n}{n}\right)^n \le \frac{1}{1-x_n}$. Следовательно, при $x_n \to 0$, $\lim_{n \to \infty} \left(1+\frac{x_n}{n}\right)^n = 1$.


- **2)** Пусть $\lim_{n \to \infty} x_n = a$, то есть $x_n = a + y_n$, где $\lim_{n \to \infty} y_n = 0$. Тогда:
  $$\left(1+\frac{x_n}{n}\right)^n = \left(1+\frac{a+y_n}{n}\right)^n = \left(1+\frac{a}{n}\right)^n \cdot \frac{\left(1+\frac{a+y_n}{n}\right)^n}{\left(1+\frac{a}{n}\right)^n} = \left(1+\frac{a}{n}\right)^n \cdot \left(\frac{n+a+y_n}{n+a}\right)^n =$$
  $$= \left(1+\frac{a}{n}\right)^n \cdot \left(1+\frac{y_n}{n+a}\right)^n = \left(1+\frac{a}{n}\right)^n \cdot \left(1+\frac{\frac{y_n}{1+\frac{a}{n}}}{n}\right)^n \to \exp a \text{ при } n \to \infty$$
  (по доказанному выше, так как $\frac{y_n}{1+\frac{a}{n}} \to 0$). $\blacksquare$

**Доказательство теоремы:**
  $$\exp u \cdot \exp v = \lim_{n \to \infty} \left(1+\frac{u}{n}\right)^n \cdot \lim_{n \to \infty} \left(1+\frac{v}{n}\right)^n = \lim_{n \to \infty} \left(\left(1+\frac{u}{n}\right)\left(1+\frac{v}{n}\right)\right)^n =$$
  $$= \lim_{n \to \infty} \left(1+\frac{u}{n}+\frac{v}{n}+\frac{uv}{n^2}\right)^n = \lim_{n \to \infty} \left(1+\frac{u+v+\frac{uv}{n}}{n}\right)^n = \exp(u+v) \text{ по лемме. } \blacksquare$$


- **Следствие.** $\exp x = e^x$

**Доказательство:**
- **1)** $\exp(x+y) = \exp x \cdot \exp y$ (по теореме выше).
- **2)** $\exp x$ строго возрастает. Если $x < y$, то $\left(1+\frac{x}{n}\right)^n < \left(1+\frac{y}{n}\right)^n$ для любого $n > N$, где $N$ выбрано так, чтобы $0 < 1+\frac{x}{N} < 1+\frac{y}{N}$.
  В пределе при $n \to \infty$: $\lim_{n \to \infty} \left(1+\frac{x}{n}\right)^n \le \lim_{n \to \infty} \left(1+\frac{y}{n}\right)^n$, следовательно $\exp x \le \exp y$.
- **3)** $\exp 1 = \lim_{n \to \infty} \left(1+\frac{1}{n}\right)^n = e$.
- По теореме о функциональном задании степени, $\exp x = e^x$. $\blacksquare$

---

### п.3. Последовательности комплексных чисел. Комплексная экспонента

- Пусть $\{z_n\}$ — последовательность чисел $z_n \in \mathbb{C}$.


- $\lim_{n \to \infty} z_n = z_0 \in \mathbb{C}$, если для любого $\varepsilon > 0$ существует $N$ такое, что для любого $n \ge N$ выполняется $|z_n - z_0| = \sqrt{(x_n - x_0)^2 + (y_n - y_0)^2} < \varepsilon$.
  Здесь $z_n = x_n + iy_n, \quad z_0 = x_0 + iy_0$.


- **Свойство.** $\lim_{n \to \infty} z_n = z_0 \iff \begin{cases} \lim_{n \to \infty} x_n = x_0 \\ \lim_{n \to \infty} y_n = y_0 \end{cases}$ *(Упражнение)*.


- **Свойства сходящихся последовательностей:**
  **1)** Предел сходящейся последовательности — единственный.
  **2)** Если $\lim_{n \to \infty} z_n = z_0$, то существует $M > 0$ такое, что для любого $n$ выполняется $|z_n| \le M$.
  **3)** Если $\lim_{n \to \infty} z_n = z_0$ и $\lim_{n \to \infty} w_n = w_0$, то:
     * $\lim_{n \to \infty} (z_n \pm w_n) = z_0 \pm w_0$,
     * $\lim_{n \to \infty} (z_n \cdot w_n) = z_0 \cdot w_0$;
     * Если $w_0 \neq 0$, то $\lim_{n \to \infty} \frac{z_n}{w_n} = \frac{z_0}{w_0}$. *(Доказательство аналогично действительному случаю. $\blacksquare$)*


- **Теорема (полярный признак сходимости).** Если $z_n = r_n(\cos\varphi_n + i\sin\varphi_n)$, где $\lim_{n \to \infty} r_n = r_0$ и $\lim_{n \to \infty} \varphi_n = \varphi_0$, то $\lim_{n \to \infty} z_n = r_0(\cos\varphi_0 + i\sin\varphi_0)$.

**Доказательство:**
Так как $\varphi_n \to \varphi_0$ при $n \to \infty$, то $\cos\varphi_n \to \cos\varphi_0$ и $\sin\varphi_n \to \sin\varphi_0$ (из свойства непрерывности функций $\cos x$ и $\sin x$ — позже!).
Следовательно, $z_n = r_n\cos\varphi_n + i r_n\sin\varphi_n \to r_0\cos\varphi_0 + i r_0\sin\varphi_0$. $\blacksquare$

---

**Комплексная экспонента**
$$\exp z = \lim_{n \to \infty} \left(1+\frac{z}{n}\right)^n$$

- **Лемма.** $\lim_{n \to \infty} \left(1+\frac{iy}{n}\right)^n = \cos y + i\sin y, \quad y \in \mathbb{R}$.

**Доказательство:**
- $\left|1+\frac{iy}{n}\right| = \sqrt{1+\frac{y^2}{n^2}}$, следовательно $\left|\left(1+\frac{iy}{n}\right)^n\right| = \sqrt{\left(1+\frac{y^2}{n^2}\right)^n} = \sqrt{\left(1+\left(\frac{y}{n}\right)^2\right)^n} \to 1$ по лемме, так как $\lim_{n \to \infty} \frac{y^2}{n^2} = 0$.


- $\varphi_n = \arg\left(\left(1+\frac{iy}{n}\right)^n\right) = n \cdot \arg\left(1+\frac{iy}{n}\right) = n \cdot \text{arctg}\frac{y/n}{1} = n \cdot \text{arctg}\frac{y}{n}$.


- Известно, что $\sin x < x < \text{tg} x$ при $0 < x < \frac{\pi}{2}$ и $\sin \alpha = \text{tg} \alpha \cdot \cos \alpha = \frac{\text{tg} \alpha}{\sqrt{1+\text{tg}^2 \alpha}}$.


- Если $y \ge 0$, то $\sin\left(\text{arctg}\frac{y}{n}\right) \le \text{arctg}\frac{y}{n} \le \text{tg}\left(\text{arctg}\frac{y}{n}\right)$.
  $$\frac{\text{tg}\left(\text{arctg}\frac{y}{n}\right)}{\sqrt{1+\text{tg}^2\left(\text{arctg}\frac{y}{n}\right)}} \le \text{arctg}\frac{y}{n} \le \text{tg}\left(\text{arctg}\frac{y}{n}\right)$$
  $$\frac{\frac{y}{n}}{\sqrt{1+\left(\frac{y}{n}\right)^2}} \le \text{arctg}\frac{y}{n} \le \frac{y}{n}$$
  $$\frac{y}{\sqrt{1+\left(\frac{y}{n}\right)^2}} \le n \cdot \text{arctg}\frac{y}{n} \le y$$


- Для $y < 0$ в силу нечетности функции знаки меняются на противоположные: $\frac{y}{\sqrt{1+\left(\frac{y}{n}\right)^2}} \ge n \cdot \text{arctg}\frac{y}{n} \ge y$.


- По теореме о зажатой последовательности: $\lim_{n \to \infty} n \cdot \text{arctg}\frac{y}{n} = y$.


- По полярному признаку сходимости, $\left(1+\frac{iy}{n}\right)^n \to 1 \cdot (\cos y + i\sin y)$ при $n \to \infty$. $\blacksquare$

---

- **Теорема.** Если $\lim_{n \to \infty} z_n = z_0 = x+iy$, то $\lim_{n \to \infty} \left(1+\frac{z_n}{n}\right)^n = e^x(\cos y + i\sin y)$.


- **Следствие.** Если $z = x+iy$, то $\lim_{n \to \infty} \left(1+\frac{z}{n}\right)^n = e^x(\cos y + i\sin y) = \exp z = e^z$.

**Доказательство:**
- **1)** Пусть $z_n \to 0$. Тогда:
  $$\left(1-\frac{|z_n|}{n}\right)^n \le \left|\left(1+\frac{z_n}{n}\right)^n\right| \le \left(1+\frac{|z_n|}{n}\right)^n$$
  для любого $n > N$ (чтобы $1-\frac{|z_n|}{n} > 0$ для любого $n \ge N$). Следовательно, $\left|\left(1+\frac{z_n}{n}\right)^n\right| \to 1$ (по лемме).

  Пусть $z_n = x_n + iy_n \to 0$, тогда $1+\frac{z_n}{n} = \left(1+\frac{x_n}{n}\right) + i\frac{y_n}{n}$, где существует $N$ такое, что для любого $n \ge N$ выполняется $1+\frac{x_n}{n} > 0$.

  Тогда $\arg\left(\left(1+\frac{z_n}{n}\right)^n\right) = n \cdot \arg\left(1+\frac{z_n}{n}\right) = n \cdot \text{arctg} \frac{\frac{y_n}{n}}{1+\frac{x_n}{n}} = n \cdot \text{arctg} \frac{y_n}{n+x_n}$.

  Так как $|\text{arctg} x| \le |x|$, то $\left|n \cdot \text{arctg} \frac{y_n}{n+x_n}\right| \le n \cdot \left|\frac{y_n}{n+x_n}\right| = \frac{n}{n} \frac{|y_n|}{\left|1+\frac{x_n}{n}\right|} \to 0$ при $n \to \infty$.

  По полярному признаку, $\left(1+\frac{z_n}{n}\right)^n \to 1 \cdot (\cos 0 + i\sin 0) = 1$ при $n \to \infty$.


- **2)** Пусть $z_n \to z \in \mathbb{C}$, тогда $z_n = z + \alpha_n = x + iy + \alpha_n$, где $\alpha_n \to 0$.

  Рассмотрим:
  $$\left(1+\frac{z_n}{n}\right)^n = \left(1+\frac{x+iy+\alpha_n}{n}\right)^n = \left(1+\frac{x}{n}\right)^n \cdot \left(1+\frac{iy}{n}\right)^n \cdot \frac{\left(1+\frac{x+iy+\alpha_n}{n}\right)^n}{\left(1+\frac{x}{n}\right)^n\left(1+\frac{iy}{n}\right)^n}$$

  Здесь $\left(1+\frac{x}{n}\right)^n \to e^x$, $\left(1+\frac{iy}{n}\right)^n \to \cos y + i\sin y$.

  Дробь преобразуется:
  $$\left( \frac{n+x+iy+\alpha_n}{n+x+iy+\frac{ixy}{n}} \right)^n = \left( 1 + \frac{\alpha_n - \frac{ixy}{n}}{n+x+iy+\frac{ixy}{n}} \right)^n = \left( 1 + \frac{\frac{\alpha_n - \frac{ixy}{n}}{n}}{1+\frac{x+iy}{n}+\frac{ixy}{n^2}} \right)^n \to 1 \text{ при } n \to \infty$$
  (по выше доказанному). $\blacksquare$

---

- **Замечание.** $\exp z = e^z = e^{x+iy} = e^x(\cos y + i\sin y)$
- **Замечание.** $\exp(z_1+z_2) = \exp z_1 \cdot \exp z_2$
- **Формула Эйлера:** $e^{\pi i} + 1 = 0$

---

## §8. Основные принципы анализа и топология во множестве действительных чисел

### п.1. Основные леммы

Лемма о вложенных отрезках (в §4).

- **Теорема (о пересекающихся отрезках):** Пересечение любой совокупности пересекающихся отрезков является отрезком (следовательно, непустое) *(Упражнение)*.


- **Лемма о конечном покрытии (принцип Бореля — Лебега):** Из любой системы интервалов, покрывающих замкнутый отрезок, то есть $[a,b] \subset \bigcup_{\alpha \in I} (a_\alpha, b_\alpha)$, можно выбрать подсистему, покрывающую этот отрезок, то есть существует конечное множество $\alpha_1, \alpha_2, \dots, \alpha_n$:
  $$[a,b] \subset \bigcup_{k=1}^n (a_{\alpha_k}, b_{\alpha_k})$$

**Доказательство:**

- Пусть $S = \{U\}$ — система интервалов, покрывающих отрезок $[a,b]$.


- Предположим, что из $\{U\}$ нельзя выбрать конечную подсистему, покрывающую $[a,b]$.


- Разделим $[a,b]$ пополам, обозначим через $[a_1, b_1]$ ту из половин $[a, \frac{a+b}{2}], [\frac{a+b}{2}, b]$, которую нельзя покрыть конечным числом интервалов из $\{U\}$. Далее, делим $[a_1, b_1]$ пополам, обозначим через $[a_2, b_2]$ ту из половин, для которой нельзя выбрать конечную подсистему, покрывающую отрезок, и так далее.


- Получим последовательность вложенных отрезков: $[a_1, b_1] \supset [a_2, b_2] \supset \dots \supset [a_n, b_n] \supset \dots$, никакая из них не допускает покрытия конечным набором интервалов из $\{U\}$.


- Длина отрезка $[a_n, b_n]$ равна $\frac{b-a}{2^n} \to 0$ при $n \to \infty$. По лемме о вложенных отрезках, существует $c \in [a_n, b_n]$ для любого $n$.


- Так как $c \in [a,b]$, то существует интервал $(\alpha, \beta) \in S$ такой, что $c \in (\alpha, \beta)$.


- Пусть $\varepsilon = \min(c-\alpha, \beta-c)$. Так как $\lim_{n \to \infty} b_n = c$ и $\lim_{n \to \infty} a_n = c$, то существует $N$ такое, что для любого $n > N$ выполняется $|b_n - c| < \varepsilon$ и $|c - a_n| < \varepsilon$.


- Следовательно, $\alpha \le c - \varepsilon < a_n \le b_n < c + \varepsilon \le \beta$, то есть для любого $n > N$ отрезок $[a_n, b_n] \subset (\alpha, \beta)$.


- Отрезок $[a_n, b_n]$ покрыт одним интервалом $(\alpha, \beta)$ — противоречие. $\blacksquare$

### п. 2. Окрестность точки

- **Окрестность точки** $a \in \mathbb{R}$: любой интервал $(\alpha, \beta) \ni a$, где $\alpha, \beta \in \mathbb{R}$.


- **Элементарная окрестность** ($\varepsilon$-окрестность) точки $a \in \mathbb{R}$: симметричный интервал $(a-\varepsilon; a+\varepsilon) = U_\varepsilon(a)$.


- **Проколотая $\varepsilon$-окрестность** точки $a$: $\mathring{U}_\varepsilon(a) = (a-\varepsilon; a+\varepsilon) \setminus \{a\}$.


  * $\varepsilon$-окрестность точки $+\infty$: $\left(\frac{1}{\varepsilon}; +\infty\right]$
  * $\varepsilon$-окрестность точки $-\infty$: $\left[-\infty; -\frac{1}{\varepsilon}\right)$
  * Проколотая $\varepsilon$-окрестность точки $+\infty$: $\mathring{U}_\varepsilon(+\infty) = \left(\frac{1}{\varepsilon}; +\infty\right)$
  * Проколотая $\varepsilon$-окрестность точки $-\infty$: $\mathring{U}_\varepsilon(-\infty) = \left(-\infty; -\frac{1}{\varepsilon}\right)$

**Свойства:**

- **1)** Если $a \neq b$, то $\exists \varepsilon > 0$: $\varepsilon$-окрестности точек $a$ и $b$ не пересекаются.
  Если $a, b \in \mathbb{R}$, то выберем $\varepsilon < \frac{|b-a|}{2}$.
  Если $a \in \mathbb{R}, b = +\infty$, то выберем $\begin{cases} a+\varepsilon < 2|a| \\ \frac{1}{\varepsilon} > 2|a| \end{cases}$, откуда $\varepsilon < \min\left(|a|, \frac{1}{2|a|}\right)$. 
  Остальные случаи — аналогично.


- **2)** $\lim_{n \to \infty} x_n = a \iff \forall \varepsilon > 0 \quad \exists N: \forall n > N \quad x_n \in U_\varepsilon(a)$. 
  (топологическое определение предела, как для $a \in \mathbb{R}$, так и для $a = \pm\infty$)


- **3)** Пересечение двух окрестностей (элементарных окрестностей) точки $a$ является окрестностью (элементарной окрестностью) точки $a$.
  * $a \in \mathbb{R}, \quad U_{\varepsilon_1}(a) \cap U_{\varepsilon_2}(a) = U_\varepsilon(a), \quad \varepsilon = \min(\varepsilon_1, \varepsilon_2)$
  * $a = +\infty, \quad U_{\varepsilon_1}(+\infty) \cap U_{\varepsilon_2}(+\infty) = U_\varepsilon(+\infty), \quad \varepsilon = \min(\varepsilon_1, \varepsilon_2)$, так как $\begin{cases} x > \frac{1}{\varepsilon_1} \\ x > \frac{1}{\varepsilon_2} \end{cases} \implies x > \max\left(\frac{1}{\varepsilon_1}, \frac{1}{\varepsilon_2}\right) = \frac{1}{\min(\varepsilon_1, \varepsilon_2)}$.
  * Для $a = -\infty$ и для несимметричных окрестностей — аналогично.


- **4)** Если $a \in (\alpha, \beta)$, то существует $U_\varepsilon(a) \subset (\alpha, \beta)$. 
  Возьмём $\varepsilon < \min(|a-\alpha|, |\beta-a|) > 0$.

---

### п. 3. Открытые и замкнутые множества

- **Определение.** Точка $x \in A$ называется **внутренней точкой** множества $A \subset \overline{\mathbb{R}}$, если $\exists \varepsilon > 0: U_\varepsilon(x) \subset A$ (точка входит во множество вместе с некоторой окрестностью).
  Множество всех внутренних точек множества называется **внутренностью множества**, обозначается $\text{int } A$. 
  Замечание: $\text{int } A \subset A$.


- **Определение.** Множество называется **открытым**, если все его точки внутренние, то есть $\text{int } A = A$.
  **Примеры:** 
  * $(\alpha, \beta)$ — открытое множество (из свойства 4), где $-\infty \le \alpha < \beta \le +\infty$
  * $\bigcup_{n=1}^m (\alpha_n, \beta_n)$ — открытое множество (где $(\alpha_n, \beta_n)$ — непересекающиеся интервалы).


- **Определение.** Точка $a \in \overline{\mathbb{R}}$ называется **предельной точкой** множества $A \subset \overline{\mathbb{R}}$, если $\forall \varepsilon > 0: \mathring{U}_\varepsilon(a) \cap A \neq \varnothing$ (любая окрестность точки $a$ содержит точки множества $A$, отличные от $a$).
  Множество всех предельных точек множества $A$ обозначается $\text{Lim } A$.


- **Определение.** **Замыкание множества** $A$ — множество $\overline{A} = A \cup \text{Lim } A$.


- **Определение.** Множество $A$ называется **замкнутым**, если оно содержит все свои предельные точки, то есть $\text{Lim } A \subset A$, или $\overline{A} = A$.
  **Примеры:**
  * $[\alpha, \beta]$ — замкнутое множество.
  * $A = (\alpha, \beta)$ — не замкнутое множество, так как $\alpha, \beta \in \text{Lim } A$, но $\alpha, \beta \notin A$. При этом $\overline{(\alpha, \beta)} = [\alpha, \beta]$.
  * $[\alpha; +\infty)$ — замкнутое в $\mathbb{R}$, но не замкнутое в $\overline{\mathbb{R}}$, так как $+\infty$ — предельная точка множества.


- **Определение.** $a \in A$ — **изолированная точка** множества $A$, если $\exists \varepsilon > 0: U_\varepsilon(a) \cap A = \{a\}$, то есть $a \in A$ и $a \notin \text{Lim } A$.

**Примеры:**

- **1)** $A = (3; 4] \cup \{5\}$. Не открытое, не замкнутое. 
  $5 \in A$ — изолированная точка. 
  $\text{int } A = (3; 4)$. 
  $\text{Lim } A = [3; 4]$ (заметим, что $3 \in \text{Lim } A$, хотя $3 \notin A$). 
  $\overline{A} = [3; 4] \cup \{5\}$.


- **2)** $A = \left\{\frac{1}{n} \mid n \in \mathbb{N}\right\} = \left\{1, \frac{1}{2}, \frac{1}{3}, \frac{1}{4}, \dots\right\}$. 
  Все точки множества $A$ — изолированные, $\text{int } A = \varnothing$. 
  Единственная предельная точка: $0$, $\text{Lim } A = \{0\}$, $\overline{A} = A \cup \{0\}$.


- **3)** $A = \mathbb{Q}$. 
  $\text{Lim } A = \overline{\mathbb{R}}$, $\overline{A} = \overline{\mathbb{R}}$, $\text{int } A = \varnothing$, изолированных точек нет.

---

**Лемма.** 
$$a \in \text{Lim } A \iff \exists \text{ последовательность } \{x_n\}: x_n \in A \; \forall n, \; x_n \neq a \; \forall n, \text{ и } \lim_{n \to \infty} x_n = a.$$

**Доказательство:**
$\implies$ Пусть $a \in \text{Lim } A$.
Для $\varepsilon = 1 \quad \exists x_1 \in \mathring{U}_1(a) \cap A$
Для $\varepsilon = \frac{1}{2} \quad \exists x_2 \in \mathring{U}_{1/2}(a) \cap A$
... и так далее.
Для $\varepsilon = \frac{1}{k} \quad \exists x_k \in \mathring{U}_{1/k}(a) \cap A$.
$\forall k \quad x_k \in A, \; x_k \neq a$.
$a \in \mathbb{R}; \quad x_k \in \left(a - \frac{1}{k}; a + \frac{1}{k}\right) \implies \lim_{k \to \infty} x_k = a$ (по теореме о зажатой последовательности).
$a = +\infty; \quad x_k > k \implies \lim_{k \to \infty} x_k = +\infty$ ($-\infty$ доказывается аналогично).

$\impliedby$ Пусть $\lim_{n \to \infty} x_n = a, \; x_n \in A, \; x_n \neq a \; \forall n$.
То есть $\forall \varepsilon > 0 \quad \exists N: x_N \in U_\varepsilon(a), \; x_N \neq a, \; x_N \in A$, то есть $a \in \text{Lim } A$. $\blacksquare$

---

**Лемма о предельной точке** (принцип Больцано-Вейерштрасса)
Всякое бесконечное ограниченное множество $X \subset \mathbb{R}$ имеет по крайней мере одну предельную точку в $\mathbb{R}$.

**Доказательство:** 
Пусть $X \subset \mathbb{R}$ — ограниченное множество, тогда $\exists [a; b] \supset X, \; a, b \in \mathbb{R}$. Покажем, что существует предельная точка множества $X$ на отрезке $[a; b]$.
Предположим, что на $[a, b]$ предельных точек множества $X$ нет.
Делим $[a, b]$ пополам, обозначим через $[a_1, b_1]$ ту половину, которая содержит бесконечное число точек множества $X$ (если обе половины такие, то выбираем любую). Пусть $x_1 \in [a_1, b_1] \cap X$ — произвольная.
Повторяем процесс, на $n$-м шаге: $[a_n, b_n]$ — половина отрезка $[a_{n-1}, b_{n-1}]$, содержащая бесконечное число точек из $X$. 
$x_n \in [a_n, b_n] \cap X$ — произвольная, $x_n \neq x_k \; \forall k = 1, 2, \dots, n-1$.
Так как $\lim_{n \to \infty} (b_n - a_n) = \lim_{n \to \infty} \frac{b-a}{2^n} = 0$, то по лемме о вложенных отрезках существует $\lim_{n \to \infty} a_n = \lim_{n \to \infty} b_n = c \in [a, b]$. 
И так как $a_n \le x_n \le b_n \; \forall n$, то и $\lim_{n \to \infty} x_n = c$. (При необходимости перейдём к подпоследовательности $\{x_{n_k}\}: x_{n_k} \neq c \; \forall k, \; \lim_{k \to \infty} x_{n_k} = c$).
Следовательно, $c \in \text{Lim } X$. $\blacksquare$

*(Второе доказательство)*
Предположим, что на $[a, b]$ предельных точек $X$ нет, то есть $\forall x \in [a, b] \quad \exists$ окрестность $U(x)$ такая, что $U(x) \cap X = \varnothing$ или $\{x\}$.
Множество $\{U(x)\}_{x \in [a, b]}$ образует покрытие $[a, b]$ интервалами. По лемме Бореля-Лебега, существует конечный набор интервалов $\{U(x_i)\}_{i=1, \dots, n}$, так что $X \subset [a, b] \subset \bigcup_{i=1}^n U(x_i)$.
Однако в каждом интервале $U(x_i)$ содержится лишь конечное число элементов множества $X$, а так как $X$ содержится в конечном объединении множеств $U(x_i)$, то само $X$ конечно — противоречие. $\blacksquare$

**Следствие.** Любое множество в $\mathbb{R}$ имеет предельную точку в $\overline{\mathbb{R}}$. 
(Если множество не ограничено сверху, то легко увидеть, что $+\infty$ — его предельная точка).

---

**Лемма.** 
- **1)** Дополнение к открытому множеству — замкнутое. 
- **2)** Дополнение к замкнутому множеству — открытое.

**Доказательство** (в $\overline{\mathbb{R}}$):
- **1)** Пусть $A \subset \overline{\mathbb{R}}$ — открытое, рассмотрим множество $B = \overline{\mathbb{R}} \setminus A = \{x \in \overline{\mathbb{R}} \mid x \notin A\}$.
  Пусть $x \in \text{Lim } B$, докажем, что $x \in B$. Предположим, что это не так, и $x \in A$.
  Так как $A$ — открытое, то существует окрестность $U_\varepsilon(x) \subset A$. Следовательно, $U_\varepsilon(x) \cap B = \varnothing$, то есть $x \notin \text{Lim } B$ — противоречие. Значит, $x \in B$, и $B$ — замкнутое. $\blacksquare$


- **2)** Пусть $B \subset \overline{\mathbb{R}}$ — замкнутое, и $A = \overline{\mathbb{R}} \setminus B$. Докажем, что $A$ — открытое.
  Пусть $x \in A$, предположим, что $x \notin \text{int } A$ ($x$ — не внутренняя точка $A$), то есть $\forall U_\varepsilon(x) \quad \exists y \in U_\varepsilon(x)$, но $y \notin A$, то есть $y \in \mathring{U}_\varepsilon(x) \cap B$.
  Таким образом, $x \in \text{Lim } B$, но $x \notin A$, а значит, $x \notin B$ — противоречие замкнутости $B$.
  Следовательно, $\forall x \in A$ — внутренняя, и $A$ — открытое. $\blacksquare$

*Законы де Моргана:*
$\overline{\mathbb{R}} \setminus \bigcap_\alpha A_\alpha = \bigcup_\alpha (\overline{\mathbb{R}} \setminus A_\alpha)$
$\overline{\mathbb{R}} \setminus \bigcup_\alpha A_\alpha = \bigcap_\alpha (\overline{\mathbb{R}} \setminus A_\alpha)$

---

**Лемма.**
- **1)** Объединение любой совокупности открытых множеств — открытое.
- **2)** Пересечение конечного числа открытых множеств — открытое.
- **3)** Пересечение любой совокупности замкнутых множеств — замкнутое.
- **4)** Объединение конечного числа замкнутых множеств — замкнутое.

*Примечание: пункты 3 и 4 следуют из (1) и (2) и предыдущей леммы, если перейти к дополнениям множеств.*

**Доказательство:**
- **1)** Пусть $A = \bigcup_\alpha A_\alpha$, где $A_\alpha$ — открытые. Пусть $x \in A$ — произвольная точка.
  Тогда $x \in A_{\alpha}$ для некоторого $\alpha$. Так как $A_{\alpha}$ — открытое, то существует окрестность $U_\varepsilon(x) \subset A_{\alpha} \subset A$, то есть $A$ — открытое.


- **2)** Пусть $A = A_1 \cap A_2$, где $A_1$ и $A_2$ — открытые. Пусть $x \in A$, то есть $x \in A_1$ и $x \in A_2$.
  Так как $A_1$ — открытое, существует $U_{\varepsilon_1}(x) \subset A_1$. Так как $A_2$ — открытое, то существует $U_{\varepsilon_2}(x) \subset A_2$.
  Тогда для $\varepsilon = \min(\varepsilon_1, \varepsilon_2)$ получим $U_\varepsilon(x) \cap U_\varepsilon(x) = U_\varepsilon(x) \subset A_1 \cap A_2 = A$, то есть $A$ — открытое.
  Для $A_1 \cap A_2 \cap \dots \cap A_n$ доказывается аналогично. $\blacksquare$

---

**Теорема о замкнутости множества предельных точек.**
Пусть $A \subset \overline{\mathbb{R}}$, тогда множество $\text{Lim } A$ — замкнуто в $\overline{\mathbb{R}}$.

**Доказательство:** 
Пусть $x \in \overline{\mathbb{R}}$ — предельная точка множества $\text{Lim } A$. Тогда для произвольного $\varepsilon > 0$:
$\forall y \in \mathring{U}_\varepsilon(x) \cap \text{Lim } A$, то есть $y \in U_\varepsilon(x), \; y \neq x, \; y \in \text{Lim } A$...