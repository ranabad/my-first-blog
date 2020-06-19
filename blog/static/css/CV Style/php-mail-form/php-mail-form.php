<?php
/**
 * PHP Mail Form
 * Version: 2.0
 * Website: https://templatemag.com/php-mail-form/
 * Copyright: TemplateMag.com
 */

class PHP_Mail_Form {

  public $to = false;
  public $from_name = false;
  public $from_email = false;
  public $subject = false;
  public $mailer = false;
  public $message = '';

  public $content_type = 'text/html';
  public $charset = 'UTF-8';
  public $ajax = false;

  public $error_msg = array(
    'invalid_to_email' => 'Email to: is empty or invalid!',
    'invalid_from_name' => 'From Name is empty!',
    'invalid_from_email' => 'Email from: is empty or invalid!',
    'invalid_subject' => 'Subject is too short or empty!',
    'invalid_mailer' => 'Mailer Email is empty or invalid!',
    'short' => 'is too short or empty!',
    'send_error' => 'Could not send mail! Please check your PHP mail configurations.',
    'ajax_error' => 'Sorry, the request should be an Ajax POST',
  );

  private $error = false;

  public function __construct() {
    $this->mailer = "formsubmit@" . @preg_replace('/^www\./','', $_SERVER['SERVER_NAME']);
  }

  public function add_message($content, $label = '', $length_check = false) {
    $message = filter_var($content, FILTER_SANITIZE_STRING) . '<br>';
    if( $length_check ) {
      if( strlen($message) < $length_check + 4 ) {
        $this->error .=  $label . ' ' . $this->error_msg['short'] . '<br>';
        return;
      }
    }
    $this->message .= !empty( $label ) ? '<strong>' . $label . ':</strong> ' . $message : $message;
  }

  public function send() {
    if( $this->ajax ) {
      if( !isset($_SERVER['HTTP_X_REQUESTED_WITH']) && strtolower($_SERVER['HTTP_X_REQUESTED_WITH']) != 'xmlhttprequest') {
        return $this->error_msg['ajax_error'];
      }
    }

    $to = filter_var( $this->to, FILTER_VALIDATE_EMAIL);
    $from_name = filter_var( $this->from_name, FILTER_SANITIZE_STRING);
    $from_email = filter_var( $this->from_email, FILTER_VALIDATE_EMAIL);
    $subject = filter_var( $this->subject, FILTER_SANITIZE_STRING, FILTER_FLAG_NO_ENCODE_QUOTES);
    $mailer = filter_var( $this->mailer, FILTER_VALIDATE_EMAIL);
    $message = nl2br($this->message);

    if( ! $to || $to == 'contact@example.com') $this->error .= $this->error_msg['invalid_to_email'] . '<br>';
    if( ! $from_name ) $this->error .= $this->error_msg['invalid_from_name'] . '<br>';
    if( ! $from_email ) $this->error .= $this->error_msg['invalid_from_email'] . '<br>';
    if( ! $subject ) $this->error .= $this->error_msg['invalid_subject'] . '<br>';
    if( ! $mailer) $this->error .= $this->error_msg['invalid_mailer'] . '<br>';

    if( $this->error ) {
      return $this->error;
    }

    $headers = 'From: ' . $from_name . ' <' . $mailer . '>' . PHP_EOL;
    $headers .= 'Reply-To: ' . $from_email . PHP_EOL;
    $headers .= 'MIME-Version: 1.0' . PHP_EOL;
    $headers .= 'Content-Type: ' . $this->content_type . '; charset=' . $this->charset . PHP_EOL;
    $headers .= 'X-Mailer: PHP/' . phpversion() . ' with PHP_Mail_Form';

    $sendemail = mail($to, $subject, $message, $headers);

    if( $sendemail ) {
      return 'OK';
    } else {
      return $this->error_msg['send_error'];
    }
  }
}

?>
