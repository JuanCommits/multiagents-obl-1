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