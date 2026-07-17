# ZHYRO — Plataforma de venta de ropa

Repositorio del proyecto **ZHYRO** para el curso de **Calidad de Software (UTP)**.
Implementa el **Nivel 3 de TMMi (Definido)**: procesos de prueba estandarizados y
documentados, con distribución y control mediante GitHub.

## Estructura

```
zhyro-ecommerce/
├── .github/
│   ├── workflows/ci-pruebas.yml      # Integración continua (pruebas + cobertura)
│   ├── ISSUE_TEMPLATE/               # Plantilla institucional de defectos
│   └── PULL_REQUEST_TEMPLATE.md      # Lista de verificación del revisor
├── docs/                             # Política, plan de pruebas y trazabilidad
├── src/                              # Código fuente por módulos
│   ├── usuarios/    (RF2: autenticación y bloqueo de cuenta)
│   ├── catalogo/    (RF1, RU1: productos y filtros)
│   ├── carrito/     (RF3, RF4: carrito, pedidos y comprobantes)
│   ├── envios/      (costos y fechas por provincia)
│   └── admin/       (RF5: gestión e inventario con alertas)
└── tests/                            # 42 casos de prueba automatizados
```

## Ejecutar las pruebas localmente

```bash
pip install -r requirements.txt
pytest tests/ --cov=src --cov-report=term --cov-fail-under=75
```

Resultado esperado: **42 passed — cobertura total ~97%** (meta institucional: ≥ 75%).

## Proceso de trabajo (Nivel 3 TMMi)

1. Crear rama `feature/rfX-descripcion` desde `develop`.
2. Implementar con sus pruebas. Commits: `tipo(módulo): descripción`.
3. Abrir Pull Request hacia `develop` (la plantilla exige trazabilidad y casos de prueba).
4. El workflow **CI - Pruebas ZHYRO** se ejecuta automáticamente; si la cobertura
   baja del 75%, el PR se bloquea.
5. Un revisor aprueba (peer review) y se realiza el merge.
6. Defectos: registrar Issue con la plantilla `DEF-ZHYRO-XXX`, corregir en rama
   `fix/issue-N-descripcion` y cerrar con `Closes #N` en el commit.

## Documentación de calidad

- [Política de pruebas](docs/politica_de_pruebas.md)
- [Plan de pruebas Sprint 2](docs/plan_pruebas_sprint2.md)
- [Matriz de trazabilidad](docs/matriz_trazabilidad.md)
- Proyecto verificado bajo el proceso Nivel 3 TMMi.
