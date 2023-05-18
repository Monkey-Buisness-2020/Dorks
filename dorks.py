import sys
import os
import time
from termcolor import colored
import webbrowser
import argparse
import random
import requests
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument('-k', '--key', help='Provide a keyword to look search.')
parser.add_argument('-b', '--browser', help='Open all the links in a browser.', action='store_true')
args = parser.parse_args()

def program(key):
    banner = """
    ------------------------------------------------------------------------
    #####                              
    #    #  ####  #####  #    #  ####  
    #    # #    # #    # #   #  #      
    #    # #    # #    # ####    ####  
    #    # #    # #####  #  #        # 
    #    # #    # #   #  #   #  #    # 
    #####   ####  #    # #    #  ####                          
    ------------------------------------------------------------------------
    """
    os.system("cls")
    print(banner)
    print(colored("************ Github Dork Link creator (must be logged in) *******************", "yellow"))
    print(colored("\npassword", "cyan"))
    print("https://github.com/search?q=%22"+key+"%22+password&type=Code")
    print(colored("\nnpmrc _auth", "cyan"))
    print("https://github.com/search?q=%22"+key+"%22+npmrc%20_auth&type=Code")
    print(colored("\ndockercfg", "cyan"))
    print("https://github.com/search?q=%22"+key+"%22+dockercfg&type=Code")
    print(colored("\npem private", "cyan"))
    print("https://github.com/search?q=%22"+key+"%22+pem%20private&type=Code")
    print(colored("\nid_rsa", "cyan"))
    print("https://github.com/search?q=%22"+key+"%22+id_rsa&type=Code")
    print(colored("\naws_access_key_id", "cyan"))
    print("https://github.com/search?q=%22"+key+"%22+aws_access_key_id&type=Code")
    print(colored("\ns3cfg", "cyan"))
    print("https://github.com/search?q=%22"+key+"%22+s3cfg&type=Code")
    print(colored("\nhtpasswd", "cyan"))
    print("https://github.com/search?q=%22"+key+"%22+htpasswd&type=Code")
    print(colored("\ngit-credentials", "cyan"))
    print("https://github.com/search?q=%22"+key+"%22+git-credentials&type=Code")
    print(colored("\nbashrc password", "cyan"))
    print("https://github.com/search?q=%22"+key+"%22+bashrc%20password&type=Code")
    print(colored("\nsshd_config", "cyan"))
    print("https://github.com/search?q=%22"+key+"%22+sshd_config&type=Code")
    print(colored("\nxoxp OR xoxb OR xoxa", "cyan"))
    print("https://github.com/search?q=%22"+key+"%22+xoxp%20OR%20xoxb%20OR%20xoxa&type=Code")
    print(colored("\nSECRET_KEY", "cyan"))
    print("https://github.com/search?q=%22"+key+"%22+SECRET_KEY&type=Code")
    print(colored("\nclient_secret", "cyan"))
    print("https://github.com/search?q=%22"+key+"%22+client_secret&type=Code")
    print(colored("\nsshd_config", "cyan"))
    print("https://github.com/search?q=%22"+key+"%22+sshd_config&type=Code")
    print(colored("\ngithub_token", "cyan"))
    print("https://github.com/search?q=%22"+key+"%22+github_token&type=Code")
    print(colored("\napi_key", "cyan"))
    print("https://github.com/search?q=%22"+key+"%22+api_key&type=Code")
    print(colored("\nFTP", "cyan"))
    print("https://github.com/search?q=%22"+key+"%22+FTP&type=Code")
    print(colored("\napp_secret", "cyan"))
    print("https://github.com/search?q=%22"+key+"%22+app_secret&type=Code")
    print(colored("\npasswd", "cyan"))
    print("https://github.com/search?q=%22"+key+"%22+passwd&type=Code")
    print(colored("\ns3.yml", "cyan"))
    print("https://github.com/search?q=%22"+key+"%22+.env&type=Code")
    print(colored("\n.exs", "cyan"))
    print("https://github.com/search?q=%22"+key+"%22+.exs&type=Code")
    print(colored("\nbeanstalkd.yml", "cyan"))
    print("https://github.com/search?q=%22"+key+"%22+beanstalkd.yml&type=Code")
    print(colored("\ndeploy.rake", "cyan"))
    print("https://github.com/search?q=%22"+key+"%22+deploy.rake&type=Code")
    print(colored("\nmysql", "cyan"))
    print("https://github.com/search?q=%22"+key+"%22+mysql&type=Code")
    print(colored("\ncredentials", "cyan"))
    print("https://github.com/search?q=%22"+key+"%22+credentials&type=Code")
    print(colored("\nPWD", "cyan"))
    print("https://github.com/search?q=%22"+key+"%22+PWD&type=Code")
    print(colored("\ndeploy.rake", "cyan"))
    print("https://github.com/search?q=%22"+key+"%22+deploy.rake&type=Code")
    print(colored("\n.bash_history", "cyan"))
    print("https://github.com/search?q=%22"+key+"%22+.bash_history&type=Code")
    print(colored("\n.sls", "cyan"))
    print("https://github.com/search?q=%22"+key+"%22+.sls&type=Code")
    print(colored("\nsecrets", "cyan"))
    print("https://github.com/search?q=%22"+key+"%22+secrets&type=Code")
    print(colored("\ncomposer.json", "cyan"))
    print("https://github.com/search?q=%22"+key+"%22+composer.json&type=Code")
    print(colored("\nDark Web Search", "red"))
    print(f"https://darksearch.io/search?query=%22{key}%22\n")

def open_links(key):
    github_links = { f"https://github.com/search?q=%22{key}%22+password&type=Code", f"https://github.com/search?q=%22{key}%22+npmrc%20_auth&type=Code", f"https://github.com/search?q=%22{key}%22+dockercfg&type=Code", f"https://github.com/search?q=%22{key}%22+pem%20private&type=Code", f"https://github.com/search?q=%22{key}%22+id_rsa&type=Code", f"https://github.com/search?q=%22{key}%22+aws_access_key_id&type=Code", f"https://github.com/search?q=%22{key}%22+s3cfg&type=Code", f"https://github.com/search?q=%22{key}%22+htpasswd&type=Code", f"https://github.com/search?q=%22{key}%22+git-credentials&type=Code", f"https://github.com/search?q=%22{key}%22+bashrc%20password&type=Code", f"https://github.com/search?q=%22{key}%22+sshd_config&type=Code", f"https://github.com/search?q=%22{key}%22+xoxp%20OR%20xoxb%20OR%20xoxa&type=Code", f"https://github.com/search?q=%22{key}%22+SECRET_KEY&type=Code", f"https://github.com/search?q=%22{key}%22+client_secret&type=Code", f"https://github.com/search?q=%22{key}%22+sshd_config&type=Code", f"https://github.com/search?q=%22{key}%22+github_token&type=Code", f"https://github.com/search?q=%22{key}%22+api_key&type=Code", f"https://github.com/search?q=%22{key}%22+FTP&type=Code", f"https://github.com/search?q=%22{key}%22+app_secret&type=Code", f"https://github.com/search?q=%22{key}%22+passwd&type=Code", f"https://github.com/search?q=%22{key}%22+.env&type=Code", f"https://github.com/search?q=%22{key}%22+.exs&type=Code", f"https://github.com/search?q=%22{key}%22+beanstalkd.yml&type=Code", f"https://github.com/search?q=%22{key}%22+deploy.rake&type=Code", f"https://github.com/search?q=%22{key}%22+mysql&type=Code", f"https://github.com/search?q=%22{key}%22+credentials&type=Code", f"https://github.com/search?q=%22{key}%22+PWD&type=Code", f"https://github.com/search?q=%22{key}%22+deploy.rake&type=Code", f"https://github.com/search?q=%22{key}%22+.bash_history&type=Code", f"https://github.com/search?q=%22{key}%22+.sls&type=Code", f"https://github.com/search?q=%22{key}%22+secrets&type=Code", f"https://github.com/search?q=%22{key}%22+composer.json&type=Code", f"https://darksearch.io/search?query=%22{key}%22" }

    print("-"*50)    
    print("\n[+] Opening the links [+]\n")    
    for link in github_links:
        print(f"Opening: {link}")
        #response = requests.get(link)
        #soup = BeautifulSoup(response.text, 'html.parser')
        #header3 = soup.findAll('h3')
        #print(soup)

        webbrowser.open(link)
        seconds = random.randint(1, 5)
        time.sleep(seconds)
    print("\n[+] DONE [+]\n")

if args.key:
    program(args.key)
if args.browser:
    open_links(args.key)
else:
    print("\nTry 'python3 dorks.py -k [keyword]'\n")
