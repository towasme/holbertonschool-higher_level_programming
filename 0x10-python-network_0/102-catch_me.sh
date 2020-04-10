#!/bin/bash
# script that responds to a server containing a message

curl -sLH "You got me!-User-Id:98" "0.0.0.0:5000/catch_me"
