# AWS Deployment Guide

This project can be deployed on AWS in multiple ways.

## Suggested production-style setup

- Frontend: AWS Amplify or S3 + CloudFront
- Backend: ECS Fargate or Elastic Beanstalk
- Database: Amazon RDS PostgreSQL
- Secrets: AWS Secrets Manager
- Logs: CloudWatch
- CI/CD: GitHub Actions

## Environment variables

```text
DATABASE_URL=postgresql+psycopg2://user:password@rds-host:5432/workflow_db
AI_PROVIDER=openai
OPENAI_API_KEY=your_key
LOCAL_FALLBACK_MODE=false
```

## Simple deployment roadmap

1. Push code to GitHub.
2. Create RDS PostgreSQL instance.
3. Build backend Docker image.
4. Push image to Amazon ECR.
5. Deploy backend to ECS Fargate.
6. Deploy frontend to Amplify.
7. Add CloudWatch logs and alarms.
8. Store API keys in AWS Secrets Manager.
