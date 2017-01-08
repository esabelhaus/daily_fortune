# Daily Fortune Tweet crontab

## Requirements

* python3
* fortunes library
  * ubuntu: `sudo apt-get install fortune-mod`
  * centos: `sudo yum install fortune-mod`
  * otherwise, google is your friend here :smiley:
* twitter consumer key/secret
* twitter access_token key/secret
* virtualenv (not required, but suggested)

## Setup

* `pyvenv twit`
* `source twit/bin/activate`
* `pip install -r requirements.txt`
* `cp config/auth.example config/auth`
* modify `config/auth` to match your twitter auth
* test by running `./run.sh`
 * output should be `200`

## Install

* once functionality is confirmed, we make a crontab
 * `crontab -e`
   * this file will have a lot of commented out hoobla, skip past that with your down arrow to the bottom of the comment block
 * type `:set paste` + `ENTER`
   * this will set VIM into paste mode
 * type `o`
   * this will open a new line below the current line
 * paste the following content:
```
# daily fortune tweet at 6AM
0  6 * * * /[path_to_run.sh]
```
   * note: if you want a different time, modify 6 to be any number between 0 and 24,
   * ex. 13 would be 1PM
 * now type `:wq` + `ENTER`
   * this will `w` write and `q` quit the vim editor
