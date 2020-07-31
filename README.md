# Project Automation

This project will automatically create a new repo at GitHub and initialise it as well as locally. Then it'll open the editor to write the code.

## pre-setup:

**For Windows OS only**
create env vars (Users) :
> projects directory as - "ap"
> Github tocken as      - "gt"

> Get a token here: https://github.com/settings/tokens/new
  > Must have repo, user, and delete_repo permissions

### How to set env vars
```
> setx [UserVariableName] "[UserVariableToken]"

For example:
> setx gt "ThisIsMyTokenInQuotes"
```

## setup: 
```bash
git clone "https://github.com/suryakantamangaraj/ProjectAutomation.git"
cd ProjectAutomation
pip install -r requirements.txt

path:
"ProjectAutomation" folder directory to path
```

## Usage:

```bash
Command to run the program type

'create <project_name>'
'create <project_name> <l>'   - only for local initialisation purpose
```
