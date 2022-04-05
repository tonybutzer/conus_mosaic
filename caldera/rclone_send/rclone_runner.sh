#! /bin/bash

year=2001

for tile in `cat tile_list.txt`; do echo $tile; rclone sync -P wss3:/ws-out/stage_caldera/netet/${tile}/${year}/  tallgrass:/caldera/projects/usgs/water/impd/skagone/${tile}/${year}/ ; done
