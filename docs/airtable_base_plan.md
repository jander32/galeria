# Base de Airtable para Gestión Artística Integrada

## Objetivo general
Diseñar una base modular en Airtable que centralice la información de artistas, clientes, proyectos y campañas digitales, permitiendo automatizar envíos de correo con IACGAT GPT, coordinar la creación de contenido para redes sociales y gestionar agentes GPT entrenados para distintos procesos comerciales.

## Estructura propuesta de la base
La base se organiza en seis bloques funcionales. Cada bloque incluye tablas vinculadas entre sí mediante relaciones *linked record* y campos de referencia.

### 1. Gestión de relaciones (CRM)
| Tabla | Propósito | Campos clave |
|-------|-----------|--------------|
| **Empresas/Clientes** | Registrar los clientes institucionales y marcas con las que se trabaja. | Nombre, Tipo de cliente (galería, marca, productora), Estado de relación (Lead, Negociación, Activo), Fuente de contacto, Segmento, Responsable interno, Información de contacto (email, teléfono), Dirección, Notas, Documentos relacionados (adjuntos). |
| **Contactos** | Personas asociadas a empresas o clientes particulares. | Nombre, Apellidos, Rol, Email, Teléfono, Empresa (relación con *Empresas/Clientes*), Preferencia de contacto, Fecha de última interacción, Próxima acción (link a *Tareas*), Consentimiento comunicaciones, Notas. |
| **Artistas** | Perfil completo de cada artista representado o colaborador. | Nombre artístico, Nombre legal, Disciplina, Estado (Activo, En evaluación, Historial), Biografía, Portfolio (URL/adjuntos), Equipo de soporte, Representante interno, Tarifas estándar, Redes sociales (link), KPI artísticos (ventas, reproducciones, seguidores), Documentación legal (adjuntos). |
| **Oportunidades/Proyectos** | Seguimiento de propuestas comerciales, exposiciones o colaboraciones. | Nombre del proyecto, Cliente/Empresa, Artista principal, Tipo de proyecto, Etapa (Prospección, Pitch, Negociación, Contrato, Ejecutando, Cerrado ganado/perdido), Fecha de inicio prevista, Fecha de cierre, Valor estimado, Probabilidad de cierre, Productos involucrados (link a *Inventario/Obras*), Notas, Documentos, Último movimiento, Próximos pasos. |
| **Inventario/Obras** | Inventario de obras disponibles, en préstamo o vendidas. | Título, Artista, Tipo (obra física, digital, NFT, merchandising), Estado logístico (Disponible, Reservada, Vendida, En traslado), Ubicación física, Dimensiones, Precio, Historial de exposición, Archivos multimedia, Documentos de autenticidad. |

### 2. Operaciones y tareas internas
| Tabla | Propósito | Campos clave |
|-------|-----------|--------------|
| **Tareas** | Planificación detallada de actividades internas. | Nombre, Tipo (Comercial, Producción, Contenido, Logística, Administración), Prioridad, Estado (Por hacer, En progreso, Completada, Bloqueada), Responsable, Fecha de vencimiento, Proyecto/Oportunidad asociada, Artista relacionado, Resultado, Comentarios. |
| **Reuniones/Visitas** | Registro de reuniones con clientes o artistas. | Título, Fecha y hora, Participantes internos (link a *Usuarios internos*), Contactos externos (link a *Contactos*), Objetivo, Notas, Documentos generados, Acciones derivadas (link a *Tareas*). |
| **Usuarios internos** | Equipo de la agencia/gestoría. | Nombre, Rol, Email, Teléfono, Disponibilidad, Especialidades, KPI asignados, Integraciones (cuentas conectadas), Notas. |

### 3. Contenido y campañas
| Tabla | Propósito | Campos clave |
|-------|-----------|--------------|
| **Campañas de Marketing** | Seguimiento de campañas multicanal. | Nombre, Objetivo (Awareness, Lanzamiento, Venta, Captación leads), Cliente/Proyecto, Artistas implicados, Presupuesto, Fecha de inicio y fin, Canales (relación con *Canales Digitales*), KPI objetivo (alcance, engagement, ventas), Estado, Notas estratégicas. |
| **Piezas de Contenido** | Calendario detallado de piezas creadas y publicadas. | Título, Tipo (Post, Reel, Newsletter, Blog, Anuncio), Estado (Idea, En redacción, En revisión, Programada, Publicada), Fecha de publicación, Campaña asociada, Plataforma, Enlace al copy (campo Long Text), Assets (adjuntos), Responsable creativo, Aprobadopor, KPI resultados (likes, comentarios, CTR). |
| **Canales Digitales** | Cuentas de redes sociales y plataformas de distribución. | Plataforma (Instagram, TikTok, YouTube, Spotify, Email marketing, Web), Usuario/URL, Propietario (Cliente/Artista), Credenciales gestionadas (campo Single Select: Interno, Cliente, Agencia partner), Estado de conexión (Activo, Requiere verificación), Integraciones activas (Zapier, Make, API propia). |
| **Plantillas IA** | Biblioteca de prompts y plantillas para IACGAT GPT u otros agentes. | Nombre de plantilla, Tipo (Email, Social media, Pitch, Reporte), Descripción, Variables requeridas (campos formula o texto), Prompt maestro (Long text), Ejemplo de salida, Agente GPT asociado, Estado de revisión. |

### 4. Automatización de comunicaciones
| Tabla | Propósito | Campos clave |
|-------|-----------|--------------|
| **Secuencias de Email** | Diseñar cadencias de correo automatizado. | Nombre, Objetivo (Seguimiento lead, Confirmación evento, Lanzamiento obra), Público objetivo (link a *Segmentos*), Agente GPT responsable, Número de pasos, Plantillas IA vinculadas, Métricas (tasa apertura, clics, respuestas). |
| **Segmentos** | Agrupaciones dinámicas de contactos. | Nombre del segmento, Criterios (fórmulas/condiciones), Lista de contactos (relación), Campañas activas asociadas, Notas. |
| **Historial de Emails** | Registro de emails enviados manual o automáticamente. | Fecha envío, Contacto, Secuencia/Plantilla utilizada, Asunto, Canal (Outlook, Gmail, Sendgrid), Resultado (Entregado, Abierto, Respondido, Rebotado), Responsable interno, Notas. |

### 5. Automatización con agentes GPT
| Tabla | Propósito | Campos clave |
|-------|-----------|--------------|
| **Agentes GPT** | Control de agentes especializados entrenados para el cliente. | Nombre del agente, Tipo (Atención lead, Copywriting, Análisis datos), Modelo base, Prompt de sistema, Dataset de entrenamiento (adjuntos/links), Propietario interno, Flujos donde interviene (link a *Flujos Automatizados*), Estado (En pruebas, Activo, Inactivo), Métricas de desempeño (CSAT, tiempo respuesta). |
| **Flujos Automatizados** | Documentar flujos de automatización que mezclan Airtable + IA + redes. | Nombre, Objetivo, Descripción paso a paso, Disparadores (ej. nuevo lead, nueva obra), Herramientas usadas (Make, Zapier, Scripts Airtable), Agentes involucrados, Variables de entrada y salida, Estado (Diseño, Implementación, Activo), KPIs monitorizados. |

### 6. Analítica y reporting
| Tabla | Propósito | Campos clave |
|-------|-----------|--------------|
| **Dashboards/KPIs** | Configuración de paneles y métricas clave. | Nombre del dashboard, Stakeholder objetivo (CEO, Representante, Marketing), KPIs incluidos (ventas, engagement, ROI campañas), Fuentes de datos (Airtable, redes sociales, ecommerce), Frecuencia de actualización, Responsable de análisis, Vínculo a visualización (Interfaces Airtable, Data Studio). |
| **Logs de Integraciones** | Auditoría de automatizaciones. | Fecha/hora, Flujo automatizado, Resultado (Éxito, Error), Mensaje de error, Acción aplicada, Responsable de revisión, Próximos pasos. |

## Formularios y vistas recomendadas
- **Formularios de captación:** Formularios públicos para registrar leads o artistas interesados. Se conectan a la tabla *Contactos* o *Artistas* con campos obligatorios (nombre, email, propuesta, consentimientos).
- **Vistas Kanban:** Para *Oportunidades/Proyectos* (agrupadas por etapa) y *Tareas* (por estado o responsable).
- **Calendarios:** Calendario editorial desde *Piezas de Contenido* y calendario de eventos para *Reuniones/Visitas*.
- **Vistas filtradas por cliente/artista:** Facilitan preparar reuniones mostrando solo la información relevante antes de la visita.
- **Interfaces personalizadas:** Una interfaz para dirección (KPIs y pipeline), otra para marketing (campañas, contenido, agentes GPT) y otra para operaciones (tareas, logística de obras).

## Campos auxiliares y automatizaciones sugeridas
1. **Campos cálculo automático**
   - Fórmulas para calcular el valor ponderado de proyectos (`Valor estimado * Probabilidad`).
   - Fórmulas de fecha relativa (días hasta vencimiento, recordatorios).
   - `Rollup` para sumar ventas por artista o cliente.
2. **Automatizaciones nativas de Airtable**
   - Notificación por Slack/Email cuando una oportunidad cambia a etapa "Negociación" o "Contrato".
   - Creación automática de tareas al registrar una nueva reunión.
   - Generación de documento (con Page Designer o Document automation) al ganar un proyecto.
   - Envío de correo personalizado con plantilla IA al mover una pieza de contenido a "Programada".
3. **Escenarios Make/Zapier**
   - Integración con plataformas de mailing (Mailerlite, Sendgrid) para sincronizar métricas en *Historial de Emails*.
   - Trigger cuando se publica contenido en redes para registrar el enlace y métricas iniciales en *Piezas de Contenido*.
   - Entrenamiento periódico de agentes GPT con nuevas piezas aprobadas (actualización de dataset).

## Datos a recopilar en la visita al cliente
Antes de construir la base definitiva, preparar un cuestionario para obtener:
- **Mapa de procesos actuales**: Cómo gestionan artistas, campañas, ventas y seguimiento de clientes.
- **Herramientas usadas**: CRMs actuales, email marketing, gestores de redes, almacenamiento de archivos.
- **Volúmenes y frecuencia**: Número de artistas activos, campañas mensuales, envíos de correo, publicaciones por canal.
- **Equipo y roles**: Quiénes usarán la base, permisos necesarios y procesos de aprobación.
- **Necesidades legales y de compliance**: Manejo de contratos, consentimientos de uso de imagen, cláusulas específicas.
- **Integraciones prioritarias**: Plataformas clave (Shopify, Ticketing, plataformas streaming, ERP).
- **KPIs críticos**: Métricas que necesitan visualizar en dashboards (ventas, engagement, leads cerrados).
- **Casos de uso para agentes GPT**: Tipos de interacciones que esperan automatizar (respuestas a leads, propuestas comerciales, gestión de soporte).

## Plan de implementación por fases
1. **Descubrimiento y diseño detallado** (Semana 1)
   - Validar con el cliente el modelo de datos propuesto.
   - Ajustar nomenclatura de campos y vistas según su lenguaje interno.
2. **Configuración inicial de la base** (Semana 2)
   - Crear tablas, relaciones y campos calculados.
   - Configurar vistas principales y formularios de entrada.
   - Cargar datos históricos prioritarios (artistas, clientes, proyectos activos).
3. **Automatizaciones y agentes** (Semanas 3-4)
   - Conectar integraciones de email, redes y almacenamiento.
   - Diseñar prompts y plantillas en *Plantillas IA*.
   - Configurar agentes GPT y flujos automatizados.
4. **Pruebas, formación y entrega** (Semana 5)
   - Pruebas funcionales con casos reales.
   - Capacitación del equipo del cliente.
   - Documentar procesos y crear manual de uso.

## Próximos pasos inmediatos
- Preparar cuestionario y agenda de la visita al cliente.
- Crear mockups o interfaz de Airtable (Interfaces Designer) para mostrar durante la reunión.
- Definir requerimientos técnicos para integrar IACGAT GPT (API keys, endpoints, seguridad).
- Establecer indicadores de éxito para medir el impacto de la implementación.

