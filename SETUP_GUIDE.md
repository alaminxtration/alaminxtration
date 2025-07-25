# 🔧 GitHub Actions Setup Guide

This guide helps you configure the remaining secrets and tokens for your workflows.

## 📊 For Profile Metrics Workflow

### 1. Create GitHub Personal Access Token
1. Go to GitHub Settings → Developer settings → Personal access tokens
2. Click "Generate new token (classic)"
3. Name it: `METRICS_TOKEN`
4. Select these scopes:
   - `public_repo` (to read repository data)
   - `read:user` (to read profile data)
   - `read:org` (if you want organization stats)

### 2. Add Token to Repository Secrets
1. Go to your repository → Settings → Secrets and variables → Actions
2. Click "New repository secret"
3. Name: `METRICS_TOKEN`
4. Value: Paste the token you created

## 🐳 For Docker Hub Deployment (Optional)

### 1. Docker Hub Setup
1. Create account at hub.docker.com
2. Create repository: `alaminxtration/my-app`

### 2. Add Docker Hub Secrets
Add these repository secrets:
- `DOCKERHUB_USERNAME`: Your Docker Hub username
- `DOCKERHUB_TOKEN`: Your Docker Hub access token

## ✅ Workflow Status After Setup

After adding the secrets, your workflows will:

### 🔨 Python CI/CD Pipeline
- ✅ **Test Suite**: Tests on Python 3.8-3.11
- ✅ **Code Quality**: Black, isort, flake8 checks
- ✅ **Security**: CodeQL vulnerability scanning
- ✅ **Docker**: Build and push to Docker Hub (if secrets added)

### 📝 Auto Update README
- ✅ **Blog Posts**: Auto-fetch from Dev.to and Medium
- ✅ **GitHub Activity**: Show recent contributions
- ✅ **Monthly Updates**: Runs 1st of each month

### 📊 Profile Metrics
- ✅ **Statistics**: GitHub activity and language stats
- ✅ **Achievements**: Badges and trophies
- ✅ **Monthly Updates**: Fresh metrics each month

### 🔗 Basic CI
- ✅ **Health Check**: Ensures Actions are working

## 🚀 Test Your Setup

### Manual Trigger Test
1. Go to Actions tab in your repository
2. Select any workflow
3. Click "Run workflow" button
4. Check if it runs successfully

### Automatic Triggers
- Push code → Python CI/CD runs
- 1st of month → Metrics and README update

## 🔍 Troubleshooting

### Common Issues:
1. **Token Permissions**: Make sure METRICS_TOKEN has correct scopes
2. **Blog Feeds**: Update RSS URLs in update-readme.yml if needed
3. **Docker Secrets**: Only needed if you want Docker deployment

### Check Workflow Logs:
1. Go to Actions tab
2. Click on failed workflow
3. Check logs for specific error messages

---

**🎉 Your GitHub profile is now professionally automated!**
