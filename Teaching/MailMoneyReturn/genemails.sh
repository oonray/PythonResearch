#!/bin/bash
template=`cat emails/email.base`

navn=`cat person.json | jq '.[] | .[] | .navn'`
tid=`cat person.json | jq '.[] | .[] | .tid'`

for i in $navn
do
    echo $tempate $i
done
