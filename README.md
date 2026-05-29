# terraform-state-agent

An AI-powered agent that reads Terraform state files, analyzes your infrastructure, and suggests improvements - executing changes only after explicit user approval.

## What it does
- Parses Terraform state files to understand current infrastructure
- Uses the Claude API to identify inefficiencies, drift, and improvement opportunities
- Presents suggestions in plain English before touching anything
- Executes approved changes only

## Why I built this
Manual Terraform state review is tedious and error-prone. This agent brings AI-assisted analysis to infrastructure management while keeping the human in control of every action.

## Tech stack
- Python
- Claude API (Anthropic)
- Terraform / tfstate JSON parsing

## Status
- In active development

## Roadmap
- [ ] Parse local tfstate files
- [ ] Claude API integration for analysis
- [ ] Suggestion review interface
- [ ] Approved change execution
- [ ] Remote state support (S3 backend)

## Author
Lonwabo Mcobothi - Cloud & DevOps Engineer in training
Durban, South Africa | Open to remote roles
