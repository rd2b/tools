#!/bin/bash
#########################################################
#	Name: 	pyv-df.bash				#
#	Description: Checks file space			#
#########################################################


filesys="/home"
warn="30"
critic="50"

total=$(df $filesys |tail -1 |awk '{print($5)}' |tr -d '%' )

ret=0
[[ $warn -lt $total ]] && ret=1
[[ $critic -lt $total ]] && ret=2



exit $ret 
