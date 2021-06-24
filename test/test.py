def stage(ctx):
    return {
        "parent": "root",
        "triggers": {
            "parent": True
        },
        "parameters": [],
        "configs": [],
        "jobs": [
        {
            "name": "testDocker",
            "steps": [{
            "tool": "git",
                "checkout": "http://192.168.0.104:3000/git/root/testDocker.git",
                "branch": "master"
            }],
            "environments": [
                {
                    "system": "any",
                    "agents_group": "all",
                    "config": "default"
                }
            ]
        },
        {
            "name": "shell_examples",
            "steps": [{
                "tool": "shell",
                "cmd": "echo 'Hello World'"
            }, {
                "tool": "shell",
                "cmd": "pwd && ls -al",
                "cwd": "/"
            }, {
                "tool": "shell",
                "cmd": "whoami"
            }, {
                "tool": "shell",
                "cmd": "whoami",
                "user": "root"
            }],
            "environments": [
                {
                    "system": "any",
                    "agents_group": "all",
                    "config": "default"
                }
            ]
        }
    ]
}

