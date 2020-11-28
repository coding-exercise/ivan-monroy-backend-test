from fastapi import FastAPI, Body, HTTPException

from utils import vocabulary_list, build_statistics_dictionary

app = FastAPI()


@app.post('/parse', status_code=200)
@app.post('/parse/', status_code=200)
async def parse(text: str = Body(..., embed=True)):
    try:
        text_split = text.split()
        # ☢☢ This needs Python 3.9.0 ☢☢
        return build_statistics_dictionary(text_split) | {'vocabulary_list': vocabulary_list(text_split)}
        # ☢☢ This needs Python 3.9.0 ☢☢
    except:
        raise HTTPException(status_code=400)
