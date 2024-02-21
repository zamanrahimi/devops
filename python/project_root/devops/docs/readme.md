<!-- build process -->
step1: 
docker build -t python_app:v1.1 .
in my case run bellow commend: 
<!-- run from project_root to access  devops/docker/Dockerfile -->
docker build -t python_app:v1.1 -f devops/docker/Dockerfile .

ste 2: 
docker login

step 3: 
tag the image (option)
docker tag python_app:v1.1 zamanrahimi1368/python_app:v1.1

step 4: 
push into docker hub 
docker push zamanrahimi1368/python_app:v1.1


step 5: 
to check 
docker rmi image_id 
docker pull zamanrahimi1368/python_app:v1.1



<!-- deploy process -->

step 1:

kubectl apply -f devops/kubernetes/deployment.yaml
kubectl apply -f devops/kubernetes/service.yaml

step 2:
minikube ip