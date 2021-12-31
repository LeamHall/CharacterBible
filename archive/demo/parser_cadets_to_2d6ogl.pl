#!/usr/bin/env perl

# parser_cadets_to_2d6ogl.pl
# version:  0.0.1
# date:     20201111
# author:   Leam Hall
# desc:     Parse a selected file and create the SQL commands to populate chars_2d6ogl table.

use strict;
use warnings;

my $csv_file  = 'tmp/data/firster_academy_cadets_1429_update.csv';
open( my $csv_fh, $csv_file) or die "Can't open $csv_file: $!";

my $sql_file  = 'tmp/data/people_add_2d6ogl_firster_academy_cadets_1429.sql';
open( my $sql_fh, '>', $sql_file ) or die "Can't open $sql_file: $!";

select $sql_fh;
print "BEGIN DEFERRED;\n";
foreach my $line ( readline($csv_fh) ) {
  my ($people_id, $last_name, $first_name, $gender, $upp, $birth_year, $birth_day, $notes) = split(/:/, $line);
  my @upp_array = split(//, $upp);
  my $str       = hex($upp_array[0]);
  my $dex       = hex($upp_array[1]);
  my $end       = hex($upp_array[2]);
  my $int       = hex($upp_array[3]);
  my $edu       = hex($upp_array[4]);
  my $soc       = hex($upp_array[5]);
  
  my $sql = "INSERT INTO chars_2d6ogl ( str, dex, end, int, edu, soc, people_id ) ";
  $sql    .= "VALUES ( $str, $dex, $end, $int, $edu, $soc, $people_id );";
  print $sql, "\n";
}
print "END;\n";

close($csv_fh);
close($sql_fh);

 
