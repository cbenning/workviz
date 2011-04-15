
while :
do
	CPU=`ps aux|awk 'NR > 0 { s +=\$3 }; END {print s}'`
	MEMTOTAL=`free -t | grep 'Total:' | awk '{ print $2}'`
	MEMUSED=`free -t | grep 'Total:' | awk '{ print $3}'`
	MEMUSEDPERC=`echo "scale=4;($MEMUSED/$MEMTOTAL)*100" | bc -l`
	##iostat requires the sysstat package in debian
	DISKLOAD=`iostat -d sda -x 10 1 | grep 'sda' | awk '{ print $12}'`
	echo "$MEMUSEDPERC,$CPU,$DISKLOAD"
	sleep 3
done
	

