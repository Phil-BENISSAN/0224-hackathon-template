import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import os

app = FastAPI()

# -------------------------------------------------   CONFIGURATION CORS   ------------------------------------------------------

origins = [
    "http://localhost:8080",
    # Vous pouvez ajouter d'autres origines si nécessaire
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------  INSERER VOTRE CODE ICI -----------------

@app.get('/')
def fn_fast_api():

    try:
        # Utiliser un chemin absolu pour games.csv
        #csv_path = os.path.join(os.getcwd(), 'games.csv')
        csv_path = 'app/game.csv'
        print(f"Trying to read CSV file from: {csv_path}")
        df = pd.read_csv(csv_path)
        return {'key': 'values', 'data': df.head().to_dict()}
    except Exception as e:
        return {'error': str(e)}


# ---------------- FIN DE TON CODE ----------------


#_______________________________________________________________________________________________________________________


if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='0.0.0.0', reload=True)