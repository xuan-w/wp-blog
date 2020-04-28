#!/bin/bash

sed 's/&quot;/"/g' $1 | sed 's/&#039;/'\''/g' | sed 's/&gt;/>/g' | sed 's/&amp;/\&/g' > tmp.tmp

rm $1

mv tmp.tmp $1
