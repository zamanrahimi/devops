import subprocess as sb
import build

commands = [
    "black run.py",
    f"docker run -it zamanrahimi1368/redhat_custom_version:{build.version} /bin/sh",
]
for cmd in commands:
    try:
        sb.run(cmd, check=True, shell=True)
    except sb.CalledProcessError as e:
        print(f"check the error: {e}")
