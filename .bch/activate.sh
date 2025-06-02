#!/usr/bin/env bash
___pref=BCH_KRON

___this=${BASH_SOURCE[0]}
___here=$(dirname $___this)
___root=$(dirname $___here)
___export() { export ${___pref}_${1}="${2}" ; }

___export  _activate    $___this
___export  _root        $___root
___export  _lib         $___here/lib
___export  _bin         $___here/bin
___export  _lbin        $___here/lbin

source $___here/init/init.sh

unset ___pref
unset ___this
unset ___here
unset ___root
unset ___export
