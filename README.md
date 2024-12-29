Análisis de Delitos en Perú (2019-2023)

Este proyecto analiza datos de delitos en Perú entre los años 2019 y 2023, con el objetivo de identificar tendencias, subgéneros de delitos con mayor incidencia y patrones temporales que puedan apoyar la toma de decisiones en políticas de seguridad.

Tabla de Contenidos

Antecedentes
Objetivos
Datos
Metodología
Resultados Clave
Herramientas Utilizadas
Lecciones Aprendidas
Próximos Pasos
Antecedentes

El presente análisis tiene como objetivo principal estudiar los patrones y tendencias de los delitos reportados en Perú durante el período de 2019 a 2023. La seguridad ciudadana se ha convertido en un tema prioritario para la sociedad peruana, afectando tanto la calidad de vida de los ciudadanos como el desarrollo económico y social del país. La delincuencia y los diferentes tipos de delitos reportados representan un desafío constante para las autoridades y requieren de ciertos análisis que permitan comprender su evolución y sus características geográficas y temporales.

Objetivos

Analizar los subgéneros de delitos con mayor incidencia en los últimos cinco años.
Identificar patrones temporales por año en la cantidad de delitos reportados.
Presentar la distribución de delitos en Perú, con un enfoque en los delitos de extorsión y otros subgéneros con alta frecuencia.
Realizar un análisis de frecuencia de palabras en las descripciones de los delitos para identificar términos comunes y tendencias en el lenguaje utilizado.
Datos

Los datos fueron recopilados y procesados a partir de archivos CSV que contienen los registros de delitos por año desde 2019 hasta 2023.

Estructura de los datos:

anio_denuncia: Año en que se registra el delito.
subgenerico: Tipo específico del delito (subgénero).
cantidad: Número de incidentes reportados por subgénero.
des_articulo: Descripción del delito.
Fuentes de datos:

Datos históricos descargados de fuentes públicas en Perú (https://www.datosabiertos.gob.pe/)
Archivos locales procesados y subidos a un repositorio en GitHub.
Metodología

Limpieza de Datos:

Eliminación de valores nulos.
Estandarización de formatos para columnas como anio_denuncia y subgenerico.
Análisis Exploratorio:

Identificación de los subgéneros de delitos más comunes utilizando un percentil de 95%.
Visualización de tendencias anuales para cada tipo de delito.
Análisis Temporal y Geográfico:

Gráficos de barras y líneas para visualizar los delitos más comunes y su comportamiento en el tiempo.
Análisis de distribución geográfica (cuando esté disponible la información).
Análisis de Frecuencia de Palabras:

Limpieza de texto en la columna des_articulo.
Identificación de las palabras más comunes y generación de una nube de palabras para visualizar los términos relevantes en las descripciones de los delitos.
Resultados Clave

Subgéneros con Mayor Incidencia:
Los delitos de Lesiones, Hurto y Delitos de Peligro Común fueron los más comunes en los últimos cinco años.
Patrones Temporales:
Un aumento significativo en ciertos tipos de delitos, especialmente en 2022, destacando la necesidad de enfoques específicos en áreas de alta incidencia.
Distribución por Año y Tipo de Delito:
Delitos de extorsión mostraron una tendencia a la alza, lo cual podría requerir intervenciones específicas en ciertas regiones.
Frecuencia de Palabras:
Se identificaron las palabras más comunes en las descripciones de delitos, lo que proporciona una visión adicional sobre el tipo de delitos reportados.
Herramientas Utilizadas

Python: Para la manipulación de datos, limpieza y visualización.
Pandas: Análisis de datos y estructuras.
Matplotlib y Seaborn: Visualización de los patrones y tendencias de delitos.
WordCloud: Generación de nubes de palabras a partir de las descripciones de delitos.
Git y GitHub: Control de versiones y almacenamiento del proyecto.
Jupyter Notebook: Entorno de desarrollo para ejecutar el análisis paso a paso.
Lecciones Aprendidas

Este análisis permitió observar las limitaciones de los datos cuando se trata de predicciones debido a la variabilidad en la frecuencia de delitos. A futuro, incluir variables adicionales como ubicación geográfica y contexto económico podría enriquecer el análisis.

Próximos Pasos

Profundizar en el Análisis Geográfico: Explorar la distribución de delitos por región.
Incluir Análisis Predictivo: Utilizar modelos predictivos en futuros proyectos donde los datos muestren tendencias más estables.
Mejora de Visualizaciones: Integrar gráficos interactivos para la presentación de resultados.
Este análisis descriptivo se presenta como parte de mi portafolio de proyectos en ciencia de datos. Los hallazgos proporcionan una visión general útil para futuras investigaciones en políticas de seguridad y estudios relacionados con la criminalidad en Perú.
