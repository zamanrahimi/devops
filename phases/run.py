import webbrowser






# 1. phase one, planning 
# 2. phase two, coding 
# 3. phase three, build 
# 4. phase four, test 
# 5. phase five, release
# 6. phase six, deploy
# 7. phase seven, operate
# 8. phase eight, monitor







import subprocess as sb

# import color module
import component.public.colors as color
commands = [
    
    # a_plan 
    "python a_plan/plan.py",

    # c_build / repo 
    "python c_build/repo/repo.py",

    # c_build / ci_server 
    # Note: comment it if create is created before, otherwise, it encounter error
    # "python c_build/ci_server/jenkins_command.py",
]

for command in commands:
    try:
        # execute main command
        sb.run(command, check=True, shell=True)
        print(
            f"{color.Colors.BLUE}----------Command {command} ---------- {color.Colors.RESET}"
        )

        print(
            f" {color.Colors.GREEN} ( {command} ) exected successfully {color.Colors.RESET} \n"
        )

    except sb.CalledProcessError as e:
        print(
            f"{color.Colors.RED}----------------Command {command} ------------------------ {color.Colors.RESET}"
        )
        print(
            f" {color.Colors.RED} The error for command ( {command} ) is {e} {color.Colors.RESET}"
        )
