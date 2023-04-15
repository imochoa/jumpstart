FMT='\e[1;34m%-6s\e[m\n'

#&& printf "permit :wheel as root\n" | sudo tee /etc/doas.conf \
printf $FMT "Creating the doas.conf file" \
&& printf "\n" \
&& printf $FMT "Setting correct permissions" \
&& sudo chown -c root:root /etc/doas.conf \
&& sudo chmod -c 0400 /etc/doas.conf \

printf $FMT "Creating the wheel group and adding current user" \
&& sudo groupadd --force wheel \
&& sudo usermod -a -G wheel "${USER}"

#printf $FMT "Checking /etc/doas.conf" \
#&& doas -C /etc/doas.conf && echo "config ok" || echo "config error"

# usermod -aG wheel 'username'

# https://wiki.archlinux.org/title/Doas
#permit persist :wheel

# Note: The configuration file must end with a newline.
# chown -c root:root /etc/doas.conf
# chmod -c 0400 /etc/doas.conf
# doas -C /etc/doas.conf && echo "config ok" || echo "config error"

#sudo printf "permit :wheel\n" > /etc/doas.conf
# You need tee to write to a file from another user
# echo "this is a line" | sudo tee file.txt

# https://wiki.archlinux.org/title/Doas
#Bash completion
#complete -cf doas


# https://wiki.gentoo.org/wiki/Doas
# testing
#user $doas -C /etc/doas.conf cat
#This test will output deny if the currently running user does not have the permissions to execute the cat command.
#
#Permissions can be checked for a specified user via:
#
#user $doas -C /etc/doas.conf cat -u larry
#If the user larry has permissions to access cat it may output permit.