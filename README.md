# 📋 Evaluación QA - Erco

Repositorio enfocado en la evidencia de la evaluación para el puesto de **Practicante QA** en **Erco**.

---

## 👤 Sobre mí

Hola, soy **Eddie Alejandro Arenas Vital**, aprendiz en **Análisis y Desarrollo de Software**.

Agradezco la oportunidad de presentar esta prueba. La verdad, fue un reto interesante para mí, ya que no tenía un conocimiento muy amplio sobre el área de QA ni había hecho uso de pruebas automatizadas en Python.  
Este reto me permitió aprender cosas nuevas y repasar saberes previos que serán muy valiosos para mi futuro.

---

## 🧠 1. Conocimientos QA

### ✅ ¿Qué es QA y por qué es importante?

El área de QA (Quality Assurance) se encarga de **verificar la calidad del software**, validando tanto su funcionalidad como su operatividad.  
La importancia de QA se refleja en casos como el ocurrido con **Microsoft**, donde varios servicios sufrieron una caída global que afectó a millones de usuarios. Con una verificación más exhaustiva, estos problemas podrían haberse prevenido.

---

### 🔍 Diferencia entre pruebas manuales y automáticas

- **Pruebas Manuales:** Ejecutadas por personas. Se usan para validar interfaces, experiencia de usuario y comportamiento visual.  
- **Pruebas Automáticas:** Ejecutadas mediante scripts. Son útiles para validar lógicas de negocio, funciones repetitivas o grandes volúmenes de datos.

**¿Cuándo usar cada una?**  
- Manuales: Ideal en pruebas exploratorias o interfaces gráficas.  
- Automáticas: Recomendables en pruebas de regresión o funcionalidad constante.

---

### 🧪 ¿Qué son los casos de prueba?

Son conjuntos de condiciones diseñadas para verificar si una funcionalidad del sistema está funcionando como se espera.

#### 📝 Ejemplo de Caso de Prueba

| Atributo              | Valor                                                                 |
|-----------------------|-----------------------------------------------------------------------|
| **ID**                | A1                                                                    |
| **Nombre**            | Validación de inicio de sesión con email y contraseña correctas       |
| **Funcionalidad**     | Inicio de sesión                                                      |
| **Tipo de Prueba**    | Manual                                                                |
| **Datos Pre-Prueba**  | email: `juan@yopemail.com`, password: `123365`                        |
| **Requisitos**        | El usuario ya debe estar registrado en el sistema                     |
| **Resultado Esperado**| El usuario accede al sistema y es redirigido a la venta de cursos     |
| **Resultado Real**    | El usuario no puede iniciar sesión; no se validan sus credenciales    |
| **Fecha Realización** | 08/04/2025                                                            |
| **Estado**            | Falló                                                                 |

---

### 🔁 ¿Qué es una prueba de regresión?

Permite verificar que los **cambios recientes** no afecten negativamente funcionalidades existentes.

**Ejemplo práctico:**  
Tengo un sitio web para venta de zapatos al por mayor. Decido agregar venta al detal, por lo que modifico la base de datos.  
Con una prueba de regresión, verifico que la funcionalidad original (mayorista) **siga funcionando correctamente** mientras se integra la nueva (detal).

---

## 🧩 2. Resolución de Problemas - Fallo Intermitente en Pasarela de Pagos NEU

### ❓ Escenario
Los usuarios reportan fallos intermitentes en la pasarela de pagos de **NEU**, sin mostrar mensajes de error. El equipo aún no ha encontrado la causa raíz.

---

### 🔍 Hipótesis del Problema

1. Falta de manejo de errores en frontend o backend.
2. Errores en la conexión con el proveedor de pagos.
3. Fallas en la validación de datos o consumo de APIs.
4. Casos específicos con ciertos métodos de pago (ej: App Bancolombia).

---

### 🧪 Pasos para Reproducir el Error

1. Probar distintos métodos de pago (tarjeta, PSE, QR, etc.).
2. Realizar pagos en diferentes horarios (tráfico bajo/alto).
3. Simular errores forzados (caída de red, sesión expirada).
4. Revisar patrones en reportes de fallos de usuarios.

---

### 📊 Datos de Prueba

- Datos con campos vacíos o formatos inesperados.
- Pagos desde dispositivos y redes distintas.
- Conexiones lentas o inestables.
- Métodos de pago de distintos bancos/apps.

---

### 🧠 Estrategia para Aislar la Causa

1. Usar herramientas de monitoreo para detectar picos de error.
2. Implementar logs detallados en cada paso del flujo.
3. Validar si hay errores silenciosos en el backend.
4. Consultar con el proveedor de pagos por fallos o límites superados.

---

### 💡 Sugerencias para Solucionarlo

- Implementar sistema de **manejo global de errores**.
- Agregar **logs detallados** (hora, paso fallido, usuario, IP, etc.).
- Usar **herramientas de monitoreo** (Ej: Sentry, Datadog, Grafana).
- Habilitar **mensajes temporales** de error para el usuario.
- Implementar **reintentos automáticos** para errores con APIs externas.

---

## 📚 Fuentes de Información

- [OpenWebinars - ¿Qué es QA y su importancia?](https://openwebinars.net/blog/que-es-qa-y-su-importancia-en-la-actualidad/)
- [Qalified - Pruebas de regresión](https://qalified.com/es/blog/pruebas-regresion/)
- [Guía de casos de prueba - Statistics Easily](https://es.statisticseasily.com/glosario/%C2%BFQu%C3%A9-es-la-gu%C3%ADa-completa-de-casos-de-prueba%3F/)

---
