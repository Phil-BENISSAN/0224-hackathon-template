import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def fn_fast_api():

# -------  INSERER VOTRE CODE ICI -----------------

    return {'key' : 'values'}


# ---------------- FIN DE TON CODE ----------------
#__________________________________________________

# PAS NECESSAIRE DANS L'IMAGE DOCKER
# if __name__ == '__main__':
#     uvicorn.run(app, port=8000, host='0.0.0.0')