#!/usr/bin/env perl

# parser_1_csv_to_sql.pl
# version:  0.0.1
# date:     20201105
# author:   Leam Hall
# desc:     Parse a selected file and create the SQL commands.


use strict;
use warnings;

my $csv_file  = 'tmp/data/firster_academy_cadets_1429_update.csv';
open( my $csv_fh, $csv_file) or die "Can't open $csv_file: $!";

my $sql_file  = 'tmp/data/firster_academy_cadets_1429_update.sql';
open( my $sql_fh, '>', $sql_file ) or die "Can't open $sql_file: $!";

select $sql_fh;
print "BEGIN DEFERRED;\n";
foreach my $line ( readline($csv_fh) ) {
  my ($id, $last_name, $first_name, $gender, $upp, $birth_year, $birth_day, $notes) = split(/:/, $line);
  chomp($notes);
  my $sql = "INSERT INTO cadets ( year, cadre, id, last_name, first_name, gender, upp, birth_year, birth_day, notes) ";
  $sql    .= "VALUES ( 1429, 4, $id, \"$last_name\", '$first_name', '$gender', '$upp', $birth_year, $birth_day, \"$notes\" );";
  print $sql, "\n";
}
print "END;\n";

close($csv_fh);
close($sql_fh);

 
