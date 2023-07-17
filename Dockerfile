FROM alpine:latest
RUN apk update && apk add python3

RUN mkdir workdir
COPY    ./Evernote  /Automation/Evernote
COPY    ./Reports  /Automation/Reports
COPY    ./Screenshots  /Automation/Screenshots
COPY    ./Testcases  /Automation/Testcases
COPY    ./common_functionality.py  /Automation/common_functionality
COPY    ./log.py  /Automation/log.py
COPY    ./requirements.txt  /Automation/requirements.txt
WORKDIR     /Automation/
RUN  pip install --no-cache-dir -r requirements.txt
WORKDIR     /Automation/Testcases


