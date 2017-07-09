#!/bin/bash
set -e

# Apache gets grumpy about PID files pre-existing
rm -f /var/run/httpd/httpd.pid

# set the app configuration depending on the environment passed from docker
rm -f /var/www/html/gcpocSettings.php
touch /var/www/html/gcpocSettings.php
echo "<?php" >> /var/www/html/gcpocSettings.php
echo "if(!defined('gcpocGuard')) {die('Direct access not permitted');}" >> /var/www/html/gcpocSettings.php
echo "\$getURI='$GCPOC_GET_URI';" >> /var/www/html/gcpocSettings.php
echo "\$postURI='$GCPOC_POST_URI';" >> /var/www/html/gcpocSettings.php
echo "?>" >> /var/www/html/gcpocSettings.php

# start apache
exec httpd -DFOREGROUND
