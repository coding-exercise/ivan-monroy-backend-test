from fastapi import FastAPI, Body, HTTPException

from utils import vocabulary_list, build_statistics_dictionary

app = FastAPI()


@app.post('/parse', status_code=200)
@app.post('/parse/', status_code=200)
async def parse(text: str = Body(..., embed=True)):
    try:
        text_split = text.split()
        a = build_statistics_dictionary(text_split)
        b = {'vocabulary_list': vocabulary_list(text_split)}
        return {**a, **b}
    except:
        raise HTTPException(status_code=400)
