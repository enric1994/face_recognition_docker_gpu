GPU-Ready implementation of the famous Python package: face_recognition

Stop losing time installing CUDA or Dlib! Docker will do it for you

## Requirements
1. GPU supporting CUDA 8 ( driver version >= 367.4x)
2. [Docker and Compose](https://gist.github.com/enric1994/3b5c20ddb2b4033c4498b92a71d909da)
3. [Nvidia-Docker](https://github.com/NVIDIA/nvidia-docker)

## Example
```
git clone https://github.com/enric1994/face_recognition_docker_gpu.git
cd face_recognition_docker_gpu/docker
docker-compose up
```

## Reference
Face recognition: https://github.com/ageitgey/face_recognition
Dlib: https://github.com/davisking/dlib
