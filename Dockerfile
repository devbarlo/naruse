FROM rendyprojects/kali-rolling:latest

RUN apt update -y && apt full-upgrade -y
RUN apt-get install -y curl git npm mediainfo neofetch python3-pip python3.9 
RUN git clone -b dev22 https://github.com/TeamKillerX/naruse /root/TeamKillerX
RUN mkdir /root/TeamKillerX/bin/
WORKDIR /root/TeamKillerX/
RUN chmod +x /usr/local/bin/*
RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
CMD ["bash", "naruse.sh"]
