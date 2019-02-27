#!/bin/sh
zenity --forms --title="Work notes" \
--text="오늘 반찬 중 맛있었던 것은??" \
--separator="," \
--add-calendar="Today" \
--add-entry="Point" \
--add-entry="Menu" \
--add-entry="Note": >> worknote.csv

case $? in
	0)
		echo "done";;
	1)
		echo "cancel";;
	-1)
		echo "cancel";;
esac
