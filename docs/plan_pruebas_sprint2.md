# Plan de Pruebas — PL-ZHYRO-S02

| Campo | Detalle |
|---|---|
| **Código** | PL-ZHYRO-S02 |
| **Proyecto / Módulo** | ZHYRO — Catálogo, Carrito, Pago |
| **Sprint** | Sprint 2 |
| **Objetivo** | Verificar el flujo completo de compra (catálogo, carrito, comprobantes de pago) según RF1, RF3, RF4 y RNF2. |
| **Alcance** | Incluye pruebas funcionales de catálogo, carrito y pago; y tiempo de carga ≤ 3 s. Excluye envíos y panel administrativo. |
| **Estrategia** | Pruebas funcionales manuales guiadas por casos; pruebas unitarias automatizadas en cada PR (GitHub Actions); rendimiento sobre consultas del catálogo. |
| **Criterios de entrada** | Historias P1, P3, P4, P5 en `develop`; entorno con MySQL 8.0 y datos de prueba. |
| **Criterios de salida** | ≥ 85% de casos ejecutados; 0 defectos críticos abiertos; cobertura ≥ 75%. |
| **Riesgos** | Retraso en la carga de comprobantes; datos de prueba insuficientes para tallas/colores. |
| **Responsables** | Líder: Jean Carlos Calderón — QA: Denni Medina |

## Casos planificados (32)
- CP-ZHYRO-001 a 008 — Catálogo (`tests/test_catalogo.py`)
- CP-ZHYRO-010 a 018 — Carrito (`tests/test_carrito.py`)
- CP-ZHYRO-030 a 036 — Pago y estados de pedido (`tests/test_carrito.py`)
- CP-ZHYRO-050 a 052 — Rendimiento (transversal)
