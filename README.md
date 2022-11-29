# MakeAIWork 3 - Workspace Configuration

## Initialize this Git repository
To be able to use this repository and handover your code, you need to have remote access to Github.

<ol>

<li>

**Configure git**

In order to commit and push your changes, you need identitify yourself.

Open a (git)bash, enter directory MakeAIWork3 and run:
```bash
install/git_config.sh {your_github_username} {your@student.email.com}
```
This script will also set the [pull policy](https://www.git-scm.com/docs/git-pull) to rebase.

</li>

<li>

**Push your repository**

```bash
git push -u origin master
```

</li>

<li>

**Make your remote github repository accessible to the teachers**

<ol>

<li>Sign in to github.com and select MakeAIWork3</li>

<li>Go to <i>Settings</i> and select <i>Collaborators</i></li>

<li>Add <i>fsmitskamp</i>, <i>hakoptak</i> and <i>AlxcNL</i> as collaborators

</ol>

</li>

<li>

**Make your remote git respository private**

<ol>

<li>

Scroll down the Settings page of your remote git respository MakeAIWork3 yo <i>Danger Zone</i>. 

</li>

<li>Click <i>Change visibility</i> and select <i>Change to private</i></li>

</ol>

</li>

</ol>

*** Required software
Watch [instruction videos at YouTube](https://youtube.com/playlist?list=PLf5zREwsIjUNQ2y4TGi9F0uXQZ1B08d_v) for detailed installation instructions of the required software. 

## Configure Python

<ol>

<li>

(Optional) Create new virtual Python environment 
```sh
install/create_virtual_env.sh
```

</li>

<li>

(Optional) Copy virtual environment from MakeAIWork2 (Windows)
```sh
 cp -r ../MakeAIWork2/env .
 ```

<li>

Install Python libraries

```bash
install/install_requirements.sh
```

</li>

</ol>

## Use Starter Scripts

### Start Jupyter
```bash
sh/jupyter.sh
```
