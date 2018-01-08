#!/bin/bash
# -------------------------------------------------------------------------------
# Filename:    get_ip.sh
# Revision:    1.0
# Date:        2017/08/24
# Author:      Qin Boqin
# Email:       bobbqqin@bupt.edu.cn
# Description: Get local ipv4 and ipv6 info
# Notes:       This plugin uses the "hostname" and "ip" command
# -------------------------------------------------------------------------------
hostname
ip -f inet addr show eth0 | grep -Po 'inet \K[\d.]+'
ip -f inet6 addr show eth0 | grep -Po 'inet6 \K[\w:]+' | grep 2001 | head -1
