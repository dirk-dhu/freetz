#!/bin/sh

PATH=/bin:/usr/bin:/sbin:/usr/sbin
. /usr/lib/libmodcgi.sh

check "$GW6_ENABLED" yes:auto "*":man
check "$GW6_LOGGING" yes:log

sec_begin '$(lang de:"Starttyp" en:"Start type")'

cat << EOF
<p>
<input id="e1" type="radio" name="enabled" value="yes"$auto_chk><label for="e1"> $(lang de:"Automatisch" en:"Automatic")</label>
<input id="e2" type="radio" name="enabled" value="no"$man_chk><label for="e2"> $(lang de:"Manuell" en:"Manual")</label>
EOF
cat << EOF
</p>
EOF

sec_end
sec_begin '$(lang de:"gw6" en:"gw6")'

cat << EOF
<table border="0">
<tr>
	<td>$(lang de:"Benutzername" en:"Username"):</td>
	<td><input type="text" name="userid" size="15" maxlength="50" value="$(html "$GW6_USERID")">
    ($(lang de:"Leer lassen f&uuml;r anonymen Login" en:"Leave this empty for anonymous login"))</td>
</tr>
<tr>
	<td>$(lang de:"Passwort" en:"Password"):</td>
	<td><input type="password" name="passwd" size="15" maxlength="50" value="$(html "$GW6_PASSWD")">
    ($(lang de:"Leer lassen f&uuml;r anonymen Login" en:"Leave this empty for anonymous login"))</td>
</tr>
<tr>
    <td>$(lang de:"Logging" en:"Logging"):</td>
    <td><input type="checkbox" name="logging" value="yes"$log_chk>$(lang de:"Nach /tmp/gw6c.log loggen." en:"Log to /tmp/gw6c.log.")</td>
</tr>
</table>

$(lang de:"Hinweis: Wenn ein Benutzername eingegeben wurde, wird gw6 ein Subnetz anfordern und automatisch
radvd auf dem Interface lan aktivieren. Wird kein Benutzername angegeben, dann wird gw6 nur eine
einzige IP-Adresse anfordern." en:"Note: If a username is given, gw6 will request a subnet and
radvd will be started automatically on interface lan. If no username is given, gw6 will request only
one single IP address.")
EOF

sec_end
