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
