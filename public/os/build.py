import subprocess as sb
version = "v1.19"
commands = [

    f"docker build -t zamanrahimi1368/redhat_custom_version:{version} .",
    f"docker push zamanrahimi1368/redhat_custom_version:{version}",
    f"docker run -it zamanrahimi1368/redhat_custom_version:{version} /bin/sh",
]
for cmd in commands:
    try:
        sb.run(cmd, check=True, shell=True)
    except sb.CalledProcessError as e:
        print(f"check the error: {e}")
