# Use the latest Red Hat OS as the base image
FROM amazonlinux

# install sudo 
RUN yum update
RUN yum install -y sudo

# Install required packages and dependencies
RUN yum -y install \
    unzip \
    && yum clean all

# Download and install AWS CLI
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && ./aws/install \
    && rm -rf aws awscliv2.zip

# install less 
RUN yum install -y less

# install python 
RUN yum -y update
RUN yum install -y python3.11 && \
    yum clean all
# install pip 
RUN yum install -y wget
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py

# install terraform 
RUN wget https://releases.hashicorp.com/terraform/1.7.4/terraform_1.7.4_linux_amd64.zip -O terraform.zip && \
    unzip terraform.zip -d /usr/local/bin && \
    rm terraform.zip


# Verify AWS CLI installation
RUN aws --version


# install docker and kubernetes


# Install dependencies

# Add Docker's official GPG key
RUN yum install -y yum-utils
RUN sudo yum update -y
# RUN sudo yum install -y docker
# RUN sudo yum install -y initscripts


# RUN yum-config-manager --add-repo https://download.docker.com/linux/rhel/docker-ce.repo
# https://download.docker.com/linux/amazon/2/$basearch/stable
# RUN sudo yum install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin


# Install kubectl
RUN wget https://storage.googleapis.com/kubernetes-release/release/$(wget -qO- https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl -O /usr/local/bin/kubectl && \
    chmod +x /usr/local/bin/kubectl

# optional  

COPY project_root /home/project_root
COPY aws/list-user.py /home


COPY aws/comment.sh /home
WORKDIR /home
RUN chmod +x comment.sh
RUN ./comment.sh

# terraform 
COPY aws/credentials.sh /home
WORKDIR /home
RUN chmod +x credentials.sh
RUN ./credentials.sh


COPY terraform/main.tf /home
