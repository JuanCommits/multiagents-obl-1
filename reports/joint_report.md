# Informe de Experimentos en Juegos Matriciales

Juan Pedro da Silva (229475) - [Repositorio de GitHub](https://github.com/JuanCommits/multiagents-obl-1)

## 1. Matching Pennies (Cara o Cruz)

### Configuración del Experimento
- Juego: Matching Pennies (juego de suma cero para 2 jugadores)
- Combinaciones de Agentes:
  - FP vs FP (Fictitious Play vs Fictitious Play)
  - FP vs Aleatorio
  - FP vs RM (Fictitious Play vs Regret Matching)
  - RM vs Aleatorio
  - RM vs RM

### Análisis de Resultados

#### FP vs FP
![Resultados FP vs FP](../results/matrix_games/matching_pennies/experiment_results_fp_vs_fp.png)
- Ambos agentes aprenden a jugar estrategias mixtas
- Convergencia al equilibrio de Nash (división 50-50)

#### FP vs Aleatorio
![Resultados FP vs Aleatorio](../results/matrix_games/matching_pennies/experiment_results_fp_vs_random.png)
- El agente FP no logra aprender a explotar la estrategia aleatoria ya que no existe forma.
- Tiende a llegar al equilibrio de Nash (50-50) sobre el final del experimento

#### FP vs RM
![Resultados FP vs RM](../results/matrix_games/matching_pennies/experiment_results_fp_vs_rm.png)
- Se puede visualizar como RM parece seguir la jugada de FP. Creando una victoria alternada.
- Tiende a converger al equilibrio de Nash

#### RM vs Aleatorio
![Resultados RM vs Aleatorio](../results/matrix_games/matching_pennies/experiment_results_rm_vs_random.png)
- El agente RM aprende efectivamente a contrarrestar el juego aleatorio
- Rendimiento más estable y mejor que FP vs RM

#### RM vs RM
![Resultados RM vs RM](../results/matrix_games/matching_pennies/experiment_results_rm_vs_rm.png)
- Ambos agentes aprenden estrategias mixtas óptimas
- Convergencia rápida al equilibrio

### Conclusión
- Ambos algoritmos FP y RM convergen al equilibrio
- Ambos algoritmos aprenden exitosamente a jugar contra oponentes aleatorios

## 2. Piedra, Papel o Tijera

### Configuración del Experimento
- Juego: Piedra, Papel o Tijera (juego de suma cero con 3 acciones)
- Mismas combinaciones de agentes que en Matching Pennies

### Análisis de Resultados

#### FP vs FP
![Resultados FP vs FP](../results/matrix_games/rock_paper_scissors/experiment_results_fp_vs_fp.png)
- Convergencia más lenta a estrategia mixta
- Eventualmente alcanza el equillibrio de Nash (p 1/3 para cada acción)

#### FP vs Aleatorio
![Resultados FP vs Aleatorio](../results/matrix_games/rock_paper_scissors/experiment_results_fp_vs_random.png)
- FP aprende a explotar el juego aleatorio
- Eventualmente alcanza el equillibrio de Nash

#### FP vs RM
![Resultados FP vs RM](../results/matrix_games/rock_paper_scissors/experiment_results_fp_vs_rm.png)
- Ningún agente se superpone al otro
- Tiende a converger al equilibrio de Nash

#### RM vs Aleatorio
![Resultados RM vs Aleatorio](../results/matrix_games/rock_paper_scissors/experiment_results_rm_vs_random.png)
- RM aprende rápidamente la estrategia óptima
- Alcanza el equillibrio de Nash

#### RM vs RM
![Resultados RM vs RM](../results/matrix_games/rock_paper_scissors/experiment_results_rm_vs_rm.png)
- Convergencia rápida al equilibrio de Nash
- Aprendizaje óptimo de estrategia mixta

### Conclusión
- Ambos algoritmos tienden a la convergencia en este juego un poco más complejo.
- Ambos algoritmos aprenden exitosamente contra oponentes aleatorios.

## 3. Juego de Blotto (10-3 y 15-5)

### Configuración del Experimento
- Juegos: 
   - Blotto con 10 soldados y 3 campos
   - Blotto con 15 soldados y 5 campos
- Mismas combinaciones de agentes que en Matching Pennies

### Análisis de Resultados

#### FP vs FP

##### 10 S - 3 N
![Resultados FP vs FP - 10 S - 3 N](../results/matrix_games/blotto10-3/experiment_results_fp_vs_fp.png)

##### 15 S - 5 N
![Resultados FP vs FP - 15 S - 5 N](../results/matrix_games/blotto15-5/experiment_results_fp_vs_fp.png)

**Análisis**
- Los agentes juegan cotrarrestando la jugada anterior del oponente. Hasta terminar en el equilibrio.
- Tienden a iterar sobre pocas acciones.

#### FP vs Aleatorio
##### 10 S - 3 N
![Resultados FP vs Aleatorio - 10 S - 3 N](../results/matrix_games/blotto10-3/experiment_results_fp_vs_random.png)

##### 15 S - 5 N
![Resultados FP vs Aleatorio - 15 S - 5 N](../results/matrix_games/blotto15-5/experiment_results_fp_vs_random.png)
**Análisis**
- FP aprende a sobreponerse sobre el juego aleatorio. Esto no es muy dificil en este tipo de juegos con muchas acciones malas.
- Encuentra una mejor acción y la explota.

#### FP vs RM
##### 10 S - 3 N
![Resultados FP vs RM - 10 S - 3 N](../results/matrix_games/blotto10-3/experiment_results_fp_vs_rm.png)

##### 15 S - 5 N
![Resultados FP vs RM - 15 S - 5 N](../results/matrix_games/blotto15-5/experiment_results_fp_vs_rm.png)
**Análisis**
- Se puede observar ambos agentes se sobreponen al otro por "estaciones"
- FP tiende a explorar una mayor cantidad de acciones que RM

#### RM vs Aleatorio
##### 10 S - 3 N
![Resultados RM vs Aleatorio - 10 S - 3 N](../results/matrix_games/blotto10-3/experiment_results_rm_vs_random.png)

##### 15 S - 5 N
![Resultados RM vs Aleatorio - 15 S - 5 N](../results/matrix_games/blotto15-5/experiment_results_rm_vs_random.png)
**Análisis**
- Al igual que FP, RM aprende rápidamente a sobreponerse sobre el oponente.
- FP tiende a jugar con una menor cantidad de acciones que RM.
- A la larga ninguno se sobrepone sobre el otro.

#### RM vs RM
##### 10 S - 3 N
![Resultados RM vs RM - 10 S - 3 N](../results/matrix_games/blotto10-3/experiment_results_rm_vs_rm.png)

##### 15 S - 5 N
![Resultados RM vs RM - 15 S - 5 N](../results/matrix_games/blotto15-5/experiment_results_rm_vs_rm.png)
**Análisis**
- Ambos agentes tienen un juego muy similar.
- Ninguno se sobreponeal otro.
- Tiende a la convergencia.

### Conclusión
- Tanto RM como FP muestran una buena adaptación en este juego más complejo
- Ambos algoritmos aprenden exitosamente contra oponentes aleatorios
- La complejidad del juego de Blotto y la cantidad de acciones malas hace que sea fácil sobreponerse al agente random.


## Conclusiones Generales

Ambos algoritmos FP y RM tienden a converger a un equilibrio en todos los juegos cuando se enfrentan contra sí mismo.
Cuando se enfrentan entre ellos de igual manera ninguno se logra sobreponer sobre el otro y también tiende a una convergencia.
RM tiende a explorar una mayor cantidad de acciones que FP.
FP tiende a explotar los patrones de juegos asumiendo que son estacionarios.
Cuando se enfrenta FP contra si mismo se puede visualizar claramente como cada agente reacciona a la acción del oponente creando "estaciones".


# Informe de Experimentos en Foraging

Juan Pedro da Silva (229475) - [Repositorio de GitHub](https://github.com/JuanCommits/multiagents-obl-1)

## Configuración de los Experimentos

### Entornos
Se realizaron experimentos en diferentes configuraciones:
- **Tamaños de Grid**: 6x6 y 8x8
- **Número de Frutas**: 1, 2 y 3
- **Número de Agentes**: 2 y 3 agentes
- **Combinaciones de Estrategias**:
  - IQL vs IQL (Independent Q-Learning)
  - IQL vs JAL-AM (Joint Action Learning - Agent Modeling)
  - JAL-AM vs JAL-AM
  - IQL vs IQL vs IQL (3 agentes)
  - IQL vs JAL-AM vs IQL (3 agentes)
  - JAL-AM vs JAL-AM vs JAL-AM (3 agentes)

### Algoritmos y Estrategias

1. **IQL (Independent Q-Learning)**
   - Aprendizaje independiente para cada agente
   - No considera las acciones que otros agentes están usando
   - Política ε-greedy para exploración
   - Tabla Q individual para cada agente

2. **JAL-AM (Joint Action Learning - Agent Modeling)**
   - Considera las acciones conjuntas de los agentes
   - Mantiene noción de las acciones que van tomando los otros agentes
   - Mejor coordinación entre agentes
   - Aprendizaje más complejo pero más efectivo

## Análisis Detallado de Resultados

### Grid 6x6 con 1 Fruta

#### Configuración de 2 Agentes

##### IQL vs IQL
![Resultados IQL vs IQL](../results/foraging/grid6x6_fruits1/2_agents/experiment_results_2agents_iql_vs_iql.png)

##### IQL vs JAL-AM
![Resultados IQL vs JAL-AM](../results/foraging/grid6x6_fruits1/2_agents/experiment_results_2agents_iql_vs_jal-am.png)

##### JAL-AM vs JAL-AM
![Resultados JAL-AM vs JAL-AM](../results/foraging/grid6x6_fruits1/2_agents/experiment_results_2agents_jal-am_vs_jal-am.png)

**Análisis**
En estos experimentos se puede ver la rapidez de aprendizaje de ambos algoritmos en entornos simples. Tanto IQL como JAL-AM aprenden a interactuar con el juego obteniendo recompensas mayores a 0. En el experimento 2 se puede ver como JAL-AM tiende a sobreponerse sobre IQL.

### Grid 6x6 con 2 Frutas

#### Configuración de 3 Agentes

##### IQL vs IQL vs IQL
![Resultados IQL vs IQL vs IQL](../results/foraging/grid6x6_fruits2/3_agents/experiment_results_3agents_iql_vs_iql_vs_iql.png)

##### IQL vs JAL-AM vs IQL
![Resultados IQL vs JAL-AM vs IQL](../results/foraging/grid6x6_fruits2/3_agents/experiment_results_3agents_iql_vs_jal-am_vs_iql.png)

##### JAL-AM vs JAL-AM vs JAL-AM
![Resultados JAL-AM vs JAL-AM vs JAL-AM](../results/foraging/grid6x6_fruits2/3_agents/experiment_results_3agents_jal-am_vs_jal-am_vs_jal-am.png)
- **Análisis**:
En este experimento podemos ver un ambiente un poco más complejo y a la vez más agentes. En esta configuración se puede ver la inestabilidad de IQL ya que en el experimento 1 ninguno de los 3 agentes logra aprender una política aceptable mientras que en el experimento 2 un agente IQL rápidamente logra aprender una política buena. Podemos ver como JAL-AM tiende a ser más estable.

### Grid 8x8

### Grid 8x8 con 2 Frutas

#### Configuración de 2 Agentes

##### IQL vs IQL
![Resultados IQL vs IQL](../results/foraging/grid8x8_fruits2/2_agents/experiment_results_2agents_iql_vs_iql.png)

##### IQL vs JAL-AM
![Resultados IQL vs JAL-AM](../results/foraging/grid8x8_fruits2/2_agents/experiment_results_2agents_iql_vs_jal-am.png)

##### JAL-AM vs JAL-AM
![Resultados JAL-AM vs JAL-AM](../results/foraging/grid8x8_fruits2/2_agents/experiment_results_2agents_jal-am_vs_jal-am.png)
- **Análisis**:
En este expeimento reafirmamos los indicios de que JAL-AM tiende a ser mejor en ambientes más complejos. Sería interesante ver si a mayor cantidad de iteraciones los agentes IQL logran aprender un política aceptable.

### Grid 8x8 con 3 Frutas

#### Configuración de 2 Agentes

##### IQL vs IQL
![Resultados IQL vs IQL](../results/foraging/grid8x8_fruits3/2_agents/experiment_results_2agents_iql_vs_iql.png)

##### IQL vs JAL-AM
![Resultados IQL vs JAL-AM](../results/foraging/grid8x8_fruits3/2_agents/experiment_results_2agents_iql_vs_jal-am.png)

##### JAL-AM vs JAL-AM
![Resultados JAL-AM vs JAL-AM](../results/foraging/grid8x8_fruits3/2_agents/experiment_results_2agents_jal-am_vs_jal-am.png)

- **Análisis**:
En este experimento se puede ver claramente como en todos los casos un agente se sobrepone ante el otro mostrando muy poca coordinación.
Se pueden ver en los dos primeros experimentos como uno de los dos agentes no recolecta ninguna fruta.
El último experimento mustra un poco de coordinación ya que se llega a una cantidad de frutas recolectadas mayor que la cantidad de frutas en el juego.

#### Configuración de 3 Agentes

##### IQL vs IQL vs IQL
![Resultados IQL vs IQL vs IQL](../results/foraging/grid8x8_fruits3/3_agents/experiment_results_3agents_iql_vs_iql_vs_iql.png)

##### IQL vs JAL-AM vs IQL
![Resultados IQL vs JAL-AM vs IQL](../results/foraging/grid8x8_fruits3/3_agents/experiment_results_3agents_iql_vs_jal-am_vs_iql.png)

#### JAL-AM vs JAL-AM vs JAL-AM
![Resultadps JAL-AM vs JAL-AM vs JAL-AM](../results/foraging/grid8x8_fruits3/3_agents/experiment_results_3agents_jal-am_vs_jal-am_vs_jal-am.png)

- **Análisis**:
En este experimento se puede observar como los agentes IQL tienden a aprender a sobreponerse a los opponentes casi sin dejar la posibilidad de contrarrestar su jugada. Estos agentes tienden a una menor colaboración sobre los agentes JAL-AM.
Como se puede ver en el 3er experimento anteriores todos agentes aprenden a colaborar entre ellos recolectando frutas en conjunto y llegando a un promedio de casi 5. Como el ambiente solo cuenta con 3 frutas esto sugiere que los agentes tienden a colaborar y recolectar frutas en conjunto. También se puede ver como ningún agente se queda sin recolectar ninguna fruta.


## Conclusiones

### IQL (Independent Q-Learning) vs JAL-AM (Joint Action Learning with Action Modeling)

JAL-AM tiende a alcanzar un mejor rendimiento en entornos más complejos sobre IQL. Esto se puede ver en los experimentos presentados como por ejemplo `grid8x8_fruits3 IQL vs JAM-AL` o `grid8x8_fruits2 IQL vs JAM-AL`.
En algunos casos IQL tiende a no aprender ninguna política que lleve a una recompensa positiva, por ejemplo `grid8x8_fruits3 IQL vs IQL vs IQL` o `grid8x8_fruits2 IQL vs IQL`
IQL iene un costo comutacional menor que JAL-AM por lo que es más rápido de ejecutar sobre la otra estrategia.
JAL-AM también tiene un mayor costo en memoria en comparación a IQL.
En los entornos que se requiere coordinación JAL-AM tiende a performar mejor que IQL ya que toma en cuenta las acciones que toman los otros agentes que están interactuando con el ambiente. Esto se puede ver en los experimentos `grid8x8_fruits3 JAM-AL vs JAM-AL vs JAM-AL` y `grid8x8_fruits3 IQL vs IQL vs IQL`.
Por último cabe mencionar que JAL-AM tiende a ser un agente más estable en el aprendizaje.


### Próximos Pasos
- Experimentar con más agentes
- Experimentar con más configuraciones de los juegos
- Experimentar con más hyperparámetros de os agentes
- Experimentar con funciones de aproximación
- Experimentar con mayo cantidad de iteraciones principalmente para los agentes IQL.
- Analizar el impacto de la memoria en JAL-AM



Se pueden ver más experimentos en la carpeta de `resultados`.