# Project Automation

This project will automatically create a new repo at GitHub and initialise it. Then it'll open the editor to write the code.


## Setup: 
```bash
git clone "https://github.com/suryakantamangaraj/ProjectAutomation.git"
cd ProjectAutomation
pip install -r requirements.txt
```

path:
```bash
"ProjectAutomation" folder directory to path
```

## Usage:

Command to run the program type

```bash
'Python create.py <project_name>'
```

## Pre-setup:

**For Windows OS only**

create env vars (Users) :
> projects directory as - "ap"

> Github tocken as      - "gt"

> Get a token here: https://github.com/settings/tokens/new (must have repo, user, and delete_repo permissions)

### How to set env vars
```
> setx [UserVariableName] "[UserVariableToken]"
```

For example:
```
> setx gt "ThisIsMyTokenInQuotes"
```
