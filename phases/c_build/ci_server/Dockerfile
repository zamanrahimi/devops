import webbrowser
import os
import sys 
# Get the absolute path to the current script

# current dir
current_directory = os.path.dirname(os.path.abspath(__file__)) 
# one dir back
one_dir_back = os.path.dirname(current_directory)
# two dir back
two_dir_back = os.path.dirname(os.path.dirname(current_directory))
# go inside the dirs
two_dirs_inside = os.path.join(one_dir_back, 'component', 'public')
# Add the absolute path to 'public' directory to the Python path
sys.path.append(two_dirs_inside)

# two_directory_back = os.path.normpath(os.path.join(current_directory, "../component/public/"))
import colors as color
# import dependiencies 

print(
    f"{color.Colors.GREEN}1-plan phase {color.Colors.RESET}"
)


# Specify the URL of the website you want to open
website_url = "https://zamanrahimirz.atlassian.net/jira/your-work"

# Open the website in the default web browser
webbrowser.open(website_url)




