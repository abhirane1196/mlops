import os
import subprocess

def run_command(command):
    """Run a shell command and return the output"""
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}\n{e.output.decode('utf-8')}")
        return None

def git_init():
    """Initialize a Git repository"""
    return run_command("git init")

def git_add(files='.', commit_all=True):
    """Add files to the staging area"""
    if commit_all:
        return run_command("git add .")
    else:
        return run_command(f"git add {files}")

def git_commit(message):
    """Commit changes with a message"""
    return run_command(f'git commit -m "{message}"')

def git_push(branch='main', remote='origin'):
    """Push changes to a remote repository"""
    return run_command(f"git push {remote} {branch}")

def main():
    # Initialize Git repository (uncomment if needed)
    # git_init()

    # Add all files to the staging area
    git_add()

    # Commit changes
    commit_message = "Automated commit from Python script"
    git_commit(commit_message)

    # Push to DagsHub
    git_push()

if __name__ == "__main__":
    main()
