from fastapi import FastAPI
from fastapi.responses import JSONResponse
import os
from typing import List, Dict, Any

app = FastAPI(
    title="FastAPI Test Server",
    description="A simple FastAPI application for testing purposes",
    version="1.0.0"
)

@app.get("/")
async def root():
    """Root endpoint that returns a welcome message"""
    return {"message": "Hello World! FastAPI Test Server is running."}

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "message": "FastAPI server is running properly"}

@app.get("/directory")
async def get_directory(path: str = "."):
    """
    Get directory contents for the specified path
    
    Args:
        path (str): Directory path to list (defaults to current directory)
    
    Returns:
        Dict containing directory information and contents
    """
    try:
        # Ensure the path exists and is a directory
        if not os.path.exists(path):
            return JSONResponse(
                status_code=404,
                content={"error": f"Path '{path}' does not exist"}
            )
        
        if not os.path.isdir(path):
            return JSONResponse(
                status_code=400,
                content={"error": f"Path '{path}' is not a directory"}
            )
        
        # Get directory contents
        contents = []
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            item_info = {
                "name": item,
                "type": "directory" if os.path.isdir(item_path) else "file",
                "size": os.path.getsize(item_path) if os.path.isfile(item_path) else None
            }
            contents.append(item_info)
        
        # Sort contents: directories first, then files, both alphabetically
        contents.sort(key=lambda x: (x["type"] == "file", x["name"].lower()))
        
        return {
            "path": os.path.abspath(path),
            "total_items": len(contents),
            "contents": contents
        }
    
    except PermissionError:
        return JSONResponse(
            status_code=403,
            content={"error": f"Permission denied to access '{path}'"}
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": f"An error occurred: {str(e)}"}
        )

@app.get("/directory/{directory_path:path}")
async def get_directory_by_path(directory_path: str):
    """
    Get directory contents for a specific path via URL parameter
    
    Args:
        directory_path (str): Directory path to list
    
    Returns:
        Dict containing directory information and contents
    """
    return await get_directory(directory_path)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)