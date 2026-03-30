# RGBFruitClassifier_MLP_ESP32
Clasificador de frutas en tiempo real usando un sensor RGB (TCS34725), Arduino Nano ESP32 y una Red Neuronal Multicapa (MLP) en Python. | Real-time fruit classifier using an RGB sensor (TCS34725), Arduino Nano ESP32, and a Multilayer Perceptron (MLP) Neural Network in Python.

# Clasificador de Frutas y Verduras con Redes Neuronales y Sensor RGB

Este proyecto implementa un sistema de clasificación automática de objetos a partir de su lectura espectral del color capturado en el espacio RGB. La solución integra un pipeline completo de hardware y software capaz de adquirir, procesar y clasificar datos en tiempo real mediante un modelo de Red Neuronal Perceptrón Multicapa (MLP).

---

## Arquitectura de Hardware e Instrumentación

El subsistema de adquisición y actuación física fue diseñado bajo una arquitectura de sistema embebido, priorizando la fidelidad en la obtención de datos físicos para su posterior procesamiento analítico.

### Componentes del Sistema
* **Microcontrolador:** Arduino Nano ESP32 (Modelo ABX00083). Seleccionado por su capacidad de procesamiento superior y arquitectura nativa de 3.3V, ideal para manejar comunicación serial de alta velocidad (115200 baudios) sin latencia en la transmisión de datos.
* **Sensor Óptico de Color:** TCS34725.Dispositivo I2C provisto de un filtro de bloqueo IR incorporado, esencial para minimizar la interferencia de la luz ambiental no visible durante la captura de muestras.
* **Interfaz de Monitoreo:** Display OLED SSD1306 (128x64 píxeles). Proporciona telemetría y retroalimentación del estado de inferencia en tiempo real de forma autónoma.
* **Actuador Visual:** LED RGB de Ánodo Común.
* **Electrónica Base:** Protoboard de 830 puntos, cableado estandarizado calibre 22 y cuatro resistencias limitadoras de corriente de 100Ω.

### Ensamblaje Físico

![Ensamblaje del Sistema Embebido](img/circuito.png)

El circuito fue estructurado para mantener una distribución óptima de las conexiones I2C y señales PWM. Adicionalmente, el transductor óptico fue aislado mediante una barrera física opaca para limitar la incidencia de luz ambiental aleatoria, asegurando condiciones de medición controladas y estables.
