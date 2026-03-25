# 📦 Repo Factory (Create & Delete)

Automatiza la **creación y eliminación de repositorios** en GitHub a partir de un archivo `repos.csv`.

---

## 🚀 Workflows

### 1. Create Repos
Crea repositorios desde templates definidos en el CSV.

### 2. Delete Repos
Elimina repositorios generados (con validación y modo seguro `dry_run`).

---

## 📄 Archivo de entrada

`repos.csv`

```csv
mxapm,name,description,type,template_source,template_docs
```

### Campos

- `mxapm`: Identificador
- `name`: Nombre base
- `description`: Descripción (opcional)
- `type`: `source`, `documentation`, `source+documentation`
- `template_source`: Template para source
- `template_docs`: Template para documentation

---

## 🧪 Ejemplo

```csv
mxapm0004521,payments-gateway,Gateway pagos,source+documentation,template1-source,template2-documentation
```

---

## 🏗️ Naming

- `source` → `{mxapm}-source-{name}`
- `documentation` → `{mxapm}-documentation-{name}`

---

## ▶️ Uso

### Crear repos
1. Ir a **Actions**
2. Ejecutar: `Repo Factory`
3. Run workflow

---

### Eliminar repos

1. Ir a **Actions**
2. Ejecutar: `Repo Factory - Delete Repos`

#### 🔍 Dry Run (recomendado)
confirm = DELETE  
dry_run = true  

#### 🚨 Eliminación real
confirm = DELETE  
dry_run = false  

---

## 🔐 Requisitos

- Secret: `ADMIN_TOKEN`
- Permisos:
  - `repo`
  - `admin:org`

---

## 🛡️ Seguridad

- Confirmación obligatoria (`DELETE`)
- `dry_run` por defecto
- Validación de existencia
- Protección por prefijo (`mxapm`)

---

## 🧠 Notas

- Soporta `source+documentation`
- No duplica repos existentes
- CSV compatible con Excel

---

## 📁 Estructura

```
.github/workflows/
  repo-factory.yml
  repo-delete.yml
scripts/
  build_matrix.py
repos.csv
```


## 📁 Al cambio de organizacion

```
cambiar ADMIN_TOKEN
cambiar OWNER: testorg202686
```

---

