# kills a process named killmenow
exec {
  command => 'pkill killmenow',
  path    => ['/usr/bin', '/usr/sbin', '/bin']
}
