rm $2
cat $1 | grep -v cos | grep -v sin > tmpfileasdasd 
cat $1 | grep month_cos | grep month_sin | grep -v weekday | grep -v hour >> tmpfileasdasd
cat $1 | grep month_cos | grep month_sin | grep weekday_cos | grep weekday_sin | grep -v hour >> tmpfileasdasd
cat $1 | grep month_cos | grep month_sin | grep weekday_cos | grep weekday_sin | grep hour_cos | grep hour_sin >> tmpfileasdasd
cat $1 | grep -v month | grep weekday_cos | grep weekday_sin | grep hour_cos | grep hour_sin >> tmpfileasdasd
cat $1 | grep -v month |  grep -v hour | grep weekday_cos | grep weekday_sin >> tmpfileasdasd
cat $1 | grep month_cos | grep month_sin | grep -v weekday | grep hour_cos | grep hour_sin >> tmpfileasdasd
cat $1 | grep -v month | grep -v weekday | grep hour_cos | grep hour_sin >> tmpfileasdasd
cat tmpfileasdasd | tr -d "[" | tr -d "]" | tr -d "'" > $2
rm tmpfileasdasd
