## Brain Tumor Classification End to End Project
clone the repository.
create conda env if not created and activate conda environment by using "conda activate '----path to env---'". in my case the path is path to brain_env
install requirements by using pip install -r requirements.txt
go to the app folder in terminal where fast api code is located run the fast api server by using "uvicorn app:app --reload", here app is folder and app is file name.
after running the server go to local host address http://127.0.0.1:8000/docs. you can see fast api ui page , you can upload image see the response.
if you want to acess the front end page go to http://127.0.0.1:8000/static/index.html. you can see ui where you can upload image and classify it.
