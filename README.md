# CV Extractor

## Installation

### Prérequis
- Python 3.11
- Docker & Docker Compose (pour le lancement via Docker)

---

## Backend

### Installation
```bash
cd backend
pip install -r requirements.txt
```

### Lancement (local)
```bash
cd backend
uvicorn main:app --reload
```

Le backend est accessible à : http://localhost:8000  
Documentation API : http://localhost:8000/docs

---

## Frontend

### Installation
```bash
cd frontend
```

Après `cd frontend`, suivez ces étapes :

1. Créer et activer un environnement virtuel 

- macOS / Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
```

- Windows (PowerShell)
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```



2. Installer les dépendances
```bash
pip install -r requirements.txt
```

3. Lancer l'application (Streamlit)
```bash
streamlit run app.py
```




## Lancement avec Docker

```bash
cd docker
docker-compose up --build
```

Services disponibles :
- Backend : http://localhost:8000/docs
- Frontend : http://localhost:8501

---

## Exemples d’API

Endpoint :
```
POST /api/v1/upload-cv
```

Entrée :
- Fichier CV au format PDF ou DOCX
- Envoi via form-data avec la clé `file`

Sortie (JSON) exemple :
```json
{
    "first_name": "hajar",
    "last_name": "skalli",
    "email": "houssainiskallihajar99@gmail.com",
    "phone": "+336xxxxxxx",
    "degree": "ingenieur informatique"
}
```
