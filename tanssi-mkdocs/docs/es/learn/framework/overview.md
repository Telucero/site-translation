---
título: Visión general del marco de desarrollo de la red
descripción: Substrate es un marco de desarrollo de blockchain construido en el lenguaje de programación Rust que agiliza y acelera el proceso de desarrollo de nuevas redes.
icono: octicons-home-24
categorías: Fundamentos
---

#Descripción general del marco de desarrollo de la red {: #network-dev-framework-overview }

## Introducción {: #introduction }

Construir una red desde cero es una tarea muy compleja que requiere un profundo conocimiento en una amplia gama de áreas, incluyendo (pero no limitado a):

- ** Algoritmos de consenso** - el consenso asegura que todos los participantes en la red blockchain están de acuerdo en la validez de las transacciones. Algunos mecanismos de consenso conocidos son Proof of Work (PoW) y Proof of Stake (PoS).

- Criptografía** - la criptografía desempeña un papel crucial en la seguridad de la cadena de bloques. Necesitará algoritmos criptográficos para tareas como la creación de firmas digitales, la verificación de transacciones y el cifrado de datos.

- Red distribuida**: una arquitectura de red que permita a los nodos comunicarse, validar transacciones y sincronizar los datos de la cadena de bloques es clave para mantener un libro de contabilidad compartido en una red descentralizada.

- Estructuras de datos**: además de la lista de bloques, en la que cada bloque contiene un conjunto de transacciones junto con una referencia al bloque anterior, se necesita una estrategia optimizada y eficaz para almacenar el estado de la red.

- Gobernanza** - si la red está diseñada para funcionar sin permisos, es importante un mecanismo de votación para que siga evolucionando y refleje la voluntad de la comunidad.

- Capacidad de actualización**: es necesario definir claramente cómo actualizar, cómo se aplican las modificaciones y cómo se resuelven los conflictos dentro de la red.

Afortunadamente, no hay necesidad de construir estos componentes de blockchain desde cero, gracias a un excelente marco de código abierto llamado [Substrate](https://docs.polkadot.com/develop/parachains/intro-polkadot-sdk/){target=\_blank}. El propio Tanssi está construido con este framework, aprovechando sus completas implementaciones base, modularidad y flexibilidad para lograr un alto nivel de personalización.

## Substrate Framework {: #substrate-framework}

Substrate es un marco extremadamente eficaz, flexible, modular y altamente personalizable para la creación de cadenas de bloques. Este marco es la base y el motor que impulsa muchos proyectos en todo el ecosistema Web3, incluyendo la propia red Tanssi y las redes desplegadas a través de Tanssi.

Muchas de sus grandes características, como el rendimiento, la facilidad de uso y la modularidad, son el resultado del lenguaje de programación elegido para su desarrollo. Aquí es donde brilla el [Lenguaje de programación Rust](#rust-programming-language): Es rápido, portable, y proporciona un modelo maravilloso para manejar la memoria, entre otras razones detalladas en la [siguiente sección](#rust-programming-language).

Cuando se desarrolla una red, Substrate representa una gran ventaja al proporcionar un conjunto de implementaciones listas para usar de los principales bloques de construcción que necesita un proyecto:

- **Algoritmos de consenso** - hay múltiples motores de consenso incorporados, como Aura (Prueba de Autoridad), Babe (Prueba de Estaca), y Grandpa (finalidad de bloque), pero debido al alto grado de personalización que Substrate ofrece, los equipos siempre pueden optar por desarrollar su consenso específico para adaptarse a las necesidades del caso de uso, como hizo el equipo Moonbeam con el [Nimbus Parachain Consensus Framework](https://docs.moonbeam.network/learn/features/consensus){target=\_blank}

- **Módulos de ejecución** - muchos módulos incorporados (explicados en detalle en la sección [modules](/learn/framework/modules/){target=\_blank}) pueden ser seleccionados y configurados en tu red, como cuentas, balances, staking, gobernanza, identidad, y más.

- **Redes** - protocolos y bibliotecas incorporados para establecer conexiones, propagar transacciones y bloques, sincronizar el estado de la cadena de bloques y gestionar las interacciones de la red

- Almacenamiento** - mecanismos de almacenamiento integrados para almacenar y recuperar datos de forma eficiente.

- Cola de transacciones**: sistema de cola de transacciones integrado que gestiona la validación, priorización e inclusión de transacciones en bloques, garantizando la coherencia e integridad del estado de la red.

- APIs RPC** - Substrate proporciona APIs de Llamada a Procedimiento Remoto (RPC) que permiten a las aplicaciones externas interactuar con la red consultando datos de la cadena de bloques, enviando transacciones y accediendo a varias funcionalidades expuestas por el tiempo de ejecución.

Todas las funciones que ofrece Substrate pueden utilizarse tal cual, ampliarse, personalizarse o sustituirse para satisfacer los requisitos específicos del caso de uso de la red.

Substrate agiliza y acelera el proceso de desarrollo de nuevas redes. Cuando se utiliza junto con Tanssi, que ayuda a gestionar la infraestructura y supervisar el despliegue, la tarea de lanzar una nueva red se simplifica considerablemente.

## Lenguaje de programación Rust {: #rust-programming-language}

[Rust](https://www.rust-lang.org){target=\_blank} es un lenguaje de programación que tiene características únicas que lo han convertido en el lenguaje más querido por séptimo año consecutivo, según [la encuesta anual de desarrolladores de Stack Overflow](https://survey.stackoverflow.co/2022#section-most-loved-dreaded-and-wanted-programming-scripting-and-markup-languages){target=blank}.

Además de ofrecer una gran experiencia a los desarrolladores, Rust destaca en muchas áreas:

- Seguridad de la memoria** - El compilador de Rust aplica estrictas comprobaciones en tiempo de compilación para evitar errores de programación comunes, como desviaciones de puntero nulo, desbordamientos de búfer y carreras de datos. Además, la memoria se gestiona mediante un novedoso sistema de propiedad (comprobado por el compilador), que elimina la necesidad de un recolector de basura.

- Rendimiento** - Rust consigue un rendimiento comparable al de C y C++ proporcionando un control de bajo nivel sobre los recursos del sistema y minimizando la sobrecarga en tiempo de ejecución. Tiene un principio de abstracción de coste cero, similar a "lo que no usas, no lo pagas" de C++, lo que significa que las abstracciones no tienen sobrecarga adicional.

- Concurrencia** - Rust tiene características incorporadas que hacen fácil escribir código concurrente y paralelo sin introducir carreras de datos. Proporciona hilos ligeros (tareas) y un potente modelo de propiedad que garantiza la compartición segura de datos entre hilos.

- Abstracciones expresivas y seguras** - Rust ofrece un rico conjunto de características del lenguaje moderno, como la concordancia de patrones, los tipos de datos algebraicos, los cierres y la inferencia de tipos, lo que permite a los desarrolladores escribir y leer código expresivo y conciso. El compilador de Rust aplica el sistema de tipos fuertes, evitando muchos errores de ejecución en tiempo de compilación.

- Compatibilidad multiplataforma** - Rust está diseñado para funcionar bien en una gran variedad de plataformas y arquitecturas. Es compatible con los principales sistemas operativos como Windows, macOS y Linux, así como con sistemas embebidos y WebAssembly. Esta versatilidad permite a los desarrolladores escribir código que puede desplegarse en diferentes entornos.

- Ecosistema en crecimiento** - Rust tiene un ecosistema en rápido crecimiento con una comunidad vibrante y una rica colección de bibliotecas y herramientas. El gestor de paquetes oficial, Cargo, simplifica la gestión de dependencias, la compilación y las pruebas.

- Interoperabilidad** - Rust ofrece una interoperabilidad sin fisuras con las bases de código existentes escritas en C y C++. Cuenta con una interfaz de funciones externas (FFI) que permite al código Rust interactuar con código escrito en otros lenguajes, lo que permite a los desarrolladores introducir gradualmente Rust en proyectos existentes, como el núcleo de Linux.
