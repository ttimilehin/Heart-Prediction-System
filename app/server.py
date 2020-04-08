import asyncio
import uvicorn
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse, JSONResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
import aiohttp
import aiofiles
from pathlib import Path
import sys
from parseForm import parseData

export_file_url = 'https://drive.google.com/uc?export=download&id=1ax8hrUEcW9ZJ_yFfHOqt_XTAK3j7Js2Y'

export_file_name = 'lr.pkl'

path = Path(__file__).parent

templates = Jinja2Templates(directory = 'templates')

app = Starlette(debug = True)
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_headers=['X-Requested-With', 'Content-Type'])
app.mount('/static', StaticFiles(directory='static'), name = 'static')


async def setup_learner():
    try: 
        learn = pickle.load(open(export_file_name, 'rb'))

        return learn
    except RuntimeError as e:
        if len(e.args) > 0 and 'CPU-only machine' in e.args[0]:
            print(e)
            message = "\n\nThis model was trained with logistic regression"
        else: 
            raise


loop = asyncio.get_event_loop()
tasks = [asyncio.ensure_future(setup_learner())]
learn = loop.run_until_complete(asyncio.gather(*tasks))[0]
loop.close()
        
@app.route('/')
async def homepage(request):
    return templates.TemplateResponse('index.html', {'request': request})

@app.route('/check', methods=['POST'])
async def check(request):

    if request.method == "POST":
        form = await request.form()
        data = np.array(parseData(form), dtype=np.float32).reshape(1,-1)

        prediction = learn.predict(data)
        print(prediction)
    

    
    return templates.TemplateResponse('result.html', {'request': request, 'prediction':prediction})

# @app.route('/analyze', methods=['POST'])
# async def analyze(request):
#     data = await request.form()
#     print("This is the data : ", data)
#     #img_bytes = await (img_data['file'].read())
#     #img = open_image(BytesIO(img_bytes))
#     prediction = loaded_model.score(data)
#     return JSONResponse({'result': str(prediction)})


if __name__ == '__main__':
    if 'serve' in sys.argv:
        uvicorn.run(app=app, host='localhost', port=5000, log_level="info")
