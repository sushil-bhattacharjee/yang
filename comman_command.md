#### To see the number of lines in one yang file

sushil@sushil:~/YANG/vendor/cisco/nx/9.3-9$ pyang Cisco-NX-OS-device.yang -f tree | wc -l

37073

### To continuously monitor while making the yang model file

$watch pyang ethernet-switch.yang -f tree
