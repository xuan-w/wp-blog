#!/bin/bash

sed -i 's/&quot;/"/g' $1 
sed -i 's/&#039;/'\''/g' $1 
sed -i 's/&gt;/>/g' $1 
sed -i 's/&amp;/\&/g' $1 
