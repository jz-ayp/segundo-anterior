# Estructuras de decisión

## Ejercicio: Segundo anterior

## Instrucciones
- Elabora el análisis y el algoritmo ***antes de escribir el código***. 
- Utiliza un diagrama de flujo para representar tu algoritmo e ilustrar su lógica.

- **Diseña un programa para calcular la hora correspondiente al segundo anterior**.
  - El programa recibirá tres números enteros que representarán, respectivamente, las horas, minutos y segundos correpondientes a un momento dado. 
  - El programa calculará, a continuación, la hora correspondiente al segundo anterior, es decir, qué hora sería un segundo antes de la hora proporcionada como entrada.
  - Considerar que la hora se representará en formato "militar" (24 horas).
  - Considerar también que se recibirán como entrada valores correspondientes a una hora válida, es decir, no es necesario validar las entradas.

- Codifica tu solución en el archivo [`segundo_anterior.py`](segundo_anterior.py).
   
- Utiliza los siguientes ejemplos para dar formato a tus entradas y salidas:
  ```
  Hora inicial:
      Hora: 1
      Minuto: 2
      Segundo: 3
  Hora final:
      Hora: 1
      Minuto: 2
      Segundo: 2
  
  Hora inicial:
      Hora: 8
      Minuto: 0
      Segundo: 0

  Hora final:
      Hora: 7
      Minuto: 59
      Segundo: 59
  ```
  
- Prueba tu programa corriéndolo varias veces con diferentes entradas. Verifica que tu algoritmo produzca las salidas correctas. Identifica y pon atención especial a los casos que pudieran ser problemáticos de manejar (casos límite).

- Añade una cadena de documentación (*docstring*) al inicio de tu programa.

  
## Entrega
Completa éste y el resto de los ejercicios y compila, para cada uno, el enunciado, análisis, diagrama de flujo, código y pruebas de ejecución, en un informe tal como se describe en los requisitos para entrega de tareas en Canvas. No olvides incluir portada y conclusiones.


## Casos de prueba de ejemplo
| Entradas | Salidas |
|:---------|:--------|
| `7`<br>`8`<br>`9` | `7`<br>`8`<br>`8` |
| `7`<br>`8`<br>`10` | `7`<br>`8`<br>`9` |
| `15`<br>`26`<br>`0` | `15`<br>`25`<br>`59` |
| `0`<br>`0`<br>`0` | `23`<br>`59`<br>`59` |

## Rúbrica
Verifica tu entrega contra la rúbrica disponible en Canvas para maximizar tu calificación.
