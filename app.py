from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    app_env = os.getenv("APP_ENV", "not set")
    db_password = os.getenv("DB_PASSWORD", "not set")
    return f"Hello from App!!!Kubernetes!,also Knoun as k8s"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8095)
#kubectl apply -f pod.yaml
#kubectl get pods
#kubectl describe pod my-nginx
#kubectl get pods -o wide
#minikube ssh -it will login into the minikube cluster  
#curl  <nginx ip-address> 
