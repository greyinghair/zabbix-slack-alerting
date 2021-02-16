# Description

This python repo is to enable Zabbix to Slack notifications pre native weebhook support within Zabbix.  </br>
Create a media type, action & add to user permissions.

# Install

## Create ".env" and put into variable:
```echo 'SLACK_TOKEN = <bot token>' > .env```

## Placement
### Clone into Alerts directory
```cd /usr/lib/zabbix/alertscripts/``` </br>

```git clone https://github.com/stacedan/tsg-netops-zabbix-slack-bot.git```

### Make file Executable
```cd tsg-netops-slack-bot``` </br>

```chmod +x slack.py```

## Install requirements:
### Install Python3 (via package kernel manager, not pyenv)
```yum install python3```

### Install modules
```pip3 install -r requirements.txt```
