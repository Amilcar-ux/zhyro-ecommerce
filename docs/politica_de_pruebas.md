# Política de Pruebas — ZHYRO (Nivel 3 TMMi)

Documento rector del proceso de pruebas. Versión 1.0 — aplicable a todos los módulos.

- **P1.** Toda funcionalidad nueva o modificada debe contar con casos de prueba documentados antes de su integración a la rama principal del repositorio.
- **P2.** Ningún cambio se integra a `main` sin revisión entre pares (Pull Request aprobado) y ejecución exitosa de las pruebas de integración continua.
- **P3.** Todos los módulos utilizan las mismas plantillas institucionales de plan de pruebas, caso de prueba y reporte de defectos.
- **P4.** Las pruebas se integran desde la fase de diseño: cada RF/RNF/RU/RS debe ser trazable a por lo menos un caso de prueba (ver `matriz_trazabilidad.md`).
- **P5.** Cobertura mínima por módulo: **75%** (verificada automáticamente por CI con `--cov-fail-under=75`). Cumplimiento del plan de pruebas por sprint: **≥ 85%**.
- **P6.** Todo defecto se registra en GitHub Issues con la plantilla institucional, se clasifica por severidad y módulo, y se cierra solo tras verificación del Analista QA.

## Roles
| Rol | Responsable |
|---|---|
| Líder de Pruebas | Jean Carlos Calderón |
| Analista QA | Denni Medina |
| Revisores (peer review) | Alex Hernandez / Amilcar Quispe |
| Product Owner | Jeamir Milla |

## Flujo de ramas
`main` (protegida) ← `develop` ← `feature/*` y `fix/*`

Mensajes de commit: `tipo(módulo): descripción` — tipos: `feat`, `fix`, `test`, `docs`, `refactor`.
