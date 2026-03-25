# 📦 Repo Factory con GitHub Actions

Este proyecto implementa un **Repo Factory automatizado** usando GitHub Actions que permite crear repositorios a partir de templates basados en un archivo `repos.csv`.

---

## 🚀 ¿Qué hace?

- Lee un archivo `repos.csv`
- Genera repositorios automáticamente en tu organización
- Soporta múltiples tipos:
  - `source`
  - `documentation`
  - `source+documentation`
- Usa **templates distintos por tipo**
- Aplica naming estándar automáticamente

---

## 📄 Estructura del CSV

El archivo `repos.csv` define los repositorios a crear:

```csv
mxapm,name,description,type,template_source,template_docs
```

### 🧩 Campos

| Campo              | Descripción |
|-------------------|------------|
| `mxapm`           | Identificador del sistema/aplicación |
| `name`            | Nombre base del repositorio |
| `description`     | Descripción del repositorio |
| `type`            | Tipo: `source`, `documentation`, `source+documentation` |
| `template_source` | Template para repos tipo source |
| `template_docs`   | Template para repos tipo documentation |

---

## 🧪 Ejemplo

```csv
mxapm,name,description,type,template_source,template_docs
mxapm0004521,payments-gateway,Gateway de pagos,source+documentation,template-source-repo,template-docs-repo
```

---

## 🎯 Resultado esperado

Para el ejemplo anterior se crearán:

```
mxapm0004521-source-payments-gateway
mxapm0004521-documentation-payments-gateway
```

---

## 🏗️ Naming Convention

| Tipo            | Formato |
|-----------------|--------|
| source          | {mxapm}-source-{name} |
| documentation   | {mxapm}-documentation-{name} |

---

## ⚙️ Requisitos

### 1. Templates
Debes tener repositorios marcados como **Template Repository**:

- template-source-repo
- template-docs-repo

Configuración:
- Ir a Settings → General
- Activar: Template repository

---

### 2. Token de acceso

Configura un secret en GitHub:

ADMIN_TOKEN

Permisos requeridos:
- repo
- admin:org (para organizaciones)
- workflow (opcional)

---

## ▶️ Ejecución

1. Ir a GitHub Actions
2. Seleccionar workflow: Repo Factory
3. Click en Run workflow

---

## 🔄 Flujo interno

1. Se lee repos.csv
2. Se transforma a JSON usando jq
3. Se expande source+documentation en múltiples entradas
4. Se ejecuta un job por repositorio (matrix)
5. Se crea el repo usando la API de GitHub

---

## 🛡️ Validaciones incluidas

- CSV no encontrado → falla
- Tipo inválido → error
- Repo ya existe → se omite
- Template no definido → error

---

---

## 💡 Notas

- Los nombres se normalizan automáticamente:
  - minúsculas
  - espacios → -
  - sin caracteres especiales
- Compatible con ejecución masiva (decenas o cientos de repos)

---
