<?php
define('gcpocGuard', TRUE);
?>
<html>
  <head>
    <title>Google Cloud POC</title>
  </head>
  <body>
    <h1>Google Cloud POC</h1>
    <?php
      require_once "GuzzleHttp/autoload.php";
      require_once "gcpocSettings.php";


      $instring = $_POST['instring'];

      $client = new GuzzleHttp\Client();
      $res = $client->post($postURI,
        array('form_params' => array(
          'instring' => $instring
        )
      ));
      if ($res->getStatusCode() == 201)
        echo "<p>The data was added successfully.</p>";
      else
        echo "<p>There was a problem adding the data.</p>";
    ?>
    <a href="gcpoc.php">Return to the front page</a>
  </body>
</html>
