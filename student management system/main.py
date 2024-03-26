from fastapi import FastAPI
import random
app = FastAPI()

@app.get("/")

def routeFunction():
    print("route functin is call")
    return("route function is called:") 


# @app.get("v1/getuser")
    
# def handleGetRouteRequest():
#     print("handleGetRouteRequest is called:")
#     return("jandleGetRouteRequest is called:")
