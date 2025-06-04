### 1. Popularidade (`popularidade`)

* **O quê e como se comporta?**
  A popularidade das músicas no dataset, medida numa escala de 0 a 100, apresenta uma **dispersão considerável**. A **média** é de `47,01` e a **mediana**, `49,00`, indicando uma distribuição que, embora próxima da simetria na parte central, é fortemente influenciada por um fenômeno específico: a **moda** ser `0`. Isso significa que o valor mais frequente corresponde a músicas com popularidade nula ou muito baixa. O **desvio padrão** de `23,03` e o **coeficiente de variação** de `48,99%` (quase metade da média) quantificam essa grande variabilidade. Os gráficos de histograma e boxplot ilustram claramente esse cenário, mostrando uma concentração de dados no extremo inferior, mas também uma dispersão que se estende até o máximo de `99`.

* **Por quê e onde?**
  A alta frequência de popularidade `0` pode ocorrer por diversos motivos: músicas recém-lançadas que ainda não acumularam reproduções, faixas de artistas menos conhecidos ou até mesmo peculiaridades na forma como o Spotify calcula essa métrica. Essa concentração no patamar mais baixo da escala, coexistindo com músicas que atingem quase o valor máximo, revela uma **distribuição desigual**, típica de plataformas digitais, onde poucos artistas concentram grande parte dos streamings (*efeito cauda longa*).

* **Relevância para o projeto:**
  Essa é, provavelmente, a **informação mais relevante** do projeto. A elevada variabilidade da `popularidade` permite investigar como fatores emocionais (como `vivacidade` e a variável categórica de emoção) explicam parte dessa dispersão. Se todas as músicas fossem igualmente populares, não haveria como avaliar o impacto das emoções (ou de qualquer outra característica) sobre esse fenômeno.

---

### 2. Valência (`vivacidade`) – A Positividade Musical

* **O quê e como se comporta?**
  A `vivacidade`, que mede a positividade emocional de uma faixa (0.0 para negativa/triste, 1.0 para positiva/alegre), apresenta uma **média** de `0,49` e uma **mediana** de `0,48`. Esses valores, próximos de 0,5, indicam que o conjunto de músicas, em média, não tende fortemente para nenhum extremo emocional, mas cobre todo o espectro. A **moda**, em `0,54`, sugere uma leve predominância de músicas um pouco mais positivas. Importante destacar que a `vivacidade` possui o **maior coeficiente de variação relativo** entre as variáveis musicais analisadas (aproximadamente `51,02%`), com um **desvio padrão** de `0,25` e amplitude total (mínimo `0,0`, máximo `1,0`).

* **Por quê e onde?**
  É natural que a música explore uma ampla gama de expressões emocionais. Essa distribuição balanceada é desejável para o estudo, pois significa que o dataset contempla músicas que vão desde as mais melancólicas até as mais eufóricas, possibilitando investigar relações com a popularidade e outros atributos musicais.

* **Relevância para o projeto:**
  A alta dispersão da `vivacidade` é **fundamental** para os objetivos do projeto. Ela garante a variação necessária na variável independente (emoção, via positividade) para testar sua relação com a `popularidade`. Se houvesse baixa variabilidade, seria impossível avaliar se músicas mais positivas são, de fato, mais populares — ou vice-versa.

---

### 3. Energia (`energia`)

* **O quê e como se comporta?**
  A `energia` é uma medida perceptual da intensidade e da atividade da música, variando de 0.0 a 1.0. A **média** (`0,65`), a **mediana** (`0,67`) e a **moda** (`0,70`) indicam que as músicas do dataset tendem a apresentar níveis de energia acima da média da escala. O **desvio padrão**, de `0,22`, e o **coeficiente de variação**, de `33,85%`, revelam uma dispersão moderada, mas relevante. O histograma, provavelmente, mostraria uma concentração de faixas na faixa de média a alta energia.

* **Por quê e onde?**
  É comum que músicas mais populares, especialmente em gêneros predominantes nas plataformas de streaming, apresentem níveis moderados a elevados de energia, visando gerar maior engajamento do público. A variabilidade observada permite investigar se diferentes níveis de energia estão associados a diferentes emoções ou níveis de popularidade.

* **Relevância para o projeto:**
  A `energia` surge como uma covariável interessante. Relaciona-se diretamente ao segundo objetivo específico: **analisar como características como dançabilidade e energia variam entre emoções**. Além disso, permite explorar relações como: músicas alegres são mais energéticas? Ou há exceções notáveis? Essas são perguntas cruciais para as análises bivariadas e multivariadas subsequentes.

---

### 4. Dançabilidade (`dancabilidade`)

* **O quê e como se comporta?**
  A `dancabilidade` (de 0.0 a 1.0) mede o quão adequada uma faixa é para dançar, levando em conta elementos como estabilidade do ritmo, regularidade da batida e estrutura. Com **média** de `0,62`, **mediana** de `0,63` e **moda** de `0,65`, as músicas são, em geral, moderadamente dançantes. Trata-se de uma das variáveis com **menor dispersão relativa** (Coeficiente de Variação de `25,81%`, Desvio Padrão de `0,16`), indicando certa homogeneidade nessa característica.

* **Por quê e onde?**
  A predominância de músicas moderadamente dançantes pode refletir o perfil das músicas mais consumidas na plataforma, ou a presença de gêneros onde a dançabilidade é um atributo valorizado (como pop, eletrônico, reggaeton e funk). A baixa dispersão sugere que, independentemente da emoção transmitida, há uma tendência geral para músicas que favoreçam movimentos rítmicos.

* **Relevância para o projeto:**
  Assim como a `energia`, a `dancabilidade` é essencial para investigar como as características musicais se distribuem entre emoções distintas. A menor variabilidade pode indicar que ela exerce um efeito mais constante ou menos decisivo na diferenciação entre emoções e na popularidade, o que será testado nas etapas seguintes.

---

### 5. Intensidade Sonora (`volume`)

* **O quê e como se comporta?**
  A `volume`, medida em decibéis (dB), possui uma **média** de `-8,00` dB e uma **mediana** de `-7,36` dB. Como esperado, os valores são negativos, visto que se referem à distância em relação ao silêncio absoluto. A amplitude é bastante ampla, com um **mínimo** de `-46,31` dB e um **máximo** de `1,51` dB. O **desvio padrão**, de `4,43` dB, gera um **coeficiente de variação** de aproximadamente `55%` (considerando o módulo da média), revelando uma dispersão alta.

* **Por quê e onde?**
  Essa grande variação pode ser atribuída a práticas de masterização distintas entre gêneros, períodos de lançamento e estilos musicais. Também reflete fenômenos como a chamada *“loudness war”* (guerra do volume), em que produtores buscam maximizar o volume percebido nas gravações.

* **Relevância para o projeto:**
  Embora `volume` não esteja diretamente relacionada à emoção no mesmo nível que `vivacidade`, ela pode impactar a percepção de energia e intensidade, afetando indiretamente tanto a resposta emocional quanto o engajamento dos ouvintes. Além disso, valores extremos, como o mínimo observado, indicam a necessidade de um tratamento prévio dos dados para remoção de outliers.

---

### 6. Andamento (`batida`)

* **O quê e como se comporta?**
  A `batida` (em batidas por minuto — BPM) tem uma **média** de `122,53` BPM, **mediana** de `122,01` BPM e **moda** de `120,00` BPM. O **desvio padrão** é de `29,19` BPM e o **coeficiente de variação**, de `23,82%`, é o menor entre todas as variáveis analisadas, sugerindo uma **consistência relativa** no andamento das músicas, geralmente dentro de um ritmo moderado a rápido. Entretanto, a presença de um **mínimo de 0 BPM** indica prováveis erros de leitura, músicas não convencionais (como áudios de silêncio, pausas ou efeitos) ou dados ausentes que precisam ser tratados.

* **Por quê e onde?**
  A concentração em torno de 120 BPM não é acidental: este é um ritmo próximo ao da marcha humana (\~120 passos por minuto) e aparece com frequência na música popular por sua relação com o conforto auditivo e motor do ouvinte. Isso explica, em parte, a homogeneidade observada.

* **Relevância para o projeto:**
  O andamento é uma variável que pode se relacionar tanto com a energia percebida quanto com certas emoções. Músicas rápidas podem ser associadas a sensações de alegria, agitação ou ansiedade, enquanto músicas lentas tendem a evocar calma, introspecção ou tristeza. Entender como o andamento varia entre emoções será uma parte fundamental da análise subsequente.
