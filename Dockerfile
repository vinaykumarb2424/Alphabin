FROM alpine:latest
RUN apk update && apk add python3 py3-pip

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


# FROM alpine
#
# RUN apk update && \
#     apk add python3 py3-pip && \
#     apk add --virtual .build-deps gcc python3-dev musl-dev libffi-dev openssl-dev
#
# COPY requirements.txt /app/
# WORKDIR /app
#
# RUN pip3 install --no-cache-dir -r requirements.txt
#
# # Clean up build dependencies
# RUN apk del .build-deps



