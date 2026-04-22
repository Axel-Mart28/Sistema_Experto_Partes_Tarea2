<h1>
3. Representación del Conocimiento (Base de Conocimiento y Base de Hechos)
</h1>
<div align="justity">
<br>
¿Qué es?
<br>
Es la memoria del sistema experto, dividida en dos grandes bloques. La Base de Conocimiento almacena la inteligencia permanente (reglas, fórmulas, probabilidades). La Base de Hechos (o memoria de trabajo) almacena los datos transitorios y específicos del problema actual que se está analizando.
<br>
<br>

¿Para qué sirve?
<br>
Para separar las leyes generales (el conocimiento del experto) de las situaciones particulares (los datos de una medición específica), permitiendo que el sistema analice múltiples escenarios usando las mismas reglas subyacentes.
<br>

¿Cómo funciona?
<br>
Funciona como una biblioteca de referencia constante. Cuando el sistema necesita tomar una decisión, consulta la Base de Conocimiento para saber "qué reglas aplicar" a los datos temporales que se encuentran en la Base de Hechos.
<br>

Ejemplo Práctico:
<br>
Base de Conocimiento: Contiene la regla: "SI la variación de posición es > 0.5 grados bajo carga estática, ENTONCES existe holgura en los engranajes".

Base de Hechos: Almacena el dato efímero de la prueba actual: "El servomotor 1 en el instante T tiene una variación de 0.6 grados".
</div>
