FROM ubuntu:latest

#Update & Upgrade with apt to ensure image has the latest security patches and whatnot
RUN apt-get update && \
	apt-get upgrade -y && \
	apt-get install -y git wget curl \
	bash python3 python3-pip

#Create a directory for, and clone the repository
RUN mkdir -p /opt/src
RUN git clone --recursive https://github.com/Rishabh1839/ARIEL.git /opt/src/ARIEL

#Install Dependencies
RUN cd /opt/src/ARIEL && \
	pip install -r requirements.txt

#Let's Ride!
RUN python3 ARIEL.py
