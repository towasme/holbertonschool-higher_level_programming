#!/bin/bash
# script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
curl -sd "email=hr@holbertonschool.com&subject=I will always be here for PLD" -X POST "$1"
