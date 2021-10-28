#!/usr/bin/env bash
echo "update the clamav virus database..."
# stop the current daemon
sudo /etc/init.d/clamav-freshclam stop
# update
sudo freshclam
# restart
sudo /etc/init.d/clamav-freshclam start


# didn't work:
# sudo systemctl stop clamav-freshclam
# sudo freshclam
# sudo systemctl start clamav-freshclam
# sudo systemctl enable clamav-freshclam
