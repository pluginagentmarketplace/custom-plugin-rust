---
name: cloud-devops-infrastructure
description: Master Cloud Platforms, DevOps, Infrastructure as Code, and System Design. Build scalable systems on AWS, Cloudflare, Docker, Kubernetes, Terraform, and Linux. Implement CI/CD pipelines and modern infrastructure.
---

# Cloud, DevOps & Infrastructure

## Quick Start

### Docker Containerization
```dockerfile
# Dockerfile for Node.js application
FROM node:18-alpine

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci --only=production

# Copy source code
COPY . .

# Expose port
EXPOSE 3000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD node healthcheck.js

# Run application
CMD ["node", "index.js"]
```

### Kubernetes Deployment
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
      - name: app
        image: myapp:1.0.0
        ports:
        - containerPort: 3000
        resources:
          requests:
            memory: "128Mi"
            cpu: "100m"
          limits:
            memory: "256Mi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /health
            port: 3000
          initialDelaySeconds: 30
          periodSeconds: 10
---
apiVersion: v1
kind: Service
metadata:
  name: app-service
spec:
  selector:
    app: myapp
  ports:
  - protocol: TCP
    port: 80
    targetPort: 3000
  type: LoadBalancer
```

### Terraform Infrastructure as Code
```hcl
# AWS provider configuration
terraform {
  required_version = ">= 1.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# VPC
resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true

  tags = {
    Name = "main-vpc"
  }
}

# EC2 Instance
resource "aws_instance" "web" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"
  subnet_id     = aws_subnet.public.id

  tags = {
    Name = "web-server"
  }
}

# RDS Database
resource "aws_db_instance" "postgres" {
  allocated_storage    = 20
  engine               = "postgres"
  engine_version       = "15.3"
  instance_class       = "db.t3.micro"
  username             = "admin"
  password             = random_password.db.result

  tags = {
    Name = "main-db"
  }
}

# Output values
output "instance_ip" {
  value = aws_instance.web.public_ip
}
```

### AWS Services Setup
```bash
# AWS CLI examples

# Create S3 bucket
aws s3api create-bucket \
  --bucket my-app-bucket \
  --region us-east-1

# Launch EC2 instance
aws ec2 run-instances \
  --image-id ami-0c55b159cbfafe1f0 \
  --count 1 \
  --instance-type t2.micro \
  --key-name my-key-pair

# Create RDS database
aws rds create-db-instance \
  --db-instance-identifier mydb \
  --db-instance-class db.t3.micro \
  --engine postgres \
  --allocated-storage 20

# Create Lambda function
aws lambda create-function \
  --function-name my-function \
  --runtime python3.11 \
  --role arn:aws:iam::123456789012:role/lambda-role \
  --handler index.handler \
  --zip-file fileb://function.zip
```

### CI/CD Pipeline with GitHub Actions
```yaml
name: Deploy Application

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3

    - name: Set up Node.js
      uses: actions/setup-node@v3
      with:
        node-version: '18'

    - name: Install dependencies
      run: npm ci

    - name: Run linter
      run: npm run lint

    - name: Run tests
      run: npm test -- --coverage

    - name: Upload coverage
      uses: codecov/codecov-action@v3

  build:
    needs: test
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3

    - name: Build Docker image
      run: docker build -t myapp:${{ github.sha }} .

    - name: Push to registry
      run: |
        docker tag myapp:${{ github.sha }} myregistry/myapp:latest
        docker push myregistry/myapp:latest

  deploy:
    needs: build
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
    - name: Deploy to production
      run: |
        kubectl set image deployment/app-deployment \
        app=myregistry/myapp:latest
```

### Linux System Administration
```bash
#!/bin/bash

# User management
sudo useradd -m -s /bin/bash newuser
sudo usermod -aG sudo newuser
sudo passwd newuser

# File permissions
chmod 755 script.sh  # rwx for owner, rx for group/others
chmod 644 config.txt # rw for owner, r for group/others

# Package management
sudo apt update && sudo apt upgrade
sudo apt install build-essential

# System monitoring
top                  # CPU and memory usage
df -h               # Disk space
free -h             # Memory usage
netstat -an         # Network connections
ps aux              # Running processes

# Service management
sudo systemctl start nginx
sudo systemctl enable nginx
sudo systemctl status nginx

# Logs and debugging
tail -f /var/log/syslog
journalctl -u nginx -n 100
```

## Learning Paths

### AWS (roadmap.sh/aws)
1. **Compute**
   - EC2 instances
   - Lambda functions
   - ECS containers

2. **Storage**
   - S3 buckets
   - EBS volumes
   - RDS databases

3. **Networking**
   - VPC and subnets
   - Security groups
   - Load balancers

4. **Services**
   - CloudFront CDN
   - CloudWatch monitoring
   - IAM permissions

### Docker (roadmap.sh/docker)
- Dockerfile syntax
- Image layering
- Container networking
- Volume management
- Docker Compose

### Kubernetes (roadmap.sh/kubernetes)
- Pods and deployments
- Services and ingress
- ConfigMaps and secrets
- Persistent volumes
- StatefulSets

### Terraform (roadmap.sh/terraform)
- State management
- Variables and outputs
- Modules
- Remote state
- Workspaces

### Cloudflare (roadmap.sh/cloudflare)
- Global network
- Workers (serverless)
- Pages (static hosting)
- Security and DDoS
- DNS management

### Linux (roadmap.sh/linux)
- Command line
- File system
- User management
- Package management
- System services

### DevOps (roadmap.sh/devops)
- Version control (Git)
- CI/CD pipelines
- Infrastructure as Code
- Monitoring & logging
- Configuration management

### System Design (roadmap.sh/system-design)
- Scalability
- Load balancing
- Caching strategies
- Database sharding
- Microservices architecture

## Infrastructure Components

| Component | Purpose | AWS | Cloud Agnostic |
|-----------|---------|-----|-----------------|
| Compute | Code execution | EC2, Lambda | Docker, Kubernetes |
| Storage | Persistent data | S3, EBS | NAS, Ceph |
| Database | Data management | RDS, DynamoDB | PostgreSQL, MongoDB |
| Load Balance | Traffic distribution | ELB, ALB | Nginx, HAProxy |
| Monitoring | System visibility | CloudWatch | Prometheus, ELK |
| CDN | Content delivery | CloudFront | Cloudflare, Akamai |

## Monitoring & Logging Stack

```bash
# Prometheus scrape config
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']
  - job_name: 'node'
    static_configs:
      - targets: ['localhost:9100']

# ELK Stack setup
# Elasticsearch - Log storage
# Logstash - Log processing
# Kibana - Visualization
```

## Security Best Practices

- [ ] Enable encryption at rest and in transit
- [ ] Use IAM roles (not root credentials)
- [ ] Enable VPC security groups
- [ ] Implement rate limiting
- [ ] Monitor and alert on suspicious activity
- [ ] Regular security patching
- [ ] Secrets management (Vault, AWS Secrets Manager)
- [ ] Network segmentation
- [ ] API gateway protection
- [ ] DDoS protection

## Resources

- [AWS Documentation](https://docs.aws.amazon.com)
- [Kubernetes Docs](https://kubernetes.io/docs)
- [Terraform Registry](https://registry.terraform.io)
- [Linux Manual Pages](https://man7.org/linux/man-pages)
