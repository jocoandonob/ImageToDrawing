# Image to Drawing Converter

A Streamlit application that converts images into artistic drawings using computer vision techniques.

## Docker Instructions

### Prerequisites
- Docker installed on your system
- Docker Hub account (for pushing images)

### Building the Docker Image

1. Build the image locally:
```bash
docker build -t your-dockerhub-username/image-to-drawing:latest .
```

### Pushing to Docker Hub

1. Login to Docker Hub:
```bash
docker login
```

2. Push the image to Docker Hub:
```bash
docker push your-dockerhub-username/image-to-drawing:latest
```

### Running the Container

1. Pull the image (if running on a different machine):
```bash
docker pull your-dockerhub-username/image-to-drawing:latest
```

2. Run the container:
```bash
docker run -p 5000:5000 your-dockerhub-username/image-to-drawing:latest
```

The application will be available at `http://localhost:5000`

### Additional Docker Commands

- View running containers:
```bash
docker ps
```

- Stop the container:
```bash
docker stop <container_id>
```

- Remove the container:
```bash
docker rm <container_id>
```

- Remove the image:
```bash
docker rmi your-dockerhub-username/image-to-drawing:latest
```

## Features
- Convert images to pencil sketches
- Convert images to pen sketches
- Download converted images
- User-friendly web interface

## Requirements
- Python 3.10.11
- OpenCV
- Streamlit
- NumPy
- Pillow
- Requests

All dependencies are automatically installed in the Docker container. 