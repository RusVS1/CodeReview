FROM python:3

RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list \
    && apt-get update && apt-get install -y \
    google-chrome-stable
    
RUN apt update
RUN apt install python3 -y

WORKDIR /usr/app/src

COPY main.py ./
COPY database.py ./
COPY bot.py ./
COPY parse.py ./

RUN pip install selenium
RUN pip install webdriver-manager
RUN pip install pyTelegramBotAPI

CMD ["python", "main.py"]