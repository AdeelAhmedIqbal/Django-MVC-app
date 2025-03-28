# Django MVC Expense Tracker

This is a simple Django-based Expense Tracker web app, built and deployed using Docker and Kubernetes.

## 🧰 Tech Stack

- Python 3.10
- Django Framework
- Docker
- Kubernetes (local cluster)
- Local Docker Registry

---

## 📦 How to Deploy

### 1. Build and Test Django App Locally

Run the app locally to ensure everything works:

```bash
python manage.py runserver
```

---

### 2. Generate `requirements.txt`

```bash
pip freeze > requirements.txt
```

---

### 3. Create a `Dockerfile`

Basic structure:

```dockerfile
# Use the official Python image as a base
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the local project files to the container's working directory
COPY expense_tracker/ .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port 8000 for the Django app
EXPOSE 8000

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

---

### 4. Build and Tag Docker Image

```bash
docker build -t django-mvc-app .
docker tag django-mvc-app localhost:5000/django-mvc-app
```

---

### 5. Push Image to Local Registry

Ensure your local registry is running:

```bash
docker run -d -p 5000:5000 --name registry registry:2
```

Then push the image:

```bash
docker push localhost:5000/django-mvc-app
```

---

### 6. Create Kubernetes YAMLs

**deployment.yaml**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: django-mvc-app-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: django-mvc-app
  template:
    metadata:
      labels:
        app: django-mvc-app
    spec:
      containers:
      - name: django-mvc-app
        image: localhost:5000/django-mvc-app
        ports:
        - containerPort: 8000
```

**service.yaml**
```yaml
apiVersion: v1
kind: Service
metadata:
  name: django-mvc-app-service
spec:
  selector:
    app: django-mvc-app
  ports:
    - protocol: TCP
      port: 8000
      targetPort: 8000
  type: NodePort
```

---

### 7. Apply Kubernetes Configs

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

---

### 8. Verify the Deployment

```bash
kubectl get pods
kubectl get services
kubectl logs <pod-name>
```

---

### 9. Access the App

Visit:

```
http://localhost:32091/
(32091 is my nodeport)
```

You’ll see the homepage, with functionality for:
- Viewing expenses
- Adding new expenses
- User login/logout


## 👤 Author

**Adeel Ahmed**  
Deakin University  
