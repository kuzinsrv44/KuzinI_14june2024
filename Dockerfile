FROM python:3.11-slim

WORKDIR /usr/src/test

COPY . /usr/src/test

RUN apt update && apt -y upgrade && \
    apt -y install wget gnupg2 apt-transport-https curl unzip && \
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    apt update && \
    apt -y install google-chrome-stable default-jre

# Install ChromeDriver
RUN CHROME_DRIVER_VERSION=$(wget -qO- https://chromedriver.storage.googleapis.com/LATEST_RELEASE) && \
    wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin/ && \
    rm /tmp/chromedriver.zip

# Install Python dependencies
RUN pip install -r requirements.txt

# Install Allure
RUN wget https://github.com/allure-framework/allure2/releases/download/2.18.1/allure_2.18.1-1_all.deb && \
    dpkg -i allure_2.18.1-1_all.deb




CMD echo "start test"; pytest; echo "allure"; allure serve "/allure_report/" --port 37001;
