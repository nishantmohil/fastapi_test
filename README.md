# FastAPI Test Server

A simple FastAPI application for testing purposes with directory listing functionality.

## Features

- **Root Endpoint** (`/`): Welcome message
- **Health Check** (`/health`): Server health status
- **Directory Listing** (`/directory`): List contents of directories
- **Path-based Directory Listing** (`/directory/{path}`): List contents of specific directory paths

## Setup

### Prerequisites
- Python 3.7+
- pip

### Installation

1. Navigate to the fastapi_test directory:
   ```bash
   cd fastapi_test
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Server

### Option 1: Using uvicorn directly
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Option 2: Using Python
```bash
python main.py
```

The server will start on `http://localhost:8000`

## API Endpoints

### 1. Root Endpoint
- **URL**: `/`
- **Method**: GET
- **Description**: Returns a welcome message
- **Example**: `http://localhost:8000/`

### 2. Health Check
- **URL**: `/health`
- **Method**: GET
- **Description**: Returns server health status
- **Example**: `http://localhost:8000/health`

### 3. Directory Listing (Query Parameter)
- **URL**: `/directory?path={directory_path}`
- **Method**: GET
- **Description**: Lists contents of the specified directory
- **Parameters**: 
  - `path` (optional): Directory path to list (defaults to current directory)
- **Examples**: 
  - `http://localhost:8000/directory` (current directory)
  - `http://localhost:8000/directory?path=/Users/username/Documents`

### 4. Directory Listing (Path Parameter)
- **URL**: `/directory/{directory_path}`
- **Method**: GET
- **Description**: Lists contents of the specified directory via URL path
- **Examples**: 
  - `http://localhost:8000/directory/Users/username/Documents`
  - `http://localhost:8000/directory/var/log`

## Response Format

Directory listing endpoints return JSON with the following structure:

```json
{
  "path": "/absolute/path/to/directory",
  "total_items": 5,
  "contents": [
    {
      "name": "subdirectory",
      "type": "directory",
      "size": null
    },
    {
      "name": "file.txt",
      "type": "file",
      "size": 1024
    }
  ]
}
```
