# 🚀 Python Environment Setup & Debugging Guide (Conda + VS Code)

> A practical, real-world guide to setting up a Python development environment using Conda, including **common errors, root causes, and production-level fixes**.

---

## 📌 Overview

This project demonstrates:
- Setting up a **Python 3.12 environment using Conda**
- Integrating with **VS Code**
- Debugging **real-world environment issues**
- Applying **Git best practices**

It is designed for:
- Beginners starting Python / Django / GenAI
- Developers struggling with Conda setup
- Anyone wanting a clean, reproducible environment

---

## 🛠️ Tech Stack

- **Python 3.12**
- **Conda (Anaconda/Miniconda)**
- **VS Code**
- **Git**

---

## ⚙️ Environment Setup

### 1️⃣ Open Project in VS Code

```
## Open your project folder in VS Code

##Create Virtual Environment
```
conda create -p venv python=3.12
```

##Activate Environment
```
conda activate ./venv

or 

conda activate venv
```

---
🔴 Issue 1: conda is not recognized

Root Cause:
Conda is not added to system PATH or not initialized.

```
conda init powershell
```

🔴 Issue 2: Run 'conda init' before 'conda activate'
Root Cause:
PowerShell profile not loaded or execution policy blocking scripts.
```
conda init powershell
```

Get-ExecutionPolicy
if Restricted
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

🔴 Issue 3: Wrong Activation Syntax
conda activate ./venv



---
Dependency Management
```
pip install ipykernel
```

---
## Preferred Named Environments
Instead of 
```
conda create -p venv python=3.12
```

use
```
conda create -n myenv python=3.12
conda activate myenv
```

Why?
- Cleaner structure
- No Git conflicts
- Easier environment management