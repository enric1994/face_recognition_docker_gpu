GPU-Ready implementation of the famous Python package: face_recognition

Stop losing time installing CUDA or Dlib! Docker will do it for you

![Hits](https://hitcounter.pythonanywhere.com/count/tag.svg?url=https%3A%2F%2Fgithub.com%2Fenric1994%2Fface%5Frecognition%5Fdocker%5Fgpu)
## Requirements
1. GPU supporting CUDA 8 ( driver version >= 367.4x)
2. [Docker and Compose](https://gist.github.com/enric1994/3b5c20ddb2b4033c4498b92a71d909da)
3. [Nvidia-Docker](https://github.com/NVIDIA/nvidia-docker) (Only for Linux)

Note: If you don't have GPU, ignore step 3 and comment the last line of the docker/docker-compose.yml: `runtime: nvidia`. Performance will be affected

## Example
Detect the faces in the `images` folder
```
git clone https://github.com/enric1994/face_recognition_docker_gpu.git
cd face_recognition_docker_gpu/docker
docker-compose up
```
  **Output:**
```
face_recognition    | [(51, 106, 99, 59), (27, 63, 75, 15)]
face_recognition    | [(109, 176, 191, 94)]
face_recognition    | [(184, 85, 266, 3), (133, 187, 231, 89)]
face_recognition    | [(49, 96, 89, 57)]
```

## References
* Face recognition: https://github.com/ageitgey/face_recognition
* Dlib: https://github.com/davisking/dlib
