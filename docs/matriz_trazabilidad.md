# Matriz de Trazabilidad — Requerimiento → Caso de Prueba → Evidencia

| Requerimiento | Descripción | Casos de prueba | Archivo de pruebas | Evidencia |
|---|---|---|---|---|
| RF1 | Catálogo con precios y descripciones | CP-ZHYRO-001 a 008 | `tests/test_catalogo.py` | PR #12 |
| RF2 | Registro e inicio de sesión con bloqueo | CP-ZHYRO-020 a 027 | `tests/test_usuarios.py` | PR #08 |
| RF3 | Carrito de compras | CP-ZHYRO-010 a 018 | `tests/test_carrito.py` | PR #15 |
| RF4 | Pago con comprobante digital | CP-ZHYRO-030 a 036 | `tests/test_carrito.py` | PR #22 |
| RF5/RF6 | Gestión administrativa e inventario | CP-ZHYRO-040 a 045 | `tests/test_admin.py` | PR #27 |
| RU1 | Filtros por talla, color y precio | CP-ZHYRO-006 a 008 | `tests/test_catalogo.py` | PR #18 |
| RS (envíos) | Costos y fechas de entrega por provincia | CP-ZHYRO-060 a 065 | `tests/test_envios.py` | PR #25 |
| RNF2 | Tiempo de carga ≤ 3 s | CP-ZHYRO-050 a 052 | Job de rendimiento en CI | Workflow |
