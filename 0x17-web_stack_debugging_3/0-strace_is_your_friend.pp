# fixes server

package {'nginx':
	ensure  => installed,
}

service {'nginx':
	require => Package['nginx'],
	ensure  => running,
}

exec {'allow "HTTP"':
        command => '/usr/bin/ufw allow "HTTP"' 
}

service {'ufw':
	require => Exec['allow "HTTP"'],
	ensure  => running,
}
