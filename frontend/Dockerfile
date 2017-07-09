FROM centos:latest

RUN yum -y update && yum -y install epel-release
RUN yum -y install httpd php php-guzzlehttp-guzzle
RUN systemctl enable httpd
RUN systemctl disable firewalld
COPY ./*.php /var/www/html/
COPY ./docker-cmd.sh /
RUN chmod 644 /var/www/html/*.php
RUN chmod 755 /docker-cmd.sh
RUN chmod 777 /var/log/httpd
RUN sed -i 's/display_errors = Off/display_errors = On/' /etc/php.ini
EXPOSE 80

CMD ["/docker-cmd.sh"]
