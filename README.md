# evaluacion-qa-erco
Repositorio enfocado en la evidencia de la evaluación para el puesto de practicante en el área de QA en Erco

Sobre mí 👩‍💻 / 👨‍💻
Soy Eddie Alejandro Arenas Vital, aprendiz en Análisis y Desarrollo de Software. Agradezco la oportunidad de presentar esta prueba. La verdad, fue un reto interesante para mí, ya que no tenía un conocimiento muy amplio sobre el área de QA y no había hecho uso de pruebas automatizadas en Python.
Este reto me permitió aprender cosas nuevas y repasar saberes previos que van a ser muy valiosos para mi futuro.

## 1. Conocimientos QA

¿Qué es QA y por qué es importante en el desarrollo de software? Proporciona un caso de la vida real donde QA haya prevenido un problema grave.

• El área de QA se encarga de verificar los problemas que pueda llegar a tener un software tanto en funcionalidad como en operatividad. La importancia del área de QA se evidencia en situaciones como lo que ocurrió el año pasado con Microsoft, donde muchos servicios de Microsoft sufrieron una caída global que afectó a millones de usuarios en todo el mundo, algo que con verificaciones mas intensas por el área de QA se podría haber evitado. 

¿Cuál es la diferencia entre pruebas manuales y pruebas automáticas? Menciona en qué casos sería recomendable usar cada una.

• Las pruebas manuales involucran que una o más personas hagan validaciones del tiempo de respuesta del software, del diseño de este, de funcionalidades como un login, etc. Y las pruebas automatizadas se encargan de encontrar errores de manera rapida atravez de scripts, en especial de las funciones y los metodos que tiene software.

¿Qué son los casos de prueba y cómo los crearías? Escribe un caso de prueba detallado para una funcionalidad sencilla (por ejemplo, un formulario de inicio de sesión).

•Es un conjunto de condiciones con las cuales una persona del area de QA determinará si un sistema está funcionando correctamente. Yo personalmente crearía un caso de prueba guiandome por los requerimientos que tiene el sistema. Si un sistema tiene como requerimiento un login, mi caso de prueba seria algo asi:
Caso Prueba
ID -> A1
Nombre -> Validación de inicio de sesión con email y contraseña correctas
Funcionalidad -> Inicio de sesion
Tipo de Prueba -> Manual
Datos Pre-Prueba -> email: juan@yopemail.com, +password: 123365
Requisitos -> El usuario ya debe estar registrado en el sistema                    
Resultado Esperado -> Usuario accede al sistema con credenciales correctas y se le redirige a la venta de cursos.
Resultado Real -> El usuario no puede iniciar sesión, no se logra validar credenciales de un usuario registrado.
Fecha Realización -> 08/04/2025
Estado -> Falló

¿Cuál es el propósito de la prueba de regresión? Explica con un ejemplo cómo se aplicaría en un proyecto.

Supongamos que tengo un sitio web para la venta de zapatos al por mayor en la Minorista y quiero agregar la funcionalidad de vender zapatos al detal. Para esto, necesito modificar algunos componentes de la base de datos.
Ahí es donde entra la prueba de regresión, la cual permite verificar que estos cambios no afecten el funcionamiento actual del software ni alteren otras funcionalidades ya implementadas.
De esta manera, se asegura que el sistema continúe funcionando correctamente mientras se integran nuevas funcionalidades.


## 2. Resolución de Problemas - Fallo Intermitente en Pasarela de Pagos NEU
Supongamos que eres responsable de probar la pasarela de pagos de NEU, y los usuarios han informado que, ocasionalmente, el proceso de pago falla sin dar ningún mensaje de error. El equipo de desarrollo no ha identificado la causa raíz aún.

### 🔍 Hipótesis del problema

Falta de manejo de errores

Errores en la conexión con el proveedor de pagos.

Fallos en la validación de datos o en la conexión con APIs.

Condiciones específicas del tipo de pago electrónico (por ejemplo, falla solo con la nueva app de Bancolombia).
---

### 🧪 Pasos para reproducirlo

Utilizar herramientas de monitoreo para identificar picos de error en momentos específicos.

Agregar validaciones y mensajes temporales para mostrar más información al usuario si algo falla.

Simular errores forzados por caida de red.

---

### Datos de prueba

Datos con campos vacíos o difíciles de procesar.

Transacciones desde distintos métodos de pago.

Usuarios con conexiones lentas.

--
###  Estrategia para aislar la causa raíz

Utilizar herramientas de monitoreo para identificar picos dede alta fecuencia en momentos específicos.

Agregar validaciones y mensajes temporales para mostrar más información al usuario si algo falla.

Verificar las APIs para revisar problemas conocidos o si se alcanzaron límites.

---

### Sugerencias para solucionarlo

Implementar un sistema de manejo de errores.

Agregar logs detallados y trazabilidad en cada paso del proceso de pago.

Usar herramientas de monitoreo que detecten errores del lado del cliente.

En caso de problemas con APIs externas, implementar reintentos automáticos si es posible.


## Fuentes de Información

https://qalified.com/es/blog/pruebas-regresion/

https://openwebinars.net/blog/que-es-qa-y-su-importancia-en-la-actualidad/

https://es.statisticseasily.com/glosario/%C2%BFQu%C3%A9-es-la-gu%C3%ADa-completa-de-casos-de-prueba%3F/