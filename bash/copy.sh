#!/bin/bash

DISKFUL=$(df -h /ntfs/ | grep sdb1 | awk '{print $5}' | cut -d "%" -f1 -)
mkdir /ntfs/pictures/

foldercount=1

until [ $DISKFUL -ge "90" ]; do
	mkdir /ntfs/pictures/$foldercount


	#method 1 -- slow 
	#for i in range{1..500}
	#do
	#	FILETOCOPY=$(shuf -n 2 /home/cstelly/cp/imagelist.txt)
	#	scp shorty:$FILETOCOPY /ntfs/pictures/$foldercount/
	#done

	#method 2 - rsync it
	rand_folder=$(( ( RANDOM % 999 ) + 1 )) 
	padded=$(seq -f "%03g" $rand_folder $rand_folder)
	rsync -zXhr shorty:/nfshome/digitalcorpora-images/$padded /ntfs/pictures/$foldercount/

	((foldercount+=1))
done

