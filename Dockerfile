FROM ubuntu:latest
MAINTAINER KangMin,Kwon "kmkwon94@gmail.com"
RUN apt-get update
RUN apt-get install -y python3 python3-pip python3-dev build-essential
RUN pip3 install --user networkx
RUN pip3 install --user karateclub
RUN pip3 install --user tqdm
RUN pip3 install --user community
RUN pip3 install --user numpy sklearn
RUN pip3 install --user pygsp
RUN pip3 install --user gensim
RUN pip3 install --user python-louvain
COPY . /workspace
WORKDIR /workspace 
EXPOSE 80
CMD python3 ./main.py
