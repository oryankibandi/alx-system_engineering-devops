# kills a process named killmenow
exec {
  command => 'pkill -15 killmenow',
}
