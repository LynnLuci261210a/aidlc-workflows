# aidlc-workflows

> Fork of [awslabs/aidlc-workflows](https://github.com/awslabs/aidlc-workflows)

A collection of AI-driven development lifecycle (AIDLC) workflows designed to automate and streamline software development processes using AI assistance.

## Overview

This project provides reusable workflow templates and automation scripts for integrating AI assistance into the software development lifecycle, including code review, documentation generation, testing, and deployment pipelines.

## Features

- 🤖 AI-assisted code review workflows
- 📝 Automated documentation generation
- 🧪 Intelligent test generation and validation
- 🔒 Security scanning with Bandit and Checkov
- 🚀 CI/CD pipeline integration

## Prerequisites

- Python 3.10+
- AWS CLI configured (for AWS-based workflows)
- Docker (optional, for containerized workflows)

## Installation

```bash
git clone https://github.com/your-org/aidlc-workflows.git
cd aidlc-workflows
pip install -r requirements.txt
```

## Quick Start

```bash
# Run the main workflow
python -m aidlc_workflows

# Or use the CLI
aidlc-workflows --help
```

## Project Structure

```
aidlc-workflows/
├── .github/              # GitHub Actions workflows and templates
├── aidlc_workflows/      # Main Python package
│   ├── __init__.py
│   ├── cli.py            # Command-line interface
│   ├── config.py         # Configuration management
│   └── workflows/        # Workflow implementations
├── tests/                # Test suite
├── docs/                 # Documentation
├── .bandit               # Bandit security configuration
├── .checkov.yaml         # Checkov IaC security configuration
└── requirements.txt      # Python dependencies
```

## Security

This project uses the following security scanning tools:

- **Bandit**: Static analysis for Python security issues
- **Checkov**: Infrastructure-as-code security scanning

Run security checks locally:

```bash
# Run Bandit
bandit -c .bandit -r .

# Run Checkov
checkov --config-file .checkov.yaml
```

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting pull requests. See [CODEOWNERS](.github/CODEOWNERS) for maintainer information.

### Reporting Issues

Use the GitHub issue templates for:
- [Bug Reports](.github/ISSUE_TEMPLATE/bug_report.yml)
- [Feature Requests](.github/ISSUE_TEMPLATE/feature_request.yml)
- [Documentation Issues](.github/ISSUE_TEMPLATE/documentation.yml)

## License

This project is licensed under the Apache License 2.0 — see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Original project: [awslabs/aidlc-workflows](https://github.com/awslabs/aidlc-workflows)
- AWS Labs team for the foundational work

## Personal Notes

> **Note:** This is my personal fork for learning and experimentation. I'm primarily exploring the AI-assisted code review and test generation workflows. Changes here may not be suitable for upstream contribution.

### My Setup

I'm running this on Python 3.11 with a local `.env` file for AWS credentials. To replicate my setup:

```bash
cp .env.example .env
# Then fill in your AWS credentials and region in .env
```

### Workflow Notes

- The **code review workflow** is the most useful one so far — I've been running it as a pre-commit step.
- TODO: experiment with the test generation workflow on my side project.
