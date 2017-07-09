<?php
define('gcpocGuard', TRUE);
?>
<html>
  <head>
    <title>Google Cloud POC</title>
  </head>
  <body>
    <h1>Google Cloud POC</h1>
    <p>This trivial little page is a proof of concept for using Google Cloud.</p>
    <p>It is actually made of of the following:</p>
    <ul>
      <li>These pages, written in PHP, hosted on an Apache Google Compute box</li>
      <li>A microservice for inserting data, written in python, on another GC box</li>
      <li>A microservice for retrieving data, written in python, on another GC box</li>
      <li>A MariaDB for storing the data, on another GC box</li>
    </ul>
    <h2>Add information to the database.</h2>
    <form action="send.php" method="post">
      <p>Item:<input type="text" name="instring" /></p>
      <input type="submit" name="Add" value="Add" />
    </form>
    <h2>The current contents of the database:</h2>
    <?php
      require_once "GuzzleHttp/autoload.php";
      require_once "gcpocSettings.php";
      echo "<p>Trying to connect to {$getURI}<p>";
      $client = new GuzzleHttp\Client();
      $res = $client->get($getURI, []);
      if ($res->getStatusCode() == 200) {
        $array = json_decode($res->getBody(),true);
        echo "<ul>";
        foreach ($array as $instring) {
          echo "<li>{$instring}</li>";
        }
        echo "</ul";
      }
    ?>
  </body>
</html>
