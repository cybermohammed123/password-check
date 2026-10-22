#!/bin/bash

cand_password=$1
echo "the password is : $cand_password"
full_hash=$(echo -n $cand_password | sha1sum | awk '{print substr($1, 0, 32)}')
prefix=$(echo $full_hash | awk '{print substr($1, 0, 5)}')
suffix=$(echo $full_hash | awk '{print substr($1, 6, 26)}')
if curl https://api.pwnedpasswords.com/range/$prefix | grep -i $suffix;
  then echo "your password is compromised";
  else echo "your password is good to use";
fi
