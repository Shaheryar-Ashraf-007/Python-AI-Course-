from fastapi import FastAPI



app = FastAPI()


@app.get("/")
def routeFunction():
    print("routeFunction is called:")
    return("routeFunction is:called")


@app.get("/v1/getUser")

def handleGetRouteRequest():
    print("handle get route request called:")
    return{
        "username":"shery"
    }