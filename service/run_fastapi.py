import uvicorn

from service.core.app import app

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=4242, log_level="info")