#!/usr/bin/env sh

# Set preferred locales
# LANG=en_US.UTF-8
# LANGUAGE=
# LC_CTYPE="en_US.UTF-8"
# LC_NUMERIC=en_AU.UTF-8
# LC_TIME=en_AU.UTF-8
# LC_COLLATE="en_US.UTF-8"
# LC_MONETARY=en_AU.UTF-8
# LC_MESSAGES="en_US.UTF-8"
# LC_PAPER=en_AU.UTF-8
# LC_NAME=en_AU.UTF-8
# LC_ADDRESS=en_AU.UTF-8
# LC_TELEPHONE=en_AU.UTF-8
# LC_MEASUREMENT=en_AU.UTF-8
# LC_IDENTIFICATION=en_AU.UTF-8
# LC_ALL=

# Check all: locale -a

# temporary change: LC_TIME=en_US.UTF-8
# permanent change: sudo update-locale LC_TIME=en_US.UTF-8

# LANG              	 Provides default value for LC_* variables that have not been explicitly set.
# LC_ADDRESS        	 How addresses are formatted (country first or last, where zip code goes etc.).
# LC_ALL            	 Overrides individual LC_* settings: if LC_ALL is set, none of the below have any effect.
# LC_COLLATE        	 How strings (file names...) are alphabetically sorted. Using the "C" or "POSIX" locale here results in a strcmp()-like sort order, which may be preferable to language-specific locales.
# LC_CTYPE          	 How characters are classified as letters, numbers etc. This determines things like how characters are converted between upper and lower case.
# LC_IDENTIFICATION 	 Metadata about the locale information.
# LC_MEASUREMENT    	 What units of measurement are used (feet, meters, pounds, kilos etc.).
# LC_MESSAGES       	 What language should be used for system messages.
# LC_MONETARY       	 What currency you use, its name, and its symbol.
# LC_NAME           	 How names are represented (surname first or last, etc.).
# LC_NUMERIC        	 How you format your numbers. For example, in many countries a period (.) is used as a decimal separator, while others use a comma (,).
# LC_PAPER          	 Paper sizes: 11 x 17 inches, A4, etc.
# LC_RESPONSE       	 Determines how responses (such as Yes and No) appear in the local language
# LC_TELEPHONE      	 What your telephone numbers look like.
# LC_TIME           	 How your time and date are formatted. Use for example "en_DK.UTF-8" to get a 24-hour-clock in some programs.
# Current locales

# de_DE.UTF-8

export LANG=en_US.UTF-8
# export LANGUAGE=en_US.UTF-8
export LC_ADDRESS=en_AU.UTF-8
export LC_COLLATE="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"
export LC_IDENTIFICATION=en_AU.UTF-8
export LC_MEASUREMENT=en_AU.UTF-8
export LC_MESSAGES="en_US.UTF-8"
export LC_MONETARY=en_AU.UTF-8
export LC_NAME=en_AU.UTF-8
export LC_NUMERIC=en_AU.UTF-8
export LC_PAPER=en_AU.UTF-8
export LC_TELEPHONE=en_AU.UTF-8
export LC_TIME=en_AU.UTF-8

# https://help.ubuntu.com/community/Locale#List_current_settings
# sudo locale-gen
