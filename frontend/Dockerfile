FROM centos:latest

RUN yum -y update && yum -y install epel-release && yum -y install httpd php php-guzzlehttp-guzzle
RUN systemctl enable httpd
COPY ./*.php /var/www/html/
RUN chmod 644 /var/www/*.html
