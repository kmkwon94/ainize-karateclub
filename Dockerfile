FROM ubuntu:latest
MAINTAINER KangMin,Kwon "kmkwon94@gmail.com"
RUN apt-get update
RUN apt-get install -y python-pip python-dev build-essential
RUN pip install --user networkx
RUN pip install --user karateclub
RUN pip install --user tqdm
RUN pip install --user community
RUN pip install --user numpy scipy scikit-learn
RUN pip install --user pygsp
RUN pip install --user gensim
COPY . /workspace
WORKDIR /workspace 
EXPOSE 80
CMD python ./main.py

